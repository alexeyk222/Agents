<!-- Context: workflows/external-context-integration | Priority: high | Version: 1.0 | Updated: 2026-01-28 -->
# Руководство: интеграция внешнего контекста

## Обзор

Это руководство объясняет, как встроить внешний контекст (полученный через ExternalScout) в workflow основного агента, чтобы subagents могли использовать его без повторной загрузки.

**Ключевой принцип**: основные агенты получают внешнюю документацию один раз → сохраняют на диск → ссылаются в сессии → subagents читают (без повторной загрузки)

---

## Когда использовать внешний контекст

Используйте ExternalScout для получения внешнего контекста, когда:

1. **Пользователь спрашивает о внешних библиотеках** (Drizzle, Better Auth, Next.js и т. д.)
2. **Задача включает интеграцию** между несколькими внешними библиотеками
3. Нужна **настройка или конфигурация** внешних инструментов
4. Релевантны **API-паттерны или лучшие практики** внешних библиотек

**Не используйте**, когда:
- Вопрос про внутренний код проекта
- Ответ есть в `.opencode/context/` (используйте ContextScout)
- Пользователь спрашивает общие концепции программирования

---

## Процесс интеграции

### Этап 1: анализ и обнаружение (до одобрения)

```
Main Agent (OpenAgent, etc.)
  ↓
  1. Analyze user request
  ↓
  2. Identify external libraries mentioned
  ↓
  3. Call ContextScout for internal context
  ↓
  4. Call ExternalScout for external docs
     - ExternalScout fetches from Context7 API
     - ExternalScout persists to .tmp/external-context/
     - ExternalScout returns file paths
  ↓
  5. Capture returned file paths
  ↓
  6. Do NOT write anything to disk yet
```

### Этап 2: предложить план (до одобрения)

```
Main Agent
  ↓
  1. Show user lightweight summary:
     - What will be done
     - Which external libraries involved
     - Which context files will be used
  ↓
  2. Include discovered external context files in proposal
  ↓
  3. Wait for user approval
```

### Этап 3: одобрение (user gate)

```
User
  ↓
  Approves plan (or redirects)
```

### Этап 4: инициализировать сессию (после одобрения)

```
Main Agent
  ↓
  1. Create .tmp/sessions/{session-id}/context.md
  ↓
  2. Populate sections:
     - ## Context Files (from ContextScout)
     - ## Reference Files (project files)
     - ## External Context Fetched (from ExternalScout)
     - ## Components
     - ## Constraints
     - ## Exit Criteria
  ↓
  3. CRITICAL: Add "## External Context Fetched" section with:
     - File paths returned by ExternalScout
     - Brief description of each file
     - Note that files are read-only
```

### Этап 5: делегировать с путем к контексту

```
Main Agent
  ↓
  1. Call TaskManager (or other subagent)
  ↓
  2. Pass session path in prompt:
     "Load context from .tmp/sessions/{session-id}/context.md"
  ↓
  3. TaskManager reads session context
  ↓
  4. TaskManager extracts external context files
  ↓
  5. TaskManager includes in subtask JSONs
```

### Этап 6: subagents читают внешний контекст

```
TaskManager / CoderAgent / TestEngineer
  ↓
  1. Read session context file
  ↓
  2. Extract "## External Context Fetched" section
  ↓
  3. Read referenced files from .tmp/external-context/
  ↓
  4. Use external docs to inform implementation
  ↓
  5. NO RE-FETCHING ✅
```

---

## Детали реализации

### Шаг 1: вызвать ExternalScout

В основном агенте (до одобрения):

```javascript
// Detect external libraries from user request
const externalLibraries = ["drizzle-orm", "better-auth", "next.js"];

// Call ExternalScout
task(
  subagent_type="ExternalScout",
  description="Fetch external documentation",
  prompt="Fetch documentation for these libraries:
          - Drizzle ORM: modular schema organization
          - Better Auth: Next.js integration
          - Next.js: App Router setup
          
          Persist fetched docs to .tmp/external-context/
          Return file paths for each fetched document"
)

// Capture returned file paths
// Example return:
// - .tmp/external-context/drizzle-orm/modular-schemas.md
// - .tmp/external-context/better-auth/nextjs-integration.md
// - .tmp/external-context/next.js/app-router-setup.md
```

### Шаг 2: предложить план с внешним контекстом

```markdown
## План реализации

**Task**: Set up Drizzle + Better Auth in Next.js

**External Libraries Involved**:
- Drizzle ORM (database)
- Better Auth (authentication)
- Next.js (framework)

**External Context Discovered**:
- `.tmp/external-context/drizzle-orm/modular-schemas.md`
- `.tmp/external-context/better-auth/nextjs-integration.md`
- `.tmp/external-context/next.js/app-router-setup.md`

**Approach**:
1. Set up Drizzle schema with modular organization
2. Configure Better Auth with Drizzle adapter
3. Integrate with Next.js App Router

**Approval needed before proceeding.**
```

