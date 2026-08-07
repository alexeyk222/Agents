---
description: Interactive wizard to add project patterns using Project Intelligence standard
tags: [context, onboarding, project-intelligence, wizard]
dependencies:
  - subagent:context-organizer
  - context:core/context-system/standards/mvi.md
  - context:core/context-system/standards/frontmatter.md
  - context:core/standards/project-intelligence.md
---

<context>
  <system>Мастер онбординга Project Intelligence для обучения агентов ВАШИМ шаблонам написания кода</system>
  <domain>Создание project-specific контекста с соблюдением MVI</domain>
  <task>Интерактивный мастер из 6 вопросов → структурированные context-файлы со 100% сохранением шаблонов</task>
</context>

<role>Мастер создания контекста, применяющий стандарты Project Intelligence + MVI + frontmatter</role>

<task>Мастер из 6 вопросов → technical-domain.md с tech stack, API/component patterns, naming, standards и security</task>

<critical_rules priority="absolute" enforcement="strict"> <rule id="project_intelligence">
ОБЯЗАТЕЛЬНО создавать technical-domain.md в директории project-intelligence/ (НЕ единый project-context.md) </rule> <rule id="frontmatter_required">
ВСЕ файлы ОБЯЗАНЫ начинаться с HTML frontmatter: <!-- Context: {category}/{function} | Priority: {level} | Version: X.Y | Updated: YYYY-MM-DD --> </rule> <rule id="mvi_compliance">
Файлы ДОЛЖНЫ содержать <200 строк и просматриваться менее чем за 30 секунд. Формула MVI: концепция в 1–3 предложениях, 3–5 ключевых пунктов, пример на 5–10 строк, ссылка на источник </rule> <rule id="codebase_refs">
ВСЕ файлы ОБЯЗАНЫ содержать раздел "📂 Codebase References", связывающий context→реальную реализацию в коде </rule> <rule id="navigation_update">
При создании/изменении файлов ОБЯЗАТЕЛЬНО обновлять navigation.md (добавлять запись в таблицу Quick Routes или Deep Dives) </rule> <rule id="priority_assignment">
ОБЯЗАТЕЛЬНО назначать priority в зависимости от частоты использования: critical (80%) | high (15%) | medium (4%) | low (1%) </rule> <rule id="version_tracking">
ОБЯЗАТЕЛЬНО отслеживать версии: Новый файл→1.0 | Обновление контента→MINOR (1.1, 1.2) | Изменение структуры→MAJOR (2.0, 3.0) </rule>
</critical_rules>

<execution_priority> <tier level="1" desc="Project Intelligence + MVI + Standards">
- @project_intelligence (technical-domain.md в директории project-intelligence/)
- @mvi_compliance (<200 строк, просмотр менее чем за 30 секунд)
- @frontmatter_required (HTML frontmatter с metadata)
- @codebase_refs (связать context→code)
- @navigation_update (обновить navigation.md)
- @priority_assignment (critical для tech stack/core patterns)
- @version_tracking (1.0 для новых файлов, увеличение версии при обновлениях) </tier> <tier level="2" desc="Workflow мастера">
- Определить существующий context→Review/Add/Replace
- Интерактивный мастер из 6 вопросов
- Создать/обновить technical-domain.md
- Провести валидацию по MVI checklist </tier> <tier level="3" desc="Пользовательский опыт">
- Понятное форматирование с разделителями ━
- Полезные примеры
- Рекомендации по следующим шагам </tier>
<conflict_resolution>Tier 1 всегда имеет приоритет над Tier 2/3 — стандарты не подлежат обсуждению</conflict_resolution>
</execution_priority>

---

## Назначение

Помогает пользователям добавлять проектные шаблоны с использованием стандарта Project Intelligence. **Самый простой способ** обучить агентов ВАШИМ шаблонам написания кода.

**Польза**: Ответьте на 6 вопросов (~5 минут) → получите правильно структурированные context-файлы → агенты будут генерировать код в соответствии с ВАШИМ проектом.

**Стандарты**: @project_intelligence + @mvi_compliance + @frontmatter_required + @codebase_refs

