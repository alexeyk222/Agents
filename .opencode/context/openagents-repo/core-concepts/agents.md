# Ключевая концепция: агенты

**Назначение**: понять, как работают агенты в OpenAgents Control  
**Приоритет**: CRITICAL - загрузите перед работой с агентами

---

## Что такое агенты?

Агенты — это файлы AI-промптов, которые задают специализированное поведение для разных задач. Это:
- **Markdown-файлы** с метаданными frontmatter
- **Организация по категориям** домена (core, development, content и т. д.)
- **Контекстная осведомленность** — загрузка релевантных контекстных файлов
- **Тестируемость** — валидация через eval-фреймворк

---

## Структура агента

### Формат файла

```markdown
---
description: "Brief description of what this agent does"
category: "category-name"
type: "agent"
tags: ["tag1", "tag2"]
dependencies: ["subagent:tester"]
---

# Agent Name

[Agent prompt content - instructions, workflows, constraints]
```

### Ключевые компоненты

1. **Frontmatter** (YAML-метаданные)
   - `description`: краткое описание
   - `category`: имя категории (core, development, content и т. д.)
   - `type`: всегда "agent"
   - `tags`: необязательные теги для обнаружения
   - `dependencies`: необязательные зависимости (например, subagents)

2. **Содержимое промпта**
   - Инструкции и workflows
   - Ограничения и правила
   - Требования к загрузке контекста
   - Паттерны использования инструментов

---

## Система категорий

Агенты организованы по доменной экспертизе:

### Категория Core (`core/`)
**Назначение**: базовые системные агенты (всегда доступны)

Агенты:
- `openagent.md` - универсальный orchestrator
- `opencoder.md` - специалист по разработке
- `system-builder.md` - генерация систем

**Когда использовать**: системные задачи, orchestration

---

### Категория Development (`development/`)
**Назначение**: специалисты по разработке ПО

Агенты:
- `frontend-specialist.md` - React, Vue, modern CSS
- `devops-specialist.md` - CI/CD, deployment, infrastructure

**Когда использовать**: создание приложений, dev-задачи

---

### Категория Content (`content/`)
**Назначение**: специалисты по созданию контента

Агенты:
- `copywriter.md` - Marketing copy, persuasive writing
- `technical-writer.md` - Documentation, technical content

**Когда использовать**: тексты, документация, маркетинг

---

### Категория Data (`data/`)
**Назначение**: специалисты по анализу данных

Агенты:
- `data-analyst.md` - Data analysis, visualization

**Когда использовать**: data-задачи, анализ, отчеты

---

### Категория Product (`product/`)
**Назначение**: специалисты по product management

**Статус**: готово для агентов (агентов пока нет)

**Когда использовать**: продуктовая стратегия, roadmaps, requirements

---

### Категория Learning (`learning/`)
**Назначение**: специалисты по обучению и coaching

**Статус**: готово для агентов (агентов пока нет)

**Когда использовать**: преподавание, тренинги, curriculum

---

## Субагенты

**Расположение**: `.opencode/agent/subagents/`

**Назначение**: делегируемые специалисты для конкретных подзадач

### Категории субагентов

