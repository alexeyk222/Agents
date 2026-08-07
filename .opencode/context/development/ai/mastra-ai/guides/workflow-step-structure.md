<!-- Context: development/workflow-step-structure | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: структура шага workflow

**Назначение**: Стандартизированный паттерн для определения поддерживаемых и тестируемых шагов workflow.

**Обновлено**: 2026-01-09

---

## Основная идея
Шаги workflow должны быть самодостаточными единицами, инкапсулирующими схемы ввода/вывода и логику выполнения. Для сложных workflows шаги следует выносить в отдельный каталог `steps/` и группировать по фазам.

## Ключевые пункты
- **Структура каталогов**: группируйте шаги по фазам (например, `steps/phase1-load.ts`, `steps/phase2-process.ts`).
- **Централизация схем**: определяйте общие схемы, например `workflowStateSchema`, в файле `schemas.ts` внутри каталога шагов.
- **Явное состояние**: используйте `stateSchema` в `createStep`, чтобы обеспечить типобезопасность при доступе к глобальному состоянию workflow.
- **Делегирование Tools**: шаги должны в основном быть оркестраторами и делегировать тяжёлую работу Tools.
- **Логирование**: добавляйте понятные `console.log`-сообщения в начале и конце каждого шага для упрощения отладки.

## Быстрый пример
```typescript
// src/mastra/workflows/v3/steps/phase1.ts
export const myStep = createStep({
  id: 'my-step-id',
  inputSchema: z.object({ ... }),
  outputSchema: z.object({ ... }),
  stateSchema: workflowStateSchema,
  execute: async ({ inputData, state, mastra }) => {
    console.log('🚀 Starting myStep...');
    const result = await myTool.execute(inputData, { mastra });
    return result;
  },
});
```

**Источник**: `src/mastra/workflows/v3/steps/`
**Связано**:
- concepts/workflows.md
- guides/modular-building.md
