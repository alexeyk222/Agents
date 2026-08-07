<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: вызов subagent

**Цель**: как корректно вызывать subagents через task tool  
**Приоритет**: HIGH — критично для делегирования агентами

---

## Проблема

**Проблема**: агенты пытаются вызывать subagents с неверным форматом `subagent_type`

**Ошибка**:
```
Unknown agent type: ContextScout is not a valid agent type
```

**Причина**: параметр `subagent_type` в task tool должен совпадать с зарегистрированным agent type в OpenCode CLI, а не с path файла.

---

## Корректный вызов subagent

### Доступные типы subagent

На основе регистрации OpenCode CLI используйте эти точные строки для `subagent_type`:

**Core-субагенты**:
- `"Task Manager"` — декомпозиция задач и планирование
- `"Documentation"` — генерация документации
- `"ContextScout"` — поиск context files

**Code-субагенты**:
- `"Coder Agent"` — реализация кода
- `"TestEngineer"` — написание тестов
- `"Reviewer"` — code review
- `"Build Agent"` — build validation

**Субагенты System Builder**:
- `"Domain Analyzer"` — domain analysis
- `"Agent Generator"` — agent generation
- `"Context Organizer"` — context organization
- `"Workflow Designer"` — проектирование workflow
- `"Command Creator"` — command creation

**Utility-субагенты**:
- `"Image Specialist"` — image generation/editing

---

## Синтаксис вызова

### ✅ Правильный формат

```javascript
task(
  subagent_type="Task Manager",
  description="Break down feature into subtasks",
  prompt="Detailed instructions..."
)
```

### ❌ Неправильные форматы

```javascript
// ❌ Using file path
task(
  subagent_type="TaskManager",
  ...
)

// ❌ Using kebab-case ID
task(
  subagent_type="task-manager",
  ...
)

// ❌ Using registry path
task(
  subagent_type=".opencode/agent/subagents/core/task-manager.md",
  ...
)
```

---

## Как найти правильный type

### Метод 1: проверьте registry

```bash
# List all subagent names
cat registry.json | jq -r '.components.subagents[] | "\(.name)"'
```

**Вывод**:
```
Task Manager
Image Specialist
Reviewer
TestEngineer
Documentation Writer
Coder Agent
Build Agent
Domain Analyzer
Agent Generator
Context Organizer
Workflow Designer
Command Creator
ContextScout
```

### Метод 2: проверьте OpenCode CLI

```bash
# List available agents (if CLI supports it)
opencode list agents
```

### Метод 3: проверьте frontmatter агента

Смотрите поле `name` во frontmatter subagent:

```yaml
---
id: task-manager
name: Task Manager  # ← Use this for subagent_type
type: subagent
---
```

---

## Частые вызовы subagent

### Task Manager

```javascript
task(
  subagent_type="Task Manager",
  description="Break down complex feature",
  prompt="Break down the following feature into atomic subtasks:
          
          Feature: {feature description}
          
          Requirements:
          - {requirement 1}
          - {requirement 2}
          
          Create subtask files in tasks/subtasks/{feature}/"
)
```

### Documentation

```javascript
task(
  subagent_type="Documentation",
  description="Update documentation for feature",
  prompt="Update documentation for {feature}:
          
          What changed:
          - {change 1}
          - {change 2}
          
          Files to update:
          - {doc 1}
          - {doc 2}"
)
```

### TestEngineer

```javascript
task(
  subagent_type="TestEngineer",
  description="Write tests for feature",
  prompt="Write comprehensive tests for {feature}:
          
          Files to test:
          - {file 1}
          - {file 2}
          
          Test coverage:
          - Positive cases
          - Negative cases
          - Edge cases"
)
```

### Reviewer

```javascript
task(
  subagent_type="Reviewer",
  description="Review implementation",
  prompt="Review the following implementation:
          
          Files:
          - {file 1}
          - {file 2}
          
          Focus areas:
          - Security
          - Performance
          - Code quality"
)
```

### Coder Agent

