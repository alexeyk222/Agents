<!-- Context: openagents-repo/events_skills | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# События OpenCode: реализация Skills Plugin

## Обзор

Этот документ объясняет, как OpenCode Skills Plugin использует хуки событий (`tool.execute.before` и `tool.execute.after`) для доставки навыков и улучшения вывода. Это практический пример системы событий из `events.md`.

---

## Используемые хуки событий

### tool.execute.before

**Тип события:** перехват выполнения инструмента

**Когда срабатывает:** до выполнения функции инструмента

**Назначение в Skills Plugin:** внедрить содержимое навыка в разговор

**Реализация:**
```typescript
const beforeHook = async (input: any, output: any) => {
  // Check if this is a skill tool
  if (input.tool.startsWith("skills_")) {
    // Look up skill from map
    const skill = skillMap.get(input.tool)
    if (skill) {
      // Inject skill content as silent prompt
      await ctx.client.session.prompt({
        path: { id: input.sessionID },
        body: {
          agent: input.agent,
          noReply: true,  // Don't trigger AI response
          parts: [
            {
              type: "text",
              text: `📚 Skill: ${skill.name}\nBase directory: ${skill.fullPath}\n\n${skill.content}`,
            },
          ],
        },
      })
    }
  }
}
```

**Зачем использовать этот хук?**
- Срабатывает до выполнения инструмента — идеально для внедрения контекста
- Имеет доступ к имени инструмента и session ID
- Может внедрять содержимое без запуска ответа AI
- Содержимое навыка сохраняется в истории разговора

**Входные параметры:**
- `input.tool` - имя инструмента (например, "skills_brand_guidelines")
- `input.sessionID` - текущий session ID
- `input.agent` - имя агента, вызвавшего инструмент
- `output.args` - аргументы инструмента

**Что можно делать:**
- ✅ Внедрять контекст (содержимое навыка)
- ✅ Валидировать входные данные
- ✅ Предобрабатывать аргументы
- ✅ Логировать вызовы инструментов
- ✅ Реализовывать проверки безопасности

**Что нельзя делать:**
- ❌ Изменять вывод инструмента (инструмент еще не запущен)
- ❌ Получать доступ к результатам инструмента

---

### tool.execute.after

**Тип события:** перехват выполнения инструмента

**Когда срабатывает:** после завершения функции инструмента

**Назначение в Skills Plugin:** улучшить вывод визуальной обратной связью

**Реализация:**
```typescript
const afterHook = async (input: any, output: any) => {
  // Check if this is a skill tool
  if (input.tool.startsWith("skills_")) {
    // Look up skill from map
    const skill = skillMap.get(input.tool)
    if (skill && output.output) {
      // Add emoji title for visual feedback
      output.title = `📚 ${skill.name}`
    }
  }
}
```

**Зачем использовать этот хук?**
- Срабатывает после выполнения инструмента — идеально для улучшения вывода
- Может изменять свойства вывода
- Может добавлять визуальную обратную связь (emoji-заголовки)
- Может реализовывать логирование/аналитику

**Входные параметры:**
- `input.tool` - имя инструмента (например, "skills_brand_guidelines")
- `input.sessionID` - текущий session ID
- `output.output` - результат/вывод инструмента
- `output.title` - заголовок вывода (можно изменить)

**Что можно делать:**
- ✅ Изменять вывод
- ✅ Добавлять заголовки/форматирование
- ✅ Логировать завершение
- ✅ Добавлять аналитику
- ✅ Преобразовывать результаты

**Что нельзя делать:**
- ❌ Изменять аргументы инструмента (уже выполнен)
- ❌ Предотвращать выполнение инструмента (уже произошло)

---

