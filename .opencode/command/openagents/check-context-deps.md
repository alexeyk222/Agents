---
description: Validate context file dependencies across agents and registry
tags:
  - registry
  - validation
  - context
  - dependencies
  - openagents
dependencies:
  - command:analyze-patterns
---

# Check Context Dependencies

**Purpose**: Убедиться, что агенты корректно объявляют зависимости от context-файлов в frontmatter и registry.

**Arguments**: `$ARGUMENTS`

---

## Что делает команда

Проверяет согласованность между:

1. **Фактическим использованием** — context-файлы, на которые ссылаются agent prompts
2. **Объявленными зависимостями** — зависимости в agent frontmatter
3. **Записями Registry** — зависимости в `registry.json`

**Определяет**:

* ✅ Отсутствующие объявления зависимостей — агент использует context, но не объявляет его
* ✅ Неиспользуемые context-файлы — существуют, но ни один агент на них не ссылается
* ✅ Сломанные ссылки — на файл ссылаются, но он не существует
* ✅ Несоответствия формата — используется неправильный формат зависимости

---

## Использование

```bash
# Проанализировать всех агентов
/check-context-deps

# Проанализировать конкретного агента
/check-context-deps contextscout

# Автоматически исправить отсутствующие зависимости
/check-context-deps --fix

# Подробный вывод (показать все места ссылок)
/check-context-deps --verbose

# Комбинировать флаги
/check-context-deps contextscout --verbose
```

---

## Рабочий процесс

<workflow id="analyze_context_dependencies">
  <stage id="1" name="ScanAgents" required="true">
    Просканировать agent-файлы на наличие ссылок на context:

```
**Шаблоны поиска**:
- `.opencode/context/` — прямые ссылки на пути
- `@.opencode/context/` — ссылки с символом @
- `context:` — объявления зависимостей во frontmatter

**Расположение**:
- `.opencode/agent/**/*.md` — все agents и subagents
- `.opencode/command/**/*.md` — команды, использующие context

**Извлечь**:
- ID агента/команды
- Путь к context-файлу
- Номер строки
- Тип ссылки (path, @-reference, dependency)
```

  </stage>

  <stage id="2" name="CheckRegistry" required="true">
    Для каждого найденного агента проверить `registry.json`:

````
```bash
jq '.components.agents[] | select(.id == "AGENT_ID") | .dependencies' registry.json
jq '.components.subagents[] | select(.id == "AGENT_ID") | .dependencies' registry.json
```

**Проверить**:
- Есть ли у агента массив dependencies?
- Объявлены ли ссылки на context-файлы в формате `context:core/standards/code`?
- Корректен ли формат зависимостей (`context:path/to/file`)?
````

  </stage>

  <stage id="3" name="ValidateContextFiles" required="true">
    Для каждого упомянутого context-файла:

````
**Проверить существование**:

```bash
test -f .opencode/context/core/standards/code-quality.md
```

**Проверить registry**:

```bash
jq '.components.contexts[] | select(.id == "core/standards/code")' registry.json
```

**Определить проблемы**:
- На context-файл ссылаются, но он не существует
- Context-файл существует, но отсутствует в registry
- Context-файл есть в registry, но нигде не используется
````

  </stage>

  <stage id="4" name="Report" required="true">
    Сформировать подробный отчёт:

````
```markdown
# Отчёт по анализу зависимостей Context

## Сводка

- Просканировано агентов: 25
- Упомянуто context-файлов: 12
- Отсутствующих зависимостей: 8
- Неиспользуемых context-файлов: 2
- Отсутствующих context-файлов: 0

## Отсутствующие зависимости
(агенты используют context, но не объявляют его)

### opencoder

**Используется, но не объявлено**:
- context:core/standards/code (упоминается 3 раза)
  - Строка 64: "Code tasks → .opencode/context/core/standards/code-quality.md (MANDATORY)"
  - Строка 170: "Read .opencode/context/core/standards/code-quality.md NOW"
  - Строка 229: "NEVER execute write/edit without loading required context first"

**Текущие зависимости**:
subagent:task-manager, subagent:coder-agent

**Рекомендуемое исправление**:
Добавить во frontmatter:

```yaml
dependencies:
  - subagent:task-manager
  - subagent:coder-agent
  - context:core/standards/code  # ДОБАВИТЬ
