<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Тестирование subagents — пошаговое руководство

**Цель**: как тестировать subagents в standalone-режиме

**Последнее обновление**: 2026-01-09

---

## ⚠️ КРИТИЧНО: добавление нового subagent во framework

**Перед тестированием** нужно обновить ТРИ места в framework-коде:

### 1. `evals/framework/src/sdk/run-sdk-tests.ts` (~line 336)
Добавьте в `subagentParentMap`:
```typescript
'contextscout': 'openagent',  // Maps subagent → parent
```

### 2. `evals/framework/src/sdk/run-sdk-tests.ts` (~line 414)
Добавьте в `subagentPathMap`:
```typescript
'contextscout': 'ContextScout',  // Maps name → path
```

### 3. `evals/framework/src/sdk/test-runner.ts` (~line 238)
Добавьте в `agentMap`:
```typescript
'contextscout': 'ContextScout.md',  // Maps name → file
```

**Если отсутствует в ЛЮБОЙ map**: тесты упадут с "No test files found" или "Unknown subagent"

---

## Быстрый старт

```bash
# Test subagent directly (standalone mode)
cd evals/framework
npm run eval:sdk -- --subagent=contextscout --pattern="01-test.yaml"

# Test via delegation (integration mode)
npm run eval:sdk -- --subagent=contextscout --delegate --pattern="01-test.yaml"

# Debug mode
npm run eval:sdk -- --subagent=contextscout --pattern="01-test.yaml" --debug
```

---

## Шаг 1: проверьте файл агента

**Проверьте, что агент существует и имеет правильную структуру**:

```bash
# Check agent file
cat .opencode/agent/subagents/core/contextscout.md | head -20

# Verify frontmatter
grep -A 5 "^id:" .opencode/agent/subagents/core/contextscout.md
```

**Ожидается**:
```yaml
id: contextscout
name: ContextScout
category: subagents/core
type: subagent
mode: subagent  # ← Will be forced to 'primary' in standalone tests
```

---

## Шаг 2: проверьте конфигурацию тестов

**Проверьте, что конфиг теста указывает на правильного агента**:

```bash
cat evals/agents/ContextScout/config/config.yaml
```

**Ожидается**:
```yaml
agent: ContextScout  # ← Full path
model: anthropic/claude-sonnet-4-5
timeout: 60000
```

---

## Шаг 3: запустите standalone-тест

**Используйте флаг `--subagent`** (не `--agent`):

```bash
cd evals/framework
npm run eval:sdk -- --subagent=ContextScout --pattern="standalone/01-simple-discovery.yaml"
```

**На что смотреть**:
```
⚡ Standalone Test Mode
   Subagent: contextscout
   Mode: Forced to 'primary' for direct testing
   
Testing agent: contextscout  # ← Should show subagent name
```

---

## Шаг 4: проверьте, что агент загрузился корректно

**Проверьте результаты тестов**:

```bash
# View latest results
cat evals/results/latest.json | jq '.meta'
```

**Ожидается**:
```json
{
  "agent": "ContextScout",  // ← Correct agent
  "model": "opencode/grok-code-fast",
  "timestamp": "2026-01-07T..."
}
```

**Тревожные признаки**:
- `"agent": "core/openagent"` ← неверно! Запущен OpenAgent
- `"agent": "contextscout"` ← отсутствует category prefix

---

## Шаг 5: проверьте использование инструментов

**Убедитесь, что subagent использовал tools**:

```bash
# Check tool calls in output
cat evals/results/latest.json | jq '.tests[0]' | grep -A 5 "Tool Calls"
```

**Ожидается** (для ContextScout):
```
Tool Calls: 1
Tools Used: glob

Tool Call Details:
  1. glob: {"pattern":"*.md","path":".opencode/context/core"}
```

**Тревожные признаки**:
- `Tool Calls: 0` ← агент не использовал tools
- `Tools Used: task` ← parent agent делегирует (неверный mode)

---

## Шаг 6: проанализируйте падения

**Если тест падает, проверьте нарушения**:

```bash
cat evals/results/latest.json | jq '.tests[0].violations'
```

**Частые проблемы**:

### Проблема 1: нет tool calls
```json
{
  "type": "missing-required-tool",
  "message": "Required tool 'glob' was not used"
}
```

**Причина**: промпт агента не делает акцент на tool usage  
**Исправление**: добавьте секцию critical rules с акцентом на tools (см. `examples/subagent-prompt-structure.md`)

### Проблема 2: запущен неверный агент
```
Agent: OpenAgent
```

**Причина**: использован `--agent` вместо `--subagent`  
**Исправление**: используйте `--subagent=ContextScout`

### Проблема 3: Tool Permission Denied
```json
{
  "type": "missing-approval",
  "message": "Execution tool 'bash' called without requesting approval"
}
```

**Причина**: агент попытался использовать ограниченный tool  
**Исправление**: см. `errors/tool-permission-errors.md`

---

## Шаг 7: проверьте результаты

**Убедитесь, что тест прошел**:

```bash
# View summary
cat evals/results/latest.json | jq '.summary'
```

**Ожидается**:
```json
{
  "total": 1,
  "passed": 1,  // ← Should be 1
  "failed": 0,
  "pass_rate": 1.0
}
```

---

## Организация test-файлов

**Лучшая практика**: организуйте по mode

```
evals/agents/ContextScout/tests/
├── standalone/           # Unit tests (--subagent flag)
│   ├── 01-simple-discovery.yaml
│   ├── 02-search-test.yaml
│   └── 03-extraction-test.yaml
└── delegation/           # Integration tests (--agent flag)
    ├── 01-openagent-delegates.yaml
    └── 02-context-loading.yaml
```

---

## Написание хороших test-промптов

**Явно указывайте использование инструментов**:

❌ **Расплывчато** (может не сработать):
```yaml
prompts:
  - text: |
      List all markdown files in .opencode/context/core/
```

✅ **Явно** (работает):
```yaml
prompts:
  - text: |
      Use the glob tool to find all markdown files in .opencode/context/core/
      
      You MUST use the glob tool like this:
      glob(pattern="*.md", path=".opencode/context/core")
      
      Then list the files you found.
```

---

## Быстрая диагностика

| Симптом | Причина | Исправление |
|---------|-------|-----|
| Запускается OpenAgent | Использован флаг `--agent` | Используйте флаг `--subagent` |
| Tool calls: 0 | Prompt не делает акцент на tools | Добавьте секцию critical rules |
| Permission denied | Tool restricted во frontmatter | Проверьте `tools:` и `permissions:` |
| Test timeout | Агент завис/зациклился | Проверьте логику prompt, добавьте timeout |

---

## Связанное

- `concepts/subagent-testing-modes.md` — понять standalone и delegation
- `lookup/subagent-test-commands.md` — быстрый справочник команд
- `errors/tool-permission-errors.md` — частые permission issues
- `examples/subagent-prompt-structure.md` — оптимизированная структура prompt

**Справка**: `evals/framework/src/sdk/run-sdk-tests.ts`
