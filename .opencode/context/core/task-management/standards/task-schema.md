<!-- Context: core/task-schema | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Стандарт: схема Task JSON

**Назначение**: справочник JSON-схемы для файлов управления задачами

**Последнее обновление**: 2026-02-14

---

## Основные концепции

Управление задачами использует два типа JSON-файлов:
- `task.json` - метаданные и отслеживание на уровне feature
- `subtask_NN.json` - отдельные атомарные задачи с зависимостями

Расположение: `.tmp/tasks/{feature-slug}/` (в корне проекта)

---

## Версии схемы

Этот документ описывает **базовую схему** (v1.0), которой должны следовать все файлы задач.

Для **расширенных функций** (точность строк, моделирование домена, контракты, ADR, приоритизация):
- См. `enhanced-task-schema.md` для расширенных полей и возможностей
- Все расширенные поля **необязательны** и обратно совместимы
- Используйте расширенную схему для multi-stage orchestration workflows

---

## Схема `task.json`

| Поле | Тип | Обязательное | Описание |
|-------|------|----------|-------------|
| `id` | string | Yes | идентификатор в kebab-case |
| `name` | string | Yes | человекочитаемое имя (max 100) |
| `status` | enum | Yes | active / completed / blocked / archived |
| `objective` | string | Yes | цель в одну строку (max 200) |
| `context_files` | array | No | **только пути стандартов** — соглашения кодирования, паттерны, правила безопасности для соблюдения |
| `reference_files` | array | No | **только исходные материалы** — проектные файлы для изучения (существующий код, config, schemas) |
| `scientific_skills` | array | No | имена scientific skills, выбранных для задачи |
| `execution_modes` | array | No | режимы действий: local / network-read / external-write / hardware |
| `runtime` | object | No | требования к изолированному runtime (Python, R, Julia, MATLAB и т. п.) |
| `exit_criteria` | array | No | условия завершения |
| `subtask_count` | int | No | всего подзадач |
| `completed_count` | int | No | завершенных подзадач |
| `created_at` | datetime | Yes | ISO 8601 |
| `completed_at` | datetime | No | ISO 8601 |

---

## Схема `subtask_NN.json`

| Поле | Тип | Обязательное | Описание |
|-------|------|----------|-------------|
| `id` | string | Yes | {feature}-{seq} |
| `seq` | string | Yes | 2 цифры (01, 02) |
| `title` | string | Yes | заголовок задачи (max 100) |
| `status` | enum | Yes | pending / in_progress / completed / blocked |
| `depends_on` | array | No | номера последовательности зависимостей |
| `parallel` | bool | No | True, если можно выполнять вместе с другими |
| `context_files` | array | No | **только пути стандартов** — соглашения и паттерны для соблюдения |
| `reference_files` | array | No | **только исходные материалы** — существующие файлы для справки |
| `suggested_agent` | string | No | рекомендуемый агент для задачи (например, OpenFrontendSpecialist) |
| `scientific_skills` | array | No | имена scientific skills для загрузки `ScientificAgent` |
| `execution_modes` | array | No | режимы действий: local / network-read / external-write / hardware |
| `runtime` | object | No | требования к изолированному runtime |
| `acceptance_criteria` | array | No | бинарные условия pass/fail |
| `deliverables` | array | No | файлы для создания/изменения |
| `agent_id` | string | No | задается при `in_progress` |
| `started_at` | datetime | No | ISO 8601 |
| `completed_at` | datetime | No | ISO 8601 |
| `completion_summary` | string | No | что было сделано (max 200) |

---

## Переходы статусов

```
pending → in_progress   (by working agent, when deps satisfied)
in_progress → completed (by TaskManager, after verification)
* → blocked             (by either, when issue found)
blocked → pending       (when unblocked)
```

---

## Флаг `parallel`

- `parallel: true` = изолированная задача, можно выполнять вместе с другими
- `parallel: false` = может затрагивать общее состояние, выполнять последовательно

Используйте `task-cli.ts parallel`, чтобы найти все параллелизуемые задачи, готовые к запуску.

---

## `context_files` vs `reference_files` — правило

У этих двух полей принципиально разные назначения. **Никогда не смешивайте их.**

