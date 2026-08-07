<!-- Context: core/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по управлению задачами

**Назначение**: система декомпозиции и отслеживания задач на основе JSON

**Последнее обновление**: 2026-02-14

---

## Структура

```
core/task-management/
├── navigation.md
├── standards/
│   ├── task-schema.md           # Base JSON schema (v1.0)
│   └── enhanced-task-schema.md  # Extended schema (v2.0) - line precision, domain modeling, contracts
├── guides/
│   ├── splitting-tasks.md       # Task decomposition
│   └── managing-tasks.md        # Workflow guide
└── lookup/
    └── task-commands.md         # CLI script reference
```

---

## Быстрые маршруты

| Задача | Путь | Приоритет |
|------|------|----------|
| **Понять базовую схему** | `standards/task-schema.md` | ⭐⭐⭐⭐⭐ |
| **Использовать расширенные функции** | `standards/enhanced-task-schema.md` | ⭐⭐⭐⭐ |
| **Разбить фичу** | `guides/splitting-tasks.md` | ⭐⭐⭐⭐⭐ |
| **Управлять жизненным циклом задачи** | `guides/managing-tasks.md` | ⭐⭐⭐⭐ |
| **Использовать CLI-команды** | `lookup/task-commands.md` | ⭐⭐⭐⭐ |

---

## Стратегия загрузки

### Для создания базовых задач:
1. Загрузить `standards/task-schema.md` (понять базовую структуру)
2. Загрузить `guides/splitting-tasks.md` (подход к декомпозиции)
3. Свериться с `lookup/task-commands.md` (валидация после создания)

### Для multi-stage orchestration:
1. Загрузить `standards/enhanced-task-schema.md` (расширенные возможности)
2. Загрузить `standards/task-schema.md` (справка по базовой структуре)
3. Загрузить `guides/splitting-tasks.md` (подход к декомпозиции)
4. Свериться с planning agents: ArchitectureAnalyzer, StoryMapper, PrioritizationEngine, ContractManager, ADRManager

### Для управления задачами:
1. Загрузить `guides/managing-tasks.md` (workflow)
2. Свериться с `lookup/task-commands.md` (использование CLI)

---

## Связанные материалы

- **Активные задачи** → `.tmp/tasks/{feature}/` (в корне проекта)
- **Завершенные задачи** → `.tmp/tasks/completed/{feature}/`
- **Агент TaskManager** → `.opencode/agent/subagents/core/task-manager.md`
- **Planning agents** → `.opencode/agent/subagents/planning/` (ArchitectureAnalyzer, StoryMapper, PrioritizationEngine, ContractManager, ADRManager)
- **Multi-stage workflow** → `../workflows/multi-stage-orchestration.md`
- **Базовая навигация** → `../navigation.md`
