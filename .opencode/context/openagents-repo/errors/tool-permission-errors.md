<!-- Context: openagents-repo/errors | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Ошибки прав инструментов

**Назначение**: диагностировать и исправлять проблемы с правами инструментов у агентов

**Последнее обновление**: 2026-01-07

---

## Ошибка: отказано в доступе к инструменту

### Симптом

```json
{
  "type": "missing-approval",
  "severity": "error",
  "message": "Execution tool 'bash' called without requesting approval"
}
```

Или агент пытается использовать инструмент, но тихо блокируется (0 tool calls).

---

### Причина

У агента инструмент **отключен** или **запрещен** во frontmatter:

```yaml
# In agent frontmatter
tools:
  bash: false    # ← Tool disabled

permission:
  bash:
    "*": "deny"  # ← Explicitly denied
```

**Как это работает**:
- `bash: false` означает, что у агента нет доступа к инструменту bash
- Фреймворк принудительно применяет это: агент не может использовать bash, даже если промпт просит
- Это НЕ проблема approval, а ограничение прав

---

### Решение

**Вариант 1: явно подчеркнуть ограничения инструментов в промпте** (рекомендуется)

Добавьте секцию critical rules в начало промпта агента:

```xml
<critical_rules priority="absolute" enforcement="strict">
  <rule id="tool_usage">
    ONLY use: glob, read, grep, list
    NEVER use: bash, write, edit, task
    You're read-only—no modifications allowed
  </rule>
  <rule id="always_use_tools">
    ALWAYS use tools to discover files
    NEVER assume or fabricate file paths
  </rule>
</critical_rules>
```

**Почему это работает**: ограничения инструментов становятся предельно явными в первых 15% промпта.

**Вариант 2: включить инструмент** (если он нужен агенту)

```yaml
tools:
  bash: true  # ← Enable if agent legitimately needs bash
```

**Предупреждение**: включайте инструмент только если он действительно нужен. Read-only субагенты НЕ должны иметь bash/write/edit.

---

### Профилактика

**Для субагентов только для чтения**:

```yaml
# Correct configuration for read-only subagents
tools:
  read: true
  grep: true
  glob: true
  list: true
  bash: false    # ← No execution
  edit: false    # ← No modifications
  write: false   # ← No file creation
  task: false    # ← No delegation (subagents don't delegate)

permissions:
  bash:
    "*": "deny"
  edit:
    "**/*": "deny"
  write:
    "**/*": "deny"
```

**Для primary-агентов**:

```yaml
# Primary agents may need execution tools
tools:
  read: true
  grep: true
  glob: true
  list: true
  bash: true     # ← May need for operations
  edit: true     # ← May need for modifications
  write: true    # ← May need for file creation
  task: true     # ← May delegate to subagents
```

---

## Ошибка: нарушение approval gate у субагента

### Симптом

```json
{
  "type": "missing-approval",
  "message": "Execution tool 'bash' called without requesting approval"
}
```

В тесте **субагента**.

---

### Причина

**У субагентов НЕ должно быть approval gates**: им делегируют primary-агенты, которые уже получили approval.

Обычно причина в одном из двух:
1. Субагент пытается использовать ограниченный инструмент (bash/write/edit)
2. Тест ожидает approval-поведение (это неверно для субагентов)

---

### Решение

**Исправление 1: убрать использование инструмента**

Субагенты не должны использовать execution tools. Обновите промпт и подчеркните read-only режим.

**Исправление 2: обновить конфигурацию теста**

Тесты субагентов должны использовать `auto-approve`:

```yaml
approvalStrategy:
  type: auto-approve  # ← No approval gates for subagents
```

**Исправление 3: проверить права инструментов**

Убедитесь, что у субагента во frontmatter задано `bash: false`.

---

## Ошибка: инструмент недоступен

### Симптом

Агент пытается использовать инструмент, но фреймворк сообщает "tool not available".

---

### Причина

Инструмент не включен во frontmatter:

```yaml
tools:
  glob: false  # ← Tool disabled
```

---

### Решение

Включите инструмент:

```yaml
tools:
  glob: true  # ← Enable
```

---

## Чек-лист проверки

После исправления прав инструмента:

- [ ] Во frontmatter агента корректная конфигурация `tools:`?
- [ ] Промпт подчеркивает разрешенные инструменты в секции critical rules?
- [ ] Промпт предупреждает о запрещенных инструментах?
- [ ] Тест использует `auto-approve` для субагентов?
- [ ] Тест проверяет использование инструментов через `mustUseTools`?

---

## Матрица прав инструментов

| Тип агента | bash | write | edit | task | read | grep | glob | list |
|------------|------|-------|------|------|------|------|------|------|
| **Субагент только для чтения** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Primary-агент** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Оркестратор** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Связанные материалы

- `concepts/subagent-testing-modes.md` - понять тестирование субагентов
- `guides/testing-subagents.md` - как тестировать субагентов
- `examples/subagent-prompt-structure.md` - структура промпта с акцентом на инструменты

**Справка**: `.opencode/agent/subagents/core/contextscout.md` (конфигурация инструментов)
