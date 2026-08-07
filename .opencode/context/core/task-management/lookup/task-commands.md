<!-- Context: core/task-commands | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Справочник: команды Task CLI

**Назначение**: краткий справочник по командам `task-cli.ts`

**Последнее обновление**: 2026-02-14

---

## Использование

```bash
npx ts-node .opencode/context/tasks/scripts/task-cli.ts <command> [args]
```

Файлы задач хранятся в `.tmp/tasks/` в корне проекта.

---

## Команды

### status [feature]

Показать сводку статуса задач для всех фич или конкретной фичи.

```bash
task-cli.ts status
task-cli.ts status my-feature
```

**Вывод**:
```
[my-feature] My Feature Name
  Status: active | Progress: 40% (2/5)
  Pending: 2 | In Progress: 1 | Completed: 2 | Blocked: 0
```

---

### next [feature]

Показать задачи, готовые к работе (зависимости выполнены).

```bash
task-cli.ts next
task-cli.ts next my-feature
```

**Вывод**:
```
=== Ready Tasks (deps satisfied) ===

[my-feature]
  02 - Create JWT service  [sequential]
  03 - Write unit tests    [parallel]
```

---

### parallel [feature]

Показать только параллелизуемые задачи, готовые сейчас.

```bash
task-cli.ts parallel
task-cli.ts parallel my-feature
```

**Использование**: объединить несколько изолированных задач для параллельного выполнения.

---

### deps \<feature\> \<seq\>

Показать дерево зависимостей для конкретной задачи.

```bash
task-cli.ts deps my-feature 04
```

**Вывод**:
```
=== Dependency Tree: my-feature/04 ===

04 - Integration tests [pending]
  ├── ✓ 01 - Setup database [completed]
  └── ○ 02 - Create API [pending]
      └── ✓ 01 - Setup database [completed]
```

---

### blocked [feature]

Показать заблокированные задачи и причины.

```bash
task-cli.ts blocked
task-cli.ts blocked my-feature
```

**Вывод**:
```
=== Blocked Tasks ===

[my-feature]
  04 - Integration tests (waiting: 02, 03)
  05 - Deploy (explicitly blocked)
```

---

### complete \<feature\> \<seq\> "summary"

Отметить задачу выполненной со сводкой (макс. 200 символов).

```bash
task-cli.ts complete my-feature 02 "Created JWT service with RS256 signing"
```

**Эффект**:
- Устанавливает `status: "completed"`
- Устанавливает временную метку `completed_at`
- Устанавливает `completion_summary`
- Обновляет счетчики в `task.json`

---

### validate [feature]

Проверить валидность JSON, зависимости и циклические ссылки.

```bash
task-cli.ts validate
task-cli.ts validate my-feature
```

**Проверки**:
- `task.json` существует
- Формат ID корректен
- Зависимости существуют
- Нет циклических зависимостей
- Счетчики совпадают

**Вывод**:
```
[my-feature]
  ✓ All checks passed

[broken-feature]
  ✗ ERROR: 03: depends on non-existent task 99
  ⚠ WARNING: 02: No acceptance criteria defined
```

---

## Коды выхода

| Код | Значение |
|------|---------|
| 0 | Успех |
| 1 | Ошибка (`validate` нашел проблемы, не хватает args) |

---

## Поддержка расширенной схемы

CLI полностью поддерживает расширенную схему задач (v2.0) с:
- **Line-number precision** - файлы контекста с конкретными диапазонами строк
- **Domain modeling** - поля `bounded_context`, `module`, `vertical_slice`
- **Contract tracking** - зависимости API/interface
- **Design artifacts** - Figma, wireframes, mockups
- **ADR references** - architecture decision records
- **Prioritization** - scores RICE/WSJF

Все расширенные поля необязательны и обратно совместимы. Подробности см. в `../standards/enhanced-task-schema.md`.

---

## Интеграция с planning workflow

Для multi-stage orchestration workflows используйте эти planning agents перед созданием задач:

| Агент | Назначение | Выход |
|-------|---------|--------|
| **ArchitectureAnalyzer** | определение DDD bounded context | `.tmp/architecture/contexts.json` |
| **StoryMapper** | user journey и story mapping | `.tmp/story-maps/map.json` |
| **PrioritizationEngine** | scoring RICE/WSJF | `.tmp/backlog/prioritized.json` |
| **ContractManager** | определение API contract | `.tmp/contracts/{service}.json` |
| **ADRManager** | architecture decision records | `docs/adr/` |

Эти агенты автоматически заполняют поля расширенной схемы (`bounded_context`, `contracts`, `related_adrs`, `rice_score` и т. д.).

Полный workflow см. в `.opencode/context/core/workflows/multi-stage-orchestration.md`.

---

## Связанные материалы

- `../standards/task-schema.md` - справочник базовой JSON-схемы
- `../standards/enhanced-task-schema.md` - расширенная схема с advanced features
- `../guides/managing-tasks.md` - руководство по workflow
- `../workflows/multi-stage-orchestration.md` - planning workflow
