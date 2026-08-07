---
description: Поддерживайте качество registry через валидацию зависимостей и проверки консистентности
tags:
  - registry
  - quality
  - validation
  - dependencies
dependencies: []
---

<!-- Context: quality/registry-dependencies | Priority: high | Version: 1.0 | Updated: 2026-01-06 -->
# Валидация зависимостей registry

**Назначение**: поддерживать качество registry через валидацию зависимостей и проверки консистентности  
**Аудитория**: участники, мейнтейнеры, CI/CD-процессы

---

## Краткий справочник

**Золотое правило**: все зависимости компонентов должны быть объявлены во frontmatter и проверены до коммита.

**Критические команды**:
```bash
# Check context file dependencies
/check-context-deps

# Auto-fix missing dependencies
/check-context-deps --fix

# Validate entire registry
./scripts/registry/validate-registry.sh

# Update registry after changes
./scripts/registry/auto-detect-components.sh --auto-add
```

---

## Система зависимостей

### Типы зависимостей

Компоненты могут зависеть от других компонентов в формате `type:id`:

| Тип | Формат | Пример | Описание |
|------|--------|---------|-------------|
| **agent** | `agent:id` | `agent:opencoder` | Профиль core-агента |
| **subagent** | `subagent:id` | `subagent:coder-agent` | Делегируемый субагент |
| **command** | `command:id` | `command:context` | Slash-команда |
| **tool** | `tool:id` | `tool:gemini` | Интеграция внешнего инструмента |
| **plugin** | `plugin:id` | `plugin:context` | Компонент плагина |
| **context** | `context:path` | `context:core/standards/code` | Контекстный файл |
| **config** | `config:id` | `config:defaults` | Файл конфигурации |

### Объявление зависимостей

**Во frontmatter компонента** (пример):
```
id: opencoder
name: OpenCoder
description: Multi-language implementation agent
dependencies:
  - subagent:task-manager      # Can delegate to task-manager
  - subagent:coder-agent        # Can delegate to coder-agent
  - subagent:tester             # Can delegate to tester
  - context:core/standards/code # Requires code standards context
```

**Зачем объявлять зависимости?**
- ✅ **Валидация**: находить отсутствующие компоненты до выполнения
- ✅ **Документация**: ясно видеть, что нужно каждому компоненту
- ✅ **Установка**: инсталляторы могут получить все нужные зависимости
- ✅ **Графы зависимостей**: визуализировать связи компонентов
- ✅ **Обнаружение ломающих изменений**: понимать, что затронуто изменениями

---

## Зависимости контекстных файлов

### Проблема

Агенты ссылаются на контекстные файлы в промптах, но часто не объявляют их как зависимости:

```markdown
<!-- In agent prompt -->
BEFORE any code implementation, ALWAYS load:
- Code tasks → .opencode/context/core/standards/code-quality.md (MANDATORY)
```

**Без объявления зависимости**:
- ❌ Нет проверки, что контекстный файл существует
- ❌ Нельзя отследить, какие агенты используют какие контекстные файлы
- ❌ Возникают ломающие изменения при перемещении/удалении контекстных файлов
- ❌ Инсталляторы не знают, что нужно получить контекстные файлы

### Решение

**Объявляйте context-зависимости во frontmatter** (пример):
```
id: opencoder
dependencies:
  - context:core/standards/code  # ← ADD THIS
```

**Используйте `/check-context-deps`, чтобы найти отсутствующие объявления**:
```bash
# Analyze all agents
/check-context-deps

# Auto-fix missing context dependencies
/check-context-deps --fix
```

### Формат context-зависимостей

**Нормализация пути**:
```
File path:     .opencode/context/core/standards/code-quality.md
Dependency:    context:core/standards/code
               ^^^^^^^ ^^^^^^^^^^^^^^^^^^^
               type    path (no .opencode/, no .md)
```