| Поле | Отвечает на | Содержит | Поведение агента |
|-------|---------|----------|----------------|
| `context_files` | "Каким правилам следовать?" | Стандарты, соглашения, паттерны из `.opencode/context/` | Загрузить и применять как coding guidelines |
| `reference_files` | "Какой существующий код смотреть?" | Исходные файлы проекта, configs, schemas | Читать для понимания существующих паттернов |

`scientific_skills` не заменяет эти поля: это короткий список capabilities, которые `ScientificAgent` должен загрузить через native skill tool. `execution_modes` описывает действия и побочные эффекты, а не чувствительность локальных данных.

**Неверно** ❌ — смешаны стандарты и исходные файлы:
```json
"context_files": [
  ".opencode/context/core/standards/code-quality.md",
  "package.json",
  "src/existing-auth.ts"
]
```

**Верно** ✅ — четкое разделение:
```json
"context_files": [
  ".opencode/context/core/standards/code-quality.md",
  ".opencode/context/core/standards/security-patterns.md"
],
"reference_files": [
  "package.json",
  "src/existing-auth.ts"
]
```

---

## Пример

```json
{
  "id": "auth-system-02",
  "seq": "02",
  "title": "Create JWT service",
  "status": "pending",
  "depends_on": ["01"],
  "parallel": false,
  "context_files": [
    ".opencode/context/core/standards/code-quality.md",
    ".opencode/context/core/standards/security-patterns.md"
  ],
  "reference_files": [
    "src/auth/token-utils.ts"
  ],
  "acceptance_criteria": ["JWT tokens signed with RS256", "Tests pass"],
  "deliverables": ["src/auth/jwt.service.ts"]
}
```

### Пример научной подзадачи

```json
{
  "id": "assay-analysis-02",
  "seq": "02",
  "title": "Проверить статистическую мощность эксперимента",
  "status": "pending",
  "depends_on": ["01"],
  "parallel": false,
  "suggested_agent": "ScientificAgent",
  "scientific_skills": ["statistical-power", "experimental-design"],
  "execution_modes": ["local"],
  "runtime": {"python": ">=3.11", "isolation": "project-local"},
  "context_files": [".opencode/context/scientific/navigation.md"],
  "reference_files": ["data/assay-results.csv"],
  "acceptance_criteria": ["Power assumptions are explicit", "Analysis is reproducible"],
  "deliverables": ["reports/power-analysis.md"],
  "agent_id": null,
  "started_at": null,
  "completed_at": null,
  "completion_summary": null
}
```

---

## Миграция на расширенную схему

Расширенная схема добавляет мощные возможности и сохраняет полную обратную совместимость:

### Когда использовать расширенную схему

Используйте `enhanced-task-schema.md`, когда нужны:
- **Line-number precision** - ссылки на конкретные разделы больших файлов (снижает когнитивную нагрузку)
- **Domain modeling** - отслеживание bounded contexts, modules, vertical slices
- **Contract tracking** - управление зависимостями API/interface
- **Design artifacts** - ссылки на Figma, wireframes, mockups
- **ADR references** - связь архитектурных решений с задачами
- **Prioritization** - scoring RICE/WSJF для планирования релиза

### Путь миграции

1. **Изменения не требуются** - существующие task files работают как есть
2. **Постепенное внедрение** - добавляйте расширенные поля инкрементально:
   - Начните с line-number precision для больших файлов контекста
   - Добавьте domain fields (`bounded_context`, `module`) при моделировании архитектуры
   - Добавьте contracts при определении API
   - Добавьте prioritization scores при планировании релизов
3. **Смешанные форматы** - старый и новый форматы можно сочетать в одном файле

### Пример: добавление line-number precision

**Старый формат** (все еще валиден):
```json
"context_files": [
  ".opencode/context/core/standards/code-quality.md"
]
```

**Новый формат** (расширенный):
```json
"context_files": [
  {
    "path": ".opencode/context/core/standards/code-quality.md",
    "lines": "53-95",
    "reason": "Pure function patterns for service layer"
  }
]
```

Оба формата работают. Агенты обрабатывают оба автоматически.

---

## Связанные материалы

- `enhanced-task-schema.md` - расширенная схема с advanced features
- `../guides/splitting-tasks.md` - как декомпозировать фичи
- `../guides/managing-tasks.md` - workflow жизненного цикла
- `../lookup/task-commands.md` - справочник CLI