## Жизненный цикл событий в Skills Plugin

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT CALLS SKILL TOOL                       │
│                  (e.g., skills_brand_guidelines)                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              EVENT: tool.execute.before fires                   │
│                                                                 │
│  Hook Function: beforeHook(input, output)                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 1. Check: input.tool.startsWith("skills_")             │   │
│  │ 2. Lookup: skillMap.get(input.tool)                    │   │
│  │ 3. Inject: ctx.client.session.prompt({                 │   │
│  │      path: { id: input.sessionID },                    │   │
│  │      body: {                                            │   │
│  │        agent: input.agent,                             │   │
│  │        noReply: true,                                  │   │
│  │        parts: [{ type: "text", text: skill.content }]  │   │
│  │      }                                                  │   │
│  │    })                                                   │   │
│  │ 4. Result: Skill content added to conversation         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Effect: Skill content persists in conversation history        │
│  No AI response triggered (noReply: true)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    TOOL.EXECUTE() RUNS                          │
│                                                                 │
│  async execute(args, toolCtx) {                                │
│    return `Skill activated: ${skill.name}`                     │
│  }                                                              │
│                                                                 │
│  Effect: Minimal confirmation returned                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              EVENT: tool.execute.after fires                    │
│                                                                 │
│  Hook Function: afterHook(input, output)                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 1. Check: input.tool.startsWith("skills_")             │   │
│  │ 2. Lookup: skillMap.get(input.tool)                    │   │
│  │ 3. Verify: output.output exists                        │   │
│  │ 4. Enhance: output.title = `📚 ${skill.name}`          │   │
│  │ 5. Result: Output title modified with emoji            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Effect: Visual feedback added to output                       │
│  Could add logging/analytics here                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  RESULT RETURNED TO AGENT                       │
│                                                                 │
│  - Tool confirmation message                                    │
│  - Skill content in conversation history                        │
│  - Enhanced output with emoji title                             │
│  - Agent can now use skill content in reasoning                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Почему хуки вместо встроенной логики?

### Проблема: встроенная доставка (антипаттерн)

```typescript
// ❌ OLD: Skill delivery inside tool.execute()
async execute(args, toolCtx) {
  const sendSilentPrompt = (text: string) =>
    ctx.client.session.prompt({...})

  await sendSilentPrompt(`The "${skill.name}" skill is loading...`)
  await sendSilentPrompt(`Base directory: ${skill.fullPath}\n\n${skill.content}`)

  return `Launching skill: ${skill.name}`
}
```

**Проблемы:**
1. **Жесткая связность**: логика инструмента и доставка неразделимы
2. **Сложно тестировать**: нельзя тестировать инструмент без доставки
3. **Нарушение SOLID**: нарушен Single Responsibility Principle
4. **Нет переиспользования**: логику доставки нельзя вынести
5. **Сложный мониторинг**: доставку нельзя отслеживать отдельно

---

### Решение: доставка через хуки (лучшая практика)

```typescript
// ✅ NEW: Separated concerns using hooks

// Tool: Minimal and focused
async execute(args, toolCtx) {
  return `Skill activated: ${skill.name}`
}

// Hook: Handles delivery
const beforeHook = async (input, output) => {
  if (input.tool.startsWith("skills_")) {
    const skill = skillMap.get(input.tool)
    if (skill) {
      await ctx.client.session.prompt({...})
    }
  }
}
```

**Преимущества:**
1. ✅ **Слабая связность**: инструмент и доставка независимы
2. ✅ **Легко тестировать**: каждый компонент тестируется отдельно
3. ✅ **Соответствие SOLID**: Single Responsibility Principle
4. ✅ **Переиспользуемость**: хуки можно комбинировать с другими плагинами
5. ✅ **Мониторинг**: логирование/аналитику можно добавлять независимо

---

## Карта поиска навыков: оптимизация производительности

### Почему Map?

Карта поиска навыков дает доступ O(1) вместо поиска O(n):

```typescript
// ✅ EFFICIENT: O(1) lookup
const skillMap = new Map<string, Skill>()
for (const skill of skills) {
  skillMap.set(skill.toolName, skill)
}

const beforeHook = async (input, output) => {
  if (input.tool.startsWith("skills_")) {
    const skill = skillMap.get(input.tool)  // O(1) constant time
    if (skill) {
      // Use skill
    }
  }
}
```

### Влияние на производительность

| Количество навыков | Поиск в массиве (O(n)) | Поиск в Map (O(1)) | Ускорение |
|------------------|-------------------|------------------|---------|
| 10 | 10 сравнений | 1 поиск | 10x |
| 100 | 100 сравнений | 1 поиск | 100x |
| 1000 | 1000 сравнений | 1 поиск | 1000x |

**Вывод:** поиск в Map важен для масштабируемости

---

## Интеграция с системой событий OpenCode