**Примечание**: Внешние context-файлы хранятся в директории `.tmp/` (например, `.tmp/external-context.md`) для временных или внешних знаний, которые впоследствии будут организованы в постоянной context-системе.

**Интеграция внешнего контекста**: Мастер автоматически обнаруживает внешние context-файлы в `.tmp/` и предлагает извлечь из них информацию и использовать её как исходный материал для проектных шаблонов.

---

## Использование

```bash
/add-context                 # Интерактивный мастер (рекомендуется, сохраняет в проект)
/add-context --update        # Обновить существующий context
/add-context --tech-stack    # Добавить/обновить только tech stack
/add-context --patterns      # Добавить/обновить только code patterns
/add-context --global        # Сохранить в global config (~/.config/opencode/) вместо проекта
```

---

## Быстрый старт

**Запуск**: `/add-context`

**Что произойдёт**:

1. Сохраняет данные в `.opencode/context/project-intelligence/` вашего проекта (всегда local)
2. Проверяет наличие внешних context-файлов в `.tmp/` и предлагает извлечь их, если они найдены
3. Проверяет существующий Project Intelligence
4. Задаёт 6 вопросов (~5 минут) ИЛИ предлагает проверить существующие шаблоны
5. Показывает полный preview создаваемых файлов перед записью
6. Создаёт/обновляет technical-domain.md + navigation.md
7. После этого агенты используют ВАШИ шаблоны

**6 вопросов** (~5 минут):

1. Какой tech stack?
2. Пример API endpoint?
3. Пример component?
4. Какие naming conventions?
5. Какие code standards?
6. Какие security requirements?

**Готово!** Теперь агенты используют ВАШИ шаблоны.

**Варианты управления**:

* Обновить шаблоны: `/add-context --update`
* Управлять внешними файлами: `/context harvest` (извлечь, организовать, очистить)
* Перенести данные в постоянный context: `/context harvest`
* Очистить context: `/context harvest` (очищает файлы .tmp/)

---

## Рабочий процесс

### Stage 0.5: Resolve Context Location

Определить, куда должны сохраняться файлы Project Intelligence. Этот этап выполняется ПЕРЕД всеми остальными.

**Поведение по умолчанию**: Всегда использовать локальный `.opencode/context/project-intelligence/`.

**Переопределение**: Флаг `--global` сохраняет данные в `~/.config/opencode/context/project-intelligence/`.

**Разрешение пути:**

1. Если указан флаг `--global` → `$CONTEXT_DIR = ~/.config/opencode/context/project-intelligence/`
2. В противном случае → `$CONTEXT_DIR = .opencode/context/project-intelligence/` (всегда local)

**Если `.opencode/context/` ещё не существует**, создай директорию без дополнительного запроса — структура директорий является частью результата, который будет показан на Stage 4.

**Переменная**: `$CONTEXT_DIR` устанавливается здесь и используется на всех последующих стадиях.

---

### Stage 0: Check for External Context Files

Проверить директорию `.tmp/` на наличие внешних context-файлов (например, `.tmp/external-context.md`, `.tmp/context-*.md`).

**Если внешние файлы найдены**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Найдены внешние context-файлы в .tmp/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Найдены файлы:
  📄 .tmp/external-context.md (2.4 KB)
  📄 .tmp/api-patterns.md (1.8 KB)
  📄 .tmp/component-guide.md (3.1 KB)

Эти файлы можно обработать и организовать в постоянный context.

Варианты:
  1. Продолжить /add-context (пока игнорировать внешние файлы)
  2. Сначала обработать внешние файлы (через /context harvest)

Выберите [1/2]: _
```

**Если выбран вариант 1 (Continue)**:

* Перейти к Stage 1 (определение существующего Project Intelligence)
* Внешние файлы остаются в `.tmp/` для последующей обработки

**Если выбран вариант 2 (Manage external files)**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Управление внешними Context Files
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Для управления внешними context-файлами используйте команду /context:

  /context harvest

Она выполнит:

  ✓ Извлечение знаний из файлов .tmp/
  ✓ Организацию в project-intelligence/
  ✓ Очистку временных файлов
  ✓ Обновление navigation.md

После harvest снова запустите /add-context для создания Project Intelligence.

Начать harvest? [y/n]: _
```

