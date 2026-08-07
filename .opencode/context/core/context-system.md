<!-- Context: core/context-system | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Система контекста

**Назначение**: Минимальная организация знаний по задачам для AI-агентов

**Последнее обновление**: 2026-01-08

---

## Базовые принципы

### 1. Minimal Viable Information (MVI)
Извлекайте только базовые концепции (1–3 предложения), ключевые пункты (3–5 bullets), минимальный пример и ссылку на источник. 
**Цель**: Сканируется за <30 секунд. Ссылайтесь на полные docs, не дублируйте их.

### 2. Структура по задачам
Организуйте по **тому, что вы делаете** (concern), затем по **тому, как вы это делаете** (подход/технология):

**Два паттерна организации**:

#### Паттерн A: по функции (для контекста конкретного репозитория)
```
category/
├── navigation.md
├── concepts/              # What it is
├── examples/              # Working code
├── guides/                # How to do it
├── lookup/                # Quick reference
└── errors/                # Common issues
```

**Используйте, когда**: Контент специфичен для репозитория (например, `openagents-repo/`)

#### Паттерн B: по задаче (для контекста разработки)
```
category/
├── navigation.md
├── {concern}/             # Organize by what you're doing
│   ├── navigation.md
│   ├── {approach}/        # Then by approach/tech
│   │   ├── navigation.md
│   │   └── {files}.md
```

**Используйте, когда**: Контент охватывает несколько технологий (например, `development/`)

**Примеры**:
- `development/backend/api-patterns/` - Задача: backend, подход: API patterns
- `development/backend/nodejs/` - Задача: backend, технология: Node.js
- `development/frontend/react/` - Задача: frontend, технология: React

### 3. Токен-эффективная навигация
У каждой категории/подкатегории есть `navigation.md` с:
- **ASCII-деревом** для быстрого обзора структуры (~50 токенов)
- **Таблицей быстрых маршрутов** для типовых задач (~100 токенов)
- **Секциями по задаче/типу** (~50 токенов)
- **Итого**: ~200–300 токенов на файл навигации

**Зачем**: Быстрее загрузка, ниже стоимость, быстрее решения AI

### 4. Специализированные файлы навигации
Для сквозных задач создавайте специализированную навигацию:
- `development/ui-navigation.md` - Охватывает frontend/ + ui/
- `development/backend-navigation.md` - Покрывает API, auth, middleware
- `development/fullstack-navigation.md` - Типовые технологические стеки

**Зачем**: Реальные процессы не всегда укладываются в аккуратные категории

### 5. Самоописывающие имена файлов
Имя файла должно объяснять содержимое:
- ❌ `code.md` → ✅ `code-quality.md`
- ❌ `tests.md` → ✅ `test-coverage.md`
- ❌ `review.md` → ✅ `code-review.md`

**Зачем**: Не нужно открывать файл, чтобы понять содержание

### 6. Сбор знаний
Извлекайте полезный контекст из AI-сводок/обзоров, затем удаляйте их. Рабочая область остается чистой, знания сохраняются.

### 5. Организация контекста технологий

**Назначение**: Обеспечить единое размещение новых технологий (фреймворков, библиотек, инструментов), чтобы их легко находить.

**Фреймворки vs архитектурные слои**:

- **Full-Stack Frameworks** (например, Tanstack Start, Next.js): Добавляйте в `development/frameworks/{tech}/`. Это «метафреймворки», охватывающие несколько слоев.
- **Специализированные задачи** (например, AI, Data): Добавляйте в `development/{concern}/{tech}/`.
- **Технологии конкретного слоя** (например, React, Node.js): Добавляйте в `development/{frontend|backend}/{tech}/`.

**Процесс выбора**:
1. Это full-stack framework? → `development/frameworks/`
2. Это специализированный домен (AI, Data)? → `development/{domain}/`
3. Это технология конкретного слоя? → `development/{frontend|backend}/`

---

## Паттерны каталогов

### Паттерн A: по функции (специфичен для репозитория)

**Используйте для**: Контекста конкретного репозитория (например, `openagents-repo/`)

