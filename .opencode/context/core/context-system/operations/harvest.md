<!-- Context: core/harvest | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Context Harvest

**Назначение**: извлечь знания из AI-сводок → постоянный контекст, затем очистить рабочую область

**Последнее обновление**: 2026-01-06

---

## Основная проблема

AI-агенты создают файлы сводок (OVERVIEW.md, SESSION-*.md, SUMMARY.md), которые содержат ценные знания, но засоряют рабочую область. Эти файлы «захламляют» кодовую базу.

**Решение**: собрать знания → постоянный контекст, затем удалить сводки.

---

## Паттерны автообнаружения

<rule id="summary_patterns" enforcement="strict">
  Harvest автоматически обнаруживает эти паттерны:
  
  Паттерны имен файлов:
  - *OVERVIEW.md
  - *SUMMARY.md
  - SESSION-*.md
  - CONTEXT-*.md
  - *NOTES.md
  
  Паттерны расположения:
  - Файлы в каталоге .tmp/
  - Файлы с "Summary", "Overview", "Session" в заголовке
  - Файлы >2KB в корневом каталоге (вероятные сводки)
</rule>

---

## 6-этапный workflow

<workflow id="harvest" enforce="@critical_rules">
  
### Этап 1: сканирование
**Действие**: найти все файлы сводок в рабочей области

**Процесс**:
1. Искать по паттернам автообнаружения
2. Проверить каталог `.tmp/`
3. Вывести файлы с размерами
4. Отсортировать по дате изменения (сначала новые)

**Выход**: список файлов-кандидатов

**Пример**:
```
Found 3 summary documents:
1. CONTEXT-SYSTEM-OVERVIEW.md (4.2 KB, modified 1 hour ago)
2. SESSION-auth-work.md (1.8 KB, modified today)
3. .tmp/IMPLEMENTATION-NOTES.md (800 bytes, modified today)
```

---

### Этап 2: анализ
**Действие**: категоризировать контент по функции

**Правила сопоставления**:
| Тип контента | Целевая папка | Как определить |
|--------------|---------------|-----------------|
| Дизайн-решения | `concepts/` | "We decided to...", "Architecture", "Pattern" |
| Решения/паттерны | `examples/` | Сниппеты кода, "Here's how we..." |
| Workflows | `guides/` | Нумерованные шаги, "How to...", "Setup" |
| Встреченные ошибки | `errors/` | Сообщения об ошибках, "Fixed issue", "Gotcha" |
| Справочные данные | `lookup/` | Таблицы, списки, пути, команды |

**Процесс**:
1. Прочитать каждый файл
2. Определить ценные разделы (пропустить планирование/диалог)
3. Категоризировать по функции
4. Определить целевой путь файла
5. Сгенерировать предварительный просмотр (первые 60 символов)

**Выход**: категоризированные элементы с буквенными ID

---

### Этап 3: одобрение (КРИТИЧНО)
**Действие**: показать UI одобрения с выбором по буквам

<rule id="approval_gate" enforcement="strict">
  ВСЕГДА показывайте UI одобрения перед извлечением/удалением.
  НИКОГДА не выполняйте auto-harvest без подтверждения пользователя.
</rule>

**Формат**:
```
### CONTEXT-SYSTEM-OVERVIEW.md (4.2 KB)

✓ [A] Design: Function-based context organization
    → Would add to: core/concepts/context-organization.md
    Preview: "Organize by function (concepts/, examples/...)..."

✓ [B] Pattern: Minimal Viable Information
    → Would add to: core/concepts/mvi-principle.md
    Preview: "Extract core only (1-3 sentences), 3-5 key points..."

✓ [C] Workflow: Harvesting summary documents
    → Would create: core/guides/harvesting.md
    Preview: "Scan for summaries → Extract → Approve → Delete"

✗ [D] Skip: Planning discussion notes (temporary knowledge)

---

### SESSION-auth-work.md (1.8 KB)

✓ [E] Error: JWT token expiration not handled
    → Would add to: development/errors/auth-errors.md
    Preview: "Symptom: 401 after 1 hour. Cause: No refresh flow..."

✓ [F] Example: JWT refresh token implementation
    → Would create: development/examples/jwt-refresh.md
    Preview: "Store refresh token → Check expiry → Request new..."

---

### .tmp/IMPLEMENTATION-NOTES.md (800 bytes)

✗ [G] Skip: Duplicate info (already in development/concepts/api-design.md)

---

**Quick options**:
- Type 'A B C E F' - Approve specific items
- Type 'all' - Approve all ✓ items (A B C E F)
- Type 'none' - Skip harvesting, delete files anyway
- Type 'cancel' - Keep files, don't harvest
```

**Валидация**:
- ОБЯЗАТЕЛЬНО дождаться ввода пользователя
- НЕЛЬЗЯ продолжать без одобрения
- Если пользователь вводит `cancel`, остановиться немедленно

**Выход**: список одобренных элементов

---

### Этап 4: извлечение
**Действие**: извлечь и минимизировать одобренные элементы

<rule id="extraction" enforce="@mvi_principle">
  Применяйте MVI ко всему извлеченному контенту:
  - Ключевая концепция: 1–3 предложения
  - Ключевые пункты: 3–5 маркеров
  - Минимальный пример: <10 строк
  - Ссылка: на исходный источник
  - Файлы: каждый <200 строк