**Если yes**: Завершить выполнение и запустить `/context harvest`

**Если no**: Продолжить `/add-context` (Stage 1)

---

### Stage 1: Detect Existing Context

Проверить `$CONTEXT_DIR`, установленный на Stage 0.5 — это либо `.opencode/context/project-intelligence/`, либо `~/.config/opencode/context/project-intelligence/`.

**Если существует**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Найден существующий Project Intelligence!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Найдены файлы:
  ✓ technical-domain.md (Version: 1.2, Updated: 2026-01-15)
  ✓ business-domain.md (Version: 1.0, Updated: 2026-01-10)
  ✓ navigation.md

Текущие шаблоны:
  📦 Tech Stack: Next.js 14 + TypeScript + PostgreSQL + Tailwind
  🔧 API: Zod validation, error handling
  🎨 Component: Functional components, TypeScript props
  📝 Naming: kebab-case files, PascalCase components
  ✅ Standards: TypeScript strict, Drizzle ORM
  🔒 Security: Input validation, parameterized queries

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Варианты:
  1. Просмотреть и обновить шаблоны (показать каждый)
  2. Добавить новые шаблоны (сохранить все существующие)
  3. Заменить все шаблоны (начать с нуля)
  4. Отмена

Выберите [1/2/3/4]: _
```

**Если пользователь выбирает 3 (Replace all):**

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Replace All: Preview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Будет создан BACKUP существующих файлов в:
  .tmp/backup/project-intelligence-{timestamp}/
    ← technical-domain.md (Version: 1.2)
    ← business-domain.md (Version: 1.0)
    ← navigation.md

Будут УДАЛЕНЫ и СОЗДАНЫ ЗАНОВО:
  $CONTEXT_DIR/technical-domain.md (новая Version: 1.0)
  $CONTEXT_DIR/navigation.md (новая Version: 1.0)

Существующие файлы будут сохранены в backup → при необходимости их можно восстановить из .tmp/backup/.

Продолжить? [y/n]: _
```

**Если context не существует**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Project Intelligence не найден. Создадим его!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Сохранение в: $CONTEXT_DIR

Будут созданы:
  - project-intelligence/technical-domain.md (tech stack и patterns)
  - project-intelligence/navigation.md (краткий обзор)

Займёт ~5 минут. Соответствует @mvi_compliance (<200 строк).

Готовы? [y/n]: _
```

---

### Stage 1.5: Review Existing Patterns (if updating)

**Выполняется только в том случае, если пользователь выбрал "Review and update" на Stage 1.**

Для каждого шаблона показать текущее значение→предложить Keep/Update/Remove.

#### Pattern 1: Tech Stack

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern 1/6: Tech Stack
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Текущее значение:
  Framework: Next.js 14
  Language: TypeScript
  Database: PostgreSQL
  Styling: Tailwind

Варианты: 1. Keep | 2. Update | 3. Remove
Выберите [1/2/3]: _

Если '2': Новый tech stack: _
```

#### Pattern 2: API Pattern

````text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern 2/6: API Pattern
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Текущий API pattern:

```typescript
export async function POST(request: Request) {
  try {
    const body = await request.json()
    const validated = schema.parse(body)
    return Response.json({ success: true })
  } catch (error) {
    return Response.json({ error: error.message }, { status: 400 })
  }
}
````

Варианты: 1. Keep | 2. Update | 3. Remove
Выберите [1/2/3]: _

Если '2': Вставьте новый API pattern: _

````

#### Pattern 3-6: Component, Naming, Standards, Security

*(Тот же формат: показать текущее→Keep/Update/Remove)*

**После проверки всех шаблонов**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Сводка проверки
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Изменения:
  ✓ Tech Stack: Обновлён (Next.js 14 → Next.js 15)
  ✓ API: Сохранён
  ✓ Component: Обновлён (новый pattern)
  ✓ Naming: Сохранён
  ✓ Standards: Обновлены (+2 новых)
  ✓ Security: Сохранён

Version: 1.2 → 1.3 (обновление контента согласно @version_tracking)
Updated: 2026-01-29

Продолжить? [y/n]: _
````

---

### Stage 2: Interactive Wizard (for new patterns)

#### Q1: Tech Stack

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 1/6: Какой у вас tech stack?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Примеры:
  1. Next.js + TypeScript + PostgreSQL + Tailwind
  2. React + Python + MongoDB + Material-UI
  3. Vue + Go + MySQL + Bootstrap
  4. Другое (опишите)

Ваш tech stack: _
```

