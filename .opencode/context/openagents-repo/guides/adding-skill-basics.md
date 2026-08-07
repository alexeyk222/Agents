<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: добавление OpenCode Skill (основы)

**Предварительно**: сначала загрузите `plugins/context/capabilities/events_skills.md`  
**Цель**: создать каталог OpenCode skill и файл SKILL.md

**Примечание**: это для **OpenCode skills** (внутренняя система). Для **Claude Code Skills** см. `creating-skills.md`.

---

## Обзор

Добавление OpenCode skill включает:
1. Создание структуры каталога skill
2. Создание файла SKILL.md
3. Создание router script (опционально)
4. Создание CLI-реализации (опционально)
5. Регистрацию в registry (опционально)
6. Тестирование

**Время**: ~10–15 минут

---

## Шаг 1: создайте каталог skill

### Выберите имя skill

- **kebab-case**: `task-management`, `brand-guidelines`
- **Описательное**: ясно показывает, что предоставляет skill
- **Короткое**: максимум 3–4 слова

### Создайте структуру

```bash
mkdir -p .opencode/skills/{skill-name}/scripts
```

**Стандартная структура**:
```
.opencode/skills/{skill-name}/
├── SKILL.md              # Required: Main skill documentation
├── router.sh             # Optional: CLI router script
└── scripts/
    └── skill-cli.ts      # Optional: CLI tool implementation
```

---

## Шаг 2: создайте SKILL.md

### Frontmatter

```markdown
---
name: {skill-name}
description: Brief description of what the skill provides
---

# Skill Name

**Purpose**: What this skill helps users do

## What I do

- Feature 1
- Feature 2
- Feature 3

## How to use me

### Basic Commands

```bash
npx ts-node .opencode/skills/{skill-name}/scripts/skill-cli.ts command1
```

### Command Reference

| Command | Description |
|---------|-------------|
| `command1` | What command1 does |
| `command2` | What command2 does |
```

### Claude Code Skills (опционально)

Для Claude Code Skills (`.claude/skills/`) добавьте дополнительный frontmatter:
- `allowed-tools` — ограничения инструментов
- `context` + `agent` — запуск в forked subagent
- `hooks` — события жизненного цикла
- `user-invocable` — скрыть из slash menu

Подробности о Claude Code Skills см. в `creating-skills.md`.

---

## Шаг 3: создайте router-скрипт (опционально)

Для CLI-based skills:

```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ $# -eq 0 ]; then
    echo "Usage: bash router.sh <command> [options]"
    exit 1
fi

COMMAND="$1"
shift

case "$COMMAND" in
    help|--help|-h)
        echo "{Skill Name} - Description"
        echo "Commands: command1, command2, help"
        ;;
    command1|command2)
        npx ts-node "$SCRIPT_DIR/scripts/skill-cli.ts" "$COMMAND" "$@"
        ;;
    *)
        echo "Unknown command: $COMMAND"
        exit 1
        ;;
esac
```

```bash
chmod +x .opencode/skills/{skill-name}/router.sh
```

---

## Следующие шаги

- **CLI-реализация** → `adding-skill-implementation.md`
- **Полный пример** → `adding-skill-example.md`
- **Claude Code Skills** → `creating-skills.md`

---

## Связанное

- `creating-skills.md` — Claude Code Skills (другая система)
- `adding-skill-implementation.md` — CLI и registry
- `adding-skill-example.md` — пример task-management
- `plugins/context/capabilities/events_skills.md` — Skills Plugin