```javascript
task(
  subagent_type="Coder Agent",
  description="Implement subtask",
  prompt="Implement the following subtask:
          
          Subtask: {subtask description}
          
          Files to create/modify:
          - {file 1}
          
          Requirements:
          - {requirement 1}
          - {requirement 2}"
)
```

---

## Особый случай ContextScout

**Статус**: ⚠️ может быть еще не зарегистрирован в OpenCode CLI

Subagent `ContextScout` есть в repository, но может отсутствовать среди доступных agent types в OpenCode CLI.

### Обходной путь

Пока ContextScout не зарегистрирован корректно, используйте прямые операции с файлами:

```javascript
// ❌ This may fail
task(
  subagent_type="ContextScout",
  description="Find context files",
  prompt="Search for context related to {topic}"
)

// ✅ Use direct operations instead
// 1. Use glob to find context files
glob(pattern="**/*.md", path=".opencode/context")

// 2. Use grep to search content
grep(pattern="registry", path=".opencode/context")

// 3. Read relevant files directly
read(filePath=".opencode/context/openagents-repo/core-concepts/registry.md")
```

---

## Исправление существующих агентов

### Агенты, которые нужно исправить

1. **repo-manager.md** — использует `ContextScout`
2. **opencoder.md** — проверьте, использует ли неверный формат

### Процесс исправления

1. **Найдите неправильные вызовы**:
   ```bash
   grep -r 'subagent_type="subagents/' .opencode/agent --include="*.md"
   ```

2. **Замените на правильный формат**:
   ```bash
   # Example: Fix task-manager invocation
   # Old: subagent_type="TaskManager"
   # New: subagent_type="Task Manager"
   ```

3. **Проверьте исправление**:
   ```bash
   # Run agent with test prompt
   # Verify subagent delegation works
   ```

---

## Валидация

### Проверяйте subagent type перед использованием

```javascript
// Pseudo-code for validation
available_types = [
  "Task Manager",
  "Documentation",
  "TestEngineer",
  "Reviewer",
  "Coder Agent",
  "Build Agent",
  "Image Specialist",
  "Domain Analyzer",
  "Agent Generator",
  "Context Organizer",
  "Workflow Designer",
  "Command Creator"
]

if subagent_type not in available_types:
  error("Invalid subagent type: {subagent_type}")
```

---

## Лучшие практики

✅ **Используйте точные имена** — совпадающие с полем `name` в registry  
✅ **Сначала проверяйте registry** — убедитесь, что subagent существует  
✅ **Тестируйте вызовы** — проверяйте делегирование перед commit  
✅ **Документируйте dependencies** — перечисляйте нужных subagents во frontmatter агента  

❌ **Не используйте paths** — никогда не используйте file paths как subagent_type  
❌ **Не используйте IDs** — не используйте kebab-case IDs  
❌ **Не предполагайте** — всегда проверяйте, что subagent зарегистрирован  

---

## Диагностика

### Ошибка: "Unknown agent type"

**Причина**: subagent type не зарегистрирован в CLI или указан неверно

**Решения**:
1. Проверьте registry на правильное name
2. Убедитесь, что subagent существует в `.opencode/agent/subagents/`
3. Используйте точное name из поля `name` в registry
4. Если subagent не зарегистрирован, используйте прямые операции вместо него

### Ошибка: "Subagent not found"

**Причина**: файл subagent не существует

**Решения**:
1. Проверьте, что файл существует по ожидаемому path
2. Убедитесь, что запись registry корректна
3. Запустите `./scripts/registry/validate-registry.sh`

### Делегирование тихо не срабатывает

**Причина**: subagent вызван, но не выполняется

**Решения**:
1. Проверьте, что у subagent включены required tools
2. Убедитесь, что permissions subagent разрешают операцию
3. Проверьте, что prompt subagent понятен и actionable

---

## Связанные файлы

- **Registry**: `registry.json` — каталог компонентов
- **Субагенты**: `.opencode/agent/subagents/` — определения subagent
- **Валидация**: `scripts/registry/validate-registry.sh`

---

**Последнее обновление**: 2025-12-29  
**Версия**: 0.5.1