**Примеры**:
```
dependencies:
  - context:core/standards/code           # .opencode/context/core/standards/code-quality.md
  - context:core/standards/docs           # .opencode/context/core/standards/documentation.md
  - context:core/workflows/delegation     # .opencode/context/core/workflows/task-delegation-basics.md
  - context:openagents-repo/guides/adding-agent  # Project-specific context
```

---

## Процесс валидации

### Чек-лист перед коммитом

Перед коммитом изменений в агентах, командах или контекстных файлах:

1. **Проверьте context-зависимости**:
   ```bash
   /check-context-deps
   ```
   - Находит агентов, которые используют контекстные файлы без объявления
   - Сообщает о неиспользуемых контекстных файлах
   - Валидирует пути контекстных файлов

2. **Исправьте отсутствующие зависимости** (если нужно):
   ```bash
   /check-context-deps --fix
   ```
   - Автоматически добавляет отсутствующие зависимости `context:` во frontmatter
   - Сохраняет существующие зависимости

3. **Обновите registry**:
   ```bash
   ./scripts/registry/auto-detect-components.sh --auto-add
   ```
   - Извлекает зависимости из frontmatter
   - Обновляет registry.json

4. **Валидируйте registry**:
   ```bash
   ./scripts/registry/validate-registry.sh
   ```
   - Проверяет, что все зависимости существуют
   - Валидирует пути компонентов
   - Сообщает об отсутствующих зависимостях

### Инструменты валидации

#### 1. Команда `/check-context-deps`

**Назначение**: анализировать использование контекстных файлов и валидировать зависимости

**Что проверяет**:
- ✅ Агенты ссылаются на контекстные файлы в промптах
- ✅ Context-зависимости объявлены во frontmatter
- ✅ Контекстные файлы существуют на диске
- ✅ Контекстные файлы есть в registry
- ✅ Неиспользуемые контекстные файлы

**Использование**:
```bash
# Full analysis
/check-context-deps

# Specific agent
/check-context-deps opencoder

# Auto-fix
/check-context-deps --fix

# Verbose (show line numbers)
/check-context-deps --verbose
```

**Пример вывода**:
```
# Отчёт анализа зависимостей контекста

## Summary
- Agents scanned: 25
- Context files referenced: 12
- Missing dependencies: 8
- Unused context files: 2

## Missing Dependencies

### opencoder
Uses but not declared:
- context:core/standards/code (referenced 3 times)
  - Line 64: "Code tasks → .opencode/context/core/standards/code-quality.md"
  
Recommended fix:
dependencies:
  - context:core/standards/code
```

#### 2. Скрипт `auto-detect-components.sh`

**Назначение**: искать новые компоненты и обновлять registry

**Валидация зависимостей**:
- Проверяет зависимости при сканировании компонентов
- Логирует предупреждения для отсутствующих зависимостей
- Не блокирует выполнение (только предупреждения)

**Использование**:
```bash
# See what would be added
./scripts/registry/auto-detect-components.sh --dry-run

# Add new components
./scripts/registry/auto-detect-components.sh --auto-add
```

**Пример предупреждения**:
```
⚠ New command: Demo (demo)
  Dependencies: subagent:coder-agent,subagent:missing-agent
    ⚠ Dependency not found in registry: subagent:missing-agent
```

#### 3. Скрипт `validate-registry.sh`

**Назначение**: комплексная валидация registry

**Проверки**:
- ✅ Все пути компонентов существуют
- ✅ Все зависимости существуют в registry
- ✅ Нет дублирующихся IDs
- ✅ Валидная структура JSON
- ✅ Обязательные поля присутствуют

**Использование**:
```bash
./scripts/registry/validate-registry.sh
```

**Пример вывода**:
```
Validating registry.json...

✗ Dependency not found: opencoder → context:core/standards/code

Missing dependencies: 1
  - opencoder (agent) → context:core/standards/code

Fix: Add missing component to registry or remove from dependencies
```

