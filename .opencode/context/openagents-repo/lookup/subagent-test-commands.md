<!-- Context: openagents-repo/lookup | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Команды тестирования субагентов — краткий справочник

**Назначение**: краткий справочник команд для тестирования субагентов

**Последнее обновление**: 2026-01-07

---

## Standalone-режим (unit-тестирование)

### Запустить все standalone-тесты
```bash
cd evals/framework
npm run eval:sdk -- --subagent=ContextScout --pattern="standalone/*.yaml"
```

### Запустить один тест
```bash
npm run eval:sdk -- --subagent=ContextScout --pattern="standalone/01-simple-discovery.yaml"
```

### Режим отладки
```bash
npm run eval:sdk -- --subagent=ContextScout --pattern="standalone/*.yaml" --debug
```

---

## Режим делегирования (интеграционное тестирование)

### Запустить тесты делегирования
```bash
npm run eval:sdk -- --agent=core/openagent --pattern="delegation/*.yaml"
```

### Проверить конкретное делегирование
```bash
npm run eval:sdk -- --agent=core/openagent --pattern="delegation/01-contextscout-delegation.yaml"
```

---

## Команды проверки

### Проверить файл агента
```bash
# View agent frontmatter
head -30 .opencode/agent/subagents/core/contextscout.md

# Check tool permissions
grep -A 10 "^tools:" .opencode/agent/subagents/core/contextscout.md
```

### Проверить конфиг теста
```bash
cat evals/agents/ContextScout/config/config.yaml
```

### Посмотреть последние результаты
```bash
# Summary
cat evals/results/latest.json | jq '.summary'

# Agent loaded
cat evals/results/latest.json | jq '.meta.agent'

# Tool calls
cat evals/results/latest.json | jq '.tests[0]' | grep -A 5 "Tool"

# Violations
cat evals/results/latest.json | jq '.tests[0].violations'
```

---

## Частые паттерны тестов

### Smoke-тест
```bash
npm run eval:sdk -- --subagent=ContextScout --pattern="smoke-test.yaml"
```

### Конкретный test suite
```bash
npm run eval:sdk -- --subagent=ContextScout --pattern="discovery/*.yaml"
```

### Все тесты субагента
```bash
npm run eval:sdk -- --subagent=ContextScout
```

---

## Справочник флагов

| Флаг | Назначение | Пример |
|------|---------|---------|
| `--subagent` | Тестировать субагента в standalone-режиме | `--subagent=ContextScout` |
| `--agent` | Тестировать primary-агента (или делегирование) | `--agent=core/openagent` |
| `--pattern` | Фильтровать тестовые файлы | `--pattern="standalone/*.yaml"` |
| `--debug` | Показать подробный вывод | `--debug` |
| `--timeout` | Переопределить timeout | `--timeout=120000` |

---

## Команды диагностики

### Проверить, какой агент запускался
```bash
# Should show subagent name for standalone mode
cat evals/results/latest.json | jq '.meta.agent'
```

### Проверить использование инструментов
```bash
# Should show tool calls > 0
cat evals/results/latest.json | jq '.tests[0]' | grep "Tool Calls"
```

### Посмотреть timeline теста
```bash
# See full conversation
cat evals/results/history/2026-01/07-*.json | jq '.tests[0].timeline'
```

### Проверить ошибки
```bash
# View violations
cat evals/results/latest.json | jq '.tests[0].violations.details'
```

---

## Расположение файлов

### Файлы агентов
```
.opencode/agent/subagents/core/{subagent}.md
```

### Файлы тестов
```
evals/agents/subagents/core/{subagent}/
├── config/config.yaml
└── tests/
    ├── standalone/
    │   ├── 01-simple-discovery.yaml
    │   └── 02-advanced-test.yaml
    └── delegation/
        └── 01-delegation-test.yaml
```

### Результаты
```
evals/results/
├── latest.json                    # Latest test run
└── history/2026-01/              # Historical results
    └── 07-HHMMSS-{agent}.json
```

---

## Быстрые проверки

### Агент загружен правильно?
```bash
# Should show: "agent": "ContextScout"
cat evals/results/latest.json | jq '.meta.agent'
```

### Агент использовал инструменты?
```bash
# Should show: Tool Calls: 1 (or more)
cat evals/results/latest.json | jq '.tests[0]' | grep "Tool Calls"
```

### Тест прошел?
```bash
# Should show: "passed": 1, "failed": 0
cat evals/results/latest.json | jq '.summary'
```

---

## Связанные материалы

- `concepts/subagent-testing-modes.md` - понять режимы тестирования
- `guides/testing-subagents.md` - пошаговое руководство по тестированию
- `errors/tool-permission-errors.md` - исправление частых проблем

**Справка**: `evals/framework/src/sdk/run-sdk-tests.ts`
