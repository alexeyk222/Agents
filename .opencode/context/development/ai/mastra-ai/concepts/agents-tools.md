<!-- Context: development/agents-tools | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Концепция: Mastra Agents & Tools

**Назначение**: Переиспользуемые единицы логики и сущности на базе LLM.

**Обновлено**: 2026-01-09

---

## Основная идея
Agents — специализированные конфигурации LLM, которые используют Tools для взаимодействия с внешними системами или выполнения конкретной логики. Tools — строительные блоки, предоставляющие функциональность agents и workflows.

## Ключевые пункты
- **Agents**: определяются через `name`, `instructions` и `model`. Им можно назначить набор `tools`.
- **Tools**: определяются через `id`, `inputSchema`, `outputSchema` и функцию `execute`.
- **Типобезопасность**: agents и tools используют Zod для валидации схем.
- **Автономное использование**: Tools можно выполнять независимо от agents, поэтому они хорошо переиспользуются.

## Быстрый пример
```typescript
// Tool
const myTool = createTool({
  id: 'my-tool',
  inputSchema: z.object({ query: z.string() }),
  execute: async ({ inputData }) => ({ result: `Processed ${inputData.query}` }),
});

// Agent
const myAgent = new Agent({
  name: 'My Agent',
  instructions: 'Use my-tool to process queries.',
  model: { provider: 'OPEN_AI', name: 'gpt-4o' },
  tools: { myTool },
});
```

**Источник**: `src/mastra/agents/`, `src/mastra/tools/`
**Связано**:
- concepts/core.md
- concepts/workflows.md