**Получить**: Framework, Language, Database, Styling

#### Q2: API Pattern

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 2/6: Пример API endpoint?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Вставьте API endpoint из ВАШЕГО проекта, соответствующий вашему API-стилю.

Пример (Next.js):
```

```typescript
export async function POST(request: Request) {
  const body = await request.json()
  const validated = schema.parse(body)
  return Response.json({ success: true })
}
```

```text
Ваш API pattern (вставьте или напишите 'skip'): _
```

**Получить**: API endpoint, error handling, validation, response format

#### Q3: Component Pattern

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 3/6: Пример component?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Вставьте component из ВАШЕГО проекта.

Пример (React):
```

```typescript
interface UserCardProps { name: string; email: string }

export function UserCard({ name, email }: UserCardProps) {
  return <div className="rounded-lg border p-4">
    <h3>{name}</h3><p>{email}</p>
  </div>
}
```

```text
Ваш component (вставьте или напишите 'skip'): _
```

**Получить**: Component structure, props pattern, styling, TypeScript

#### Q4: Naming Conventions

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 4/6: Какие naming conventions?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Примеры:
  Files: kebab-case (user-profile.tsx)
  Components: PascalCase (UserProfile)
  Functions: camelCase (getUserProfile)
  Database: snake_case (user_profiles)

Ваши conventions:
  Files: _
  Components: _
  Functions: _
  Database: _
```

#### Q5: Code Standards

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 5/6: Какие code standards?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Примеры:
  - TypeScript strict mode
  - Validate w/ Zod
  - Use Drizzle for DB queries
  - Prefer server components

Ваши standards (по одному на строку, 'done' для завершения):
  1. _
```

#### Q6: Security Requirements

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q 6/6: Какие security requirements?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Примеры:
  - Validate all user input
  - Use parameterized queries
  - Sanitize before rendering
  - HTTPS only

Ваши requirements (по одному на строку, 'done' для завершения):
  1. _
```

---

### Stage 3: Generate/Update Context

**Preview**:

````text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Preview: technical-domain.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- Context: project-intelligence/technical | Priority: critical | Version: 1.0 | Updated: 2026-01-29 -->

# Technical Domain

**Purpose**: Tech stack, архитектура и development patterns этого проекта.
**Last Updated**: 2026-01-29

## Quick Reference

**Update Triggers**: Изменения tech stack | Новые patterns | Архитектурные решения
**Audience**: Разработчики, AI agents

## Primary Stack

| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| Framework | {framework} | {version} | {why} |
| Language | {language} | {version} | {why} |
| Database | {database} | {version} | {why} |
| Styling | {styling} | {version} | {why} |

## Code Patterns

### API Endpoint

```{language}
{user_api_pattern}
````

### Component

```{language}
{user_component_pattern}
```

## Naming Conventions

| Type       | Convention         | Example   |
| ---------- | ------------------ | --------- |
| Files      | {file_naming}      | {example} |
| Components | {component_naming} | {example} |
| Functions  | {function_naming}  | {example} |
| Database   | {db_naming}        | {example} |

## Code Standards

{user_code_standards}

## Security Requirements

{user_security_requirements}

## 📂 Codebase References

**Implementation**: `{detected_files}` - {desc}
**Config**: package.json, tsconfig.json

## Related Files

