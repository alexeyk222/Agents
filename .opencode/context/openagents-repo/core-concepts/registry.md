<!-- Context: openagents-repo/registry | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Ключевая концепция: система registry

**Назначение**: понять, как работают отслеживание и распространение компонентов  
**Приоритет**: CRITICAL - загрузите перед работой с registry

---

## Что такое registry?

Registry — это централизованный каталог (`registry.json`), который отслеживает все компоненты OpenAgents Control:
- **Agents** - промпты AI-агентов
- **Subagents** - делегируемые специалисты
- **Commands** - slash commands
- **Tools** - кастомные инструменты
- **Contexts** - контекстные файлы

**Расположение**: `registry.json` (корневая директория)

---

## Схема registry

### Верхнеуровневая структура

```json
{
  "version": "0.5.0",
  "schema_version": "2.0.0",
  "components": {
    "agents": [...],
    "subagents": [...],
    "commands": [...],
    "tools": [...],
    "contexts": [...]
  },
  "profiles": {
    "essential": {...},
    "developer": {...},
    "business": {...}
  }
}
```

### Запись компонента

```json
{
  "id": "frontend-specialist",
  "name": "Frontend Specialist",
  "type": "agent",
  "path": ".opencode/agent/subagents/development/frontend-specialist.md",
  "description": "Expert in React, Vue, and modern CSS",
  "category": "development",
  "tags": ["react", "vue", "css", "frontend"],
  "dependencies": ["subagent:tester"],
  "version": "0.5.0"
}
```

**Поля**:
- `id`: уникальный идентификатор (kebab-case)
- `name`: отображаемое имя
- `type`: тип компонента (agent, subagent, command, tool, context)
- `path`: путь файла относительно корня репозитория
- `description`: краткое описание
- `category`: имя категории (для agents)
- `tags`: необязательные tags для обнаружения
- `dependencies`: необязательные зависимости
- `version`: версия при добавлении/обновлении

---

## Система auto-detect

Система auto-detect сканирует `.opencode/` и автоматически обновляет registry.

### Как это работает

```
1. Scan .opencode/ directory
2. Find all .md files with frontmatter
3. Extract metadata (description, category, type, tags)
4. Validate paths exist
5. Generate component entries
6. Update registry.json
```

### Запуск auto-detect

```bash
# Dry run (see what would be added)
./scripts/registry/auto-detect-components.sh --dry-run

# Actually add components
./scripts/registry/auto-detect-components.sh --auto-add

# Force update existing entries
./scripts/registry/auto-detect-components.sh --auto-add --force
```

### Что обнаруживается

✅ **Agents** - `.opencode/agent/{category}/*.md`  
✅ **Subagents** - `.opencode/agent/subagents/**/*.md`  
✅ **Commands** - `.opencode/command/**/*.md`  
✅ **Tools** - `.opencode/tool/**/index.ts`  
✅ **Contexts** - `.opencode/context/**/*.md`  

### Требования к frontmatter

Чтобы auto-detect работал, в файлах должен быть frontmatter:

```yaml
---
description: "Brief description"
category: "category-name"  # For agents
type: "agent"              # Or subagent, command, tool, context
tags: ["tag1", "tag2"]     # Optional
---
```

---

## Валидация

### Валидация registry

```bash
# Validate registry
./scripts/registry/validate-registry.sh

# Verbose output
./scripts/registry/validate-registry.sh -v
```

### Что валидируется

✅ **Schema** - корректная структура JSON  
✅ **Paths** - все пути существуют  
✅ **IDs** - уникальные IDs  
✅ **Categories** - валидные категории  
✅ **Dependencies** - зависимости существуют  
✅ **Versions** - консистентность версий  

### Ошибки валидации

```bash
# Example errors
ERROR: Path does not exist: (example: .opencode/agent/core/missing.md)
ERROR: Duplicate ID: frontend-specialist
ERROR: Invalid category: invalid-category
ERROR: Missing dependency: subagent:nonexistent
```

---

## Агенты и субагенты

**Основные агенты** (2 в Developer profile):
- openagent: универсальный агент координации
- opencoder: сложный coding и архитектура

**Субагенты-специалисты** (8 в Developer profile):
- frontend-specialist: React, Vue, CSS architecture
- devops-specialist: CI/CD, infrastructure, deployment

- task-manager: декомпозиция и планирование фич
- documentation: создание и обновление docs
- coder-agent: выполнение coding-подзадач
- reviewer: code review и безопасность
- tester: написание unit и integration tests
- build-agent: type checking и validation
- image-specialist: генерация и редактирование изображений

**Команды** (7 в Developer profile):
- analyze-patterns: анализ codebase на паттерны
- commit, test, context, clean, optimize, validate-repo

---

## Профили компонентов

Профили — это заранее настроенные bundles компонентов для быстрой установки.

### Доступные профили

#### Профиль Essential
**Назначение**: минимальный setup для базового использования

**Включает**:
- Core agents (openagent, opencoder)
- Основные commands (commit, test)
- Core context files

```json
"essential": {
  "description": "Minimal setup for basic usage",
  "components": [
    "agent:openagent",
    "agent:opencoder",
    "command:commit",
    "command:test"
  ]
}
```

---

#### Профиль Developer
**Назначение**: полный setup для разработки

**Включает**:
- Все core agents
- Development specialists
- Все subagents
- Dev commands
- Dev context files