### Сопоставление событий

| Событие OpenCode | Хук Skills Plugin | Назначение |
|---|---|---|
| `tool.execute.before` | `beforeHook` | внедрение содержимого навыка |
| `tool.execute.after` | `afterHook` | улучшение вывода |

### Возвращаемый объект плагина

```typescript
return {
  // Custom tools
  tool: tools,

  // Hook: Runs before tool execution
  "tool.execute.before": beforeHook,

  // Hook: Runs after tool execution
  "tool.execute.after": afterHook,
}
```

**Главное:**
- Хуки применяются ко ВСЕМ инструментам (фильтруйте через `if`)
- Несколько плагинов могут регистрировать хуки без конфликтов
- Хуки выполняются в порядке регистрации
- Хуки могут быть async

---

## Сравнение с другими хуками событий

### Доступные хуки выполнения инструментов

| Хук | Когда | Сценарий |
|------|------|----------|
| `tool.execute.before` | До запуска инструмента | Валидация входных данных, внедрение контекста, предобработка |
| `tool.execute.after` | После завершения инструмента | Форматирование вывода, логирование, аналитика |

### Другие хуки событий (не используются в Skills Plugin)

| Хук | Когда | Сценарий |
|------|------|----------|
| `session.created` | Сессия начинается | Приветственные сообщения, инициализация |
| `message.updated` | Сообщение меняется | Мониторинг, логирование |
| `session.idle` | Сессия завершается | Очистка, фоновые задачи |
| `session.error` | Возникает ошибка | Обработка ошибок, логирование |

---

## Практический пример: поток доставки навыка

### Шаг 1: агент вызывает инструмент навыка

```
Agent: "Use the brand-guidelines skill"
↓
OpenCode: Calls skills_brand_guidelines tool
```

### Шаг 2: срабатывает before hook

```typescript
const beforeHook = async (input, output) => {
  // input.tool = "skills_brand_guidelines"
  // input.sessionID = "ses_abc123"
  // input.agent = "my-helper"

  if (input.tool.startsWith("skills_")) {
    const skill = skillMap.get("skills_brand_guidelines")
    // skill = {
    //   name: "brand-guidelines",
    //   description: "Brand guidelines for the project",
    //   content: "# Brand Guidelines\n\n...",
    //   fullPath: "/path/to/skill"
    // }

    await ctx.client.session.prompt({
      path: { id: "ses_abc123" },
      body: {
        agent: "my-helper",
        noReply: true,
        parts: [
          {
            type: "text",
            text: "📚 Skill: brand-guidelines\nBase directory: /path/to/skill\n\n# Brand Guidelines\n\n..."
          }
        ]
      }
    })
  }
}
```

**Результат:** содержимое навыка добавлено в разговор, ответа AI нет

### Шаг 3: инструмент выполняется

```typescript
async execute(args, toolCtx) {
  // Minimal logic
  return `Skill activated: brand-guidelines`
}
```

**Результат:** возвращается простое подтверждение

### Шаг 4: срабатывает after hook

```typescript
const afterHook = async (input, output) => {
  // input.tool = "skills_brand_guidelines"
  // output.output = "Skill activated: brand-guidelines"

  if (input.tool.startsWith("skills_")) {
    const skill = skillMap.get("skills_brand_guidelines")
    if (skill && output.output) {
      output.title = `📚 brand-guidelines`
    }
  }
}
```

**Результат:** заголовок вывода улучшен emoji

### Шаг 5: агент получает результат

```
Conversation History:
├─ User: "Use the brand-guidelines skill"
├─ Tool Call: skills_brand_guidelines
├─ Silent Message: "📚 Skill: brand-guidelines\n..."
├─ Tool Result: "Skill activated: brand-guidelines"
│  (with title: "📚 brand-guidelines")
└─ Agent: "I now have the brand guidelines. I can help with..."
```

---

## Тестирование хуков

### Тестирование before hook

