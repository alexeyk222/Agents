<!-- Context: core/update | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Update

**Назначение**: обновлять контекст при изменении API, фреймворков или контрактов

**Последнее обновление**: 2026-01-06

---

## Когда использовать

- Обновления версий фреймворков (Next.js 14 → 15)
- Изменения API (несовместимые изменения, депрекации)
- Новые функции добавлены к существующим темам
- Нужны руководства по миграции

---

## 8-этапный workflow

### Этап 1: определить изменения (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: пользователь описывает, что изменилось

**Формат**:
```
What changed in {topic}?
  [A] API changes
  [B] Deprecations
  [C] New features
  [D] Breaking changes
  [E] Other (describe)

Select all that apply (A B C D or describe):
```

**Уточнение**: получить конкретные детали для каждого выбранного типа

**Валидация**: ОБЯЗАТЕЛЬНО получить ввод пользователя перед продолжением

---

### Этап 2: найти затронутые файлы
**Действие**: найти файлы, ссылающиеся на тему

**Процесс**:
1. Выполнить grep ссылок на тему по всему контексту
2. Посчитать ссылки по файлам
3. Показать анализ влияния

**Формат**:
```
Found 5 files referencing {topic}:
  📄 concepts/routing.md (3 references, 145 lines)
  📄 examples/app-router-example.md (7 references, 78 lines)
  📄 guides/setting-up-nextjs.md (2 references, 132 lines)
  📄 errors/nextjs-errors.md (1 reference, 98 lines)
  📄 lookup/nextjs-commands.md (4 references, 54 lines)

Total impact: 17 references across 5 files
```

---

### Этап 3: предварительный просмотр изменений (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать построчный diff для каждого файла

**Формат**:
```
Proposed updates:

━━━ concepts/routing.md ━━━

Line 15:
  - App router is optional (use pages/ or app/)
  + App router is now default in Next.js 15 (pages/ still supported)

Line 42:
  + ## Metadata API (New in v15)
  + Next.js 15 introduces new metadata API...

━━━ examples/app-router-example.md ━━━

Line 8:
  - // Optional: use app router
  + // Default in Next.js 15+

Preview next file? (yes/no/show-all)
Approve changes? (yes/no/edit):
```

**Режим edit**: построчное одобрение каждого изменения

**Валидация**: ОБЯЗАТЕЛЬНО получить одобрение перед продолжением

---

### Этап 4: резервная копия
**Действие**: создать резервную копию перед обновлением

**Расположение**: `.tmp/backup/update-{topic}-{timestamp}/`

**Назначение**: включить откат, если обновления вызовут проблемы

---

### Этап 5: обновить файлы
**Действие**: применить одобренные изменения

**Процесс**:
1. Обновить concepts, examples, guides, lookups
2. Сохранить формат MVI (<200 строк)
3. Обновить даты "Last Updated"
4. Сохранить структуру файлов

**Обеспечение**: `@critical_rules.mvi_strict`

---

### Этап 6: добавить заметки миграции
**Действие**: добавить руководство по миграции в `errors/`

**Формат**:
```markdown
## Migration: {Old Version} → {New Version}

**Breaking Changes**:
- Change 1
- Change 2

**Migration Steps**:
1. Step 1
2. Step 2

**Reference**: [Link to changelog]
```

**Расположение**: `{category}/errors/{topic}-errors.md`

---

### Этап 7: проверка
**Действие**: проверить все ссылки

**Проверки**:
- Все внутренние ссылки все еще работают
- Нет битых ссылок
- Все файлы все еще <200 строк
- Формат MVI сохранен

---

### Этап 8: отчет
**Действие**: показать полные результаты

**Формат**:
```
✅ Updated X files
📝 Modified Y references
🔄 Added migration notes to errors/
💾 Backup: .tmp/backup/update-{topic}-{timestamp}/

Summary of changes:
  - concepts/routing.md: 2 updates (145 → 162 lines)
  - examples/app-router-example.md: 4 updates (78 → 89 lines)
  - guides/setting-up-nextjs.md: 1 update (132 → 133 lines)

All files still under 200 line limit ✓

Rollback available if needed.
```

---

## Типы изменений

### Изменения API
- Изменились сигнатуры методов
- Параметры добавлены/удалены
- Изменились возвращаемые типы

### Депрекации
- Фичи помечены deprecated
- Доступны API-замены
- Есть график удаления

### Новые функции
- Добавлены новые возможности
- Представлены новые API
- Доступны новые паттерны

### Несовместимые изменения
- Несовместимые изменения
- Требуется миграция
- Старый код не будет работать

---

## Примеры

### Обновление фреймворка
```bash
/context update for Next.js 15
/context update for React 19
```

### Изменения API
```bash
/context update for Stripe API v2024
/context update for OpenAI API breaking changes
```

### Обновление библиотеки
```bash
/context update for Tailwind CSS v4
```

---

## Критерии успеха

- [ ] Пользователь описал изменения?
- [ ] Все затронутые файлы найдены?
- [ ] Предварительный просмотр diff показан?
- [ ] Пользователь одобрил изменения?
- [ ] Резервная копия создана?
- [ ] Заметки миграции добавлены?
- [ ] Все ссылки проверены?
- [ ] Все файлы все еще <200 строк?

---

## Связанные материалы

- guides/workflows.md - интерактивные diff-примеры
- standards/mvi.md - поддержание формата MVI
- operations/error.md - добавление migration notes
