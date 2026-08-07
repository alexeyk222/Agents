<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: добавление нового агента (основы)

**Предварительно**: сначала загрузите `core-concepts/agents.md`  
**Цель**: создать и зарегистрировать нового агента за 4 шага

---

## Обзор

Добавление нового агента включает:
1. Создание файла агента
2. Создание структуры тестов
3. Обновление registry
4. Проверку, что всё работает

**Время**: ~15–20 минут

---

## Шаг 1: создайте файл агента

### Выберите категорию

```bash
# Available categories:
# - core/          (system agents)
# - development/   (dev specialists)
# - content/       (content creators)
# - data/          (data analysts)
# - product/       (product managers)
# - learning/      (educators)
```

### Создайте файл с frontmatter

```bash
touch .opencode/agent/{category}/{agent-name}.md
```

```markdown
---
description: "Brief description of what this agent does"
category: "{category}"
type: "agent"
tags: ["tag1", "tag2"]
dependencies: []
---

# Agent Name

**Purpose**: What this agent does

## Focus
- Key responsibility 1
- Key responsibility 2

## Рабочий процесс
1. Step 1
2. Step 2

## Constraints
- Constraint 1
- Constraint 2
```

---

## Шаг 2: создайте структуру тестов

```bash
# Create directories
mkdir -p evals/agents/{category}/{agent-name}/{config,tests}

# Create config
cat > evals/agents/{category}/{agent-name}/config/config.yaml << 'EOF'
agent: {category}/{agent-name}
model: anthropic/claude-sonnet-4-5
timeout: 60000
suites:
  - smoke
EOF

# Create smoke test
cat > evals/agents/{category}/{agent-name}/tests/smoke-test.yaml << 'EOF'
name: Smoke Test
description: Basic functionality check
agent: {category}/{agent-name}
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Hello, can you help me?"
expectations:
  - type: no_violations
EOF
```

---

## Шаг 3: обновите registry

```bash
# Dry run first
./scripts/registry/auto-detect-components.sh --dry-run

# Add to registry
./scripts/registry/auto-detect-components.sh --auto-add

# Verify
cat registry.json | jq '.components.agents[] | select(.id == "{agent-name}")'
```

---

## Шаг 4: проверьте

```bash
# Validate registry
./scripts/registry/validate-registry.sh

# Run smoke test
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent-name} --pattern="smoke-test.yaml"

# Test installation
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

---

## Чеклист

- [ ] Файл агента создан с корректным frontmatter
- [ ] Структура тестов создана (config + smoke test)
- [ ] Registry обновлен через auto-detect
- [ ] Валидация registry проходит
- [ ] Smoke-тест проходит
- [ ] Агент отображается в `./install.sh --list`

---

## Следующие шаги

- **Добавить больше тестов** → `adding-agent-testing.md`
- **Тщательно протестировать** → `testing-agent.md`
- **Разобрать ошибки** → `debugging.md`

---

## Связанное

- `core-concepts/agents.md` — концепции агентов
- `adding-agent-testing.md` — дополнительные шаблоны тестов
- `testing-agent.md` — руководство по тестированию
- `creating-subagents.md` — Claude Code subagents (другая система)
