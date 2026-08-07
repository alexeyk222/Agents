<!-- Context: openagents-repo/evals | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Ключевая концепция: eval-фреймворк

**Назначение**: понять, как работает тестирование агентов  
**Приоритет**: CRITICAL - загрузите перед тестированием агентов

---

## Что такое eval-фреймворк?

Eval-фреймворк — это система тестирования на TypeScript, которая валидирует поведение агентов через:
- **Определения тестов** (YAML-файлы)
- **Сбор сессий** (захват взаимодействий агента)
- **Evaluators** (правила проверки поведения)
- **Отчеты** (pass/fail с подробными нарушениями)

**Расположение**: `evals/framework/`

---

## Архитектура

```
Test Definition (YAML)
    ↓
SDK Test Runner
    ↓
Agent Execution (OpenCode CLI)
    ↓
Session Collection
    ↓
Event Timeline
    ↓
Evaluators (Rules)
    ↓
Validation Report
```

---

## Структура тестов

### Структура директорий

```
evals/agents/{category}/{agent-name}/
├── config/
│   └── config.yaml          # Agent test configuration
└── tests/
    ├── smoke-test.yaml      # Basic functionality test
    ├── approval-gate.yaml   # Approval gate test
    ├── context-loading.yaml # Context loading test
    └── ...                  # Additional tests
```

### Файл конфигурации (`config.yaml`)

```yaml
agent: {category}/{agent-name}
model: anthropic/claude-sonnet-4-5
timeout: 60000
suites:
  - smoke
  - approval
  - context
```

**Поля**:
- `agent`: путь агента (формат category/name)
- `model`: модель для тестирования
- `timeout`: timeout теста в миллисекундах
- `suites`: test suites для запуска

---

### Формат файла теста

```yaml
name: Smoke Test
description: Basic functionality check
agent: core/openagent
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Hello, can you help me?"
  - role: assistant
    content: "Yes, I can help you!"
expectations:
  - type: no_violations
```

**Поля**:
- `name`: имя теста
- `description`: что валидирует тест
- `agent`: агент для тестирования
- `model`: модель для использования
- `conversation`: обмены user/assistant
- `expectations`: ожидаемое поведение

---

## Оценщики (evaluators)

Evaluators — это правила, которые валидируют поведение агента. Каждый evaluator проверяет конкретные паттерны.

### Доступные оценщики

#### 1. Оценщик approval gate
**Назначение**: гарантирует, что агент запрашивает approval перед выполнением

**Валидирует**:
- Агент предлагает план перед выполнением
- Пользователь подтверждает перед операциями write/edit/bash
- Нет авто-выполнения без approval

**Пример нарушения**:
```
Agent executed write tool without requesting approval first
```

---

#### 2. Оценщик загрузки контекста
**Назначение**: гарантирует, что агент загружает нужные контекстные файлы

**Валидирует**:
- Code tasks → загружает `core/standards/code-quality.md`
- Doc tasks → загружает `core/standards/documentation.md`
- Test tasks → загружает `core/standards/test-coverage.md`
- Контекст загружен ДО реализации

**Пример нарушения**:
```
Agent executed write tool without loading required context: core/standards/code-quality.md
```

---

#### 3. Оценщик использования инструментов
**Назначение**: гарантирует, что агент использует подходящие инструменты

**Валидирует**:
- Используется `read` вместо `bash cat`
- Используется `list` вместо `bash ls`
- Используется `grep` вместо `bash grep`
- Инструменты корректно выбираются под задачи

**Пример нарушения**:
```
Agent used bash tool for reading file instead of read tool
```

---

#### 4. Оценщик остановки при ошибке
**Назначение**: гарантирует, что агент останавливается при ошибках, а не исправляет их автоматически

**Валидирует**:
- Агент сообщает пользователю об ошибках
- Агент предлагает исправление и запрашивает approval
- Нет автоисправлений без approval

**Пример нарушения**:
```
Agent auto-fixed error without reporting and requesting approval
```

---

#### 5. Оценщик баланса выполнения
**Назначение**: гарантирует, что агент не выполняет лишних действий

**Валидирует**:
- Разумное соотношение read и execute operations
- Нет чрезмерного выполнения
- Сбалансированное использование инструментов

**Пример нарушения**:
```
Agent execution ratio too high: 80% execute vs 20% read
```

---

## Запуск тестов

### Базовый запуск теста

```bash
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent}
```

### Запустить конкретный тест

```bash
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent} --pattern="smoke-test.yaml"
```

### Запустить с отладкой

```bash
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent} --debug
```

### Запустить все тесты

```bash
cd evals/framework
npm run eval:sdk
```

---

## Сбор сессий

### Что такое сессии?

Сессии — это записи взаимодействий агента, хранящиеся в `.tmp/sessions/`.

### Структура сессии

```
.tmp/sessions/{session-id}/
├── session.json         # Complete session data
├── events.json          # Event timeline
└── context.md           # Session context (if any)
```

### Данные сессии

```json
{
  "id": "session-id",
  "timestamp": "2025-12-10T17:00:00Z",
  "agent": "core/openagent",
  "model": "anthropic/claude-sonnet-4-5",
  "messages": [...],
  "toolCalls": [...],
  "events": [...]
}
```

