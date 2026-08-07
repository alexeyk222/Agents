<!-- Context: development/mastra-config | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Справочник: конфигурация Mastra

**Назначение**: Краткий справочник по расположению файлов Mastra и регистрации.

**Обновлено**: 2026-01-09

---

## Расположение файлов

| Компонент | Каталог | Файл регистрации |
|-----------|-----------|-------------------|
| **Экземпляр Mastra** | `src/mastra/` | `src/mastra/index.ts` |
| **Agents** | `src/mastra/agents/` | `src/mastra/index.ts` |
| **Tools** | `src/mastra/tools/` | `src/mastra/index.ts` |
| **Workflows** | `src/mastra/workflows/` | `src/mastra/index.ts` |
| **Scorers** | `src/mastra/scorers/` | `src/mastra/index.ts` |
| **Сервисы** | `src/services/` | `src/mastra/shared.ts` |

## Таблицы базы данных

| Имя таблицы | Описание |
|------------|-------------|
| `mastra_traces` | Трассировки выполнения workflow |
| `mastra_ai_spans` | Span-ы вызовов LLM и использование токенов |
| `mastra_scorers` | Результаты оценок и баллы |
| `mastra_workflow_state` | Текущее состояние запущенных workflows |

## Типовые команды

| Команда | Описание |
|---------|-------------|
| `npm run dev` | Запустить Mastra в режиме разработки |
| `npm run traces` | Посмотреть последние трассировки выполнения |
| `npm run test:workflow` | Запустить скрипт тестового workflow |

**Связано**:
- concepts/core.md
- concepts/workflows.md
