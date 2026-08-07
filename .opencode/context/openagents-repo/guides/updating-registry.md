<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: обновление registry

**Предварительно**: сначала загрузите `core-concepts/registry.md`  
**Цель**: как обновлять registry компонентов

---

## Быстрые команды

```bash
# Auto-detect and add new components
./scripts/registry/auto-detect-components.sh --auto-add

# Validate registry
./scripts/registry/validate-registry.sh

# Dry run (see what would change)
./scripts/registry/auto-detect-components.sh --dry-run
```

---

## Когда обновлять registry

Обновляйте registry, когда вы:
- ✅ Добавляете нового агента
- ✅ Добавляете новую команду
- ✅ Добавляете новый tool
- ✅ Добавляете новый context file
- ✅ Меняете metadata компонента
- ✅ Перемещаете или переименовываете компоненты

---

## Auto-detect (рекомендуется)

### Шаг 1: dry run

```bash
# See what would be added/updated
./scripts/registry/auto-detect-components.sh --dry-run
```

**Вывод**:
```
Scanning .opencode/ for components...

Would add:
  - agent: development/api-specialist
  - context: development/api-patterns.md

Would update:
  - agent: core/openagent (description changed)
```

### Шаг 2: примените изменения

```bash
# Actually update registry
./scripts/registry/auto-detect-components.sh --auto-add
```

### Шаг 3: проверьте

```bash
# Validate registry
./scripts/registry/validate-registry.sh
```

---

## Метаданные frontmatter (извлекаются автоматически)

Скрипт auto-detect автоматически извлекает `tags` и `dependencies` из frontmatter компонента. Это **рекомендуемый способ** добавлять метаданные.

### Поддерживаемые форматы

**Многострочные массивы** (рекомендуется для читаемости):
```yaml
---
description: Your component description
tags:
  - tag1
  - tag2
  - tag3
dependencies:
  - subagent:coder-agent
  - context:core/standards/code
  - command:context
---
```

**Inline-массивы** (компактный формат):
```yaml
---
description: Your component description
tags: [tag1, tag2, tag3]
dependencies: [subagent:coder-agent, context:core/standards/code]
---
```

### Примеры для компонентов

**Command** (`.opencode/command/your-command.md`):
```yaml
---
description: Brief description of what this command does
tags:
  - category
  - feature
  - use-case
dependencies:
  - subagent:context-organizer
  - subagent:contextscout
---
```

**Subagent** (`.opencode/agent/subagents/category/your-agent.md`):
```yaml
---
id: your-agent
name: Your Agent Name
description: What this agent does
category: specialist
type: specialist
tags:
  - domain
  - capability
dependencies:
  - subagent:coder-agent
  - context:core/standards/code
---
```

**Контекст** (`.opencode/context/category/your-context.md`):
```yaml
---
description: What knowledge this context provides
tags:
  - domain
  - topic
dependencies:
  - context:core/standards/code
---
```

### Формат dependencies

Dependencies используют формат: `type:id`

**Допустимые типы**:
- `subagent:` — ссылка на subagent (например, `subagent:coder-agent`)
- `command:` — ссылка на command (например, `command:context`)
- `context:` — ссылка на context file (например, `context:core/standards/code`)
- `agent:` — ссылка на main agent (например, `agent:openagent`)

**Примеры**:
```yaml
dependencies:
  - subagent:coder-agent          # Depends on coder-agent subagent
  - context:core/standards/code   # Requires code standards context
  - command:context               # Uses context command
```

### Как это работает

1. **Создайте компонент** с frontmatter (tags + dependencies)
2. **Запустите auto-detect**: `./scripts/registry/auto-detect-components.sh --dry-run`
3. **Проверьте извлечение**: убедитесь, что tags/dependencies появились в выводе
4. **Примените изменения**: `./scripts/registry/auto-detect-components.sh --auto-add`
5. **Проверьте**: `./scripts/registry/validate-registry.sh`

Скрипт автоматически:
- ✅ Извлекает `description`, `tags`, `dependencies` из frontmatter
- ✅ Обрабатывает inline и многострочные форматы массивов
- ✅ Преобразует в корректные JSON arrays в registry
- ✅ Проверяет, что dependency references существуют

---

## Ручные обновления (не рекомендуется)

Редактируйте `registry.json` вручную только если auto-detect не работает.

**Предпочитайте frontmatter**: добавляйте tags/dependencies в frontmatter компонента, а не правьте registry напрямую.

### Ручное добавление компонента

```json
{
  "id": "agent-name",
  "name": "Agent Name",
  "type": "agent",
  "path": ".opencode/agent/category/agent-name.md",
  "description": "Brief description",
  "category": "category",
  "tags": ["tag1", "tag2"],
  "dependencies": [],
  "version": "0.5.0"
}
```

### Проверка после ручного редактирования

```bash
./scripts/registry/validate-registry.sh
```

---

## Валидация

### Что проверяется

✅ **Схема** — корректная структура JSON  
✅ **Пути** — все пути существуют  
✅ **IDs** — уникальные IDs  
✅ **Категории** — допустимые категории  
✅ **Зависимости** — зависимости существуют  

### Ошибки валидации

```bash
# Example errors
ERROR: Path does not exist: (example: .opencode/agent/core/missing.md)
ERROR: Duplicate ID: frontend-specialist
ERROR: Invalid category: invalid-category
ERROR: Missing dependency: subagent:nonexistent
```

### Исправление ошибок

1. **Путь не найден**: исправьте путь или удалите запись
2. **Дублирующийся ID**: переименуйте один компонент
3. **Неверная категория**: используйте допустимую категорию
4. **Отсутствующая зависимость**: добавьте зависимость или удалите ссылку

---

## Тестирование изменений registry

### Проверьте локально

