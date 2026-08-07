<!-- Context: openagents-repo/lookup | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Справочник: карты фреймворка субагентов

**Назначение**: краткий справочник по добавлению субагентов в eval-фреймворк  
**Последнее обновление**: 2026-01-09

---

## Критично: нужно обновить ТРИ карты

При добавлении нового субагента обновите эти ТРИ места:

### 1. Parent map (run-sdk-tests.ts ~строка 336)
**Назначение**: связывает subagent → parent agent для тестирования делегирования

```typescript
const subagentParentMap: Record<string, string> = {
  'contextscout': 'openagent',     // Core subagents → openagent
  'task-manager': 'openagent',
  'documentation': 'openagent',
  
  'coder-agent': 'opencoder',      // Code subagents → opencoder
  'tester': 'opencoder',
  'reviewer': 'opencoder',
};
```

### 2. Path map (run-sdk-tests.ts ~строка 414)
**Назначение**: связывает имя субагента → путь файла для поиска тестов

```typescript
const subagentPathMap: Record<string, string> = {
  'contextscout': 'ContextScout',
  'task-manager': 'TaskManager',
  'coder-agent': 'CoderAgent',
};
```

### 3. Agent map (test-runner.ts ~строка 238)
**Назначение**: связывает имя субагента → файл агента для eval-runner

```typescript
const agentMap: Record<string, string> = {
  'contextscout': 'ContextScout.md',
  'task-manager': 'TaskManager.md',
  'coder-agent': 'CoderAgent.md',
};
```

---

## Сообщения об ошибках

| Ошибка | Где отсутствует | Исправление |
|-------|--------------|-----|
| "No test files found" | Path map (#2) | Добавьте в `subagentPathMap` |
| "Unknown subagent" | Parent map (#1) | Добавьте в `subagentParentMap` |
| "Agent file not found" | Agent map (#3) | Добавьте в `agentMap` |

---

## Команды тестирования

```bash
# Standalone mode (forces mode: primary)
npm run eval:sdk -- --subagent=contextscout

# Delegation mode (tests via parent)
npm run eval:sdk -- --subagent=contextscout --delegate
```

---

## Связанные материалы

- `guides/testing-subagents.md` - полное руководство по тестированию
- `guides/adding-agent.md` - создание новых агентов