### Шаг 3: создать сессию с внешним контекстом

После одобрения создайте `.tmp/sessions/{session-id}/context.md`:

```markdown
# Task Context: Drizzle + Better Auth Integration

Session ID: 2026-01-28-drizzle-auth
Created: 2026-01-28T14:30:22Z
Status: in_progress

## Current Request
Set up Drizzle ORM with Better Auth in a Next.js application

## Файлы контекста (стандарты для соблюдения)
- .opencode/context/core/standards/code-quality.md
- .opencode/context/core/standards/test-coverage.md

## Справочные файлы (исходный материал)
- package.json
- src/db/schema.ts (existing)
- src/auth/config.ts (existing)

## External Context Fetched
These are live documentation files fetched from external libraries. Subagents should reference these instead of re-fetching.

### Drizzle ORM
- `.tmp/external-context/drizzle-orm/modular-schemas.md` — Schema organization patterns for modular architecture
- `.tmp/external-context/drizzle-orm/postgresql-setup.md` — PostgreSQL configuration and setup

### Better Auth
- `.tmp/external-context/better-auth/nextjs-integration.md` — Integration guide for Next.js App Router
- `.tmp/external-context/better-auth/drizzle-adapter.md` — Drizzle adapter setup and configuration

### Next.js
- `.tmp/external-context/next.js/app-router-setup.md` — App Router basics and configuration
- `.tmp/external-context/next.js/server-actions.md` — Server Actions patterns for mutations

**Important**: These files are read-only and cached for reference. Do not modify them.

## Components
- Drizzle schema setup with modular organization
- Better Auth configuration with Drizzle adapter
- Next.js App Router integration

## Constraints
- TypeScript strict mode
- Must support PostgreSQL
- Backward compatible with existing auth system

## Exit Criteria
- [ ] Drizzle schema set up with modular organization
- [ ] Better Auth configured with Drizzle adapter
- [ ] Next.js App Router integration complete
- [ ] All tests passing
- [ ] Documentation updated

## Progress
- [ ] Session initialized
- [ ] Tasks created
- [ ] Implementation complete
- [ ] Tests passing
- [ ] Handoff complete
```

### Шаг 4: делегировать TaskManager

```javascript
task(
  subagent_type="TaskManager",
  description="Break down Drizzle + Better Auth integration",
  prompt="Load context from .tmp/sessions/2026-01-28-drizzle-auth/context.md

          Read the context file for full requirements, standards, and external documentation.
          
          Break down this feature into atomic subtasks:
          1. Drizzle schema setup with modular organization
          2. Better Auth configuration with Drizzle adapter
          3. Next.js App Router integration
          4. Test suite
          
          For each subtask, include:
          - context_files: Standards from context.md
          - reference_files: Project files to understand
          - external_context: External docs to reference
          
          Create subtask files in tasks/subtasks/drizzle-auth-integration/"
)
```

### Шаг 5: TaskManager создает подзадачи с внешним контекстом

TaskManager создает JSON подзадач, например:

```json
{
  "id": "01-drizzle-schema-setup",
  "title": "Set up Drizzle schema with modular organization",
  "description": "Create modular Drizzle schema following best practices",
  "context_files": [
    ".opencode/context/core/standards/code-quality.md",
    ".opencode/context/core/standards/test-coverage.md"
  ],
  "reference_files": [
    "package.json",
    "src/db/schema.ts"
  ],
  "external_context": [
    ".tmp/external-context/drizzle-orm/modular-schemas.md",
    ".tmp/external-context/drizzle-orm/postgresql-setup.md"
  ],
  "instructions": "Set up Drizzle schema following modular patterns from external context. Reference .tmp/external-context/drizzle-orm/modular-schemas.md for best practices.",
  "acceptance_criteria": [
    "Schema organized into separate files by domain",
    "PostgreSQL configuration matches external docs",
    "TypeScript types properly exported",
    "Tests cover schema setup"
  ]
}
```

### Шаг 6: CoderAgent реализует, используя внешний контекст

CoderAgent читает JSON подзадачи и:

1. Загружает `context_files` (стандарты)
2. Читает `reference_files` (существующий код)
3. **Читает файлы `external_context`** (внешняя документация)
4. Реализует с учетом всех стандартов и внешней документации
5. Возвращает завершенную подзадачу

---

## Лучшие практики

### Для основных агентов

✅ **ДЕЛАЙТЕ**:
- Вызывайте ExternalScout рано на этапе планирования
- Сохраняйте возвращенные пути файлов
- Добавляйте в контекст сессии в раздел "## External Context Fetched"
- Передавайте путь сессии subagents
- Включайте внешний контекст в предложение пользователю

❌ **НЕ ДЕЛАЙТЕ**:
- Не забывайте вызывать ExternalScout, когда задействованы внешние библиотеки
- Не пропускайте добавление внешнего контекста в сессию
- Не загружайте внешнюю документацию повторно (доверяйте сохранению ExternalScout)
- Не изменяйте файлы внешнего контекста

