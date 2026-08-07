<!-- Context: development/core | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Концепция: Mastra Core

**Назначение**: Центральный слой оркестрации AI-агентов, workflows и tools в этом проекте.

**Обновлено**: 2026-01-09

---

## Основная идея
Mastra — центральный узел, который связывает agents, tools, workflows и наблюдаемость. Он даёт единый интерфейс для выполнения сложных AI-задач со встроенным хранением состояния и логированием.

## Ключевые пункты
- **Централизованная конфигурация**: все компоненты регистрируются в `src/mastra/index.ts`.
- **Хранение**: использует `LibSQLStore` (SQLite) для хранения traces, spans и состояний workflow.
- **Наблюдаемость**: встроенные tracing и logging (Pino) для каждого выполнения.
- **Модульный дизайн**: agents, tools и workflows определяются отдельно и собираются в основном экземпляре.

## Быстрый пример
```typescript
import { Mastra } from '@mastra/core/mastra';
import { agents, tools, workflows } from './components';

export const mastra = new Mastra({
  agents,
  tools,
  workflows,
  storage: new LibSQLStore({ url: 'file:./mastra.db' }),
});
```

**Источник**: `src/mastra/index.ts`
**Связано**:
- concepts/workflows.md
- concepts/agents-tools.md
- lookup/mastra-config.md
