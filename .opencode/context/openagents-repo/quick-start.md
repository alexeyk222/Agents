<!-- Context: openagents-repo/quick-start | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Репозиторий OpenAgents Control — быстрый старт

**Назначение**: сориентироваться в репозитории за 2 минуты

---

## Что это за репозиторий?

OpenAgents Control — фреймворк AI-агентов с:
- **агентами по категориям** (core, development, content, data, product, learning)
- **eval-фреймворком** для проверки поведения агентов
- **registry-системой** для распространения компонентов
- **системой установки** для быстрой настройки

---

## Ключевые концепции (загрузите сначала)

Перед работой с репозиторием разберитесь в 4 системах:

1. **Агенты** → загрузить: `core-concepts/agents.md`
   - Как устроены агенты
   - Система категорий
   - Варианты промптов
   - Субагенты vs агенты категорий

2. **Evals** → загрузить: `core-concepts/evals.md`
   - Как работает тестирование
   - Запуск тестов
   - Evaluators (правила проверки)
   - Сбор сессий

3. **Registry** → загрузить: `core-concepts/registry.md`
   - Как отслеживаются компоненты
   - Система auto-detect
   - Валидация
   - Система установки

4. **Категории** → загрузить: `core-concepts/categories.md`
   - Как устроена организация
   - Соглашения об именовании
   - Паттерны путей

---

## Мне нужно...

| Задача | Загрузите эти файлы |
|------|------------------|
| Добавить нового агента | `core-concepts/agents.md` + `guides/adding-agent.md` |
| Протестировать агента | `core-concepts/evals.md` + `guides/testing-agent.md` |
| Исправить registry | `core-concepts/registry.md` + `guides/updating-registry.md` |
| Отладить проблему | `guides/debugging.md` |
| Найти файлы | `lookup/file-locations.md` |
| Создать релиз | `guides/creating-release.md` |
| Написать контент или copy | `core-concepts/categories.md` + `../content-creation/principles/navigation.md` |
| Использовать помощников Claude Code | `core-concepts/agents.md` + `guides/adding-agent.md` + `../to-be-consumed/claude-code-docs/create-subagents.md` |

---

## Основные пути (топ-15)

```
.opencode/agent/core/                    # Core agents (openagent, opencoder)
.opencode/agent/{category}/              # Category agents
.opencode/agent/subagents/               # Subagents
evals/agents/{category}/{agent}/         # Agent tests
evals/framework/src/                     # Eval framework code
registry.json                            # Component catalog
install.sh                               # Installer
scripts/registry/validate-registry.sh    # Validate registry
scripts/registry/auto-detect-components.sh # Auto-detect components
scripts/validation/validate-test-suites.sh # Validate tests
.opencode/context/                       # Context files
.opencode/command/                       # Slash commands
docs/                                    # Documentation
VERSION                                  # Current version
package.json                             # Node dependencies
```

---

## Частые команды (топ-10)

```bash
# Add new agent (auto-detect)
./scripts/registry/auto-detect-components.sh --auto-add

# Validate registry
./scripts/registry/validate-registry.sh

# Test agent
cd evals/framework && npm run eval:sdk -- --agent={category}/{agent}

# Run smoke test
cd evals/framework && npm run eval:sdk -- --agent={agent} --pattern="smoke-test.yaml"

# Test with debug
cd evals/framework && npm run eval:sdk -- --agent={agent} --debug

# Validate test suites
./scripts/validation/validate-test-suites.sh

# Install locally (test)
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list

# Bump version
echo "0.X.Y" > VERSION && jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json

# Check version consistency
cat VERSION && cat package.json | jq '.version'

# Run full validation
./scripts/registry/validate-registry.sh && ./scripts/validation/validate-test-suites.sh
```

---

## Структура репозитория (кратко)

```
opencode-agents/
├── .opencode/
│   ├── agent/{category}/        # Agents by domain
│   │   ├── core/                # Core system agents
│   │   ├── development/         # Dev specialists
│   │   ├── content/             # Content creators
│   │   ├── data/                # Data analysts
│   │   ├── product/             # Product managers
│   │   ├── learning/            # Educators
│   │   └── subagents/           # Delegated specialists
│   ├── command/                 # Slash commands
│   └── context/                 # Shared knowledge
├── evals/
│   ├── agents/{category}/       # Test suites
│   └── framework/               # Eval framework
├── scripts/
│   ├── registry/                # Registry tools
│   └── validation/              # Validation tools
├── docs/                        # Documentation
├── registry.json                # Component catalog
└── install.sh                   # Installer
```

---

## Быстрая диагностика

| Проблема | Решение |
|---------|----------|
| Валидация registry падает | `./scripts/registry/auto-detect-components.sh --auto-add` |
| Тест падает | Загрузите `guides/debugging.md` |
| Не получается найти файл | Загрузите `lookup/file-locations.md` |
| Установка падает | Проверьте: `which curl jq` |
| Проблемы с разрешением путей | Проверьте `core-concepts/categories.md` |

---

## Следующие шаги

1. **Впервые здесь?** → прочитайте `core-concepts/agents.md`, `evals.md`, `registry.md`
2. **Добавляете агента?** → загрузите `guides/adding-agent.md`
3. **Тестируете?** → загрузите `guides/testing-agent.md`
4. **Нужны детали?** → загрузите конкретные файлы из `core-concepts/` или `guides/`

---

**Последнее обновление**: 2026-01-13  
**Версия**: 0.5.1