* Business Domain (пример: business-domain.md)
* Decisions Log (пример: decisions-log.md)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Размер: {line_count} строк (лимит: 200 согласно @mvi_compliance)
Status: ✅ MVI compliant

Сохранить в: $CONTEXT_DIR/technical-domain.md

Всё правильно? [y/n/edit]: _

````

**Действия**:

- Confirm: записать файл согласно @project_intelligence
- Edit: открыть в editor→после этого провести validation
- Update: показать diff→выделить новое→получить подтверждение

---

### Stage 4: Validation & Creation

**Валидация**:

```text
Запуск validation...

✅ <200 строк (@mvi_compliance)
✅ Присутствует HTML frontmatter (@frontmatter_required)
✅ Присутствуют metadata (Purpose, Last Updated)
✅ Присутствуют codebase refs (@codebase_refs)
✅ Назначен priority: critical (@priority_assignment)
✅ Установлена version: 1.0 (@version_tracking)
✅ Соответствует MVI (<30 секунд на просмотр)
✅ Нет дублирования
````

**Preview navigation.md** (также создаётся/обновляется):

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Preview: navigation.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Project Intelligence

| File | Description | Priority |
|------|-------------|----------|
| technical-domain.md | Tech stack & patterns | critical |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Полный план создания**:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Файлы для записи:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CREATE  $CONTEXT_DIR/technical-domain.md ({line_count} строк)
  CREATE  $CONTEXT_DIR/navigation.md ({nav_line_count} строк)

Итого: 2 файла

Продолжить? [y/n]: _
```

---

### Stage 5: Confirmation & Next Steps

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Project Intelligence успешно создан!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Созданы файлы:
  $CONTEXT_DIR/technical-domain.md
  $CONTEXT_DIR/navigation.md

Расположение: $CONTEXT_DIR

Теперь агенты автоматически используют ВАШИ шаблоны!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Что дальше?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Протестировать:
   opencode --agent OpenCoder
   > "Create API endpoint"
   (Использует ВАШ pattern!)

2. Проверить:
   cat $CONTEXT_DIR/technical-domain.md

3. Добавить business context:
   /add-context --business

4. Начать разработку:
   opencode --agent OpenCoder > "Create user auth system"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Совет: Обновляйте context по мере развития проекта
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Когда вы:
  Добавляете библиотеку → /add-context --update
  Меняете patterns → /add-context --update
  Мигрируете tech → /add-context --update

Агенты останутся синхронизированы!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Совет: Global patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Хотите использовать одинаковые patterns во ВСЕХ проектах?

  /add-context --global

  → Сохраняет в ~/.config/opencode/context/project-intelligence/
  → Используется как fallback для проектов без local context

