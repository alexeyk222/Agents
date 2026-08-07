<!-- Context: core/navigation-examples | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Примеры: файлы навигации

**Назначение**: практические примеры хороших файлов навигации

**Последнее обновление**: 2026-01-08

---

## Пример 1: навигация категории (по функциям)

**Файл**: `openagents-repo/navigation.md`

**Паттерн**: по функциям (специфично для репозитория)

**Количество токенов**: ~250 токенов

```markdown
# OpenAgents Control Repository Navigation

**Purpose**: Navigate OpenAgents Control repository context

---

## Structure

```
openagents-repo/
├── navigation.md
├── quick-start.md
│
├── core-concepts/
│   ├── agent-architecture.md
│   ├── eval-framework.md
│   └── registry-system.md
│
├── guides/
│   ├── adding-agent.md
│   ├── testing-agent.md
│   └── debugging-issues.md
│
├── lookup/
│   ├── commands.md
│   └── file-locations.md
│
└── errors/
    └── tool-permission-errors.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **New here** | `quick-start.md` |
| **Add agent** | `guides/adding-agent.md` |
| **Test agent** | `guides/testing-agent.md` |
| **Debug issue** | `guides/debugging-issues.md` |
| **Find files** | `lookup/file-locations.md` |
| **Fix error** | `errors/tool-permission-errors.md` |

---

## By Type

**Core Concepts** → Foundational understanding (agents, evals, registry)
**Guides** → Step-by-step workflows
**Lookup** → Quick reference tables
**Errors** → Troubleshooting
```

**Почему это работает**:
- ✅ Токен-эффективно (~250 токенов)
- ✅ ASCII-дерево показывает структуру
- ✅ Быстрые маршруты для частых задач
- ✅ Организовано по типу информации

---

## Пример 2: навигация категории (по задачам)

**Файл**: `development/navigation.md`

**Паттерн**: по задачам (несколько технологий)

**Количество токенов**: ~280 токенов

```markdown
# Development Navigation

**Purpose**: Software development across all stacks

---

## Structure

```
development/
├── navigation.md
├── ui-navigation.md           # Specialized
├── backend-navigation.md      # Specialized
│
├── principles/
│   ├── clean-code.md
│   └── api-design.md
│
├── frontend/
│   ├── react/
│   └── vue/
│
├── backend/
│   ├── api-patterns/
│   ├── nodejs/
│   └── authentication/
│
└── data/
    ├── sql-patterns/
    └── orm-patterns/
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **UI/Frontend** | `ui-navigation.md` |
| **Backend/API** | `backend-navigation.md` |
| **Clean code** | `principles/clean-code.md` |
| **API design** | `principles/api-design.md` |

---

## By Concern

**Principles** → Universal development practices
**Frontend** → React, Vue, state management
**Backend** → APIs, Node.js, Python, auth
**Data** → SQL, NoSQL, ORMs
```

**Почему это работает**:
- ✅ Токен-эффективно (~280 токенов)
- ✅ Показывает специализированные файлы навигации
- ✅ Организовано по задаче (frontend, backend, data)
- ✅ Указывает на специализированную навигацию для сложных процессов

---

## Пример 3: специализированная навигация

**Файл**: `development/ui-navigation.md`

**Паттерн**: сквозной (охватывает несколько категорий)

**Количество токенов**: ~270 токенов

```markdown
# UI Development Navigation

**Scope**: Frontend code + visual design

---

## Structure

```
Frontend Code (development/frontend/):
├── react/
│   ├── hooks-patterns.md
│   ├── component-architecture.md
│   └── tanstack/
│       ├── query-patterns.md
│       └── router-patterns.md
└── vue/

Visual Design (ui/web/):
├── animation-patterns.md
├── ui-styling-standards.md
└── design-systems.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **React patterns** | `frontend/react/hooks-patterns.md` |
| **TanStack Query** | `frontend/react/tanstack/query-patterns.md` |
| **Animations** | `../../ui/web/animation-patterns.md` |
| **Styling** | `../../ui/web/ui-styling-standards.md` |

---

## By Framework

**React** → `frontend/react/`
**Vue** → `frontend/vue/`
**TanStack** → `frontend/react/tanstack/`

## By Concern

**Code patterns** → `development/frontend/`
**Visual design** → `ui/web/`
```

**Почему это работает**:
- ✅ Токен-эффективно (~270 токенов)
- ✅ Охватывает несколько категорий (`development/` + `ui/`)
- ✅ Сфокусировано на задаче (UI-разработка)
- ✅ Показывает пути и к коду, и к дизайну

---

## Пример 4: навигация подкатегории

**Файл**: `development/backend/navigation.md`

**Паттерн**: подкатегория по задачам

**Количество токенов**: ~240 токенов

```markdown
# Backend Development Navigation

**Scope**: Server-side, APIs, databases, auth

---

## Structure

```
backend/
├── navigation.md
│
├── api-patterns/
│   ├── rest-design.md
│   ├── graphql-design.md
│   └── grpc-patterns.md
│
├── nodejs/
│   ├── express-patterns.md
│   └── fastify-patterns.md
│
├── python/
│   └── fastapi-patterns.md
│
└── authentication/
    ├── jwt-patterns.md
    └── oauth-patterns.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **REST API** | `api-patterns/rest-design.md` |
| **GraphQL** | `api-patterns/graphql-design.md` |
| **Node.js** | `nodejs/express-patterns.md` |
| **Auth (JWT)** | `authentication/jwt-patterns.md` |

---

## By Approach

**REST** → `api-patterns/rest-design.md`
**GraphQL** → `api-patterns/graphql-design.md`

## By Language

**Node.js** → `nodejs/`
**Python** → `python/`
```

