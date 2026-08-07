<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

---
description: "Руководство по тестированию subagents и обработке approval gates"
type: "context"
category: "openagents-repo"
tags: [testing, subagents, approval-gates]
---

# Тестирование subagents: approval gates

**Контекст**: openagents-repo/guides | **Приоритет**: HIGH | **Обновлено**: 2026-01-09

---

## Критическое правило: subagents не нужны approval gates

**ВАЖНО**: при написании тестов для subagents НЕ добавляйте `expectedViolations` для `approval-gate`.

### Почему?

Subagents получают задачи через делегирование от parent agents (OpenAgent, OpenCoder и т. д.). Parent agent уже запросил и получил approval перед делегированием. Поэтому:

- ✅ Subagents могут напрямую выполнять tools без запроса approval
- ✅ Subagents наследуют approval от parent
- ❌ Subagents НЕ нужно тестировать на violations approval gate

### Конфигурация тестов для subagents

**Правильно** (без ожиданий approval gate):
```yaml
category: developer
agent: ContextScout

approvalStrategy:
  type: auto-approve

behavior:
  mustUseTools:
    - read
    - glob
  forbiddenTools:
    - write
    - edit
  minToolCalls: 2
  maxToolCalls: 15

# NO expectedViolations for approval-gate!
```

**Неправильно** (так не делайте):
```yaml
expectedViolations:
  - rule: approval-gate        # ❌ WRONG for subagents
    shouldViolate: false
    severity: error
```

---

## Когда тестировать approval gates

**Тестируйте approval gates для**:
- ✅ Primary agents (OpenAgent, OpenCoder, System Builder)
- ✅ Category agents (frontend-specialist, data-analyst и т. д.)

**Не тестируйте approval gates для**:
- ❌ Subagents (contextscout, tester, reviewer, coder-agent и т. д.)
- ❌ Любого агента с `mode: subagent` во frontmatter

---

## Стратегия approval для subagents

Всегда используйте `auto-approve` для тестов subagent:

```yaml
approvalStrategy:
  type: auto-approve
```

Это имитирует ситуацию, где parent agent уже одобрил делегирование.

---

## Пример: тест ContextScout

```yaml
id: contextscout-code-standards
name: "ContextScout: Code Standards Discovery"
description: Tests that ContextScout discovers code-related context files

category: developer
agent: ContextScout

prompts:
  - text: |
      Search for context files related to: coding standards
      
      Task type: code
      
      Return:
      - Exact file paths
      - Priority order
      - Key findings

approvalStrategy:
  type: auto-approve

behavior:
  mustUseTools:
    - read
    - glob
  forbiddenTools:
    - write
    - edit
  minToolCalls: 2
  maxToolCalls: 15

timeout: 60000

tags:
  - contextscout
  - discovery
  - subagent
```

---

## Связанные файлы

- **Тестирование subagents**: `.opencode/context/openagents-repo/guides/testing-subagents.md`
- **Вызов subagent**: `.opencode/context/openagents-repo/guides/subagent-invocation.md`
- **Концепции агентов**: `.opencode/context/openagents-repo/core-concepts/agents.md`

---

**Последнее обновление**: 2026-01-09  
**Версия**: 1.0.0
