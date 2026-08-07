---
id: analyze-patterns
name: analyze-patterns
description: "Analyze codebase for patterns and similar implementations"
type: command
category: analysis
version: 1.0.0
---

# Команда: analyze-patterns

## Описание

Анализирует codebase на повторяющиеся patterns, похожие реализации и возможности для refactoring. Заменяет функциональность subagent `codebase-pattern-analyst` через command-based интерфейс.

## Использование

```bash
/analyze-patterns [--pattern=<pattern>] [--language=<lang>] [--depth=<level>] [--output=<format>]
```

## Параметры

| Параметр     | Тип    | Обязательный | Описание                                                                                       |
| ------------ | ------ | ------------ | ---------------------------------------------------------------------------------------------- |
| `--pattern`  | string | Нет          | Название pattern или regex для поиска, например `"singleton"`, `"factory"`, `"error-handling"` |
| `--language` | string | Нет          | Фильтрация по языку: js, ts, py, go, rust, java и т. д.                                        |
| `--depth`    | string | Нет          | Глубина поиска: shallow (текущая директория) | medium (`src/`) | deep (весь repository)        |
| `--output`   | string | Нет          | Формат вывода: text (по умолчанию) | json | markdown                                           |

## Поведение

### Поиск Patterns

* Ищет совпадения patterns в codebase с помощью regex + semantic analysis
* Определяет похожие реализации в разных файлах
* Группирует результаты по типу pattern + similarity score
* Предлагает возможности для refactoring

### Результат анализа

* Найденные вхождения pattern с расположением файлов + номерами строк
* Метрики similarity — насколько реализации похожи друг на друга
* Предложения по refactoring — consolidate, extract, standardize
* Информация о качестве кода — duplication, inconsistency

### Формат результата

```text
Отчёт по анализу Patterns
=========================

Pattern: [pattern_name]
Вхождений: [count]
Файлы: [file_list]

Реализации:
  1. [file:line] - [описание] (similarity: X%)
  2. [file:line] - [описание] (similarity: Y%)
  ...

Предложения по Refactoring:
  - [предложение 1]
  - [предложение 2]
  ...

Наблюдения по качеству:
  - [наблюдение 1]
  - [наблюдение 2]
  ...
```

## Примеры

### Найти все patterns обработки ошибок

```bash
/analyze-patterns --pattern="error-handling" --language=ts
```

### Проанализировать factory patterns во всём codebase

```bash
/analyze-patterns --pattern="factory" --depth=deep --output=json
```

### Найти похожие реализации API endpoints

```bash
/analyze-patterns --pattern="api-endpoint" --language=js --output=markdown
```

### Найти singleton patterns

```bash
/analyze-patterns --pattern="singleton" --depth=medium
```

## Реализация

### Делегирование

* Делегирует выполнение: **opencoder** (основной агент)
* Использует возможности context search для поиска patterns
* Возвращает структурированные результаты анализа patterns

### Требования к Context

* Структура codebase + организация файлов
* Language-specific patterns + conventions
* Project-specific naming conventions
* Существующие guidelines по refactoring

### Этапы обработки

1. Распарсить параметры команды
2. Проверить корректность синтаксиса pattern — regex или predefined
3. Выполнить поиск по codebase с помощью инструментов glob + grep
4. Проанализировать semantic similarity найденных совпадений
5. Сгруппировать результаты по pattern + similarity
6. Сформировать предложения по refactoring
7. Отформатировать результат в соответствии с указанным форматом
8. Вернуть отчёт анализа

## Предопределённые Patterns

### JavaScript/TypeScript

* `singleton` — реализации Singleton pattern
* `factory` — реализации Factory pattern
* `observer` — реализации Observer/event pattern
* `error-handling` — patterns обработки ошибок
* `async-patterns` — patterns Promise/async-await
* `api-endpoint` — определения API endpoints
* `middleware` — реализации Middleware

### Python

* `decorator` — реализации Decorator pattern
* `context-manager` — Context Manager patterns
* `error-handling` — patterns обработки exceptions
* `async-patterns` — Async/await patterns
* `class-patterns` — patterns проектирования классов

### Go

* `interface-patterns` — реализации interfaces
* `error-handling` — patterns обработки ошибок
* `goroutine-patterns` — patterns использования goroutines
* `middleware` — реализации Middleware

### Пользовательские Patterns

Пользователи могут передавать собственные regex patterns для domain-specific анализа.

## Форматы вывода

### Text (по умолчанию)

Читаемый человеком отчёт с понятными разделами и форматированием.

### JSON

Структурированные данные для программной обработки:

```json
{
  "pattern": "error-handling",
  "occurrences": 12,
  "files": ["file1.ts", "file2.ts"],
  "implementations": [
    {
      "file": "file1.ts",
      "line": 42,
      "description": "try-catch block",
      "similarity": 0.95
    }
  ],
  "suggestions": ["Consolidate error handling", "Extract to utility"]
}
```

### Markdown

Формат для документации и распространения:

```markdown
# Анализ Pattern: error-handling

**Вхождений**: 12  
**Файлов**: 3  
**Диапазон Similarity**: 85-98%

## Реализации
...
```

## Интеграция

### Registry Entry

```json
{
  "id": "analyze-patterns",
  "name": "analyze-patterns",
  "type": "command",
  "category": "analysis",
  "description": "Analyze codebase for patterns and similar implementations",
  "delegates_to": ["opencoder"],
  "parameters": ["pattern", "language", "depth", "output"]
}
```

### Назначение Profiles

* **Developer Profile**: ✅ Включён
* **Full Profile**: ✅ Включён
* **Advanced Profile**: ✅ Включён
* **Business Profile**: ❌ Не включён

## Примечания

* Заменяет функциональность subagent `codebase-pattern-analyst`
* Command-based интерфейс более гибкий и удобный для обнаружения
* Поддерживает как predefined, так и custom patterns
* Результаты можно экспортировать для документации
* Интегрируется с workflows по refactoring

---

## Checklist валидации

✅ Структура команды определена
✅ Параметры задокументированы
✅ Поведение описано
✅ Примеры добавлены
✅ Детали реализации указаны
✅ Форматы вывода определены
✅ Интеграция подготовлена
✅ Готово к интеграции с registry

**Status**: Ready for deployment
