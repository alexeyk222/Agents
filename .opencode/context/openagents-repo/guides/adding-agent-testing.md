<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: добавление тестов агента

**Предварительно**: сначала загрузите `adding-agent-basics.md`  
**Цель**: дополнительные шаблоны тестов для агентов

---

## Дополнительные типы тестов

### Тест approval gate

```yaml
# evals/agents/{category}/{agent-name}/tests/approval-gate.yaml
name: Approval Gate Test
description: Verify agent requests approval before execution
agent: {category}/{agent-name}
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Create a new file called test.js"
expectations:
  - type: specific_evaluator
    evaluator: approval_gate
    should_pass: true
```

### Тест загрузки контекста

```yaml
# evals/agents/{category}/{agent-name}/tests/context-loading.yaml
name: Context Loading Test
description: Verify agent loads required context
agent: {category}/{agent-name}
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Write a new function"
expectations:
  - type: context_loaded
    contexts: ["core/standards/code-quality.md"]
```

---

## Полный пример: API Specialist

```bash
# 1. Create agent file
cat > .opencode/agent/subagents/development/api-specialist.md << 'EOF'
---
description: "Expert in REST and GraphQL API design"
category: "development"
type: "agent"
tags: ["api", "rest", "graphql"]
dependencies: ["subagent:tester"]
---

# API Specialist

**Purpose**: Design and implement robust APIs

## Focus
- REST API design
- GraphQL schemas
- API documentation
- Authentication/authorization

## Рабочий процесс
1. Analyze requirements
2. Design API structure
3. Implement endpoints
4. Add tests
5. Document API

## Constraints
- Follow REST best practices
- Use proper HTTP methods
- Include error handling
- Add comprehensive tests
EOF

# 2. Create test structure
mkdir -p evals/agents/development/api-specialist/{config,tests}

cat > evals/agents/development/api-specialist/config/config.yaml << 'EOF'
agent: development/api-specialist
model: anthropic/claude-sonnet-4-5
timeout: 60000
suites:
  - smoke
EOF

cat > evals/agents/development/api-specialist/tests/smoke-test.yaml << 'EOF'
name: Smoke Test
description: Basic functionality check
agent: development/api-specialist
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Hello, can you help me design an API?"
expectations:
  - type: no_violations
EOF

# 3. Update registry
./scripts/registry/auto-detect-components.sh --auto-add

# 4. Validate
./scripts/registry/validate-registry.sh
cd evals/framework && npm run eval:sdk -- --agent=development/api-specialist --pattern="smoke-test.yaml"
```

---

## Частые проблемы

| Проблема | Решение |
|---------|----------|
| Auto-detect не находит агента | Проверьте, что frontmatter — валидный YAML |
| Registry validation падает | Проверьте корректность пути к файлу |
| Тест неожиданно падает | Загрузите `debugging.md` для диагностики |

---

## Claude Code Subagent (опционально)

Для помощников только для Claude Code создайте project subagent:

- **Путь**: `.claude/agents/{subagent-name}.md`
- **Обязательно**: frontmatter `name`, `description`
- **Опционально**: `tools`, `disallowedTools`, `permissionMode`, `skills`, `hooks`
- **Перезагрузка**: перезапустите Claude Code или выполните `/agents`

Подробности о Claude Code subagent см. в `creating-subagents.md`.

---

## Связанное

- `adding-agent-basics.md` — базовое создание агента
- `testing-agent.md` — руководство по тестированию
- `debugging.md` — диагностика проблем
- `creating-subagents.md` — Claude Code subagents