```
.opencode/context/{category}/
├── navigation.md              # Fast, token-efficient navigation
├── quick-start.md             # Optional: 2-minute orientation
│
├── core-concepts/             # Foundational concepts (optional)
│   ├── navigation.md
│   └── {concept}.md
│
├── concepts/                  # What it is
│   ├── navigation.md
│   └── {concept}.md
│
├── examples/                  # Working code
│   ├── navigation.md
│   └── {example}.md
│
├── guides/                    # How to do it
│   ├── navigation.md
│   └── {guide}.md
│
├── lookup/                    # Quick reference
│   ├── navigation.md
│   └── {lookup}.md
│
└── errors/                    # Common issues
    ├── navigation.md
    └── {error}.md
```

---

### Паттерн B: по задаче (контекст разработки)

**Используйте для**: Контекста разработки с несколькими технологиями (например, `development/`)

```
.opencode/context/{category}/
├── navigation.md                       # Main navigation
├── {concern}-navigation.md             # Specialized navigation (optional)
│
├── principles/                         # Universal principles (optional)
│   ├── navigation.md
│   └── {principle}.md
│
├── {concern}/                          # Organize by concern
│   ├── navigation.md
│   │
│   ├── {approach}/                     # Then by approach
│   │   ├── navigation.md
│   │   └── {pattern}.md
│   │
│   └── {tech}/                         # Or by tech
│       ├── navigation.md
│       └── {pattern}.md
```

**Пример**:
```
development/
├── navigation.md
├── ui-navigation.md                    # Specialized
├── backend-navigation.md               # Specialized
├── fullstack-navigation.md             # Specialized
│
├── principles/                         # Universal
│   ├── clean-code.md
│   └── api-design.md
│
├── frontend/                           # Concern
│   ├── react/                          # Tech
│   │   ├── hooks-patterns.md
│   │   └── tanstack/                   # Sub-tech
│   │       ├── query-patterns.md
│   │       └── router-patterns.md
│   └── vue/                            # Tech
│
├── backend/                            # Concern
│   ├── api-patterns/                   # Approach
│   │   ├── rest-design.md
│   │   └── graphql-design.md
│   ├── nodejs/                         # Tech
│   └── authentication/                 # Functional concern
│
└── data/                               # Concern
    ├── sql-patterns/                   # Approach
    └── orm-patterns/                   # Approach
```

---

## Формат файла навигации

### Токен-эффективный шаблон

```markdown
# {Category} Navigation

**Purpose**: [1 sentence]

---

## Structure

```
{category}/
├── navigation.md
├── {subcategory}/
│   ├── navigation.md
│   └── {files}.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **{Task 1}** | `{path}` |
| **{Task 2}** | `{path}` |

---

## By {Concern/Type}

**{Section 1}** → {description}
**{Section 2}** → {description}
```

**Цель**: 200–300 токенов

---

## Принципы организации

### 1. Базовые стандарты (универсальные)

Расположение: `.opencode/context/core/standards/`

**Назначение**: Универсальные стандарты, применимые ко ВСЕЙ разработке

**Содержимое**:
- Принципы качества кода (все языки)
- Стандарты покрытия тестами
- Стандарты документации
- Паттерны безопасности
- Подходы к анализу кода

**Используется**: Всеми агентами, всеми проектами

**Влияние на другие категории**: 
- Другие категории могут ссылаться на эти стандарты
- Пользователи могут редактировать базовые стандарты, чтобы глобально менять поток контекста
- Стандарты, специфичные для разработки, размещаются в `development/principles/`

---

### 2. Принципы разработки vs базовые стандарты

| Расположение | Область | Примеры |
|----------|-------|----------|
| `core/standards/` | **Универсальная** (все проекты, все языки) | Качество кода, тестирование, docs, безопасность |
| `development/principles/` | **Специфичная для разработки** (software engineering) | Clean code, дизайн API, обработка ошибок |

**Нужны оба уровня**: Базовые стандарты универсальны, принципы разработки зависят от домена

---

### 3. Расположение контекста данных

**Решение**: Паттерны данных находятся в `development/data/` (не на верхнем уровне)

**Обоснование**: Слой данных — часть процесса разработки

**Структура**:
```
development/data/
├── navigation.md
├── sql-patterns/
├── nosql-patterns/
└── orm-patterns/
```

**Категория верхнего уровня `data/`**: Зарезервирована для data engineering/analytics (другая задача)

---

### 4. Стратегия специализированной навигации

**Full-stack навигация включает**:
- Быстрые маршруты (в формате таблицы)
- Типовые паттерны стеков (MERN, T3 и т. д.)

**Пример**:
```markdown
## Быстрые маршруты
| Task | Path |
|------|------|
| **Frontend** | `ui-navigation.md` |

## Common Stacks

