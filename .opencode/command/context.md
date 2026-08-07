---
description: Context system manager - harvest summaries, extract knowledge, organize context
tags:
  - context
  - knowledge-management
  - harvest
dependencies:
  - subagent:context-organizer
  - subagent:contextscout
---

# Context Manager

<critical_rules priority="absolute" enforcement="strict">

Файлы ДОЛЖНЫ содержать <200 строк. Извлекай только ключевые концепции: 1–3 предложения, 3–5 основных пунктов, минимальный пример и reference link.

<execution_priority>

- Файлы <200 строк (@critical_rules.mvi_strict)
- Показывать подтверждение перед cleanup (@critical_rules.approval_gate)
- Использовать function-based структуру (@critical_rules.function_structure)
- Загружать context перед выполнением операций (@critical_rules.lazy_load)

- Workflows: Harvest (по умолчанию), Extract, Organize, Update

- Cross-references, validation, navigation

<conflict_resolution>
Tier 1 всегда имеет приоритет над Tier 2/3.
</conflict_resolution>
</execution_priority>

**Arguments**: `$ARGUMENTS`

---

## Поведение по умолчанию (без аргументов)

При вызове без аргументов: `/context`

```text
Найдено 3 summary-файла:
  📄 CONTEXT-SYSTEM-OVERVIEW.md (4.2 KB)
  📄 SESSION-auth-work.md (1.8 KB)
  📄 .tmp/NOTES.md (800 bytes)

Рекомендуемое действие:
  /context harvest  - Очистить summaries → перенести в постоянный context

Другие варианты:
  /context extract {source}  - Извлечь context из docs/code
  /context organize {category}  - Реструктурировать существующие файлы
  /context help  - Показать все операции
```

**Purpose**: Быстрая очистка и упорядочивание. По умолчанию предполагается, что пользователь хочет обработать summaries и сделать workspace компактнее.

---

## Операции

### Основная: Harvest & Compact (фокус по умолчанию)

**`/context harvest [path]`** ⭐ Используется чаще всего

* Извлекает знания из AI summaries → сохраняет их в постоянный context
* Очищает workspace — архивирует/удаляет summaries
* **Читает**: `operations/harvest.md` + `standards/mvi.md`

**`/context compact {file}`**

* Сжимает подробный файл до формата MVI
* **Читает**: `guides/compact.md` + `standards/mvi.md`

---

### Дополнительная: Создание пользовательского Context

**`/context extract from {source}`**

* Извлекает context из docs/code/URLs
* **Читает**: `operations/extract.md` + `standards/mvi.md` + `guides/compact.md`

**`/context organize {category}`**

* Преобразует плоскую структуру файлов → function-based folders
* **Читает**: `operations/organize.md` + `standards/structure.md`

**`/context update for {topic}`**

* Обновляет context при изменении APIs/frameworks
* **Читает**: `operations/update.md` + `guides/workflows.md`

**`/context error for {error}`**

* Добавляет повторяющуюся ошибку в knowledge base
* **Читает**: `operations/error.md` + `standards/templates.md`

**`/context create {category}`**

* Создаёт новую context-категорию с необходимой структурой
* **Читает**: `guides/creation.md` + `standards/structure.md` + `standards/templates.md`

---

### Migration

**`/context migrate`**

* Копирует project-intelligence из global (`~/.config/opencode/context/`) в local (`.opencode/context/`)
* Для пользователей, которые установили систему глобально, но хотят project-specific context, хранящийся в git
* Показывает diff, если local-файлы уже существуют, и запрашивает подтверждение перед перезаписью
* Опционально очищает global project-intelligence после migration
* **Читает**: `standards/mvi.md`

---

### Вспомогательные операции

**`/context map [category]`**

* Показывает текущую структуру context и количество файлов

**`/context validate`**

* Проверяет целостность, references и размеры файлов

**`/context help`**

* Показывает все операции с примерами

---

## Стратегия Lazy Loading

<lazy_load_map>

Читать: `operations/harvest.md`, `standards/mvi.md`

**Все файлы расположены в**: `.opencode/context/core/context-system/`

---

## Маршрутизация Subagents

<subagent_routing>

---

## Краткий справочник

### Структура

```text
.opencode/context/core/context-system/
├── operations/     # Как выполнять операции (harvest, extract, organize, update)
├── standards/      # Каким правилам следовать (mvi, structure, templates)
└── guides/         # Пошаговые инструкции (workflows, compact, creation)
```

### Принцип MVI (кратко)

* Ключевая концепция: 1–3 предложения
* Основные пункты: 3–5 bullets
* Минимальный пример: <10 строк
* Reference link: ссылка на полную документацию
* Размер файла: <200 строк

### Function-Based Structure (кратко)

```text
{category}/
├── navigation.md   # Навигация
├── concepts/       # Что это такое
├── examples/       # Рабочий код
├── guides/         # Как использовать
├── lookup/         # Быстрый справочник
└── errors/         # Распространённые проблемы
```

---

## Примеры

### По умолчанию (быстрое сканирование)

```bash
/context
# Сканирует workspace и предлагает harvest, если найдены summaries
```

### Harvest Summaries

```bash
/context harvest
/context harvest .tmp/
/context harvest OVERVIEW.md
```

### Извлечение из Docs

```bash
/context extract from docs/api.md
/context extract from https://react.dev/hooks
```

### Организация существующих файлов

```bash
/context organize development/
/context organize development/ --dry-run
```

### Обновление при изменениях

```bash
/context update for Next.js 15
/context update for React 19 breaking changes
```

### Migration из Global в Local

```bash
/context migrate
# Копирует project-intelligence из ~/.config/opencode/context/ в .opencode/context/
# Показывает, что будет скопировано, и запрашивает подтверждение перед выполнением
```

---

## Критерии успешного выполнения

После любой операции:

* [ ] Все файлы <200 строк? (@critical_rules.mvi_strict)
* [ ] Используется function-based структура? (@critical_rules.function_structure)
* [ ] Для destructive operations показан approval UI? (@critical_rules.approval_gate)
* [ ] Необходимый context загружен? (@critical_rules.lazy_load)
* [ ] navigation.md обновлён?
* [ ] Файлы просматриваются менее чем за 30 секунд?

---

## Полная документация

**Расположение Context System**: `.opencode/context/core/context-system/`

**Структура**:

* `operations/` — подробные workflows операций
* `standards/` — MVI, structure, templates
* `guides/` — интерактивные примеры и стандарты создания

**Прочитать перед использованием**: `standards/mvi.md` — описание принципа Minimal Viable Information
