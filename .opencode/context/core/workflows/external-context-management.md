<!-- Context: workflows/external-context | Priority: high | Version: 1.0 | Updated: 2026-01-28 -->
# Управление внешним контекстом

## Обзор

Внешний контекст — это актуальная документация, полученная из внешних библиотек и фреймворков (через Context7 API или официальную документацию). Вместо повторной загрузки для каждой задачи мы **сохраняем внешний контекст** в `.tmp/external-context/`, чтобы основные агенты могли передавать его subagents.

**Ключевой принцип**: ExternalScout получает один раз → сохраняет на диск → основные агенты ссылаются → subagents читают (без повторной загрузки)

---

## Структура каталогов

```
.tmp/external-context/
├── .manifest.json                    # Metadata about all cached external docs
├── drizzle-orm/
│   ├── modular-schemas.md           # Fetched: "How to organize schemas modularly"
│   ├── postgresql-setup.md          # Fetched: "PostgreSQL setup with Drizzle"
│   └── typescript-config.md         # Fetched: "TypeScript configuration"
├── better-auth/
│   ├── nextjs-integration.md        # Fetched: "Better Auth + Next.js setup"
│   ├── drizzle-adapter.md           # Fetched: "Drizzle adapter for Better Auth"
│   └── session-management.md        # Fetched: "Session handling"
├── next.js/
│   ├── app-router-setup.md          # Fetched: "App Router basics"
│   ├── server-actions.md            # Fetched: "Server Actions patterns"
│   └── middleware.md                # Fetched: "Middleware configuration"
└── tanstack-query/
    ├── server-components.md         # Fetched: "TanStack Query + Server Components"
    └── prefetching.md               # Fetched: "Prefetching strategies"
```

### Правила именования

- **Имя пакета** (каталог): точное имя npm-пакета (kebab-case)
  - ✅ `drizzle-orm`, `better-auth`, `next.js`, `@tanstack/react-query`
  - ❌ `drizzle`, `nextjs`, `tanstack-query`

- **Имя файла** (topic): описание темы в kebab-case
  - ✅ `modular-schemas.md`, `nextjs-integration.md`, `server-components.md`
  - ❌ `modular schemas.md`, `NextJS Integration.md`, `ServerComponents.md`

---

## Файл manifest

**Расположение**: `.tmp/external-context/.manifest.json`

**Назначение**: отслеживать, что закэшировано, когда получено и из какого источника

**Структура**:
```json
{
  "last_updated": "2026-01-28T14:30:22Z",
  "packages": {
    "drizzle-orm": {
      "files": [
        "modular-schemas.md",
        "postgresql-setup.md",
        "typescript-config.md"
      ],
      "last_updated": "2026-01-28T14:30:22Z",
      "source": "Context7 API",
      "official_docs": "https://orm.drizzle.team"
    },
    "better-auth": {
      "files": [
        "nextjs-integration.md",
        "drizzle-adapter.md",
        "session-management.md"
      ],
      "last_updated": "2026-01-28T14:25:10Z",
      "source": "Context7 API",
      "official_docs": "https://better-auth.com"
    },
    "next.js": {
      "files": [
        "app-router-setup.md",
        "server-actions.md",
        "middleware.md"
      ],
      "last_updated": "2026-01-28T14:20:05Z",
      "source": "Context7 API",
      "official_docs": "https://nextjs.org"
    }
  }
}
```

---

## Формат файла

Каждый файл внешнего контекста содержит metadata header, затем содержимое документации.

**Шаблон**:
```markdown
---
source: Context7 API
library: Drizzle ORM
package: drizzle-orm
topic: modular-schemas
fetched: 2026-01-28T14:30:22Z
official_docs: https://orm.drizzle.team/docs/goodies#multi-file-schemas
---

# Modular Schemas in Drizzle ORM

[Filtered documentation content from Context7 API]

## Key Concepts

[Relevant sections only]

## Code Examples

[Practical examples from official docs]

---

**Source**: Context7 API (live, version-specific)
**Official Docs**: https://orm.drizzle.team/docs/goodies#multi-file-schemas
**Fetched**: 2026-01-28T14:30:22Z
```

---

## Процесс: как проходит внешний контекст

### Этап 1: основному агенту нужен внешний контекст