```bash
# Test with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list

# Try installing a component
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --component agent:your-agent
```

### Убедитесь, что компонент отображается

```bash
# List all agents
cat registry.json | jq '.components.agents[].id'

# Check specific component
cat registry.json | jq '.components.agents[] | select(.id == "your-agent")'
```

---

## Частые задачи

### Добавить новый компонент в registry

```bash
# 1. Create component file with frontmatter (including tags/dependencies)
# 2. Run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add

# 3. Validate
./scripts/registry/validate-registry.sh
```

**Пример**: добавление новой command с tags/dependencies:

```bash
# 1. Create .opencode/command/my-command.md with frontmatter:
cat > .opencode/command/my-command.md << 'EOF'
---
description: My custom command description
tags: [automation, workflow]
dependencies: [subagent:coder-agent]
---

# My Command
...
EOF

# 2. Auto-detect extracts metadata
./scripts/registry/auto-detect-components.sh --dry-run

# 3. Apply changes
./scripts/registry/auto-detect-components.sh --auto-add

# 4. Validate
./scripts/registry/validate-registry.sh
```

### Обновить метаданные компонента

```bash
# 1. Update frontmatter in component file (tags, dependencies, description)
# 2. Run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add

# 3. Validate
./scripts/registry/validate-registry.sh
```

**Пример**: добавление tags к существующему компоненту:

```bash
# 1. Edit .opencode/command/existing-command.md frontmatter:
# Add or update:
#   tags: [new-tag, another-tag]
#   dependencies: [subagent:new-dependency]

# 2. Auto-detect picks up changes
./scripts/registry/auto-detect-components.sh --dry-run

# 3. Apply
./scripts/registry/auto-detect-components.sh --auto-add
```

### Удалить компонент

```bash
# 1. Delete component file
# 2. Run auto-detect (will remove from registry)
./scripts/registry/auto-detect-components.sh --auto-add

# 3. Validate
./scripts/registry/validate-registry.sh
```

---

## Интеграция CI/CD

### Автоматическая валидация

Registry проверяется при:
- Pull requests (`.github/workflows/validate-registry.yml`)
- Merges to main
- Release tags

### Автообновление при merge

Registry можно автоматически обновлять после merge:
```yaml
# .github/workflows/update-registry.yml
- name: Update Registry
  run: ./scripts/registry/auto-detect-components.sh --auto-add
```

---

## Лучшие практики

✅ **Используйте frontmatter** — добавляйте tags/dependencies в файлы компонентов, не в registry  
✅ **Используйте auto-detect** — не редактируйте registry вручную  
✅ **Проверяйте часто** — ловите проблемы рано  
✅ **Тестируйте локально** — используйте local registry для тестов  
✅ **Сначала dry run** — смотрите изменения перед применением  
✅ **Согласованность версий** — держите версии синхронизированными  
✅ **Многострочные массивы** — читаемее inline format  
✅ **Осмысленные tags** — используйте описательные, searchable tags  
✅ **Объявляйте dependencies** — помогает discovery и validation компонентов  

---

## Связанные файлы

- **Концепции registry**: `core-concepts/registry.md`
- **Добавление агентов**: `guides/adding-agent.md`
- **Диагностика**: `guides/debugging.md`

---

## Диагностика

### Поля `tags`/`dependencies` не извлекаются

**Проблема**: auto-detect не извлекает tags или dependencies из frontmatter.

**Решения**:
1. **Проверьте формат frontmatter**:
   - Должен быть в начале файла
   - Должен начинаться и заканчиваться `---`
   - Должен использовать валидный YAML syntax

2. **Проверьте формат массива**:
   ```yaml
   # ✅ Valid formats
   tags: [tag1, tag2]
   tags:
     - tag1
     - tag2
   
   # ❌ Invalid
   tags: tag1, tag2  # Missing brackets
   ```

3. **Проверьте формат dependency**:
   ```yaml
   # ✅ Valid
   dependencies: [subagent:coder-agent, context:core/standards/code]
   
   # ❌ Invalid
   dependencies: [coder-agent]  # Missing type prefix
   ```

4. **Запустите dry-run для debug**:
   ```bash
   ./scripts/registry/auto-detect-components.sh --dry-run
   # Check output shows extracted tags/dependencies
   ```

### Ошибки валидации зависимостей

**Проблема**: validation падает с ошибкой "Missing dependency".

**Решение**: убедитесь, что referenced component существует в registry:
```bash
# Check if dependency exists
jq '.components.subagents[] | select(.id == "coder-agent")' registry.json

# If missing, add the dependency component first
```

### Контекст не найден (aliases)

**Проблема**: ошибка `Could not find path for context:old-name`, хотя файл существует.

**Причина**: context file мог быть переименован, или ID в registry не совпадает с запрошенным именем.

**Решение**: добавьте alias к компоненту в `registry.json`.

1. Найдите компонент в `registry.json`
2. Добавьте `"aliases": ["old-name", "alternative-name"]`
3. Проверьте registry

---

## Управление aliases

Aliases позволяют ссылаться на компоненты по нескольким именам. Это полезно для:
- Обратной совместимости (переименованные файлы)
- Коротких ссылок
- Альтернативных соглашений об именовании

### Добавление aliases

Сейчас aliases нужно добавлять **вручную** в `registry.json` (auto-detect пока их не поддерживает).

```json
{
  "id": "session-management",
  "name": "Session Management",
  "type": "context",
  "path": ".opencode/context/core/workflows/session-management.md",
  "aliases": [
    "workflows-sessions",
    "sessions"
  ],
  ...
}
```

**Примечание**: всегда проверяйте registry после ручных правок:
```bash
./scripts/registry/validate-registry.sh
```

---

**Последнее обновление**: 2025-01-06  
**Версия**: 2.0.0
