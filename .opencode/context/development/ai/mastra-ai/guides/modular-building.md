<!-- Context: development/modular-building | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: модульная сборка Mastra

**Назначение**: Лучшие практики структурирования крупной реализации Mastra.

**Обновлено**: 2026-01-09

---

## Основная идея
Модульная сборка помогает сохранять компоненты тестируемыми, переиспользуемыми и удобными для навигации по мере роста проекта. Это достигается разделением логики по специализированным каталогам и использованием центрального реестра.

## Ключевые пункты
- **Разделение компонентов**: держите `agents`, `tools`, `workflows` и `scorers` в отдельных каталогах верхнего уровня внутри `src/mastra/`.
- **Общие сервисы**: используйте файл `shared.ts` для создания сервисов (БД, репозитории), чтобы избежать циклических зависимостей между workflows и основным экземпляром Mastra.
- **Центральный реестр**: регистрируйте все компоненты в `src/mastra/index.ts`. Это единый источник истины для экземпляра Mastra.
- **Шаги по фичам**: группируйте связанные шаги workflow в подкаталоги (например, `src/mastra/workflows/v3/steps/`), чтобы файлы workflow оставались чистыми.

## Быстрый пример
```typescript
// src/mastra/shared.ts
export const services = createServices();

// src/mastra/index.ts
import { services } from './shared';
export const mastra = new Mastra({
  workflows: { myWorkflow },
  agents: { myAgent },
  // ...
});
```

**Источник**: `src/mastra/index.ts`, `src/mastra/shared.ts`
**Связано**:
- concepts/core.md
- guides/workflow-step-structure.md
