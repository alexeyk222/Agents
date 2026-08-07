<!-- Context: openagents-repo/concepts | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Режимы тестирования субагентов

**Назначение**: понять два способа тестирования субагентов (standalone vs delegation)

**Последнее обновление**: 2026-01-07

---

## Ключевая концепция

У субагентов есть **два отдельных режима тестирования** — выбор зависит от того, что вы проверяете:

1. **Standalone-режим** - прямой тест логики субагента (unit testing)
2. **Режим делегирования** - тест процесса parent → subagent (integration testing)

Режим определяет, какой агент запускается и как используются инструменты.

---

## Standalone-режим (unit-тестирование)

**Назначение**: тестировать логику субагента изолированно

**Команда**:
```bash
npm run eval:sdk -- --subagent=ContextScout
```

**Что происходит**:
- Eval-фреймворк принудительно ставит `mode: primary` (переопределяет `mode: subagent`)
- ContextScout запускается как primary agent
- ContextScout использует инструменты напрямую (glob, read, grep, list)
- Parent agent не участвует

**Когда использовать**:
- Unit-тестирование логики субагента
- Отладка использования инструментов
- Разработка фич
- Проверка изменений промпта

**Расположение тестов**: `evals/agents/subagents/core/{subagent}/tests/standalone/`

---

## Режим делегирования (интеграционное тестирование)

**Назначение**: тестировать реальный production-процесс (parent делегирует субагенту)

**Команда**:
```bash
npm run eval:sdk -- --agent=core/openagent --pattern="delegation/*.yaml"
```

**Что происходит**:
- OpenAgent запускается как primary agent
- OpenAgent использует инструмент `task` для делегирования ContextScout
- ContextScout запускается с `mode: subagent` (естественный режим)
- Проверяется полный процесс делегирования

**Когда использовать**:
- Интеграционное тестирование
- Проверка production-поведения
- Тестирование логики делегирования
- End-to-end процессы

**Расположение тестов**: `evals/agents/subagents/core/{subagent}/tests/delegation/`

---

## Критическое различие

| Аспект | Standalone-режим | Режим делегирования |
|--------|----------------|-----------------|
| **Флаг** | `--subagent=NAME` | `--agent=PARENT` |
| **Режим агента** | Принудительно `primary` | Естественный `subagent` |
| **Кто запускается** | Субагент напрямую | Parent → Subagent |
| **Использование инструментов** | Субагент использует инструменты | Parent использует инструмент `task` |
| **Тесты** | `standalone/*.yaml` | `delegation/*.yaml` |

**Частая ошибка**:
```bash
# ❌ WRONG - This runs OpenAgent, not ContextScout
npm run eval:sdk -- --agent=ContextScout

# ✅ CORRECT - This runs ContextScout directly
npm run eval:sdk -- --subagent=ContextScout
```

---

## Как проверить правильный режим

### Индикаторы standalone-режима:
```
⚡ Standalone Test Mode
   Subagent: contextscout
   Mode: Forced to 'primary' for direct testing
```

### Индикаторы режима делегирования:
```
Testing agent: core/openagent
🎯 PARENT: OpenAgent
   Delegating to: contextscout
```

---

## Когда использовать каждый режим

**Используйте standalone-режим, когда**:
- Тестируете ключевую логику субагента
- Отлаживаете, почему субагент не использует инструменты
- Проверяете изменения промпта
- Быстро итерируете при разработке

**Используйте режим делегирования, когда**:
- Тестируете production-процесс
- Проверяете коммуникацию parent → subagent
- Тестируете передачу контекста
- Проводите интеграционное тестирование

---

## Связанные материалы

- `guides/testing-subagents.md` - пошаговое руководство по тестированию
- `lookup/subagent-test-commands.md` - краткий справочник команд
- `errors/tool-permission-errors.md` - типовые проблемы тестирования

**Справка**: `evals/framework/src/sdk/run-sdk-tests.ts` (логика принудительного режима)
