<!-- Context: workflows/delegation | Priority: high | Version: 3.1 | Updated: 2026-02-05 -->
# Шаблон контекста делегирования

## Краткая справка

**Процесс**: обнаружить → предложить → одобрить → инициализировать сессию → сохранить контекст → делегировать → очистить

**Расположение**: `.tmp/sessions/{YYYY-MM-DD}-{task-slug}/context.md`

**Ключевой принцип**: ContextScout находит пути. Оркестратор сохраняет их в `context.md` ПОСЛЕ одобрения. Нижестоящие агенты читают `context.md` — без повторного поиска.

---

## Когда создавать сессию

Создавайте сессию только когда:
- Пользователь **одобрил** предложенный подход (никогда раньше)
- Задача требует делегирования в TaskManager или рабочим агентам
- Задача достаточно сложная и требует общего контекста (4+ файла, >60 мин)

Для простых задач (1-3 файла, прямое выполнение) полностью пропускайте создание сессии.

---

## Поток

```
Stage 1: DISCOVER   → ContextScout finds paths (read-only, nothing written)
Stage 2: PROPOSE    → Show user lightweight summary (nothing written)
Stage 3: APPROVE    → User says yes. NOW we can write.
Stage 4: INIT       → Create session dir + context.md (persist discovered paths here)
Stage 5: DELEGATE   → Pass session path to TaskManager / working agents
Stage 6: CLEANUP    → Ask user, then delete session dir
```

---

## Структура шаблона

**Расположение**: `.tmp/sessions/{YYYY-MM-DD}-{task-slug}/context.md`

```markdown
# Task Context: {Task Name}

Session ID: {YYYY-MM-DD}-{task-slug}
Created: {ISO timestamp}
Status: in_progress

## Current Request
{What user asked for — verbatim or close paraphrase}

## Файлы контекста (стандарты для соблюдения)
Paths ContextScout discovered. Downstream agents load these for coding standards.
- .opencode/context/core/standards/code-quality.md
- {other paths}

## Справочные файлы (исходный материал)
Project files relevant to the task — NOT standards.
- {e.g. package.json}
- {e.g. src/existing-module.ts}

## External Context Fetched
Live docs fetched via ExternalScout. Read-only cache.
- `.tmp/external-context/{package}/{topic}.md` — {description}

## Components
- {Component 1} — {what it does}
- {Component 2} — {what it does}

## Constraints
{Technical constraints, preferences, version requirements}

## Exit Criteria
- [ ] {specific completion condition}

## Progress
- [ ] Session initialized
- [ ] Tasks created (if using TaskManager)
- [ ] Implementation complete
```

---

## Процесс делегирования

**Шаги 1-3: обнаружить, предложить, одобрить** (до любых записей)
- Вызвать ContextScout, сохранить пути
- Вызвать ExternalScout, если задействованы внешние библиотеки
- Показать пользователю краткое резюме, дождаться одобрения

**Шаг 4: инициализировать сессию** (первые записи, после одобрения)
- Создать `.tmp/sessions/{YYYY-MM-DD}-{task-slug}/`
- Записать `context.md` с найденными путями

**Шаг 5: делегировать**
```javascript
task(
  subagent_type="TaskManager",
  description="{brief}",
  prompt="Load context from .tmp/sessions/{session-id}/context.md
          {specific instructions}"
)
```

**Шаг 6: очистка**
- Спросить пользователя: "Задача завершена. Очистить файлы сессии?"
- Если одобрено: удалить каталог сессии

---

## Семантические правила для Task JSON

| Поле | Содержит | Пример |
|-------|----------|---------|
| `context_files` | **Только стандарты** | `.opencode/context/core/standards/code-quality.md` |
| `reference_files` | **Только исходные материалы** | `src/auth/service.ts` |
| `external_context` | **Только внешняя документация** (только чтение) | `.tmp/external-context/drizzle/schemas.md` |

**Никогда не смешивайте их.** Стандарты, исходные материалы и внешняя документация — разные вещи.

---

## Что ожидают нижестоящие агенты

| Агент | Читает | Делает |
|-------|-------|------|
| **TaskManager** | `context.md` (полностью) | Извлекает файлы, создает JSON подзадач |
| **CoderAgent** | JSON подзадачи | Загружает стандарты, сверяется с исходниками, реализует |
| **TestEngineer** | путь сессии | Пишет тесты по тем же стандартам |
| **CodeReviewer** | путь сессии | Проверяет по примененным стандартам |

---

## Связанные материалы

- `task-delegation-specialists.md` - когда какому специалисту делегировать
- `task-delegation-caching.md` - кэширование контекста для повторяющихся шаблонов
- `../context-system/standards/mvi.md` - принцип MVI
