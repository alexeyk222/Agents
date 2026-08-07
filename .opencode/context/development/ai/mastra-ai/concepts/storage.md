<!-- Context: development/storage | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Концепция: хранилище данных Mastra

**Назначение**: Слой хранения для cases, documents, assessments и наблюдаемости.

**Обновлено**: 2026-01-09

---

## Основная идея
Mastra использует подход с двумя хранилищами: локальную базу SQLite (через Drizzle ORM) для бизнес-сущностей и встроенный `LibSQLStore` для данных выполнения Mastra (traces, spans).

## Ключевые пункты
- **Бизнес-сущности**: управляются в `src/db/schema.ts`. Включают `cases`, `documents`, `assessments` и `outputs`.
- **Хранилище Mastra**: `LibSQLStore` обслуживает `mastra_traces`, `mastra_ai_spans` и `mastra_scorers`.
- **Расширения V3**: отдельные таблицы для `timeline_events`, `evidence_gaps`, `sub_claims` и `vulnerability_flags`.
- **Наблюдаемость**: `prompt_execution_traces` даёт детальное отслеживание стоимости и токенов для каждого AI-вызова.
- **Файловое хранение**: крупные blob-объекты (PDF, JSON-выводы) хранятся в `./tmp/`, а пути на них указаны в БД.

## Быстрый пример
```typescript
// Business Schema (Drizzle)
export const cases = sqliteTable('cases', {
  id: text('id').primaryKey(),
  status: text('status').default('new'),
});

// Mastra Store Config
storage: new LibSQLStore({
  url: process.env.MASTRA_DB_PATH || 'file:./mastra.db',
}),
```

**Источник**: `src/db/schema.ts`, `src/mastra/index.ts`
**Связано**:
- concepts/core.md
- lookup/mastra-config.md