### MERN Stack
Frontend: development/frontend/react/
Backend:  development/backend/nodejs/
Data:     development/data/nosql-patterns/mongodb.md
```

---

## Операции

### Harvest (`/context harvest`)

**Назначение**: Извлечь знания из summary-файлов → постоянный контекст, затем очистить.

**Процесс**:
1. Просканировать паттерны: `*OVERVIEW.md`, `*SUMMARY.md`, `SESSION-*.md`, `CONTEXT-*.md`
2. Проанализировать содержимое:
   - Дизайн-решения → `concepts/`
   - Решения/паттерны → `examples/`
   - Процессы → `guides/`
   - Встреченные ошибки → `errors/`
   - Справочные данные → `lookup/`
3. Показать UI подтверждения (по буквам: `A B C` или `all`)
4. Извлечь + минимизировать (применить MVI)
5. Архивировать/удалить сводки
6. Сообщить результаты

---

### Extract (`/context extract`)

**Назначение**: Извлечь контекст из docs/кода/URL.

**Процесс**:
1. Прочитать источник
2. Извлечь базовые концепции (по 1–3 предложения)
3. Найти минимальные примеры
4. Определить процессы (нумерованные шаги)
5. Собрать lookup-таблицы
6. Зафиксировать ошибки/gotchas
7. Создать ссылки

**Вывод**: Следовать шаблону MVI

---

### Organize (`/context organize`)

**Назначение**: Переструктурировать существующие файлы в подходящий паттерн.

**Процесс**:
1. Просканировать категорию
2. Определить паттерн (по функции или по задаче)
3. Создать недостающие каталоги
4. Переместить/отрефакторить файлы
5. Обновить navigation.md
6. Исправить ссылки

---

### Update (`/context update`)

**Назначение**: Обновить контекст при изменении API/фреймворков.

**Процесс**:
1. Определить, что изменилось
2. Найти затронутые файлы
3. Обновить concepts, examples, guides, lookups
4. Добавить заметки миграции в errors/
5. Проверить ссылки

---

## Соглашения об именовании файлов

### Файлы навигации
- `navigation.md` - Основная навигация для категории/подкатегории
- `{domain}-navigation.md` - Специализированная сквозная навигация

### Файлы контента
- Используйте описательные имена: `code-quality.md`, а не `code.md`
- Добавляйте тип, когда это полезно: `rest-design.md`, `jwt-patterns.md`
- Используйте kebab-case: `scroll-linked-animations.md`

---

## Правила извлечения

### ✅ Извлекайте:
- Базовые концепции (минимально)
- Ключевые паттерны
- Пошаговые процессы
- Критические ошибки
- Быстрые справочные данные
- Ссылки на подробные docs

### ❌ Не извлекайте:
- Многословные объяснения
- Полную API-документацию
- Детали реализации
- Исторический контекст
- Маркетинговый контент
- Дублирующую информацию

---

## Критерии успеха

✅ **Минимально** - Только базовая информация, <200 строк на файл
✅ **Навигируемо** - navigation.md на каждом уровне
✅ **Организовано** - Подходящий паттерн (по функции или по задаче)
✅ **Токен-эффективно** - Файлы навигации ~200–300 токенов
✅ **Самоописывающе** - Имена файлов говорят, что внутри
✅ **Ссылаемо** - Есть ссылки на полные docs
✅ **Ищется** - Легко найти через навигацию
✅ **Поддерживаемо** - Легко обновлять

---

## Связанная документация

- `context-system/guides/navigation-design.md` - Как создавать файлы навигации
- `context-system/guides/organizing-context.md` - Как выбрать паттерн организации
- `context-system/examples/navigation-examples.md` - Хорошие примеры навигации
- `context-system/standards/templates.md` - Шаблоны файлов

---

## Быстрые команды

```bash
/context                      # Quick scan, suggest actions
/context harvest              # Clean up summaries → permanent context
/context extract {source}     # From docs/code/URLs
/context organize {category}  # Restructure flat files → function folders
/context update {what}        # When APIs/frameworks change
/context migrate              # Move global project-intelligence → local project
/context create {category}    # Create new context category
/context error {error}        # Add recurring error to knowledge base
/context compact {file}       # Minimize verbose file to MVI format
/context map [category]       # View context structure
/context validate             # Check integrity, references, sizes
```

**Все операции показывают preview того, что будет создано/перемещено/удалено, перед запросом подтверждения.**