</rule>

**Процесс**:
1. Для каждого одобренного элемента:
   - Извлечь ключевое содержимое
   - Применить MVI-минимизацию (см. compact.md)
   - Сгенерировать предварительный просмотр итогового контента
2. Показать предварительный просмотр извлечения (ТРЕБУЕТСЯ ОДОБРЕНИЕ):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extraction Preview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] → core/concepts/context-organization.md (CREATE, 45 lines)
┌─────────────────────────────────────────────────────────┐
│ # Concept: Context Organization                         │
│                                                         │
│ **Purpose**: Function-based knowledge organization      │
│                                                         │
│ ## Core Concept                                         │
│ Organize context by function: concepts/, examples/...   │
│ ...                                                     │
└─────────────────────────────────────────────────────────┘

[E] → development/errors/auth-errors.md (ADD to existing, 98 → 112 lines)
┌─────────────────────────────────────────────────────────┐
│ + ## Error: JWT Token Expiration Not Handled             │
│ +                                                       │
│ + **Symptom**: 401 after 1 hour                         │
│ + **Cause**: No refresh token flow                      │
│ + ...                                                   │
└─────────────────────────────────────────────────────────┘

... ({remaining_count} more items)

Show all? [y/n] | Approve extraction? [y/n/edit]: _
```

3. После одобрения:
   - Записать файлы на диск
   - Добавить перекрестные ссылки
   - Обновить карты `navigation.md`

**Выход**: список созданных/обновленных файлов

---

### Этап 5: очистка (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: архивировать или удалить исходные файлы сводок

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cleanup: Source Files
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Successfully harvested from:
  CONTEXT-SYSTEM-OVERVIEW.md (4.2 KB)
  SESSION-auth-work.md (1.8 KB)

Skipped (no valuable content):
  .tmp/IMPLEMENTATION-NOTES.md (800 bytes)

How should we handle these source files?

  1. Archive (safe) — move to .tmp/archive/harvested/{date}/
     → Can restore later if needed

  2. Delete — permanently remove harvested files
     → Frees disk space, no undo

  3. Keep — leave source files in place
     → No cleanup, files remain where they are

Choose [1/2/3] (default: 1): _
```

<rule id="cleanup_safety" enforcement="strict">
  Очищайте ТОЛЬКО файлы, из которых контент был успешно собран.
  Если извлечение не удалось, сохраните исходный файл.
</rule>

**Выход**: отчет об очистке

---

### Этап 6: отчет
**Действие**: показать полное резюме результатов

**Формат**:
```
✅ Harvested 5 items into permanent context:
   - Added to core/concepts/context-organization.md
   - Added to core/concepts/mvi-principle.md
   - Created core/guides/harvesting.md
   - Added to development/errors/auth-errors.md
   - Created development/examples/jwt-refresh.md

🗑️ Cleaned up workspace:
   - Archived: CONTEXT-SYSTEM-OVERVIEW.md → .tmp/archive/harvested/2026-01-06/
   - Archived: SESSION-auth-work.md → .tmp/archive/harvested/2026-01-06/
   - Deleted: .tmp/IMPLEMENTATION-NOTES.md (no valuable content)

📊 Updated navigation maps:
   - .opencode/context/core/navigation.md
   - .opencode/context/development/navigation.md

💾 Disk space freed: 6.8 KB
```

</workflow>

---

## Примеры использования

### Сканировать всю рабочую область
```bash
/context harvest
```

### Сканировать конкретный каталог
```bash
/context harvest .tmp/
/context harvest docs/sessions/
```

### Собрать конкретный файл
```bash
/context harvest OVERVIEW.md
/context harvest SESSION-2026-01-06.md
```

---

## Умное обнаружение контента

### ✅ Извлекать (ценные знания)
- Дизайн-решения ("We chose X because...")
- Паттерны, которые сработали ("This pattern solved...")
- Встреченные ошибки + решения
- Изменения API ("Updated from v1 to v2...")
- Наблюдения по производительности ("Optimization reduced...")
- Объясненные ключевые концепции

### ❌ Пропускать (временное/шум)
- Обсуждения планирования ("Should we...?", "Maybe try...")
- Диалоговые заметки ("I think...", "We talked about...")
- Дублирующая информация (уже в контексте)
- TODO-списки (вместо этого перенести в систему задач)
- Временные метки и метаданные сессии

---

## Функции безопасности

1. **Точка одобрения** - никогда не удалять автоматически без подтверждения
2. **Архивировать по умолчанию** - перемещать в `.tmp/archive/`, а не удалять навсегда
3. **Валидация** - проверять размеры файлов и структуру перед коммитом
4. **Откат** - при необходимости можно восстановить из архива
5. **Пробный запуск** - показать, что произойдет, до выполнения

---

## Критерии успеха

После операции harvest:

- [ ] Ценные знания извлечены в постоянный контекст?
- [ ] Все извлеченные файлы <200 строк?
- [ ] Файлы в правильных функциональных папках?
- [ ] Навигация `navigation.md` обновлена?
- [ ] Файлы сводок архивированы/удалены?
- [ ] Рабочая область чище, чем раньше?
- [ ] Знания не потеряны?

---

## Связанные материалы

- compact.md - как минимизировать извлеченный контент
- mvi-principle.md - что извлекать
- structure.md - куда помещать файлы
- creation.md - правила создания файлов