---

## Стандарты качества

### Хорошо поддерживаемый registry

Качественный registry имеет:

✅ **Полные зависимости**: все зависимости компонентов объявлены
✅ **Проверенные зависимости**: все зависимости существуют в registry
✅ **Нет сирот**: каждый контекстный файл используется хотя бы одним компонентом
✅ **Единый формат**: зависимости используют формат `type:id`
✅ **Актуальность**: registry отражает текущее состояние компонентов
✅ **Нет битых путей**: все пути компонентов валидны

### Стандарты объявления зависимостей

**Делайте**:
- ✅ Объявляйте всех субагентов, которым делегируете
- ✅ Объявляйте все контекстные файлы, на которые ссылаетесь
- ✅ Объявляйте все команды, которые вызываете
- ✅ Используйте корректный формат: `type:id`
- ✅ Храните зависимости во frontmatter (не хардкодьте в промптах)

**Не делайте**:
- ❌ Не ссылайтесь на контекстные файлы без объявления зависимости
- ❌ Не используйте неверные форматы зависимостей
- ❌ Не объявляйте зависимости, которые фактически не используете
- ❌ Не забывайте обновлять registry после добавления зависимостей

---

## Рекомендации по коммитам

### При добавлении/изменении компонентов

**1. Добавьте компонент с корректным frontmatter** (пример):
```
id: my-agent
name: My Agent
description: Does something useful
tags:
  - development
  - coding
dependencies:
  - subagent:coder-agent
  - context:core/standards/code
```

**2. Валидируйте зависимости**:
```bash
/check-context-deps my-agent
```

**3. Обновите registry**:
```bash
./scripts/registry/auto-detect-components.sh --auto-add
```

**4. Валидируйте registry**:
```bash
./scripts/registry/validate-registry.sh
```

**5. Сделайте коммит с описательным сообщением**:
```bash
git add .opencode/agent/my-agent.md registry.json
git commit -m "Add my-agent with coder-agent and code standards dependencies"
```

### При изменении контекстных файлов

**1. Проверьте, какие агенты зависят от файла**:
```bash
jq '.components[] | .[] | select(.dependencies[]? | contains("context:core/standards/code")) | {id, name}' registry.json
```

**2. Обновите контекстный файл**:
```bash
# Make your changes
vim .opencode/context/core/standards/code-quality.md
```

**3. Проверьте, что нет битых ссылок**:
```bash
/check-context-deps --verbose
```

**4. Обновите registry, если нужно**:
```bash
./scripts/registry/auto-detect-components.sh --auto-add
```

**5. Сделайте коммит с примечанием о влиянии**:
```bash
git commit -m "Update code standards - affects opencoder, openagent, reviewer"
```

### При удалении компонентов

**1. Сначала проверьте зависимости**:
```bash
# Find what depends on this component
jq '.components[] | .[] | select(.dependencies[]? == "subagent:old-agent") | {id, name}' registry.json
```

**2. Удалите из зависимых компонентов**:
```bash
# Update agents that depend on it
# Remove the dependency from their frontmatter
```

**3. Удалите компонент**:
```bash
rm .opencode/agent/subagents/old-agent.md
```

**4. Обновите registry**:
```bash
./scripts/registry/auto-detect-components.sh --auto-add
```

**5. Валидируйте**:
```bash
./scripts/registry/validate-registry.sh
```

---

## Диагностика

### Отсутствующие context-зависимости

**Симптом**:
```
/check-context-deps reports:
  opencoder: missing context:core/standards/code
```

**Исправление**:
```bash
# Option 1: Auto-fix
/check-context-deps --fix

# Option 2: Manual fix
# Edit .opencode/agent/core/opencoder.md
# Add to frontmatter:
dependencies:
  - context:core/standards/code

# Then update registry
./scripts/registry/auto-detect-components.sh --auto-add
```

### Зависимость не найдена в registry