**Почему это работает**:
- ✅ Токен-эффективно (~240 токенов)
- ✅ Сначала организовано по подходу (REST, GraphQL)
- ✅ Затем по технологии (Node.js, Python)
- ✅ Функциональные задачи разделены (`authentication/`)

---

## Пример 5: full-stack навигация

**Файл**: `development/fullstack-navigation.md`

**Паттерн**: сфокусирован на workflow

**Количество токенов**: ~300 токенов

```markdown
# Full-Stack Development Navigation

**Scope**: End-to-end application development

---

## Common Stacks

### MERN (MongoDB, Express, React, Node)
```
Frontend: development/frontend/react/
Backend:  development/backend/nodejs/express-patterns.md
Data:     development/data/nosql-patterns/mongodb.md
API:      development/backend/api-patterns/rest-design.md
```

### T3 Stack (Next.js, tRPC, Prisma, Tailwind)
```
Frontend: development/frontend/react/ + ui/web/ui-styling-standards.md
Backend:  development/backend/nodejs/ + api-patterns/trpc-patterns.md
Data:     development/data/orm-patterns/prisma.md
```

---

## Быстрые маршруты

| Layer | Navigate To |
|-------|-------------|
| **Frontend** | `ui-navigation.md` |
| **Backend** | `backend-navigation.md` |
| **Data** | `data/navigation.md` |

---

## Common Workflows

**New API endpoint**:
1. `principles/api-design.md` (principles)
2. `backend/api-patterns/rest-design.md` (approach)
3. `backend/nodejs/express-patterns.md` (implementation)

**New React feature**:
1. `frontend/react/component-architecture.md` (structure)
2. `frontend/react/hooks-patterns.md` (logic)
3. `ui/web/ui-styling-standards.md` (styling)
```

**Почему это работает**:
- ✅ Токен-эффективно (~300 токенов)
- ✅ Показывает типовые технологические стеки
- ✅ Сфокусировано на workflow (как строить фичи)
- ✅ Указывает на навигацию по слоям

---

## Пример 6: минимальная навигация

**Файл**: `content/navigation.md`

**Паттерн**: простая категория (мало файлов)

**Количество токенов**: ~150 токенов

```markdown
# Content Navigation

**Purpose**: Copywriting and content creation

---

## Structure

```
content/
├── navigation.md
├── copywriting-frameworks.md
└── tone-voice.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **Write copy** | `copywriting-frameworks.md` |
| **Set tone** | `tone-voice.md` |

---

## Files

**copywriting-frameworks.md** → AIDA, PAS, persuasive writing
**tone-voice.md** → Brand voice, tone guidelines
```

**Почему это работает**:
- ✅ Токен-эффективно (~150 токенов)
- ✅ Простая структура (только 2 файла)
- ✅ Нет лишней сложности
- ✅ Понятно и быстро просматривается

---

## Антипаттерны (чего НЕ делать)

### ❌ Слишком многословно

```markdown
# Development Navigation

**Purpose**: This comprehensive navigation file is designed to help you navigate the extensive collection of software development patterns, standards, and best practices that we have carefully curated across all technology stacks including frontend frameworks like React and Vue, backend technologies such as Node.js and Python, database systems both SQL and NoSQL, and infrastructure tools for deployment and operations.

## Introduction

The development category represents a significant portion of our context system...

[Continues for 800+ tokens]
```

**Проблемы**:
- ❌ 800+ токенов (должно быть 200–300)
- ❌ Многословные объяснения (нужно кратко)
- ❌ Трудно сканировать (нужны таблицы/деревья)

---

### ❌ Нет структуры

```markdown
# Development Navigation

Here are the files:
- clean-code.md
- api-design.md
- react-patterns.md
- express-patterns.md
```

**Проблемы**:
- ❌ Нет ASCII-дерева (иерархию трудно увидеть)
- ❌ Нет быстрых маршрутов (задачи трудно найти)
- ❌ Нет организации (просто список)

---

### ❌ Слишком подробно

```markdown
# Development Navigation

## React Patterns

### Hooks
React hooks allow you to use state and lifecycle features in functional components. The most common hooks are:

1. useState - For managing component state
   - Syntax: const [state, setState] = useState(initialValue)
   - Example: const [count, setCount] = useState(0)
   
2. useEffect - For side effects
   [... continues with full documentation]
```

**Проблемы**:
- ❌ Содержит содержимое файлов (должен только указывать на файлы)
- ❌ Дублирует информацию (нужны ссылки, не повторы)
- ❌ Слишком подробно (это navigation, не документация)

---

## Ключевые выводы

### ✅ Хорошие файлы навигации

1. **Токен-эффективные** (200–300 токенов)
2. **Быстро просматриваемые** (ASCII-деревья, таблицы)
3. **Сфокусированные на задачах** (быстрые маршруты)
4. **Организованные** (по задаче/типу)
5. **Краткие** (описания 3–5 слов)

### ❌ Плохие файлы навигации

1. **Многословные** (500+ токенов)
2. **Трудно сканировать** (абзацы)
3. **Без фокуса** (нет ясных маршрутов)
4. **Неорганизованные** (просто списки)
5. **Слишком подробные** (дублируют содержимое)

---

## Связанные материалы

- `../guides/navigation-design.md` - как создавать файлы навигации
- `../guides/organizing-context.md` - как выбрать организационный паттерн
- `../standards/mvi.md` - принцип MVI
