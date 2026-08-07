<!-- Context: openagents-repo/tools | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Создание пользовательских инструментов

Плагины могут добавлять пользовательские инструменты, которые агенты OpenCode вызывают автономно.

## Определение инструмента

Пользовательские инструменты используют Zod для схемы и хелпер `tool` из `@opencode-ai/plugin`.

```typescript
import { z } from 'zod';
import { tool } from '@opencode-ai/plugin';

export const MyCustomTool = tool(
  z.object({
    query: z.string().describe('Search query'),
    limit: z.number().default(10).describe('Results limit')
  }),
  async (args, context) => {
    const { query, limit } = args;
    // Implementation logic
    return { success: true, data: [] };
  }
).describe('Search your database');
```

## Инструменты на основе shell

Можно использовать shell API Bun (`$`), чтобы запускать команды на любом языке.

```typescript
export const PythonCalculatorTool = tool(
  z.object({ expression: z.string() }),
  async (args, context) => {
    const { $ } = context;
    const result = await $`python3 -c 'print(eval("${args.expression}"))'`;
    return { result: result.stdout };
  }
).describe('Calculate mathematical expressions');
```

## Интеграция

Чтобы зарегистрировать инструменты в плагине:

```typescript
export const MyPlugin = async (context) => {
  return {
    tool: [MyCustomTool, PythonCalculatorTool]
  };
};
```
