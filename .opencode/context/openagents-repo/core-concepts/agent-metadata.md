<!-- Context: openagents-repo/core-concepts/agent-metadata | Priority: critical | Version: 1.0 | Updated: 2026-01-31 -->
# Ключевая концепция: система метаданных агентов

**Назначение**: понять централизованную систему метаданных OpenAgents Control  
**Приоритет**: CRITICAL - загрузите перед работой с метаданными агентов

---

## Что такое система метаданных агентов?

Система метаданных агентов отделяет **конфигурацию агента, совместимую с OpenCode**, от **метаданных registry OpenAgents Control**. Это решает проблему ошибок валидации OpenCode, когда агенты содержат поля не из схемы агента OpenCode.

**Ключевой принцип**: frontmatter агента содержит ТОЛЬКО валидные поля OpenCode. Все остальные метаданные находятся в централизованном файле.

---

## Какую проблему мы решили

### До (ошибки валидации)

Frontmatter агента содержал поля, которые OpenCode не распознает:

```yaml
---
id: opencoder                    # ❌ Not valid OpenCode field
name: OpenCoder                  # ❌ Not valid OpenCode field
category: core                   # ❌ Not valid OpenCode field
type: core                       # ❌ Not valid OpenCode field
version: 1.0.0                   # ❌ Not valid OpenCode field
author: opencode                 # ❌ Not valid OpenCode field
tags: [development, coding]      # ❌ Not valid OpenCode field
dependencies: []              # ❌ Not valid OpenCode field
description: "..."               # ✅ Valid OpenCode field
mode: primary                    # ✅ Valid OpenCode field
temperature: 0.1                 # ✅ Valid OpenCode field
tools: {...}                     # ✅ Valid OpenCode field
permission: {...}                # ✅ Valid OpenCode field
---
```

**Результат**: ошибки валидации OpenCode:
```
Extra inputs are not permitted, field: 'id', value: 'opencoder'
Extra inputs are not permitted, field: 'category', value: 'core'
Extra inputs are not permitted, field: 'type', value: 'core'
... (9 validation errors)
```

### После (чистое разделение)

**Frontmatter агента** (`.opencode/agent/core/opencoder.md`):
```yaml
---
# Metadata stored in: .opencode/config/agent-metadata.json
description: "Orchestration agent for complex coding, architecture, and multi-file refactoring"
mode: primary
temperature: 0.1
tools: {...}
permission: {...}
---
```

**Централизованные метаданные** (`.opencode/config/agent-metadata.json`):
```json
{
  "agents": {
    "opencoder": {
      "id": "opencoder",
      "name": "OpenCoder",
      "category": "core",
      "type": "agent",
      "version": "1.0.0",
      "author": "opencode",
      "tags": ["development", "coding", "implementation"],
      "dependencies": [
        "subagent:documentation",
        "subagent:coder-agent",
        "context:core/standards/code"
      ]
    }
  }
}
```

**Результат**: ✅ нет ошибок валидации, чистое разделение ответственности

---

## Валидные поля агента OpenCode

