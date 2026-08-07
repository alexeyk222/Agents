<!-- Context: core/managing-tasks | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: управление жизненным циклом задач

**Назначение**: пошаговый workflow для управления задачами на основе JSON

**Последнее обновление**: 2026-01-11

---

## Предварительные условия

- Доступен агент TaskManager
- Папка feature создана в `.tmp/tasks/` (в корне проекта)

---

## Обзор workflow

```
1. Initiation    → TaskManager creates task.json + subtasks
2. Selection     → Find eligible tasks (deps satisfied)
3. Execution     → Working agent implements task
4. Verification  → TaskManager validates completion
5. Archiving     → Move to completed/ when done
```

---

## 1. Инициация (TaskManager)

Создать папку feature и файлы:
```
.tmp/tasks/{feature-slug}/
├── task.json
├── subtask_01.json
├── subtask_02.json
└── subtask_03.json
```

Проверить через: `task-cli.ts validate {feature}`

---

## 2. Выбор задачи

Найти подходящие задачи через CLI:
```bash
task-cli.ts next {feature}      # All ready tasks
task-cli.ts parallel {feature}  # Parallelizable only
```

Критерии выбора:
- `status == "pending"`
- Все задачи из `depends_on` имеют `status == "completed"`

---

## 3. Выполнение (рабочий агент)

При взятии задачи:

1. Прочитать JSON подзадачи
2. Обновить status:
   ```json
   {
     "status": "in_progress",
     "agent_id": "coder-agent",
     "started_at": "2026-01-11T14:30:00Z"
   }
   ```
3. Загрузить `context_files` (лениво)
4. Реализовать `deliverables`
5. Добавить `completion_summary` (макс. 200 символов)

---

## 4. Проверка (TaskManager)

После сигнала агента о завершении:

1. Проверить каждый `acceptance_criteria`
2. Если все проходят → отметить completed:
   ```bash
   task-cli.ts complete {feature} {seq} "summary"
   ```
3. Если есть провал → оставить `in_progress`, сообщить об ошибках

---

## 5. Архивация

Когда `completed_count == subtask_count`:

1. Обновить `task.json`: `status: "completed"`
2. Переместить папку: `.tmp/tasks/{slug}/` → `.tmp/tasks/completed/{slug}/`

---

## Владение статусами

| Статус | Кто задает | Когда |
|--------|----------|------|
| pending | TaskManager | начальное создание |
| in_progress | рабочий агент | берет задачу |
| completed | TaskManager | после проверки |
| blocked | любой | найдена зависимость/проблема |

---

## Сводка CLI-команд

| Команда | Сценарий |
|---------|----------|
| `status` | краткий обзор |
| `next` | над чем работать |
| `parallel` | пакетная параллельная работа |
| `deps` | понять блокеры |
| `blocked` | найти проблемы |
| `complete` | отметить задачу выполненной |
| `validate` | проверить состояние |

---

## Связанные материалы

- `../standards/task-schema.md` - справочник JSON-полей
- `splitting-tasks.md` - как создавать подзадачи
- `../lookup/task-commands.md` - полный справочник CLI