```
Main Agent (e.g., OpenAgent)
  ↓
  Detects: "User is asking about Drizzle + Better Auth + Next.js"
  ↓
  Calls: ExternalScout to fetch live docs
```

### Этап 2: ExternalScout получает и сохраняет

```
ExternalScout
  ↓
  1. Detects libraries: Drizzle, Better Auth, Next.js
  ↓
  2. Fetches from Context7 API (primary) or official docs (fallback)
  ↓
  3. Filters to relevant sections
  ↓
  4. Persists to .tmp/external-context/{package-name}/{topic}.md
  ↓
  5. Updates .manifest.json
  ↓
  Returns: File paths + formatted documentation
```

### Этап 3: основной агент ссылается в контексте сессии

```
Main Agent
  ↓
  Creates session: .tmp/sessions/{session-id}/context.md
  ↓
  Adds section: "## External Context Fetched"
  ↓
  Lists files:
    - .tmp/external-context/drizzle-orm/modular-schemas.md
    - .tmp/external-context/better-auth/nextjs-integration.md
    - .tmp/external-context/next.js/app-router-setup.md
  ↓
  Delegates to TaskManager with session path
```

### Этап 4: subagents читают внешний контекст

```
TaskManager (or CoderAgent, TestEngineer, etc.)
  ↓
  Reads: .tmp/sessions/{session-id}/context.md
  ↓
  Extracts: "## External Context Fetched" section
  ↓
  Reads: .tmp/external-context/{package-name}/{topic}.md files
  ↓
  Uses: External docs to inform implementation
  ↓
  NO RE-FETCHING needed ✅
```

---

## Интеграция с делегированием задач

### В файле контекста сессии

Добавьте этот раздел в `.tmp/sessions/{session-id}/context.md`:

```markdown
## External Context Fetched

These are live documentation files fetched from external libraries. Subagents should reference these instead of re-fetching.

### Drizzle ORM
- `.tmp/external-context/drizzle-orm/modular-schemas.md` — Schema organization patterns
- `.tmp/external-context/drizzle-orm/postgresql-setup.md` — PostgreSQL configuration

### Better Auth
- `.tmp/external-context/better-auth/nextjs-integration.md` — Next.js integration guide
- `.tmp/external-context/better-auth/drizzle-adapter.md` — Drizzle adapter setup

### Next.js
- `.tmp/external-context/next.js/app-router-setup.md` — App Router basics
- `.tmp/external-context/next.js/server-actions.md` — Server Actions patterns

**Important**: These files are read-only and should not be modified. They're cached for reference only.
```

### В JSON подзадач (создает TaskManager)

Когда TaskManager создает JSON подзадач, он должен включать файлы внешнего контекста:

```json
{
  "id": "01-drizzle-schema-setup",
  "title": "Set up Drizzle schema with modular organization",
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
  "instructions": "Set up Drizzle schema following modular patterns from external context..."
}
```

---

## Очистка и сопровождение

### Когда очищать

Файлы внешнего контекста нужно очищать, когда:
1. Задача завершена и сессия удалена
2. Внешняя документация устарела (>7 дней)
3. Пользователь явно запросил очистку
4. Нужно место на диске

### Как очищать

**Ручная очистка** (сначала спросите пользователя):
```bash
rm -rf .tmp/external-context/{package-name}/
# Update .manifest.json to remove package entry
```

**Автоматическая очистка** (будущее улучшение):
- Добавить скрипт очистки, удаляющий файлы старше 7 дней
- Запускать как часть процесса очистки сессии
- Обновлять manifest после очистки

### Очистка manifest

После удаления файлов внешнего контекста обновите `.manifest.json`:
```json
{
  "last_updated": "2026-01-28T15:00:00Z",
  "packages": {
    // Remove entries for deleted packages
  }
}
```

---

## Лучшие практики

### Для основных агентов (OpenAgent и т. д.)

1. **Вызывайте ExternalScout рано** на этапе планирования
2. **Сохраняйте возвращенные пути файлов** от ExternalScout
3. **Добавляйте в контекст сессии** в раздел "## External Context Fetched"
4. **Передавайте путь сессии subagents**, чтобы они знали, где искать внешнюю документацию
5. **Не загружайте повторно** — доверяйте корректному сохранению ExternalScout

### Для ExternalScout