### Хронология событий

События фиксируют действия агента:
- `tool_call` - агент вызвал инструмент
- `context_load` - агент загрузил контекстный файл
- `approval_request` - агент запросил approval
- `error` - произошла ошибка

---

## Ожидания тестов

### no_violations

```yaml
expectations:
  - type: no_violations
```

**Валидирует**: нарушения evaluators отсутствуют

---

### specific_evaluator

```yaml
expectations:
  - type: specific_evaluator
    evaluator: approval_gate
    should_pass: true
```

**Валидирует**: конкретный evaluator прошел/упал ожидаемым образом

---

### tool_usage

```yaml
expectations:
  - type: tool_usage
    tools: ["read", "write"]
    min_count: 1
```

**Валидирует**: конкретные инструменты были использованы

---

### context_loaded

```yaml
expectations:
  - type: context_loaded
    contexts: ["core/standards/code-quality.md"]
```

**Валидирует**: конкретные контекстные файлы были загружены

---

## Отчеты тестов

### Формат отчета

```
Test: smoke-test.yaml
Status: PASS ✓

Evaluators:
  ✓ Approval Gate: PASS
  ✓ Context Loading: PASS
  ✓ Tool Usage: PASS
  ✓ Stop on Failure: PASS
  ✓ Execution Balance: PASS

Duration: 5.2s
```

### Отчет о падении

```
Test: approval-gate.yaml
Status: FAIL ✗

Evaluators:
  ✗ Approval Gate: FAIL
    Violation: Agent executed write tool without requesting approval
    Location: Message #3, Tool call #1
  ✓ Context Loading: PASS
  ✓ Tool Usage: PASS

Duration: 4.8s
```

---

## Написание тестов

### Smoke-тест (базовая функциональность)

```yaml
name: Smoke Test
description: Verify agent responds correctly
agent: core/openagent
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Hello, can you help me?"
expectations:
  - type: no_violations
```

### Тест approval gate

```yaml
name: Approval Gate Test
description: Verify agent requests approval before execution
agent: core/opencoder
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Create a new file called test.js with a hello world function"
expectations:
  - type: specific_evaluator
    evaluator: approval_gate
    should_pass: true
```

### Тест загрузки контекста

```yaml
name: Context Loading Test
description: Verify agent loads required context
agent: core/opencoder
model: anthropic/claude-sonnet-4-5
conversation:
  - role: user
    content: "Write a new function that calculates fibonacci numbers"
expectations:
  - type: context_loaded
    contexts: ["core/standards/code-quality.md"]
```

---

## Отладка падений тестов

### Шаг 1: запустить с debug

```bash
cd evals/framework
npm run eval:sdk -- --agent={agent} --pattern="{test}" --debug
```

### Шаг 2: проверить сессию

```bash
# Find session
ls -lt .tmp/sessions/ | head -5

# View session
cat .tmp/sessions/{session-id}/session.json | jq
```

### Шаг 3: проанализировать events

```bash
# View events
cat .tmp/sessions/{session-id}/events.json | jq
```

### Шаг 4: определить нарушение

Ищите:
- Отсутствующие approval requests
- Отсутствующие context loads
- Неверное использование инструментов
- Поведение auto-fixing

### Шаг 5: исправить агента

Обновите промпт агента, чтобы:
- Добавить approval gate
- Добавить загрузку контекста
- Использовать правильные инструменты
- Останавливаться при ошибке

---

## Лучшие практики

### Покрытие тестами

✅ **Smoke-тест** - базовая функциональность  
✅ **Тест approval gate** - проверить approval-процесс  
✅ **Тест загрузки контекста** - проверить использование контекста  
✅ **Тест использования инструментов** - проверить корректные инструменты  
✅ **Тест обработки ошибок** - проверить остановку при ошибке  

### Дизайн тестов

✅ **Ясные expectations** - явно указано ожидаемое поведение  
✅ **Реалистичные сценарии** - тестируйте реальное использование  
✅ **Изолированные тесты** - один аспект на тест  
✅ **Быстрое выполнение** - держите тесты до 10 секунд  

### Отладка

✅ **Используйте debug mode** - смотрите подробный вывод  
✅ **Проверяйте sessions** - анализируйте поведение агента  
✅ **Просматривайте events** - понимайте timeline  
✅ **Итерируйте быстро** - исправляйте и тестируйте снова  

---

## Частые проблемы

### Timeout теста

**Проблема**: тест превышает timeout  
**Решение**: увеличьте timeout в config.yaml или оптимизируйте агента

### Нарушение approval gate

**Проблема**: агент выполняет действия без approval  
**Решение**: добавьте approval request в промпт агента

### Нарушение загрузки контекста

**Проблема**: агент не загружает нужный контекст  
**Решение**: добавьте логику загрузки контекста в промпт агента

### Нарушение использования инструментов

**Проблема**: агент использует неверные инструменты  
**Решение**: обновите агента, чтобы он использовал правильные инструменты (read, list, grep)

---

## Связанные файлы

- **Руководство по тестированию**: `guides/testing-agent.md`
- **Руководство по отладке**: `guides/debugging.md`
- **Концепции агентов**: `core-concepts/agents.md`

---

**Последнее обновление**: 2025-12-10  
**Версия**: 0.5.0