Уже есть global patterns? Перенесите их в этот проект:

  /context migrate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Подробнее
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Project Intelligence: .opencode/context/core/standards/project-intelligence.md
- MVI Principles: .opencode/context/core/context-system/standards/mvi.md
- Context System: CONTEXT_SYSTEM_GUIDE.md
```

---

## Детали реализации

### External Context Detection (Stage 0)

**Процесс**:

1. Проверить: `ls .tmp/external-context.md .tmp/context-*.md .tmp/*-context.md 2>/dev/null`
2. Если файлы найдены:

   * Показать список внешних context-файлов
   * Предложить варианты: Continue | Manage (через `/context harvest`)
3. Если выбран вариант 1 (Continue):

   * Перейти к Stage 1 (определение существующего Project Intelligence)
   * Внешние файлы остаются в `.tmp/` для последующей обработки через `/context harvest`
4. Если выбран вариант 2 (Manage):

   * Предложить пользователю команду `/context harvest`
   * Объяснить, что делает harvest (extract, organize, clean)
   * Завершить add-context
   * Пользователь запускает `/context harvest` для обработки внешних файлов
   * После завершения harvest пользователь снова запускает `/add-context`

### Pattern Detection (Stage 1)

**Процесс**:

1. Проверить: `ls $CONTEXT_DIR/` (путь определён на Stage 0.5)
2. Прочитать: `cat technical-domain.md` (если существует)
3. Распарсить существующие patterns:

   * Frontmatter: version, updated date
   * Tech stack: таблица "Primary Stack"
   * API/Component: раздел "Code Patterns"
   * Naming: таблица "Naming Conventions"
   * Standards: раздел "Code Standards"
   * Security: раздел "Security Requirements"
4. Показать summary
5. Предложить варианты: Review/Add/Replace/Cancel

### Pattern Review (Stage 1.5)

**Для каждого pattern**:

1. Показать текущее значение, полученное из файла
2. Спросить: Keep | Update | Remove
3. Если Update: запросить новое значение
4. Сохранить изменения в `changes_to_make[]`

**После проверки всех patterns**:

1. Показать summary
2. Рассчитать version согласно @version_tracking (content→MINOR, structure→MAJOR)
3. Получить подтверждение
4. Перейти к Stage 3

### Delegation to ContextOrganizer

```yaml
operation: create | update
template: technical-domain  # Шаблон Project Intelligence
target_directory: project-intelligence

# Для операций create/update
user_responses:
  tech_stack: {framework, language, database, styling}
  api_pattern: string | null
  component_pattern: string | null
  naming_conventions: {files, components, functions, database}
  code_standards: string[]
  security_requirements: string[]

frontmatter:
  context: project-intelligence/technical
  priority: critical  # @priority_assignment (80% случаев использования)
  version: {calculated}  # @version_tracking
  updated: {current_date}

validation:
  max_lines: 200  # @mvi_compliance
  has_frontmatter: true  # @frontmatter_required
  has_codebase_references: true  # @codebase_refs
  navigation_updated: true  # @navigation_update
```

**Примечание**: Управление внешними context-файлами (harvest, extract, organize) выполняется командой `/context harvest`, а не `/add-context`.

### File Structure Inference

**Определять типичную структуру на основе tech stack**:

Next.js: `src/app/ components/ lib/ db/`

React: `src/components/ hooks/ utils/ api/`

Express: `src/routes/ controllers/ models/ middleware/`

---

## Критерии успешного выполнения

**Пользовательский опыт**:

* [ ] Мастер завершён менее чем за 5 минут
* [ ] Следующие шаги понятны
* [ ] Процесс обновления понятен

**Качество файлов**:

* [ ] @mvi_compliance (<200 строк, просмотр <30 секунд)
* [ ] @frontmatter_required (HTML frontmatter)
* [ ] @codebase_refs (раздел codebase references)
* [ ] @priority_assignment (critical для tech stack)
* [ ] @version_tracking (1.0 для нового файла, увеличение версии при обновлении)

**Системная интеграция**:

* [ ] @project_intelligence (technical-domain.md в project-intelligence/)
* [ ] @navigation_update (navigation.md обновлён)
* [ ] Агенты загружают и используют patterns
* [ ] Нет дублирования

---

## Примеры

### Пример 1: Первый запуск (Context отсутствует)

```bash
/add-context

# Q1: Next.js + TypeScript + PostgreSQL + Tailwind
# Q2: [вставляет Next.js API route]
# Q3: [вставляет React component]
# Q4-6: [ответы]

✅ Созданы: technical-domain.md, navigation.md
```

### Пример 2: Review & Update

```bash
/add-context

# Найден существующий context → выбрать "1. Review and update"
# Pattern 1: Tech Stack → Update (Next.js 14 → 15)
# Pattern 2-6: Keep

✅ Обновлено: Version 1.2 → 1.3
```

### Пример 3: Быстрое обновление

```bash
/add-context --tech-stack

# Текущее: Next.js 15 + TypeScript + PostgreSQL + Tailwind
# Новое: Next.js 15 + TypeScript + PostgreSQL + Drizzle + Tailwind

✅ Version 1.4 → 1.5
```

### Пример 4: Присутствуют внешние Context Files

```bash
/add-context

# Найдены внешние context-файлы в .tmp/
#   📄 .tmp/external-context.md (2.4 KB)
#   📄 .tmp/api-patterns.md (1.8 KB)
#
# Варианты:
#   1. Продолжить /add-context (пока игнорировать внешние файлы)
#   2. Сначала обработать внешние файлы (через /context harvest)
#
# Выберите [1/2]: 2
#
# Для управления внешними context-файлами используйте:
#   /context harvest
#
# Команда выполнит:
#   ✓ Извлечение знаний из файлов .tmp/
#   ✓ Организацию в project-intelligence/
#   ✓ Очистку временных файлов
#   ✓ Обновление navigation.md
#
# После harvest снова запустите /add-context.
```

### Пример 5: После Harvest внешнего Context

```bash
# После выполнения: /context harvest

/add-context

# В .tmp/ не найдено внешних context-файлов
# Переход к поиску существующего Project Intelligence...
#
# ✅ Создан: technical-domain.md (объединён с patterns, полученными через harvest)
```

---

## Обработка ошибок

**Некорректный ввод**:

```text
⚠️ Некорректный ввод

Ожидалось: описание Tech stack
Получено: [empty]

Пример: Next.js + TypeScript + PostgreSQL + Tailwind
```

**Файл слишком большой**:

```text
⚠️ Превышено ограничение 200 строк (@mvi_compliance)

Текущее значение: 245 | Лимит: 200

Упростите patterns или разделите их на несколько файлов.
```

**Некорректный синтаксис**:

```text
⚠️ Некорректный синтаксис кода в API pattern

Ошибка: Unexpected token line 3

Проверьте код и повторите попытку.
```

---

## Советы

**Держите всё просто**: Сосредоточьтесь на наиболее распространённых patterns, остальные можно добавить позже.

**Используйте реальные примеры**: Вставляйте настоящий код из ВАШЕГО проекта.

**Регулярно обновляйте**: Запускайте `/add-context --update`, когда patterns изменяются.

**Протестируйте после изменений**: Создайте что-нибудь простое, чтобы убедиться, что агенты корректно используют patterns.

---

## Устранение неполадок

**Q: Агенты не используют patterns?**

A: Проверьте, что файл существует и содержит <200 строк. Запустите `/context validate`.

**Q: Как посмотреть содержимое context?**

A: `cat .opencode/context/project-intelligence/technical-domain.md` (local) или `cat ~/.config/opencode/context/project-intelligence/technical-domain.md` (global)

**Q: Можно использовать несколько context-файлов?**

A: Да! Создавайте их в директории project-intelligence. Агенты загрузят все.

**Q: Как удалить pattern?**

A: Отредактируйте напрямую: `nano .opencode/context/project-intelligence/technical-domain.md`

**Q: Можно поделиться с командой?**

A: Да! Используйте local install (`.opencode/context/project-intelligence/`) и добавьте его в repo. Участники команды автоматически получат ваши patterns.

**Q: Local vs global?**

A: Local (`.opencode/`) = project-specific, хранится в git и используется командой. Global (`~/.config/opencode/`) = личные значения по умолчанию для всех проектов. Local имеет приоритет над global.

**Q: OAC установлен globally, но нужны project patterns?**

A: Запустите `/add-context` — по умолчанию используется local. Команда создаст `.opencode/context/project-intelligence/` внутри проекта, даже если OAC был установлен globally.

**Q: Есть внешние context-файлы в .tmp/?**

A: Запустите `/context harvest`, чтобы извлечь информацию и организовать её в постоянный context.

**Q: Нужно очистить файлы .tmp/?**

A: Запустите `/context harvest`, чтобы извлечь знания и очистить временные файлы.

**Q: Как перенести файлы .tmp/ в постоянный context?**

A: Запустите `/context harvest`, чтобы извлечь и организовать их.

**Q: Как обновить внешние context-файлы?**

A: Отредактируйте напрямую: `nano .tmp/external-context.md`, затем запустите `/context harvest`.

**Q: Как удалить конкретный внешний файл?**

A: Удалите напрямую: `rm .tmp/external-context.md`, затем запустите `/context harvest`.

---

## Связанные команды

* `/context` — управление context-файлами (harvest, organize, validate)
* `/context validate` — проверка целостности
* `/context map` — просмотр структуры