1. **Всегда сохраняйте** полученную документацию в `.tmp/external-context/`
2. **Обновляйте manifest** после каждой загрузки
3. **Добавляйте metadata header** в каждый файл (source, library, package, topic, fetched timestamp)
4. **Фильтруйте агрессивно** — включайте только релевантные разделы
5. **Цитируйте источники** — добавляйте ссылки на официальную документацию

### Для subagents (TaskManager, CoderAgent и т. д.)

1. **Читайте файлы внешнего контекста** из контекста сессии
2. **Не загружайте повторно** — используйте сохраненные файлы
3. **Ссылайтесь в реализации** — указывайте, какая внешняя документация повлияла на решения
4. **Не изменяйте** файлы внешнего контекста — они только для чтения
5. **Включайте в JSON подзадач** — передавайте `external_context` нижестоящим агентам

---

## Примеры

### Пример 1: интеграция Drizzle + Better Auth

**Поток основного агента**:
```
1. User asks: "Set up Drizzle + Better Auth in Next.js"
2. Main agent calls ExternalScout
3. ExternalScout fetches:
   - drizzle-orm/modular-schemas.md
   - drizzle-orm/postgresql-setup.md
   - better-auth/nextjs-integration.md
   - better-auth/drizzle-adapter.md
   - next.js/app-router-setup.md
4. ExternalScout persists all files to .tmp/external-context/
5. Main agent creates session with "## External Context Fetched" section
6. Main agent delegates to TaskManager with session path
7. TaskManager reads external context, creates subtasks
8. CoderAgent implements using external docs (no re-fetching)
```

**Файл контекста сессии**:
```markdown
## External Context Fetched

### Drizzle ORM
- `.tmp/external-context/drizzle-orm/modular-schemas.md`
- `.tmp/external-context/drizzle-orm/postgresql-setup.md`

### Better Auth
- `.tmp/external-context/better-auth/nextjs-integration.md`
- `.tmp/external-context/better-auth/drizzle-adapter.md`

### Next.js
- `.tmp/external-context/next.js/app-router-setup.md`
```

### Пример 2: TanStack Query + Server Components

**Поток основного агента**:
```
1. User asks: "How do I use TanStack Query with Next.js Server Components?"
2. Main agent calls ExternalScout
3. ExternalScout fetches:
   - tanstack-query/server-components.md
   - tanstack-query/prefetching.md
   - next.js/server-components.md
4. ExternalScout persists to .tmp/external-context/
5. Main agent creates session with external context references
6. Subagents read and implement using external docs
```

---

## Устранение неполадок

### Файлы внешнего контекста не найдены

**Проблема**: subagent не может найти `.tmp/external-context/{package-name}/{topic}.md`

**Решение**:
1. Проверьте, что ExternalScout выполнился успешно
2. Убедитесь, что путь в контексте сессии совпадает с фактическим расположением файла
3. Проверьте `.manifest.json`, чтобы увидеть, что закэшировано
4. Если файла нет, повторно запустите ExternalScout для загрузки и сохранения

### Устаревший внешний контекст

**Проблема**: внешняя документация устарела (>7 дней)

**Решение**:
1. Удалите устаревшие файлы: `rm -rf .tmp/external-context/{package-name}/`
2. Обновите `.manifest.json`
3. Повторно запустите ExternalScout для получения свежей документации
4. Обновите контекст сессии новыми путями файлов

### Manifest не синхронизирован

**Проблема**: `.manifest.json` не соответствует фактическим файлам

**Решение**:
1. Пересоздайте manifest по списку фактических файлов:
   ```bash
   find .tmp/external-context -name "*.md" | sort
   ```
2. Обновите `.manifest.json`, чтобы он совпадал
3. Убедитесь, что у всех файлов есть metadata headers

---

## Ссылки

- **ExternalScout**: `.opencode/agent/subagents/core/externalscout.md` — получает и сохраняет внешнюю документацию
- **Делегирование задач**: `.opencode/context/core/workflows/task-delegation-basics.md` — как ссылаться на внешний контекст в сессиях
- **Управление сессиями**: `.opencode/context/core/workflows/session-management.md` — жизненный цикл сессии
- **Реестр библиотек**: `.opencode/skills/context7/library-registry.md` — поддерживаемые библиотеки и паттерны запросов