```typescript
describe("beforeHook", () => {
  it("should inject skill content for skill tools", async () => {
    const input = {
      tool: "skills_brand_guidelines",
      sessionID: "ses_test",
      agent: "test-agent"
    }
    const output = { args: {} }

    const mockPrompt = jest.fn()
    ctx.client.session.prompt = mockPrompt

    await beforeHook(input, output)

    expect(mockPrompt).toHaveBeenCalledWith(
      expect.objectContaining({
        path: { id: "ses_test" },
        body: expect.objectContaining({
          agent: "test-agent",
          noReply: true,
          parts: expect.arrayContaining([
            expect.objectContaining({
              type: "text",
              text: expect.stringContaining("brand-guidelines")
            })
          ])
        })
      })
    )
  })

  it("should skip non-skill tools", async () => {
    const input = { tool: "read_file", sessionID: "ses_test" }
    const output = { args: {} }

    const mockPrompt = jest.fn()
    ctx.client.session.prompt = mockPrompt

    await beforeHook(input, output)

    expect(mockPrompt).not.toHaveBeenCalled()
  })
})
```

### Тестирование after hook

```typescript
describe("afterHook", () => {
  it("should add emoji title for skill tools", async () => {
    const input = { tool: "skills_brand_guidelines" }
    const output = { output: "Skill activated" }

    await afterHook(input, output)

    expect(output.title).toBe("📚 brand-guidelines")
  })

  it("should skip non-skill tools", async () => {
    const input = { tool: "read_file" }
    const output = { output: "File content" }

    await afterHook(input, output)

    expect(output.title).toBeUndefined()
  })

  it("should skip if output is missing", async () => {
    const input = { tool: "skills_brand_guidelines" }
    const output = { output: null }

    await afterHook(input, output)

    expect(output.title).toBeUndefined()
  })
})
```

---

## Частые паттерны

### Паттерн 1: хуки для конкретных инструментов

```typescript
const beforeHook = async (input, output) => {
  switch (input.tool) {
    case "skills_brand_guidelines":
      // Handle brand guidelines
      break
    case "skills_api_reference":
      // Handle API reference
      break
    default:
      // Skip non-skill tools
  }
}
```

### Паттерн 2: условная обработка

```typescript
const beforeHook = async (input, output) => {
  if (input.tool.startsWith("skills_")) {
    const skill = skillMap.get(input.tool)
    if (skill && skill.allowedTools?.includes(input.agent)) {
      // Process only if allowed
    }
  }
}
```

### Паттерн 3: логирование и мониторинг

```typescript
const beforeHook = async (input, output) => {
  if (input.tool.startsWith("skills_")) {
    console.log(`[BEFORE] Skill tool called: ${input.tool}`)
    console.log(`[BEFORE] Session: ${input.sessionID}`)
  }
}

const afterHook = async (input, output) => {
  if (input.tool.startsWith("skills_")) {
    console.log(`[AFTER] Skill tool completed: ${input.tool}`)
    console.log(`[AFTER] Output length: ${output.output?.length || 0}`)
  }
}
```

### Паттерн 4: обработка ошибок

```typescript
const beforeHook = async (input, output) => {
  try {
    if (input.tool.startsWith("skills_")) {
      const skill = skillMap.get(input.tool)
      if (!skill) {
        throw new Error(`Skill not found: ${input.tool}`)
      }
      // Process skill
    }
  } catch (error) {
    console.error(`Hook error:`, error)
    // Don't rethrow - let tool execute anyway
  }
}
```

---

## Главное

1. **Хуки — это middleware**: они перехватывают выполнение инструмента в заданных точках
2. **Хук before**: для предобработки, валидации, внедрения контекста
3. **Хук after**: для улучшения вывода, логирования, аналитики
4. **Карты поиска**: дают доступ O(1) вместо поиска O(n)
5. **Разделение ответственности**: инструменты делают одно, хуки — другое
6. **Композиция**: несколько плагинов могут регистрировать хуки без конфликтов
7. **Тестируемость**: каждый компонент можно тестировать независимо
8. **Поддерживаемость**: изменения изолированы в конкретных хуках

---

## Ссылки

- **События OpenCode**: `context/capabilities/events.md`
- **Определение инструмента**: `context/capabilities/tools.md`
- **Лучшие практики**: `context/reference/best-practices.md`
- **Пример Skills Plugin**: `skills-plugin/example.ts`
- **Жизненный цикл хуков**: `skills-plugin/hook-lifecycle-and-patterns.md`
- **Паттерн реализации**: `skills-plugin/implementation-pattern.md`