1. **code/** - специалисты по коду
   - `tester.md` - написание тестов и TDD
   - `reviewer.md` - code review и безопасность
   - `coder-agent.md` - сфокусированные реализации
   - `build-agent.md` - type checking и builds

2. **core/** - специалисты по core workflow
   - `task-manager.md` - декомпозиция и управление задачами
   - `documentation.md` - генерация документации

3. **system-builder/** - специалисты по генерации систем
   - `agent-generator.md` - генерация файлов агентов
   - `command-creator.md` - создание slash commands
   - `domain-analyzer.md` - анализ доменов
   - `context-organizer.md` - организация контекста
   - `workflow-designer.md` - проектирование workflows

4. **utils/** - utility-специалисты
   - `image-specialist.md` - редактирование и анализ изображений

### Субагенты vs агенты категорий

| Аспект | Агенты категорий | Субагенты |
|--------|----------------|-----------|
| **Назначение** | Специалисты для пользователя | Делегируемые подзадачи |
| **Вызов** | Напрямую пользователем | Через инструмент task |
| **Область** | Широкий домен | Узкий фокус |
| **Пример** | `frontend-specialist` | `tester` |

---

## Совместимость с Claude Code (опционально)

OpenAgents Control может работать вместе с Claude Code для локальных workflows и распространения:

- **Субагенты**: проектные helpers в `.claude/agents/`
- **Skills**: автоматически вызываемые инструкции в `.claude/skills/`
- **Hooks**: shell-команды на события жизненного цикла (используйте умеренно)
- **Плагины**: общий доступ к agents/skills/hooks между проектами

Используйте это, когда нужно, чтобы Claude Code следовал стандартам OpenAgents Control, или чтобы поставлять переиспользуемые helpers.

---

## Разрешение путей

Система поддерживает несколько форматов путей для обратной совместимости:

### Поддерживаемые форматы

```bash
# Short ID (backward compatible)
"openagent" → resolves to → ".opencode/agent/core/openagent.md"

# Category path
"core/openagent" → resolves to → ".opencode/agent/core/openagent.md"

# Full category path
"development/frontend-specialist" → resolves to → ".opencode/agent/subagents/development/frontend-specialist.md"

# Subagent path
"TestEngineer" → resolves to → ".opencode/agent/subagents/code/test-engineer.md"
```

### Правила разрешения

1. Если путь содержит `/` → использовать как путь категории
2. Если `/` нет → сначала проверить core/ (backward compat)
3. Если не найдено в core/ → искать во всех категориях
4. Если не найдено → ошибка

---

## Варианты промптов

**Расположение**: `.opencode/prompts/{category}/{agent}/`

**Назначение**: оптимизации промптов под конкретные модели

### Поддерживаемые модели

- `gemini.md` - оптимизации Google Gemini
- `grok.md` - оптимизации xAI Grok
- `llama.md` - оптимизации Meta Llama
- `openrouter.md` - оптимизации OpenRouter

### Когда создавать варианты

- У модели есть особые требования к форматированию
- Модель лучше работает с другой структурой
- У модели есть уникальные capabilities, которые нужно использовать

### Резервное поведение

Если варианта для модели нет, используется базовый файл агента.

---

## Загрузка контекста

Агенты должны загружать релевантные контекстные файлы по типу задачи:

### Core-контекст (всегда учитывайте)

```markdown
<!-- Context: standards/code | Priority: critical -->
```

Загружает: `.opencode/context/core/standards/code-quality.md`

### Контекст категории

```markdown
<!-- Context: development/react-patterns | Priority: high -->
```

Загружает: `.opencode/context/ui/web/react-patterns.md`

### Несколько контекстов

```markdown
<!-- Context: standards/code, standards/tests | Priority: critical -->
```

---

## Жизненный цикл агента

### 1. Создание
```bash
# Create agent file
touch .opencode/agent/{category}/{agent-name}.md

# Add frontmatter and content
# (See guides/adding-agent.md for details)
```

### 2. Тестирование
```bash
# Create test structure
mkdir -p evals/agents/{category}/{agent-name}/{config,tests}

# Run tests
cd evals/framework && npm run eval:sdk -- --agent={category}/{agent-name}
```

### 3. Регистрация
```bash
# Auto-detect and add to registry
./scripts/registry/auto-detect-components.sh --auto-add

# Validate
./scripts/registry/validate-registry.sh
```

### 4. Распространение
```bash
# Users install via install.sh
./install.sh {profile}
```

---

## Лучшие практики

### Проектирование агента

✅ **Единая ответственность** - один домен, один агент  
✅ **Ясные инструкции** - явные workflows и ограничения  
✅ **Контекстная осведомленность** - загрузка релевантных контекстных файлов  
✅ **Тестируемость** - включайте eval-тесты  
✅ **Хорошая документация** - понятное описание и использование  

### Соглашения об именовании

- **Агенты категорий**: `{domain}-specialist.md` (например, `frontend-specialist.md`)
- **Core-агенты**: `{name}.md` (например, `openagent.md`)
- **Субагенты**: `{purpose}.md` (например, `tester.md`)

### Требования к frontmatter

```yaml
---
description: "Required - brief description"
category: "Required - category name"
type: "Required - always 'agent'"
tags: ["Optional - for discovery"]
dependencies: ["Optional - e.g., 'subagent:tester'"]
---
```

---

## Частые паттерны

### Делегирование субагентам

```markdown
When task requires testing:
1. Implement feature
2. Delegate to TestEngineer for test creation
```

### Загрузка контекста

```markdown
Before implementing:
1. Load core/standards/code-quality.md
2. Load category-specific context if available
3. Apply standards to implementation
```

### Approval gates

```markdown
Before execution:
1. Present plan to user
2. Request approval
3. Execute incrementally
```

---

## Связанные файлы

- **Добавление агентов**: `guides/adding-agent.md`
- **Тестирование агентов**: `guides/testing-agent.md`
- **Система категорий**: `core-concepts/categories.md`
- **Расположение файлов**: `lookup/file-locations.md`
- **Субагенты Claude Code**: `../to-be-consumed/claude-code-docs/create-subagents.md`
- **Skills Claude Code**: `../to-be-consumed/claude-code-docs/agent-skills.md`
- **Hooks Claude Code**: `../to-be-consumed/claude-code-docs/hooks.md`
- **Plugins Claude Code**: `../to-be-consumed/claude-code-docs/plugins.md`

---

**Последнее обновление**: 2026-01-13  
**Версия**: 0.5.1
