<!-- Context: core/extract | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Extract

**Назначение**: извлекать контекст из документации, кода или URL в организованные файлы контекста

**Последнее обновление**: 2026-01-06

---

## Когда использовать

- Извлечение из документации (документация React, API-документация и т. д.)
- Извлечение из кодовой базы (паттерны, соглашения)
- Извлечение из URL (посты в блогах, руководства)
- Создание начального контекста для новых тем

---

## 7-этапный workflow

### Этап 1: прочитать источник
```
/context extract from https://react.dev/hooks
  ↓
Agent: "Reading source (8,500 lines)...
Analyzing content for extractable items..."
```

**Действие**: прочитать и проанализировать исходный материал

---

### Этап 2: проанализировать и категоризировать
**Действие**: извлечь и категоризировать контент по функции

**Категоризация**:
- Дизайн-решения → `concepts/`
- Рабочий код → `examples/`
- Пошаговые процессы → `guides/`
- Справочные данные (команды, пути) → `lookup/`
- Ошибки/подводные камни → `errors/`

**Выход**: список извлекаемых элементов с предварительными просмотрами

---

### Этап 3: выбрать категорию (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: пользователь выбирает целевую категорию и элементы

**Формат**:
```
Found 12 extractable items from {source}:

Concepts (8):
  ✓ [A] useState - State management hook
  ✓ [B] useEffect - Side effects hook
  ... (6 more)

Errors (4):
  ✓ [I] Hooks called conditionally
  ✓ [J] Hooks in loops
  ... (2 more)

Which category?
  [1] development/
  [2] core/
  [3] Create new category: ___

Select items (A B I or 'all') + category (1/2/3):
```

**Валидация**: ОБЯЗАТЕЛЬНО дождаться ввода пользователя перед продолжением

---

### Этап 4: предварительный просмотр (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать, что будет создано, проверить конфликты

**Формат**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extraction Plan: development/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CREATE (new files):
  concepts/use-state.md (45 lines)
  concepts/use-effect.md (52 lines)
  concepts/use-context.md (38 lines)
  ... (6 more)
  guides/custom-hooks.md (87 lines)
  guides/debugging-hooks.md (65 lines)

ADD TO (existing files):
  errors/react-hooks-errors.md (98 → 124 lines)
    + 4 new error entries

⚠️  CONFLICT (file already exists):
  concepts/use-memo.md already exists (42 lines)
    Options:
      [A] Skip — keep existing file
      [B] Overwrite — replace with extracted version
      [C] Merge — add new content to existing file (42 → 58 lines)
    Choose [A/B/C]: _

NAVIGATION UPDATE:
  development/navigation.md
    + 9 new entries in Concepts table
    + 2 new entries in Guides table
    + 1 updated entry in Errors table

Total: 12 files, ~650 lines

Preview content? (type filename, 'all' for batch, or 'skip')
Approve? [y/n/edit]: _
```

**Если пользователь вводит `all`**: последовательно показать первые 10 строк каждого файла
**Если пользователь вводит имя файла**: показать полное содержимое этого файла
**Если пользователь вводит `skip`**: перейти к одобрению

**Валидация**: ОБЯЗАТЕЛЬНО получить одобрение перед продолжением

---

### Этап 5: создать
**Действие**: создать файлы в функциональных папках

**Процесс**:
1. Применить формат MVI (1–3 предложения, 3–5 ключевых пунктов, минимальный пример)
2. Создать файлы в правильных функциональных папках
3. Убедиться, что все файлы <200 строк
4. Добавить перекрестные ссылки

**Обеспечение**: `@critical_rules.mvi_strict` + `@critical_rules.function_structure`

---

### Этап 6: обновить навигацию (предварительный просмотр включен в этап 4)
**Действие**: обновить `navigation.md` и добавить перекрестные ссылки

**Процесс**:
1. Обновить `navigation.md` категории новыми файлами (как в предварительном просмотре этапа 4)
2. Добавить уровни приоритета (critical/high/medium/low)
3. Добавить перекрестные ссылки между связанными файлами
4. Обновить даты "Last Updated"

---

### Этап 7: отчет
**Действие**: показать полные результаты

**Формат**:
```
✅ Extracted X items into {category}
📄 Created Y files
📊 Updated {category}/README.md

Files created:
  - {category}/concepts/ (N files)
  - {category}/examples/ (N files)
  - {category}/errors/ (N files)
```

---

## Примеры

### Извлечь из URL
```bash
/context extract from https://react.dev/hooks
```

### Извлечь из локальных docs
```bash
/context extract from docs/api.md
/context extract from docs/architecture/
```

### Извлечь из кода
```bash
/context extract from src/utils/
```

---

## Критерии успеха

- [ ] Все файлы <200 строк?
- [ ] Формат MVI применен (1–3 предложения, 3–5 пунктов, пример, ссылка)?
- [ ] Файлы в правильных функциональных папках?
- [ ] `README.md` обновлен?
- [ ] Перекрестные ссылки добавлены?
- [ ] Пользователь одобрил перед созданием?

---

## Связанные материалы

- standards/mvi.md - что извлекать
- guides/compact.md - как минимизировать
- guides/workflows.md - интерактивные примеры
