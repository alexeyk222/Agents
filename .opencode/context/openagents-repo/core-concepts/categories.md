# Ключевая концепция: система категорий

**Назначение**: понять, как организованы компоненты  
**Приоритет**: HIGH - загрузите перед добавлением категорий или организацией компонентов

---

## Что такое категории?

Категории — это доменные группы, которые организуют агентов, контекстные файлы и тесты по области экспертизы.

**Преимущества**:
- **Масштабируемость** - легко добавлять новые домены
- **Обнаружение** - поиск агентов по домену
- **Организация** - понятная структура
- **Модульность** - устанавливайте только нужное

---

## Доступные категории

### Core-категория (`core/`)
**Назначение**: базовые системные агенты (всегда доступны)

**Агенты**:

**Когда использовать**: системные задачи, orchestration, coding (простые или сложные)

**Статус**: ✅ Stable

---

### Development-субагенты (`subagents/development/`)
**Назначение**: доменные специалисты по разработке (вызываются core agents)

**Субагенты**:
- frontend-specialist, devops-specialist

**Контекст**:
- clean-code.md, react-patterns.md, api-design.md

**Когда использовать**: делегированные frontend, backend или DevOps-задачи внутри более крупного workflow

**Статус**: ✅ Active

---

### Content (`content/`)
**Назначение**: специалисты по созданию контента

**Агенты**:
- copywriter, technical-writer

**Контекст**:
- copywriting-frameworks.md
- tone-voice.md
- audience-targeting.md
- hooks.md

**Когда использовать**: тексты, документация, маркетинг

**Статус**: ✅ Active

---

### Data (`data/`)
**Назначение**: специалисты по анализу данных

**Агенты**:
- data-analyst

**Контекст**:
- (готово для data-specific context)

**Когда использовать**: data-задачи, анализ, отчеты

**Статус**: ✅ Active

---

---

## Структура категорий

### Структура директорий

```
.opencode/
├── agent/{category}/           # Agents by category
├── context/{category}/         # Context by category
├── prompts/{category}/         # Prompt variants by category
evals/agents/{category}/        # Tests by category
```

### Пример: Core-агенты + Development-субагенты

```
.opencode/agent/core/
├── 0-category.json             # Category metadata
├── openagent.md
├── opencoder.md

.opencode/agent/subagents/development/
├── 0-category.json             # Subagent category metadata
├── frontend-specialist.md
└── devops-specialist.md

.opencode/context/development/
├── navigation.md
├── clean-code.md
├── react-patterns.md
└── api-design.md
```

---

## Метаданные категории

### 0-category.json

У каждой категории есть файл метаданных:

```json
{
  "name": "Development",
  "description": "Software development specialists",
  "icon": "💻",
  "order": 2,
  "status": "active"
}
```

**Поля**:
- `name`: отображаемое имя
- `description`: краткое описание
- `icon`: emoji-иконка
- `order`: порядок отображения
- `status`: active, ready, planned

---

## Соглашения об именовании

### Имена категорий

✅ **Нижний регистр** - `development`, не `Development`  
✅ **Единственное число** - `content`, не `contents`  
✅ **Описательность** - понятное имя домена  
✅ **Консистентность** - следуйте существующим паттернам  

### Имена агентов

✅ **Kebab-case** - `frontend-specialist.md`  
✅ **Описательность** - понятное назначение  
✅ **Суффикс** - используйте `-specialist`, `-agent`, `-writer` по ситуации  

### Имена контекста

✅ **Kebab-case** - `react-patterns.md`  
✅ **Описательность** - понятная тема  
✅ **Конкретность** - фокус на одной теме  

---

## Разрешение путей

Система гибко разрешает пути агентов:

### Порядок разрешения

