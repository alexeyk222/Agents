<!-- Context: development/workflows | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Концепция: Mastra Workflows

**Назначение**: Линейные и параллельные цепочки выполнения для сложных AI-задач.

**Обновлено**: 2026-01-09

---

## Основная идея
Workflows в Mastra — это ориентированные графы шагов, которые обрабатывают данные последовательно или параллельно. Они дают структурированный способ выполнять многоэтапные LLM-операции со встроенным управлением состоянием и поддержкой human-in-the-loop (HITL).

## Ключевые пункты
- **Определение шага**: создаётся через `createStep`; требует `inputSchema`, `outputSchema` и функцию `execute`.
- **Цепочки**: шаги связываются через `.then()` для последовательного выполнения и `.parallel()` для параллельного.
- **Поддержка HITL**: шаги могут `suspend` выполнение, чтобы дождаться ввода человека, и `resume`, когда данные предоставлены.
- **Доступ к состоянию**: каждый шаг имеет доступ к глобальному `state` workflow и `inputData` из предыдущего шага.

## Быстрый пример
```typescript
const workflow = createWorkflow({ id: 'my-workflow', inputSchema, outputSchema })
  .then(step1)
  .parallel([step2a, step2b])
  .then(mergeStep)
  .commit();

const { runId, start } = workflow.createRun();
const result = await start({ inputData: { ... } });
```

**Источник**: `src/mastra/workflows/`
**Связано**:
- concepts/core.md
- examples/workflow-example.md
