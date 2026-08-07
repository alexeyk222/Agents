<!-- Context: openagents-repo/lookup | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Справочник: команды

**Назначение**: краткий справочник частых команд

---

## Команды registry

### Валидировать registry

```bash
# Basic validation
./scripts/registry/validate-registry.sh

# Verbose output
./scripts/registry/validate-registry.sh -v
```

### Auto-detect компонентов

```bash
# Dry run (see what would change)
./scripts/registry/auto-detect-components.sh --dry-run

# Add new components
./scripts/registry/auto-detect-components.sh --auto-add

# Force update existing
./scripts/registry/auto-detect-components.sh --auto-add --force
```

### Валидировать структуру компонента

```bash
./scripts/registry/validate-component.sh
```

---

## Команды тестирования

### Запуск тестов

```bash
# Single test
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent} --pattern="{test}.yaml"

# All tests for agent
npm run eval:sdk -- --agent={category}/{agent}

# All tests (all agents)
npm run eval:sdk

# With debug
npm run eval:sdk -- --agent={agent} --debug
```

### Валидировать test suites

```bash
./scripts/validation/validate-test-suites.sh
```

---

## Команды установки

### Установить компоненты

```bash
# List available components
./install.sh --list

# Install profile
./install.sh {profile}
# Profiles: essential, developer, business

# Install specific component
./install.sh --component agent:{agent-name}

# Test with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

### Обработка конфликтов

```bash
# Skip existing files
./install.sh developer --skip-existing

# Overwrite all
./install.sh developer --force

# Backup existing
./install.sh developer --backup
```

---

## Команды версий

### Проверить версию

```bash
# Check all version files
cat VERSION
cat package.json | jq '.version'
cat registry.json | jq '.version'
```

### Обновить версию

```bash
# Update VERSION
echo "0.X.Y" > VERSION

# Update package.json
jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json

# Update registry.json
jq '.version = "0.X.Y"' registry.json > tmp && mv tmp registry.json
```

### Скрипт повышения версии

```bash
./scripts/versioning/bump-version.sh 0.X.Y
```

---

## Git-команды

### Создать релиз

```bash
# Commit version changes
git add VERSION package.json CHANGELOG.md
git commit -m "chore: bump version to 0.X.Y"

# Create tag
git tag -a v0.X.Y -m "Release v0.X.Y"

# Push
git push origin main
git push origin v0.X.Y
```

### Создать GitHub release

```bash
# Via GitHub CLI
gh release create v0.X.Y \
  --title "v0.X.Y" \
  --notes "See CHANGELOG.md for details"
```

---

## Команды валидации

### Полная валидация

```bash
# Validate everything
./scripts/registry/validate-registry.sh && \
./scripts/validation/validate-test-suites.sh && \
cd evals/framework && npm run eval:sdk
```

### Проверить context-зависимости

```bash
# Analyze all agents
/check-context-deps

# Analyze specific agent
/check-context-deps contextscout

# Auto-fix missing dependencies
/check-context-deps --fix
```

### Валидировать context references

```bash
./scripts/validation/validate-context-refs.sh
```

### Настроить pre-commit hook

```bash
./scripts/validation/setup-pre-commit-hook.sh
```

---

## Команды разработки

### Запустить demo

```bash
./scripts/development/demo.sh
```

### Запустить dashboard

```bash
./scripts/development/dashboard.sh
```

---

## Команды обслуживания

### Очистить устаревшие sessions

```bash
./scripts/maintenance/cleanup-stale-sessions.sh
```

### Удалить

```bash
./scripts/maintenance/uninstall.sh
```

---

## Команды отладки

### Проверить sessions

```bash
# List recent sessions
ls -lt .tmp/sessions/ | head -5

# View session
cat .tmp/sessions/{session-id}/session.json | jq

# View events
cat .tmp/sessions/{session-id}/events.json | jq
```

### Проверить context-логи

```bash
# Check session cache
./scripts/check-context-logs/check-session-cache.sh

# Count agent tokens
./scripts/check-context-logs/count-agent-tokens.sh

# Show API payload
./scripts/check-context-logs/show-api-payload.sh

# Show cached data
./scripts/check-context-logs/show-cached-data.sh
```

---

## Быстрые процессы

### Добавление нового агента

```bash
# 1. Create agent file
touch .opencode/agent/{category}/{agent-name}.md
# (Add frontmatter and content)

# 2. Create test structure
mkdir -p evals/agents/{category}/{agent-name}/{config,tests}
# (Create config.yaml and smoke-test.yaml)

# 3. Update registry
./scripts/registry/auto-detect-components.sh --auto-add

# 4. Validate
./scripts/registry/validate-registry.sh
cd evals/framework && npm run eval:sdk -- --agent={category}/{agent-name}
```

### Тестирование агента

```bash
# 1. Run smoke test
cd evals/framework
npm run eval:sdk -- --agent={category}/{agent} --pattern="smoke-test.yaml"

# 2. If fails, debug
npm run eval:sdk -- --agent={category}/{agent} --debug

# 3. Check session
ls -lt .tmp/sessions/ | head -1
cat .tmp/sessions/{session-id}/session.json | jq
```

### Создание релиза

```bash
# 1. Update version
echo "0.X.Y" > VERSION
jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json

# 2. Update CHANGELOG
# (Edit CHANGELOG.md)

# 3. Commit and tag
git add VERSION package.json CHANGELOG.md
git commit -m "chore: bump version to 0.X.Y"
git tag -a v0.X.Y -m "Release v0.X.Y"

# 4. Push
git push origin main
git push origin v0.X.Y

# 5. Create GitHub release
gh release create v0.X.Y --title "v0.X.Y" --notes "See CHANGELOG.md"
```

---

## Частые паттерны

### Найти файлы

```bash
# Find agent
find .opencode/agent -name "{agent-name}.md"

# Find tests
find evals/agents -name "*.yaml"

# Find context
find .opencode/context -name "*.md"

# Find scripts
find scripts -name "*.sh"
```

### Проверить registry

```bash
# List all agents
cat registry.json | jq '.components.agents[].id'

# Check specific component
cat registry.json | jq '.components.agents[] | select(.id == "{agent-name}")'

# Count components
cat registry.json | jq '.components.agents | length'
```

### Тестировать локально

```bash
# Test with local registry
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list

# Install locally
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh developer
```

---

## NPM-команды (eval-фреймворк)

```bash
cd evals/framework

# Install dependencies
npm install

# Run tests
npm test

# Run eval SDK
npm run eval:sdk

# Build
npm run build

# Lint
npm run lint
```

---

## Связанные файлы

- **Быстрый старт**: `quick-start.md`
- **Расположение файлов**: `lookup/file-locations.md`
- **Руководства**: `guides/`

---

**Последнее обновление**: 2025-12-10  
**Версия**: 0.5.0
