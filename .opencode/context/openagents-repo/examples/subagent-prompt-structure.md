<!-- Context: openagents-repo/examples | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Структура промпта субагента (оптимизированная)

**Назначение**: шаблон хорошо структурированных промптов субагентов с акцентом на использование инструментов

**Последнее обновление**: 2026-01-07

---

## Ключевой принцип

**Позиционная чувствительность**: критические инструкции в первых 15% промпта улучшают соблюдение правил.

Для субагентов самая важная инструкция: **какие инструменты использовать**.

---

## Оптимизированная структура

```xml
---
# Frontmatter (lines 1-50)
id: subagent-name
name: Subagent Name
category: subagents/core
type: subagent
mode: subagent
tools:
  read: true
  grep: true
  glob: true
  list: true
  bash: false
  edit: false
  write: false
permissions:
  bash: "*": "deny"
  edit: "**/*": "deny"
  write: "**/*": "deny"
---

# Agent Name

> **Mission**: One-sentence mission statement

Brief description (1-2 sentences).

---

<!-- CRITICAL: This section must be in first 15% -->
<critical_rules priority="absolute" enforcement="strict">
  <rule id="tool_usage">
    ONLY use: glob, read, grep, list
    NEVER use: bash, write, edit, task
    You're read-only—no modifications allowed
  </rule>
  <rule id="always_use_tools">
    ALWAYS use tools to discover/verify
    NEVER assume or fabricate information
  </rule>
  <rule id="output_format">
    ALWAYS include: exact paths, specific details, evidence
  </rule>
</critical_rules>

---

<context>
  <system>What system this agent operates in</system>
  <domain>What domain knowledge it needs</domain>
  <task>What it does</task>
  <constraints>What limits it has</constraints>
</context>

<role>One-sentence role description</role>

<task>One-sentence task description</task>

---

<execution_priority>
  <tier level="1" desc="Critical Operations">
    - @tool_usage: Use ONLY allowed tools
    - @always_use_tools: Verify everything
    - @output_format: Precise results
  </tier>
  <tier level="2" desc="Core Workflow">
    - Main workflow steps
  </tier>
  <tier level="3" desc="Quality">
    - Quality checks
    - Validation
  </tier>
  <conflict_resolution>
    Tier 1 always overrides Tier 2/3
  </conflict_resolution>
</execution_priority>

---

## Рабочий процесс

### Stage 1: Discovery
**Action**: Use tools to discover information
**Process**: 1. Use glob/list, 2. Use read, 3. Use grep
**Output**: Discovered items

### Stage 2: Analysis
**Action**: Analyze discovered information
**Process**: Extract key details
**Output**: Analyzed results

### Stage 3: Present
**Action**: Return structured response
**Process**: Format according to @output_format
**Output**: Complete response

---

## What NOT to Do

- ❌ **NEVER use bash/write/edit/task tools** (@tool_usage)
- ❌ Don't assume information—verify with tools
- ❌ Don't fabricate paths or details
- ❌ Don't skip required output fields

---

## Remember

**Your Tools**: glob (discover) | read (extract) | grep (search) | list (structure)

**Your Constraints**: Read-only, verify everything, precise output

**Your Value**: Accurate, verified information using tools
```

---

## Примененные ключевые оптимизации

### 1. Critical Rules в начале (строки 50-80)

**До** (спрятано на строке 596):
```markdown
## Important Guidelines
...
(400 lines later)
### Tool Usage
- Use glob, read, grep, list
```

**После** (на строке 50):
```xml
<critical_rules priority="absolute" enforcement="strict">
  <rule id="tool_usage">
    ONLY use: glob, read, grep, list
    NEVER use: bash, write, edit, task
  </rule>
</critical_rules>
```

**Эффект**: длина промпта уменьшена на 47,5%, использование инструментов выделено в начале.

---

### 2. Приоритеты выполнения (3-уровневая система)

```xml
<execution_priority>
  <tier level="1" desc="Critical">
    - Tool usage rules
    - Verification requirements
  </tier>
  <tier level="2" desc="Core">
    - Main workflow
  </tier>
  <tier level="3" desc="Quality">
    - Nice-to-haves
  </tier>
  <conflict_resolution>Tier 1 always overrides</conflict_resolution>
</execution_priority>
```

**Почему**: разрешает конфликты и явно задает приоритеты.

---

### 3. Уплощенная вложенность (≤4 уровня)

**До** (6-7 уровней):
```xml
<instructions>
  <workflow>
    <stage>
      <process>
        <step>
          <action>
            <detail>...</detail>
          </action>
        </step>
      </process>
    </stage>
  </workflow>
</instructions>
```

**После** (3-4 уровня):
```xml
<workflow>
  <stage id="1" name="Discovery">
    <action>Use tools</action>
    <process>1. glob, 2. read, 3. grep</process>
  </stage>
</workflow>
```

**Почему**: повышает ясность и снижает когнитивную нагрузку.

---

### 4. Явная секция «Чего НЕ делать»

```markdown
## What NOT to Do

- ❌ **NEVER use bash/write/edit/task tools**
- ❌ Don't assume—verify with tools
- ❌ Don't fabricate information
```

**Почему**: негативные примеры предотвращают частые ошибки.

---

## Целевые размеры файла

| Секция | Целевые строки | Назначение |
|---------|--------------|---------|
| Frontmatter | 30-50 | Метаданные агента |
| Critical rules | 20-30 | Использование инструментов, ключевые правила |
| Context/Role/Task | 20-30 | Идентичность агента |
| Приоритеты выполнения | 20-30 | Система приоритетов |
| Процесс | 80-120 | Основные инструкции |
| Рекомендации | 40-60 | Лучшие практики |
| **Итого** | **<400 строк** | Соответствие MVI |

---

## Чек-лист валидации

Перед применением оптимизированного промпта:

- [ ] Critical rules в первых 15% (строки 50-80)?
- [ ] Использование инструментов указано явно?
- [ ] Вложенность ≤4 уровней?
- [ ] Приоритеты выполнения определены?
- [ ] Секция «Чего НЕ делать» включена?
- [ ] Всего строк <400?
- [ ] Семантический смысл сохранен?

---

## Реальный пример

**Оптимизация ContextScout**:
- **До**: 750 строк, critical rules на строке 596
- **После**: 394 строки (сокращение на 47,5%), critical rules на строке 50
- **Результат**: тест прошел (раньше падал с 0 tool calls)

**Файлы**:
- Оптимизированный: `.opencode/agent/subagents/core/contextscout.md`
- Backup: (пример: `.opencode/agent/ContextScout-original-backup.md`)

---

## Связанные материалы

- `concepts/subagent-testing-modes.md` - как тестировать оптимизированные промпты
- `guides/testing-subagents.md` - как проверить, что инструменты используются
- `errors/tool-permission-errors.md` - исправление проблем с инструментами

**Справка**: `.opencode/command/prompt-engineering/prompt-optimizer.md` (принципы оптимизации)
