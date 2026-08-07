<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: диагностика частых проблем

**Цель**: руководство по устранению частых проблем

---

## Быстрая диагностика

```bash
# Check system health
./scripts/registry/validate-registry.sh
./scripts/validation/validate-test-suites.sh

# Check version consistency
cat VERSION && cat package.json | jq '.version'

# Test core agents
cd evals/framework && npm run eval:sdk -- --agent=core/openagent --pattern="smoke-test.yaml"
```

---

## Проблемы registry

### Валидация registry падает

**Симптомы**:
```
ERROR: Path does not exist: (example: .opencode/agent/core/missing.md)
```

**Диагностика**:
```bash
./scripts/registry/validate-registry.sh -v
```

**Решения**:
1. **Путь не существует**: удалите запись или создайте файл
2. **Дублирующийся ID**: переименуйте один компонент
3. **Неверная категория**: используйте допустимую category

**Исправление**:
```bash
# Re-run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add

# Validate
./scripts/registry/validate-registry.sh
```

---

### Компонент не в registry

**Симптомы**:
- Компонент не отображается в `./install.sh --list`
- Auto-detect не находит компонент

**Диагностика**:
```bash
# Check frontmatter
head -10 .opencode/agent/{category}/{agent}.md

# Dry run auto-detect
./scripts/registry/auto-detect-components.sh --dry-run
```

**Решения**:
1. **Отсутствует frontmatter**: добавьте frontmatter
2. **Невалидный YAML**: исправьте YAML syntax
3. **Неверное расположение**: переместите в правильный каталог

**Исправление**:
```bash
# Add frontmatter
cat > .opencode/agent/{category}/{agent}.md << 'EOF'
---
description: "Brief description"
category: "category"
type: "agent"
---

# Agent Content
EOF

# Re-run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add
```

---

## Ошибки тестов

### Нарушение approval gate

**Симптомы**:
```
✗ Approval Gate: FAIL
  Violation: Agent executed write tool without requesting approval
```

**Диагностика**:
```bash
# Run with debug
cd evals/framework
npm run eval:sdk -- --agent={agent} --pattern="{test}" --debug

# Check session
ls -lt .tmp/sessions/ | head -5
cat .tmp/sessions/{session-id}/session.json | jq
```

**Решение**:
Добавьте approval request в agent prompt:
```markdown
Before executing:
1. Present plan to user
2. Request approval
3. Execute after approval
```

---

### Нарушение загрузки контекста

**Симптомы**:
```
✗ Context Loading: FAIL
  Violation: Agent executed write tool without loading required context
```

**Диагностика**:
```bash
# Check what context was loaded
cat .tmp/sessions/{session-id}/events.json | jq '.[] | select(.type == "context_load")'
```

**Решение**:
Добавьте загрузку context в agent prompt:
```markdown
Before implementing:
1. Load core/standards/code-quality.md
2. Apply standards to implementation
```

---

### Нарушение использования инструментов

**Симптомы**:
```
✗ Tool Usage: FAIL
  Violation: Agent used bash tool for reading file instead of read tool
```

**Диагностика**:
```bash
# Check tool usage
cat .tmp/sessions/{session-id}/events.json | jq '.[] | select(.type == "tool_call")'
```

**Решение**:
Обновите агента, чтобы он использовал правильные tools:
- Используйте `read` вместо `bash cat`
- Используйте `list` вместо `bash ls`
- Используйте `grep` вместо `bash grep`

---

## Проблемы установки

### Install script падает

**Симптомы**:
```
ERROR: Failed to fetch registry
ERROR: Component not found
```

**Диагностика**:
```bash
# Check dependencies
which curl jq

# Test with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

**Решения**:
1. **Отсутствуют зависимости**: установите curl и jq
2. **Registry не найден**: проверьте, что registry.json существует
3. **Компонент не найден**: убедитесь, что компонент есть в registry

**Исправление**:
```bash
# Install dependencies (macOS)
brew install curl jq