### Для ExternalScout

✅ **ДЕЛАЙТЕ**:
- Всегда сохраняйте полученную документацию в `.tmp/external-context/`
- Обновляйте `.manifest.json` после каждой загрузки
- Включайте metadata header в каждый файл
- Агрессивно фильтруйте до релевантных разделов
- Цитируйте источники и добавляйте ссылки на официальную документацию

❌ **НЕ ДЕЛАЙТЕ**:
- Не забывайте сохранять файлы
- Не пропускайте обновления manifest
- Не возвращайте всю документацию целиком
- Не выдумывайте содержимое документации
- Не пишите за пределами `.tmp/external-context/`

### Для TaskManager

✅ **ДЕЛАЙТЕ**:
- Извлекайте `external_context` из контекста сессии
- Включайте в JSON подзадач
- Передавайте нижестоящим агентам
- Документируйте, какая внешняя документация повлияла на решения

❌ **НЕ ДЕЛАЙТЕ**:
- Не забывайте включать `external_context` в подзадачи
- Не смешивайте `external_context` с `context_files`
- Не предполагайте, что subagents будут загружать повторно

### Для subagents (CoderAgent, TestEngineer и т. д.)

✅ **ДЕЛАЙТЕ**:
- Читайте файлы `external_context` из JSON подзадачи
- Используйте внешнюю документацию для реализации
- Ссылайтесь на внешнюю документацию в комментариях
- Следуйте паттернам из внешней документации

❌ **НЕ ДЕЛАЙТЕ**:
- Не загружайте внешнюю документацию повторно
- Не игнорируйте файлы внешнего контекста
- Не изменяйте файлы внешнего контекста
- Не считайте внешнюю документацию необязательной

---

## Пример: полный поток

### Запрос пользователя
```
"Set up Drizzle ORM with Better Auth in Next.js, using modular schema organization"
```

### Поток основного агента

1. **Анализ**: обнаружить Drizzle, Better Auth, Next.js
2. **Обнаружение**: вызвать ContextScout + ExternalScout
3. **Предложение**: показать план с файлами внешнего контекста
4. **Одобрение**: пользователь одобряет
5. **Инициализация сессии**: создать `context.md` с разделом внешнего контекста
6. **Делегирование**: вызвать TaskManager с путем сессии
7. **Проверка**: проверить, что тесты проходят
8. **Завершение**: обновить docs, очистить

### Поток ExternalScout

1. **Обнаружение**: Drizzle, Better Auth, Next.js
2. **Получение**: получить документацию из Context7 API
3. **Фильтрация**: извлечь релевантные разделы
4. **Сохранение**: записать в `.tmp/external-context/{package}/{topic}.md`
5. **Обновление**: добавить в `.manifest.json`
6. **Возврат**: вернуть пути файлов основному агенту

### Поток TaskManager

1. **Чтение**: `context.md` сессии
2. **Извлечение**: файлы внешнего контекста
3. **Создание**: подзадачи с полем `external_context`
4. **Делегирование**: передать CoderAgent

### Поток CoderAgent

1. **Чтение**: JSON подзадачи
2. **Загрузка**: `context_files` (стандарты)
3. **Справка**: `reference_files` (существующий код)
4. **Чтение**: файлы `external_context` (внешняя документация)
5. **Реализация**: реализовать по всем стандартам и внешней документации
6. **Завершение**: вернуть реализованную подзадачу

---

## Устранение неполадок

### Файлы внешнего контекста не найдены

**Проблема**: subagent не может найти `.tmp/external-context/{package}/{topic}.md`

**Решение**:
1. Проверьте, что ExternalScout выполнился успешно
2. Убедитесь, что путь в контексте сессии совпадает с фактическим расположением
3. Проверьте `.manifest.json`, чтобы увидеть, что закэшировано
4. Если файла нет, повторно запустите ExternalScout

### Устаревший внешний контекст

**Проблема**: внешняя документация устарела

**Решение**:
1. Удалите устаревшие файлы: `scripts/external-context/manage-external-context.sh delete-package {package}`
2. Повторно запустите ExternalScout для свежей документации
3. Обновите контекст сессии новыми путями файлов

### Manifest не синхронизирован

**Проблема**: `.manifest.json` не соответствует фактическим файлам

**Решение**:
1. Пересоздайте manifest: `scripts/external-context/manage-external-context.sh regenerate-manifest`
2. Убедитесь, что у всех файлов есть metadata headers

---

## Ссылки

- **ExternalScout**: `.opencode/agent/subagents/core/externalscout.md`
- **Управление внешним контекстом**: `.opencode/context/core/workflows/external-context-management.md`
- **Делегирование задач**: `.opencode/context/core/workflows/task-delegation-basics.md`
- **Скрипт управления**: `scripts/external-context/manage-external-context.sh`