**Симптом**:
```
⚠ Dependency not found in registry: context:core/standards/code
```

**Причины**:
1. Контекстный файл не существует
2. Контекстный файл существует, но отсутствует в registry
3. Неверный формат зависимости

**Исправление**:
```bash
# Check if file exists
ls -la .opencode/context/core/standards/code-quality.md

# If exists, add to registry
./scripts/registry/auto-detect-components.sh --auto-add

# If doesn't exist, remove dependency or create file
```

### Неиспользуемые контекстные файлы

**Симптом**:
```
/check-context-deps reports:
  Unused: context:core/standards/analysis (0 references)
```

**Исправление**:
```bash
# Option 1: Add to an agent that should use it
# Edit agent frontmatter to add dependency

# Option 2: Remove if truly unused
rm .opencode/context/core/standards/code-analysis.md
./scripts/registry/auto-detect-components.sh --auto-add
```

### Циклические зависимости

**Симптом**:
```
Agent A depends on Agent B
Agent B depends on Agent A
```

**Исправление**:
- Выполните рефакторинг и уберите циклическую зависимость
- Вынесите общую логику в третий компонент
- Используйте dependency injection

---

## Интеграция CI/CD

### Pre-commit hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Validating registry dependencies..."

# Check context dependencies
/check-context-deps || {
  echo "❌ Context dependency validation failed"
  echo "Run: /check-context-deps --fix"
  exit 1
}

# Validate registry
./scripts/registry/validate-registry.sh || {
  echo "❌ Registry validation failed"
  exit 1
}

echo "✅ Registry validation passed"
```

### GitHub Actions

```yaml
name: Validate Registry

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Validate registry
        run: ./scripts/registry/validate-registry.sh
      
      - name: Check context dependencies
        run: /check-context-deps
```

---

## Лучшие практики

### Для авторов компонентов

1. **Всегда объявляйте зависимости** во frontmatter
2. **Используйте `/check-context-deps`** перед коммитом
3. **Обновляйте registry** после добавления компонентов
4. **Валидируйте** перед push
5. **Документируйте**, зачем нужны зависимости

### Для мейнтейнеров

1. **Проверяйте зависимости** в PR
2. **Запускайте валидацию** в CI/CD
3. **Держите контекстные файлы** организованными и документированными
4. **Отслеживайте неиспользуемые** контекстные файлы
5. **Рефакторьте**, когда графы зависимостей усложняются

### Для CI/CD

1. **Падайте в build** при ошибках валидации
2. **Сообщайте** об отсутствующих зависимостях
3. **Отслеживайте** изменения зависимостей во времени
4. **Оповещайте** о циклических зависимостях
5. **Принудительно применяйте** стандарты объявления зависимостей

---

## Связанная документация

- **Руководство по registry**: `.opencode/context/openagents-repo/guides/updating-registry.md`
- **Концепции registry**: `.opencode/context/openagents-repo/core-concepts/registry.md`
- **Добавление агентов**: `.opencode/context/openagents-repo/guides/adding-agent-basics.md`
- **Справочник команд**: команда `/check-context-deps`

---

## Итоги

**Ключевые выводы**:
1. Объявляйте все зависимости во frontmatter (subagents, context files и т. д.)
2. Используйте `/check-context-deps`, чтобы находить отсутствующие context-зависимости
3. Валидируйте registry перед коммитами
4. Держите registry синхронизированным с изменениями компонентов
5. Соблюдайте формат зависимости: `type:id`

**Чек-лист качества**:
- [ ] У всех упомянутых контекстных файлов объявлены зависимости
- [ ] Все зависимости существуют в registry
- [ ] Нет неиспользуемых контекстных файлов (или задокументировано почему)
- [ ] Registry валидируется без ошибок
- [ ] Формат зависимостей консистентен

**Помните**: зависимости — это документация. Они помогают пользователям понять, что нужно компонентам, а системе — валидировать целостность.
