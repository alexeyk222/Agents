<!-- Context: enterprise/lookup | Priority: high | Version: 1.0 | Updated: 2026-10-02 -->

# Impala: разведка схем и данных

**Назначение**: безопасно изучать структуру и наполнение таблиц DWH/Data Lake
через Impala — от метаданных к агрегатам, без выгрузки сырых строк.

---

## Уровни разведки

| Уровень | Что делаем | Кто | Подтверждение |
|---|---|---|---|
| 0. Метаданные | `SHOW`, `DESCRIBE`, статистика | `ContextScout` (через MCP) | Нет, если MCP настроен read-only |
| 1. Профиль | `COUNT`, `NDV`, доля NULL, min/max на одной партиции | `OpenCoder` / `ScientificAgent` | Да |
| 2. Выборка | Агрегаты, распределения, топ-значения справочников | `ScientificAgent` | Да |
| 3. Изменения | `INSERT`, `CREATE`, `DROP`, `COMPUTE STATS`, `INVALIDATE METADATA` | Только по явному запросу | Обязательно |

`ContextScout` работает **только на уровне 0**. Всё, что выше, он формулирует
как готовые запросы для основного агента.

---

## Уровень 0: метаданные

```sql
SHOW DATABASES LIKE '*dwh*';
SHOW TABLES IN dwh LIKE '*transaction*';
DESCRIBE FORMATTED dwh.dm_transactions;   -- колонки, типы, комментарии, владелец, формат, location
SHOW PARTITIONS dwh.dm_transactions;       -- ключи партиций, число файлов, размер
SHOW TABLE STATS dwh.dm_transactions;      -- #rows (если COMPUTE STATS выполнялся)
SHOW COLUMN STATS dwh.dm_transactions;     -- NDV, #nulls, max/avg size
SHOW CREATE TABLE dwh.dm_transactions;
```

Комментарии колонок из `DESCRIBE FORMATTED` — первый кандидат на описание
атрибута; сверяй их с Confluence.

---

## Уровень 1–2: профилирование (с подтверждением)

Правила:

- **Всегда фильтр по партиции** (`WHERE dt = '2026-09-30'` или узкий диапазон).
- **Всегда `LIMIT`** для запросов, возвращающих строки; по умолчанию — агрегаты.
- `NDV()` вместо `COUNT(DISTINCT)` на больших таблицах.
- Сырые значения чувствительных полей (ФИО, телефон, номер карты, счёт) не
  выводить — только заполненность и длины/форматы.

```sql
-- Заполненность и кардинальность атрибута на одной партиции
SELECT COUNT(*)                                    AS rows_total,
       COUNT(mcc_code)                             AS rows_filled,
       ROUND(100 * COUNT(mcc_code) / COUNT(*), 2)  AS fill_pct,
       NDV(mcc_code)                               AS ndv
FROM dwh.dm_transactions
WHERE dt = '2026-09-30';

-- Топ значений справочного атрибута
SELECT channel_code, COUNT(*) AS cnt
FROM dwh.dm_transactions
WHERE dt = '2026-09-30'
GROUP BY channel_code
ORDER BY cnt DESC
LIMIT 20;

-- Проверка гранулярности (дубли ключа)
SELECT operation_id, COUNT(*) AS c
FROM dwh.dm_transactions
WHERE dt = '2026-09-30'
GROUP BY operation_id
HAVING COUNT(*) > 1
LIMIT 20;
```

Правила корректности SQL (гранулярность, NULL, join cardinality) — в skill
`sql-queries`.

---

## Особенности Impala

- Метаданные могут отставать от Hive: если таблицы «нет», попроси пользователя
  проверить `INVALIDATE METADATA` / `REFRESH` — сам агент это не запускает.
- `SHOW TABLE STATS` показывает `-1`, если статистика не собрана — это не ноль строк.
- Строковые даты и `TIMESTAMP` без таймзоны — фиксируй принятое допущение.
- Типы `DECIMAL(p,s)` важны для сумм — не приводи к `DOUBLE` без причины.

---

## Ограничения

- ❌ Никаких DML/DDL и `COMPUTE STATS` без явного запроса.
- ❌ Никаких полных сканов больших таблиц без фильтра по партиции.
- ❌ Не выводи в чат сырые персональные данные.
- ✅ Каждое утверждение о данных подкрепляй запросом, который его доказывает.
