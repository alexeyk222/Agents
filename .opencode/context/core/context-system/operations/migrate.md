<!-- Context: core/migrate | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Context Migrate

**Назначение**: копировать файлы контекста из global (`~/.config/opencode/context/`) в local (`.opencode/context/`), чтобы они были специфичны для проекта и попадали в git.

**Последнее обновление**: 2026-02-06

---

## Основная проблема

У пользователей, установивших OAC глобально, файлы project-intelligence находятся в `~/.config/opencode/context/project-intelligence/`. Это паттерны конкретного проекта, но они не коммитятся в git и не доступны команде.

**Решение**: мигрировать project-intelligence из global → local, чтобы паттерны версионировались и были доступны команде.

---

## 4-этапный workflow

<workflow id="migrate" enforce="@critical_rules">

### Этап 1: обнаружить источники

Просканировать файлы контекста в глобальном каталоге конфигурации:

```
Scanning global context...

Global location: ~/.config/opencode/context/

Found:
  project-intelligence/
    technical-domain.md (1.2 KB, Version: 1.3)
    navigation.md (800 bytes, Version: 1.0)
    business-domain.md (1.5 KB, Version: 1.1)

Local location: .opencode/context/

Status: No local project-intelligence/ found
```

**Если global context не найден:**
```
No global context found at ~/.config/opencode/context/

Nothing to migrate. Use /add-context to create project intelligence.
```
→ Выход

**Если global project-intelligence не найден (но другой global context существует):**
```
Global context found at ~/.config/opencode/context/ but no project-intelligence/ directory.

Only project-intelligence files are migrated (project-specific patterns).
Core standards stay in global (they're universal, not project-specific).

Nothing to migrate. Use /add-context to create project intelligence.
```
→ Выход

---

### Этап 2: проверить конфликты

Если локальный `.opencode/context/project-intelligence/` уже существует:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Conflict: Local project-intelligence already exists
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Global files:                              Local files:
  technical-domain.md                        technical-domain.md
    Version: 1.3, Updated: 2026-01-15         Version: 1.0, Updated: 2026-02-01
  navigation.md                              navigation.md
    Version: 1.0, Updated: 2026-01-10         Version: 1.0, Updated: 2026-02-01
  business-domain.md                         (not present locally)
    Version: 1.1, Updated: 2026-01-12

Options:
  1. Skip existing — only copy files that don't exist locally
     → Will copy: business-domain.md
     → Will skip: technical-domain.md, navigation.md (local kept)

  2. Overwrite all — replace local with global versions
     → Will overwrite: technical-domain.md, navigation.md
     → Will copy: business-domain.md
     → Local backup created first

  3. Cancel

Choose [1/2/3]: _
```

**Если пользователь выбирает 2 (Overwrite), сначала покажите diff содержимого:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Diff: technical-domain.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Local (current):                    Global (incoming):
  Version: 1.0                        Version: 1.3
  Tech Stack: Next.js 14              Tech Stack: Next.js 15  ← different
  API: basic validation                API: Zod validation     ← different
  Component: same                      Component: same
  Naming: same                         Naming: same

Show full diff? [y/n]: _

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Backup local files to .tmp/backup/migrate-{timestamp}/ before overwriting?
[y/n] (default: y): _
```

Если конфликтов нет → перейти прямо к этапу 3.

---

### Этап 3: одобрение и копирование

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Migration Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Will copy from: ~/.config/opencode/context/project-intelligence/
Will copy to:   .opencode/context/project-intelligence/

Files to copy:
  ✓ technical-domain.md (1.2 KB)
  ✓ navigation.md (800 bytes)
  ✓ business-domain.md (1.5 KB)

After migration:
  → Local files committed to git = team gets your patterns
  → Agents load local (overrides global)
  → Global files remain as fallback for other projects

Proceed? [y/n]: _
```

**Действия после одобрения:**
1. Создать `.opencode/context/project-intelligence/`, если он не существует
2. Скопировать каждый файл из global → local
3. Проверить скопированные файлы (frontmatter, соответствие MVI)

---

### Этап 4: очистка и подтверждение

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Migration Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Copied 3 files to .opencode/context/project-intelligence/

  ✓ technical-domain.md
  ✓ navigation.md
  ✓ business-domain.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Clean up global project-intelligence?

The global files are no longer needed for THIS project (local takes priority).
Keeping them means they still apply as fallback to other projects.

  1. Keep global files (safe default)
  2. Remove global project-intelligence/ (only affects this user)

Choose [1/2] (default: 1): _
```

**Если пользователь выбирает 2 (Remove):**
- Удалить только `~/.config/opencode/context/project-intelligence/`
- НЕ трогать `~/.config/opencode/context/core/` или любой другой глобальный контекст

</workflow>

---

## Что мигрируется

| Мигрируется (специфично для проекта) | НЕ мигрируется (универсальное) |
|---|---|
| `project-intelligence/` | `core/standards/` |
| `project-intelligence/technical-domain.md` | `core/context-system/` |
| `project-intelligence/business-domain.md` | `core/workflows/` |
| `project-intelligence/navigation.md` | `core/guides/` |
| `project-intelligence/decisions-log.md` | Любые другие файлы `core/` |
| `project-intelligence/living-notes.md` | |

**Обоснование**: project intelligence специфичен для проекта (ВАШ технологический стек, ВАШИ паттерны). Core standards универсальны (качество кода, стандарты документации) и должны оставаться глобальными.

---

## Обработка ошибок

**Нет прав доступа:**
```
Error: Cannot write to .opencode/context/project-intelligence/
Check directory permissions and try again.
```

**Глобальный путь не найден:**
```
No global OpenCode config found at ~/.config/opencode/

If you installed to a custom location, set OPENCODE_INSTALL_DIR:
  export OPENCODE_INSTALL_DIR=/your/custom/path
  /context migrate
```

---

## Связанные материалы

- `/add-context` — создать новый project intelligence (интерактивный мастер)
- `/context harvest` — извлечь знания из сводок
- Разрешение путей контекста: `.opencode/context/core/system/context-paths.md`