Согласно [документации OpenCode](https://opencode.ai/docs/agents/), это ЕДИНСТВЕННЫЕ валидные поля frontmatter:

### Обязательные поля
- `description` - когда использовать этого агента (обязательно)
- `mode` - тип агента: `primary`, `subagent` или `all` (по умолчанию `all`)

### Необязательные поля
- `model` - переопределение модели (например, `anthropic/claude-sonnet-4-20250514`)
- `temperature` - случайность ответа (0.0-1.0)
- `maxSteps` - максимум agentic-итераций
- `disable` - установите `true`, чтобы отключить агента
- `prompt` - путь к кастомному файлу промпта (например, `{file:./prompts/build.txt}`)
- `hidden` - скрыть из @ autocomplete (только subagents)
- `tools` - конфигурация доступа к инструментам
- `permission` - правила прав для инструментов (v1.1.1+, заменяет устаревшее `permissions`)

### Пример валидного frontmatter

```yaml
---
description: "Code review agent with security focus"
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  read: true
  grep: true
  glob: true
  write: false
  edit: false
permission:  # v1.1.1+ (singular, not plural)
  bash:
    "*": ask
    "git *": allow
  edit: deny
---
```

---

## Централизованный файл метаданных

**Расположение**: `.opencode/config/agent-metadata.json`

### Схема

```json
{
  "$schema": "https://opencode.ai/schemas/agent-metadata.json",
  "schema_version": "1.0.0",
  "description": "Centralized metadata for OpenAgents Control agents",
  "agents": {
    "agent-id": {
      "id": "agent-id",
      "name": "Agent Name",
      "category": "core|development|content|data|product|learning|meta",
      "type": "agent|subagent",
      "version": "1.0.0",
      "author": "opencode",
      "tags": ["tag1", "tag2"],
      "dependencies": [
        "subagent:subagent-id",
        "context:path/to/context"
      ]
    }
  },
  "defaults": {
    "agent": {
      "version": "1.0.0",
      "author": "opencode",
      "type": "agent",
      "tags": []
    },
    "subagent": {
      "version": "1.0.0",
      "author": "opencode",
      "type": "subagent",
      "tags": []
    }
  }
}
```

### Поля метаданных

| Поле | Обязательно | Описание | Пример |
|-------|----------|-------------|---------|
| `id` | Да | Уникальный идентификатор (kebab-case) | `"opencoder"` |
| `name` | Да | Отображаемое имя | `"OpenCoder"` |
| `category` | Да | Категория агента | `"core"` |
| `type` | Да | Тип компонента | `"agent"` или `"subagent"` |
| `version` | Да | Номер версии | `"1.0.0"` |
| `author` | Да | Идентификатор автора | `"opencode"` |
| `tags` | Нет | Tags для обнаружения | `["development", "coding"]` |
| `dependencies` | Нет | Зависимости компонента | `["subagent:tester"]` |

---

## Как это работает

### 1. Создание агента

При создании нового агента:

**Шаг 1**: создайте файл агента ТОЛЬКО с валидными полями OpenCode

```bash
# Create agent file
touch .opencode/agent/category/my-agent.md
```

```yaml
---
description: "My agent description"
mode: subagent
temperature: 0.2
tools:
  read: true
  write: true
---

# Agent prompt content here
```

**Шаг 2**: добавьте метаданные в `.opencode/config/agent-metadata.json`

```json
{
  "agents": {
    "my-agent": {
      "id": "my-agent",
      "name": "My Agent",
      "category": "development",
      "type": "subagent",
      "version": "1.0.0",
      "author": "opencode",
      "tags": ["custom", "helper"],
      "dependencies": ["context:core/standards/code"]
    }
  }
}
```

**Шаг 3**: запустите auto-detect для обновления registry

```bash
./scripts/registry/auto-detect-components.sh --auto-add
```

Скрипт auto-detect:
1. Читает frontmatter из файла агента (description, mode и т. д.)
2. Читает метаданные из `agent-metadata.json` (id, name, tags, dependencies)
3. Объединяет оба источника в запись registry.json

### 2. Интеграция auto-detect

Скрипт auto-detect (`scripts/registry/auto-detect-components.sh`) расширен, чтобы:

1. **Извлекать frontmatter** - читать description из файла агента
2. **Искать метаданные** - проверять `agent-metadata.json` по agent ID
3. **Объединять данные** - совмещать frontmatter + metadata
4. **Обновлять registry** - записывать полную запись в registry.json

**Фрагмент кода** (из скрипта auto-detect):

```bash
# Check if agent-metadata.json exists and merge metadata from it
local metadata_file="$REPO_ROOT/.opencode/config/agent-metadata.json"
if [ -f "$metadata_file" ] && command -v jq &> /dev/null; then
    # Try to find metadata for this agent ID
    local metadata_entry
    metadata_entry=$(jq -r ".agents[\"$id\"] // empty" "$metadata_file" 2>/dev/null)
    
    if [ -n "$metadata_entry" ] && [ "$metadata_entry" != "null" ]; then
        # Merge name, tags, dependencies from metadata
        # ...
    fi
fi
```

### 3. Вывод registry

Запись registry.json содержит объединенные данные:

```json
{
  "id": "opencoder",
  "name": "OpenCoder",
  "type": "agent",
  "path": ".opencode/agent/core/opencoder.md",
  "description": "Orchestration agent for complex coding...",
  "category": "core",
  "tags": ["development", "coding", "implementation"],
  "dependencies": [
    "subagent:documentation",
    "subagent:coder-agent",
    "context:core/standards/code"
  ]
}
```

---

## Процесс

### Добавление нового агента

```bash
# 1. Create agent file (OpenCode-compliant frontmatter only)
vim .opencode/agent/category/my-agent.md

# 2. Add metadata entry
vim .opencode/config/agent-metadata.json

# 3. Update registry
./scripts/registry/auto-detect-components.sh --auto-add

# 4. Validate
./scripts/registry/validate-registry.sh
```

### Обновление метаданных агента

**Чтобы обновить конфигурацию OpenCode** (tools, permissions, temperature):
```bash
# Edit agent file frontmatter
vim .opencode/agent/category/my-agent.md
```

**Чтобы обновить метаданные registry** (tags, dependencies, version):
```bash
# Edit metadata file
vim .opencode/config/agent-metadata.json

# Re-run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add
```

### Обновление зависимостей

**Добавить зависимость**:
```json
{
  "agents": {
    "my-agent": {
      "dependencies": [
        "subagent:tester",
        "context:core/standards/code",
        "subagent:new-dependency"  // ← Add here
      ]
    }
  }
}
```

Затем запустите:
```bash
./scripts/registry/auto-detect-components.sh --auto-add
./scripts/registry/validate-registry.sh
```

---

## Преимущества

### ✅ Соответствие OpenCode
- Frontmatter агента содержит ТОЛЬКО валидные поля OpenCode
- Нет ошибок валидации от OpenCode
- Агенты корректно работают с OpenCode CLI

### ✅ Совместимость registry
- Registry по-прежнему содержит все метаданные (id, name, category, tags, dependencies)
- Скрипт auto-detect объединяет frontmatter + metadata
- Обратная совместимость с существующими tools

### ✅ Единый источник истины
- Метаданные централизованы в одном файле
- Легко обновлять зависимости сразу у нескольких агентов
- Четкое разделение: конфиг OpenCode vs. метаданные registry

### ✅ Поддерживаемость
- Обновление зависимостей в одном месте
- Консистентные метаданные у всех агентов
- Легко добавлять новые поля метаданных

### ✅ Валидация
- OpenCode валидирует frontmatter (без лишних полей)
- Registry validator проверяет, что зависимости существуют
- Понятные сообщения об ошибках при отсутствии метаданных

---

## Руководство по миграции

### Миграция с permissions (мн. число) на permission (ед. число)

**Изменение OpenCode v1.1.1+**: имя поля изменилось с `permissions:` (мн. число) на `permission:` (ед. число).

**До** (устарело):
```yaml
permissions:
  bash:
    "*": "deny"
```

**После** (v1.1.1+):
```yaml
permission:
  bash:
    "*": "deny"
```

**Шаги миграции**:
1. Найдите всех агентов, использующих `permissions:` (мн. число)
   ```bash
   grep -r "^permissions:" .opencode/agent/
   ```

2. Замените на `permission:` (ед. число) в каждом файле

3. Убедитесь, что ошибок валидации нет:
   ```bash
   opencode agent validate
   ```

### Миграция существующих агентов

**Шаг 1**: найдите агентов с лишними полями

```bash
# Find agents with invalid OpenCode fields
grep -r "^id:\|^name:\|^category:\|^type:\|^version:\|^author:\|^tags:\|^dependencies:" .opencode/agent/
```

**Шаг 2**: извлеките метаданные в `agent-metadata.json`

Для каждого агента:
1. Скопируйте `id`, `name`, `category`, `type`, `version`, `author`, `tags`, `dependencies` в файл метаданных
2. Удалите эти поля из frontmatter агента
3. Оставьте во frontmatter ТОЛЬКО валидные поля OpenCode

**Шаг 3**: обновите registry

```bash
# Remove old entries
jq 'del(.components.agents[] | select(.id == "agent-id"))' registry.json > tmp.json && mv tmp.json registry.json

# Re-add with new metadata
./scripts/registry/auto-detect-components.sh --auto-add
```

**Шаг 4**: валидируйте

```bash
./scripts/registry/validate-registry.sh
```

---

## Лучшие практики

### Frontmatter агента

✅ **Делайте**:
- Держите frontmatter минимальным (только поля OpenCode)
- Добавляйте комментарий со ссылкой на файл метаданных
- Используйте единое форматирование

❌ **Не делайте**:
- Не добавляйте кастомные поля во frontmatter
- Не дублируйте метаданные в двух местах
- Не пропускайте файл метаданных

### Файл метаданных

✅ **Делайте**:
- Храните файл метаданных в version control
- Обновляйте метаданные при добавлении/удалении зависимостей
- Используйте единое именование (kebab-case для IDs)
- Документируйте, зачем нужны зависимости

❌ **Не делайте**:
- Не забывайте обновлять метаданные при создании агентов
- Не оставляйте orphaned entries (агенты, которых не существует)
- Не пропускайте валидацию после обновлений

### Зависимости

✅ **Делайте**:
- Объявляйте ВСЕ зависимости (subagents, contexts)
- Используйте корректный формат: `type:id`
- Валидируйте, что зависимости существуют в registry

❌ **Не делайте**:
- Не ссылайтесь на компоненты без объявления зависимости
- Не используйте неверные форматы зависимостей
- Не забывайте обновлять при изменении зависимостей

---

## Диагностика

### Ошибки валидации OpenCode

**Проблема**: `Extra inputs are not permitted, field: 'id'`

**Решение**: удалите невалидные поля из frontmatter агента и добавьте их в файл метаданных

```bash
# 1. Edit agent file - remove id, name, category, type, version, author, tags, dependencies
vim .opencode/agent/category/agent.md

# 2. Add to metadata file
vim .opencode/config/agent-metadata.json

# 3. Update registry
./scripts/registry/auto-detect-components.sh --auto-add
```

### Отсутствующие метаданные

**Проблема**: auto-detect не может найти метаданные агента

**Решение**: добавьте запись в `agent-metadata.json`

```json
{
  "agents": {
    "agent-id": {
      "id": "agent-id",
      "name": "Agent Name",
      "category": "core",
      "type": "agent",
      "version": "1.0.0",
      "author": "opencode",
      "tags": [],
      "dependencies": []
    }
  }
}
```

### Registry не синхронизирован

**Проблема**: registry содержит старые метаданные

**Решение**: удалите запись и повторно запустите auto-detect

```bash
# Remove old entry
jq 'del(.components.agents[] | select(.id == "agent-id"))' registry.json > tmp.json && mv tmp.json registry.json

# Re-add with current metadata
./scripts/registry/auto-detect-components.sh --auto-add
```

---

## Связанные файлы

- **Документация агентов OpenCode**: https://opencode.ai/docs/agents/
- **Система registry**: `.opencode/context/openagents-repo/core-concepts/registry.md`
- **Добавление агентов**: `.opencode/context/openagents-repo/guides/adding-agent-basics.md`
- **Зависимости**: `.opencode/context/openagents-repo/quality/registry-dependencies.md`

---

**Последнее обновление**: 2026-01-31  
**Версия**: 1.0.0