1. **Проверить `/`** - если есть, считать путем категории
2. **Проверить core/** - для обратной совместимости
3. **Искать в категориях** - проверить все категории
4. **Ошибка** - если не найдено

### Примеры

```bash
# Short ID (backward compatible)
"openagent" → ".opencode/agent/core/openagent.md"

# Subagent path
"subagents/development/frontend-specialist" → ".opencode/agent/subagents/development/frontend-specialist.md"

# Subagent path
"TestEngineer" → ".opencode/agent/subagents/code/test-engineer.md"
```

---

## Добавление новой категории

### Шаг 1: создать структуру директорий

```bash
# Create agent directory
mkdir -p .opencode/agent/{category}

# Create context directory
mkdir -p .opencode/context/{category}

# Create eval directory
mkdir -p evals/agents/{category}
```

### Шаг 2: добавить метаданные категории

```bash
cat > .opencode/agent/{category}/0-category.json << 'EOF'
{
  "name": "Category Name",
  "description": "Brief description",
  "icon": "🎯",
  "order": 10,
  "status": "ready"
}
EOF
```

### Шаг 3: добавить README контекста

```bash
cat > .opencode/context/{category}/navigation.md << 'EOF'
# Category Name Context

Context files for {category} specialists.

## Available Context

- (List context files here)

## When to Use

- (Describe when to use this context)
EOF
```

### Шаг 4: валидировать

```bash
# Validate structure
./scripts/registry/validate-component.sh

# Update registry
./scripts/registry/auto-detect-components.sh --auto-add
```

---

## Рекомендации по категориям

### Когда создавать новую категорию

✅ **Отдельный домен** - ясная область экспертизы  
✅ **Несколько агентов** - планируйте 2+ агентов  
✅ **Общий контекст** - есть общие знания для шаринга  
✅ **Спрос пользователей** - запрошено пользователями  

### Когда НЕ создавать категорию

❌ **Один агент** - используйте существующую категорию  
❌ **Пересечение** - подходит под существующую категорию  
❌ **Слишком конкретно** - слишком узкий фокус  
❌ **Нечеткий домен** - область плохо определена  

---

## Категория vs субагент

### Используйте агента категории, когда:
- Это специалист для пользователя
- Нужна широкая доменная экспертиза
- Пользователь вызывает напрямую
- Пример: `frontend-specialist`

### Используйте субагента, когда:
- Это делегируемая подзадача
- Нужен узкий фокус
- Вызывается другими агентами
- Пример: `tester`

---

## Организация контекста

### Структура контекста категории

```
.opencode/context/{category}/
├── navigation.md               # Overview
├── {topic-1}.md           # Specific topic
├── {topic-2}.md           # Specific topic
└── {topic-3}.md           # Specific topic
```

### Загрузка контекста

Агенты загружают контекст категории на основе задачи:

```markdown
<!-- Context: development/react-patterns | Priority: high -->
```

Загружает: `.opencode/context/ui/web/react-patterns.md`

---

## Лучшие практики

### Организация

✅ **Ясные категории** - хорошо определенные домены  
✅ **Консистентное именование** - следуйте соглашениям  
✅ **Корректные метаданные** - полный 0-category.json  
✅ **README-файлы** - документируйте каждую категорию  

### Масштабируемость

✅ **Модульность** - категории независимы  
✅ **Расширяемость** - легко добавлять новые категории  
✅ **Поддерживаемость** - понятная структура  
✅ **Тестируемость** - у каждой категории есть тесты  

### Обнаружение

✅ **Описательные имена** - понятное назначение  
✅ **Хорошие описания** - объясняют, когда использовать  
✅ **Правильные tags** - помогают обнаружению  
✅ **Документация** - документируйте в README  

---

## Миграция с плоской структуры

### Старая структура (плоская)

```
.opencode/agent/
├── openagent.md
├── opencoder.md
├── frontend-specialist.md
└── copywriter.md
```

### Новая структура (на основе категорий)

```
.opencode/agent/
├── core/
│   ├── openagent.md
│   ├── opencoder.md
├── subagents/
│   ├── development/
│   │   ├── frontend-specialist.md
│   │   └── devops-specialist.md
│   └── code/
│       ├── coder-agent.md
│       └── tester.md
└── content/
    └── copywriter.md
```

### Обратная совместимость

Старые пути продолжают работать:
- `openagent` → resolves to `core/openagent`
- `opencoder` → resolves to `core/opencoder`

Новые агенты используют пути категорий:
- `subagents/development/frontend-specialist`
- `content/copywriter`

---

## Частые паттерны

### Core-категория с несколькими агентами

```
core/
├── 0-category.json
├── openagent.md
├── opencoder.md
```

### Development-субагенты

```
subagents/development/
├── 0-category.json
├── frontend-specialist.md
└── devops-specialist.md
```

### Категория с общим контекстом

```
context/development/
├── navigation.md
├── clean-code.md
├── react-patterns.md
└── api-design.md
```

### Категория с тестами

```
evals/agents/core/
├── openagent/
│   ├── config/config.yaml
│   └── tests/smoke-test.yaml
├── opencoder/
```

---

## Связанные файлы

- **Добавление агентов**: `guides/adding-agent.md`
- **Добавление категорий**: `guides/add-category.md`
- **Концепции агентов**: `core-concepts/agents.md`
- **Расположение файлов**: `lookup/file-locations.md`
- **Принципы создания контента**: `../content-creation/principles/navigation.md`

---

**Последнее обновление**: 2026-01-13  
**Версия**: 0.5.1