# Install dependencies (Linux)
sudo apt-get install curl jq

# Test locally
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

---

### Обработка конфликтов

**Симптомы**:
```
File exists: .opencode/agent/core/openagent.md
```

**Решения**:
1. **Skip**: оставить существующий файл
2. **Overwrite**: заменить новым файлом
3. **Backup**: сделать backup существующего и установить новый

**Исправление**:
```bash
# Skip all collisions
./install.sh developer --skip-existing

# Overwrite all collisions
./install.sh developer --force

# Backup all collisions
./install.sh developer --backup
```

---

## Проблемы разрешения путей

### Агент не найден

**Симптомы**:
```
ERROR: Agent not found: development/frontend-specialist
```

**Диагностика**:
```bash
# Check file exists
ls -la .opencode/agent/subagents/development/frontend-specialist.md

# Check registry
cat registry.json | jq '.components.agents[] | select(.id == "frontend-specialist")'
```

**Решения**:
1. **Файл не существует**: создайте файл
2. **Неверный путь**: исправьте path в registry
3. **Нет в registry**: запустите auto-detect

**Исправление**:
```bash
# Re-run auto-detect
./scripts/registry/auto-detect-components.sh --auto-add

# Validate
./scripts/registry/validate-registry.sh
```

---

## Проблемы версий

### Несовпадение версий

**Симптомы**:
```
VERSION: 0.5.0
package.json: 0.4.0
registry.json: 0.5.0
```

**Диагностика**:
```bash
cat VERSION
cat package.json | jq '.version'
cat registry.json | jq '.version'
```

**Решение**:
Обновите всё до одной версии:
```bash
echo "0.5.0" > VERSION
jq '.version = "0.5.0"' package.json > tmp && mv tmp package.json
jq '.version = "0.5.0"' registry.json > tmp && mv tmp registry.json
```

---

## Проблемы CI/CD

### Сбой workflow

**Симптомы**:
- Registry validation падает в CI
- Тесты падают в CI, но проходят локально

**Диагностика**:
```bash
# Run same commands as CI
./scripts/registry/validate-registry.sh
./scripts/validation/validate-test-suites.sh
cd evals/framework && npm run eval:sdk
```

**Решения**:
1. **Registry невалиден**: исправьте registry
2. **Тесты падают**: исправьте тесты
3. **Зависимости отсутствуют**: обновите CI config

---

## Проблемы производительности

### Timeout тестов

**Симптомы**:
```
ERROR: Test timeout after 60000ms
```

**Решение**:
Увеличьте timeout в config.yaml:
```yaml
timeout: 120000  # 2 minutes
```

---

### Медленный auto-detect

**Симптомы**:
Auto-detect выполняется слишком долго

**Решение**:
Ограничьте scope:
```bash
# Only scan specific directory
./scripts/registry/auto-detect-components.sh --path .opencode/agent/development/
```

---

## Как получить помощь

### Проверьте логи

```bash
# Session logs
ls -lt .tmp/sessions/ | head -5
cat .tmp/sessions/{session-id}/session.json | jq

# Event timeline
cat .tmp/sessions/{session-id}/events.json | jq
```

### Запустите диагностику

```bash
# Full system check
./scripts/registry/validate-registry.sh -v
./scripts/validation/validate-test-suites.sh
cd evals/framework && npm run eval:sdk -- --agent=core/openagent
```

### Частые команды

```bash
# Validate everything
./scripts/registry/validate-registry.sh && \
./scripts/validation/validate-test-suites.sh && \
cd evals/framework && npm run eval:sdk

# Reset and rebuild
./scripts/registry/auto-detect-components.sh --auto-add --force
./scripts/registry/validate-registry.sh

# Test installation
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

---

## Связанные файлы

- **Руководство по тестированию**: `guides/testing-agent.md`
- **Руководство по registry**: `guides/updating-registry.md`
- **Концепции eval**: `core-concepts/evals.md`

---

**Последнее обновление**: 2025-12-10  
**Версия**: 0.5.0