```

### openagent

**Используется, но не объявлено**:
- context:core/standards/code (упоминается 5 раз)
- context:core/standards/docs (упоминается 3 раза)
- context:core/standards/tests (упоминается 3 раза)
- context:core/workflows/review (упоминается 2 раза)
- context:core/workflows/delegation (упоминается 4 раза)

**Рекомендуемое исправление**:
Добавить во frontmatter:

```yaml
dependencies:
  - subagent:task-manager
  - subagent:documentation
  - context:core/standards/code
  - context:core/standards/docs
  - context:core/standards/tests
  - context:core/workflows/review
  - context:core/workflows/delegation
```

## Неиспользуемые Context Files
(существуют, но ни один агент на них не ссылается)

- context:core/standards/analysis (0 ссылок)
- context:core/workflows/sessions (0 ссылок)

**Рекомендация**:
Рассмотреть удаление или задокументировать предполагаемое использование

## Отсутствующие Context Files
(на них ссылаются, но они не существуют)

Не найдено ✅

## Карта использования Context Files

| Context File | Используется | Количество ссылок |
|--------------|--------------|-------------------|
| core/standards/code | opencoder, openagent, frontend-specialist, reviewer | 15 |
| core/standards/docs | openagent, documentation, technical-writer | 8 |
| core/standards/tests | openagent, tester | 6 |
| core/workflows/delegation | openagent, task-manager | 5 |
| core/workflows/review | openagent, reviewer | 4 |

---

## Следующие шаги

1. Проверить перечисленные выше отсутствующие зависимости
2. Выполнить `/check-context-deps --fix` для автоматического обновления frontmatter
3. Выполнить `./scripts/registry/auto-detect-components.sh` для обновления registry
4. Проверить результат через `./scripts/registry/validate-registry.sh`
```
````

  </stage>

  <stage id="5" name="Fix" when="--fix flag provided">
    Для каждого агента с отсутствующими context-зависимостями:

````
1. Прочитать agent-файл
2. Распарсить frontmatter YAML
3. Добавить отсутствующие context dependencies в массив dependencies
4. Сохранить существующие зависимости
5. Записать обновлённый файл
6. Сообщить, что было изменено

**Пример**:

```diff
---
id: opencoder
dependencies:
  - subagent:task-manager
  - subagent:coder-agent
+ - context:core/standards/code
---
```

**Безопасность**:
- Добавляй только те dependencies, на которые действительно есть ссылки в файле
- Не удаляй существующие dependencies
- Сохраняй форматирование frontmatter
- Перед применением показывай diff, если работа выполняется в интерактивном режиме
````

  </stage>
</workflow>

---

## Детали реализации

### Шаблоны поиска

**Найти прямые ссылки на пути**:

```bash
grep -rn "\\.opencode/context/" .opencode/agent/ .opencode/command/
```

**Найти @ references**:

```bash
grep -rn "@\\.opencode/context/" .opencode/agent/ .opencode/command/
```

**Найти объявления dependencies**:

```bash
grep -rn "^\s*-\s*context:" .opencode/agent/ .opencode/command/
```

### Нормализация путей

**Преобразование в формат dependency**:

* `.opencode/context/core/standards/code-quality.md` → `context:core/standards/code`
* `@.opencode/context/openagents-repo/quick-start.md` → `context:openagents-repo/quick-start`
* `context/core/standards/code` → `context:core/standards/code`

**Правила**:

1. Удалить префикс `.opencode/`
2. Удалить расширение `.md`
3. Добавить префикс `context:` для dependencies

### Поиск в Registry

**Проверить наличие context-файла в registry**:

```bash
jq '.components.contexts[] | select(.id == "core/standards/code")' registry.json
```

**Получить dependencies агента**:

```bash
jq '.components.agents[] | select(.id == "opencoder") | .dependencies[]?' registry.json
```

---

## Делегирование

Эта команда делегирует выполнение работы analysis-агенту:

```javascript
task(
  subagent_type="PatternAnalyst",
  description="Analyze context dependencies",
  prompt=`
    Analyze context file usage across all agents in this repository.

    TASK:
    1. Use grep to find all references to context files in:
       - .opencode/agent/**/*.md
       - .opencode/command/**/*.md

    2. Search for these patterns:
       - ".opencode/context/core/" (direct paths)
       - "@.opencode/context/" (@ references)
       - "context:" in frontmatter (dependency declarations)

    3. For each agent file found:
       - Extract agent ID from frontmatter
       - List all context files it references
       - Check registry.json for declared dependencies
       - Identify missing dependency declarations

    4. For each context file in .opencode/context/core/:
       - Count how many agents reference it
       - Check if it exists in registry.json
       - Identify unused context files

    5. Generate a comprehensive report showing:
       - Agents with missing context dependencies
       - Unused context files
       - Missing context files (referenced but don't exist)
       - Context file usage map (which agents use which files)

    ${ARGUMENTS.includes('--fix') ? `
    6. AUTO-FIX MODE:
       - Update agent frontmatter to add missing context dependencies
       - Use format: context:core/standards/code
       - Preserve existing dependencies
       - Show what was changed
    ` : ''}

    ${ARGUMENTS.includes('--verbose') ? `
    VERBOSE MODE: Include all reference locations (file:line) in report
    ` : ''}

    ${ARGUMENTS.length > 0 && !ARGUMENTS.includes('--') ? `
    FILTER: Only analyze agent: ${ARGUMENTS[0]}
    ` : ''}

    REPORT FORMAT:
    - Summary statistics
    - Missing dependencies by agent (with recommended fixes)
    - Unused context files
    - Context file usage map
    - Next steps

    DO NOT make changes without --fix flag.
    ALWAYS show what would be changed before applying fixes.
  `
)
```

---

## Примеры

### Пример 1: Базовый анализ

```bash
/check-context-deps
```

**Вывод**:

```text
Анализ использования context-файлов среди 25 агентов...

Найдено 8 агентов с отсутствующими context dependencies:
- opencoder: отсутствует context:core/standards/code
- openagent: отсутствует 5 context dependencies
- frontend-specialist: отсутствует context:core/standards/code
...

Выполни /check-context-deps --fix для автоматического обновления frontmatter
```

### Пример 2: Анализ конкретного агента

```bash
/check-context-deps contextscout
```

**Вывод**:

```text
Анализ агента: contextscout

Упомянутые context-файлы:
✓ .opencode/context/core/context-system.md (1 ссылка)
  - Строка 15: "Load: context:core/context-system"

✓ .opencode/context/core/context-system/standards/mvi.md (2 ссылки)
  - Строка 16: "Load: context:core/context-system/standards/mvi"
  - Строка 89: "MVI-aware prioritization"

Dependencies в Registry:
✓ context:core/context-system DECLARED
✓ context:core/context-system/standards/mvi DECLARED

Все зависимости объявлены корректно ✅
```

### Пример 3: Auto-Fix

```bash
/check-context-deps --fix
```

**Вывод**:

```text
Анализ и исправление context dependencies...

Обновлён opencoder:
+ Добавлено: context:core/standards/code

Обновлён openagent:
+ Добавлено: context:core/standards/code
+ Добавлено: context:core/standards/docs
+ Добавлено: context:core/standards/tests
+ Добавлено: context:core/workflows/review
+ Добавлено: context:core/workflows/delegation

Итого: обновлено 2 агента, добавлено 6 dependencies

Далее: выполни ./scripts/registry/auto-detect-components.sh для обновления registry
```

---

## Критерии успешного выполнения

✅ Все агенты, которые ссылаются на context-файлы, объявляют их в dependencies

✅ Все context-файлы из registry действительно используются хотя бы одним агентом

✅ Нет сломанных ссылок — все упомянутые context-файлы существуют

✅ Формат dependencies единообразен: `context:path/to/file`

---

## Примечания

* **По умолчанию read-only** — команда только сообщает о найденных проблемах и не изменяет файлы
* **Используй `--fix` для обновления** — автоматически добавляет отсутствующие dependencies во frontmatter
* **После исправления** — выполни `./scripts/registry/auto-detect-components.sh --auto-add` для синхронизации registry
* **Формат dependency** — `context:path/to/file` без префикса `.opencode/` и без расширения `.md`
* **Сканируются оба варианта** — прямые ссылки на пути и @ references

## Связанные инструменты

* **Проверка Registry**: `./scripts/registry/validate-registry.sh`
* **Auto-detect components**: `./scripts/registry/auto-detect-components.sh`
* **Context guide**: `.opencode/context/openagents-repo/quality/registry-dependencies.md`