```json
"developer": {
  "description": "Full development setup",
  "components": [
    "agent:*",
    "subagent:*",
    "command:*",
    "context:core/*",
    "context:development/*"
  ]
}
```

---

#### Профиль Business
**Назначение**: фокус на content и product

**Включает**:
- Core agents
- Content specialists
- Product specialists
- Content context files

```json
"business": {
  "description": "Content and product focus",
  "components": [
    "agent:openagent",
    "agent:copywriter",
    "agent:technical-writer",
    "context:core/*",
    "context:content/*"
  ]
}
```

---

## Система установки

Система установки использует registry для распространения компонентов.

### Поток установки

```
1. User runs install.sh
2. Check for local registry.json (development mode)
3. If not local, fetch from GitHub (production mode)
4. Parse registry.json
5. Show component selection UI
6. Resolve dependencies
7. Download components from GitHub
8. Install to .opencode/
9. Handle collisions (skip/overwrite/backup)
```

### Локальный registry (development)

```bash
# Test with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list

# Install with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh developer
```

### Удаленный registry (production)

```bash
# Install from GitHub
./install.sh developer

# List available components
./install.sh --list
```

---

## Разрешение зависимостей

### Формат зависимости

```json
"dependencies": [
  "subagent:tester",
  "context:core/standards/code"
]
```

### Правила разрешения

1. Разобрать строку зависимости (`type:id`)
2. Найти компонент в registry
3. Проверить, установлен ли уже компонент
4. Добавить в очередь установки
5. Рекурсивно разрешить зависимости
6. Установить в порядке зависимостей

### Пример

```
User installs: frontend-specialist
  ↓
Depends on: subagent:tester
  ↓
Depends on: context:core/standards/tests
  ↓
Install order:
  1. context:core/standards/tests
  2. subagent:tester
  3. frontend-specialist
```

---

## Обработка конфликтов

При установке компонентов, которые уже существуют:

### Стратегии конфликтов

1. **Skip** - оставить существующий файл
2. **Overwrite** - заменить новым файлом
3. **Backup** - сделать backup существующего и установить новый

### Интерактивный режим

```bash
File exists: .opencode/agent/core/openagent.md
[S]kip, [O]verwrite, [B]ackup, [A]ll skip, [F]orce all? 
```

### Неинтерактивный режим

```bash
# Skip all collisions
./install.sh developer --skip-existing

# Overwrite all collisions
./install.sh developer --force

# Backup all collisions
./install.sh developer --backup
```

---

## Управление версиями

### Поля версии

- **Версия registry**: общая версия registry (например, "0.5.0")
- **Версия схемы**: версия схемы registry (например, "2.0.0")
- **Версия компонента**: версия при добавлении/обновлении компонента

### Консистентность версий

```bash
# Check version consistency
cat VERSION
cat package.json | jq '.version'
cat registry.json | jq '.version'

# All should match
```

### Обновление версий

```bash
# Bump version
echo "0.X.Y" > VERSION
jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json
jq '.version = "0.X.Y"' registry.json > tmp && mv tmp registry.json
```

---

## Интеграция CI/CD

### GitHub workflows

#### Валидация registry (проверки PR)

```yaml
# .github/workflows/validate-registry.yml
- name: Validate Registry
  run: ./scripts/registry/validate-registry.sh
```

#### Автообновление registry (после merge)

```yaml
# .github/workflows/update-registry.yml
- name: Update Registry
  run: ./scripts/registry/auto-detect-components.sh --auto-add
```

#### Увеличение версии (при релизе)

```yaml
# .github/workflows/version-bump.yml
- name: Bump Version
  run: ./scripts/versioning/bump-version.sh
```

---

## Лучшие практики

### Добавление компонентов

✅ **Добавляйте frontmatter** - требуется для auto-detect  
✅ **Запускайте auto-detect** - не редактируйте registry вручную  
✅ **Валидируйте** - всегда валидируйте после изменений  
✅ **Тестируйте локально** - используйте локальный registry для тестирования  

### Поддержка registry

✅ **Сначала auto-detect** - пусть scripts обрабатывают обновления  
✅ **Валидируйте часто** - ловите проблемы рано  
✅ **Консистентность версий** - держите версии синхронизированными  
✅ **CI validation** - автоматизируйте валидацию в CI  

### Зависимости

✅ **Явные зависимости** - перечисляйте все зависимости  
✅ **Проверяйте resolution** - убедитесь, что зависимости разрешаются  
✅ **Избегайте циклов** - никаких циклических зависимостей  

---

## Частые проблемы

### Путь не найден

**Проблема**: registry ссылается на несуществующий путь  
**Решение**: запустите auto-detect или исправьте путь вручную

### Дублирующийся ID

**Проблема**: два компонента с одинаковым ID  
**Решение**: переименуйте один компонент

### Неверная категория

**Проблема**: у агента неверная категория  
**Решение**: используйте валидную категорию (core, development, content, data, product, learning)

### Отсутствующая зависимость

**Проблема**: зависимость не существует в registry  
**Решение**: добавьте зависимость или удалите ссылку

### Несовпадение версий

**Проблема**: VERSION, package.json и registry.json не совпадают  
**Решение**: обновите все version-файлы до совпадения

---

## Связанные файлы

- **Обновление registry**: `guides/updating-registry.md`
- **Добавление агентов**: `guides/adding-agent.md`
- **Категории**: `core-concepts/categories.md`

---

**Последнее обновление**: 2025-01-28  
**Версия**: 0.5.2
