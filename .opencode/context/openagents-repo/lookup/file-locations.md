<!-- Context: openagents-repo/lookup | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Справочник: расположение файлов

**Назначение**: краткий справочник для поиска файлов

---

## Дерево директорий

```
opencode-agents/
├── .opencode/
│   ├── agent/
│   │   ├── core/                    # Core system agents
│   │   ├── development/             # Dev specialists
│   │   ├── content/                 # Content creators
│   │   ├── data/                    # Data analysts
│   │   ├── product/                 # Product managers (ready)
│   │   ├── learning/                # Educators (ready)
│   │   └── subagents/               # Delegated specialists
│   │       ├── code/                # Code-related
│   │       ├── core/                # Core workflows
│   │       ├── system-builder/      # System generation
│   │       └── utils/               # Utilities
│   ├── command/                     # Slash commands
│   ├── context/                     # Shared knowledge
│   │   ├── core/                    # Core standards & workflows
│   │   ├── development/             # Dev context
│   │   ├── content-creation/        # Content creation context
│   │   ├── data/                    # Data context
│   │   ├── product/                 # Product context
│   │   ├── learning/                # Learning context
│   │   └── openagents-repo/         # Repo-specific context
│   ├── prompts/                     # Model-specific variants
│   ├── tool/                        # Custom tools
│   └── plugin/                      # Plugins
├── evals/
│   ├── framework/                   # Eval framework (TypeScript)
│   │   ├── src/                     # Source code
│   │   ├── scripts/                 # Test utilities
│   │   └── docs/                    # Framework docs
│   └── agents/                      # Agent test suites
│       ├── core/                    # Core agent tests
│       ├── development/             # Dev agent tests
│       └── content/                 # Content agent tests
├── scripts/
│   ├── registry/                    # Registry management
│   ├── validation/                  # Validation tools
│   ├── testing/                     # Test utilities
│   ├── versioning/                  # Version management
│   ├── docs/                        # Doc tools
│   └── maintenance/                 # Maintenance
├── docs/                            # Documentation
│   ├── agents/                      # Agent docs
│   ├── contributing/                # Contribution guides
│   ├── features/                    # Feature docs
│   └── getting-started/             # User guides
├── registry.json                    # Component catalog
├── install.sh                       # Installer
├── VERSION                          # Current version
└── package.json                     # Node dependencies
```

---

## Где находится...?

| Компонент | Расположение |
|-----------|----------|
| **Core-агенты** | `.opencode/agent/core/` |
| **Агенты категорий** | `.opencode/agent/{category}/` |
| **Субагенты** | `.opencode/agent/subagents/` |
| **Команды** | `.opencode/command/` |
| **Контекстные файлы** | `.opencode/context/` |
| **Варианты промптов** | `.opencode/prompts/{category}/{agent}/` |
| **Инструменты** | `.opencode/tool/` |
| **Плагины** | `.opencode/plugin/` |
| **Тесты агентов** | `evals/agents/{category}/{agent}/` |
| **Eval-фреймворк** | `evals/framework/src/` |
| **Скрипты registry** | `scripts/registry/` |
| **Скрипты валидации** | `scripts/validation/` |
| **Документация** | `docs/` |
| **Registry** | `registry.json` |
| **Installer** | `install.sh` |
| **Версия** | `VERSION` |

---

## Куда добавить...?

| Что | Куда |
|------|-------|
| **Новый core-агент** | `.opencode/agent/core/{name}.md` |
| **Новый агент категории** | `.opencode/agent/{category}/{name}.md` |
| **Новый субагент** | `.opencode/agent/subagents/{category}/{name}.md` |
| **Новая команда** | `.opencode/command/{name}.md` |
| **Новый контекст** | `.opencode/context/{category}/{name}.md` |
| **Тесты агента** | `evals/agents/{category}/{agent}/tests/` |
| **Конфиг теста** | `evals/agents/{category}/{agent}/config/config.yaml` |
| **Документация** | `docs/{section}/{topic}.md` |
| **Скрипт** | `scripts/{purpose}/{name}.sh` |

---

## Конкретные пути файлов

### Core-файлы

```
registry.json                        # Component catalog
install.sh                           # Main installer
update.sh                            # Update script
VERSION                              # Current version (0.5.0)
package.json                         # Node dependencies
CHANGELOG.md                         # Release notes
README.md                            # Main documentation
```

### Core-агенты

```
.opencode/agent/core/openagent.md
.opencode/agent/core/opencoder.md
.opencode/agent/meta/system-builder.md
```

### Development-агенты

```
.opencode/agent/subagents/development/frontend-specialist.md
.opencode/agent/subagents/development/devops-specialist.md
```

### Content-агенты

```
.opencode/agent/content/copywriter.md
.opencode/agent/content/technical-writer.md
```

### Ключевые subagents

```
.opencode/agent/subagents/code/test-engineer.md
.opencode/agent/subagents/code/reviewer.md
.opencode/agent/subagents/code/coder-agent.md
.opencode/agent/subagents/core/task-manager.md
.opencode/agent/subagents/core/documentation.md
```

### Core-контекст

```
.opencode/context/core/standards/code-quality.md
.opencode/context/core/standards/documentation.md
.opencode/context/core/standards/test-coverage.md
.opencode/context/core/standards/security-patterns.md
.opencode/context/core/workflows/task-delegation-basics.md
.opencode/context/core/workflows/code-review.md
```

### Скрипты registry

```
scripts/registry/validate-registry.sh
scripts/registry/auto-detect-components.sh
scripts/registry/register-component.sh
scripts/registry/validate-component.sh
```

### Скрипты валидации

```
scripts/validation/validate-context-refs.sh
scripts/validation/validate-test-suites.sh
scripts/validation/setup-pre-commit-hook.sh
```

### Eval-фреймворк

```
evals/framework/src/sdk/              # Test runner
evals/framework/src/evaluators/       # Rule evaluators
evals/framework/src/collector/        # Session collection
evals/framework/src/types/            # TypeScript types
```

---

## Паттерны путей

### Агенты

```
.opencode/agent/{category}/{agent-name}.md
```

**Примеры**:
- `.opencode/agent/subagents/development/frontend-specialist.md`
- `.opencode/agent/subagents/code/test-engineer.md`

### Контекст

```
.opencode/context/{category}/{topic}.md
```

**Примеры**:
- `.opencode/context/core/standards/code-quality.md`
- `.opencode/context/ui/web/react-patterns.md`
- `.opencode/context/content-creation/principles/copywriting-frameworks.md`

### Тесты

```
evals/agents/{category}/{agent-name}/
├── config/config.yaml
└── tests/{test-name}.yaml
```

**Примеры**:
- `evals/agents/core/openagent/tests/smoke-test.yaml`
- `evals/agents/development/frontend-specialist/tests/approval-gate.yaml`

### Скрипты

```
scripts/{purpose}/{action}-{target}.sh
```

**Примеры**:
- `scripts/registry/validate-registry.sh`
- `scripts/validation/validate-test-suites.sh`
- `scripts/versioning/bump-version.sh`

---

## Соглашения об именовании

### Файлы

- **Агенты**: `{name}.md` или `{domain}-specialist.md`
- **Контекст**: `{topic}.md`
- **Тесты**: `{test-name}.yaml`
- **Скрипты**: `{action}-{target}.sh`
- **Документация**: `{topic}.md`

### Директории

- **Категории**: lowercase, singular (например, `development`, `content`)
- **Назначения**: lowercase, descriptive (например, `registry`, `validation`)

---

## Быстрый поиск

### Найти файл агента

```bash
# By name
find .opencode/agent -name "{agent-name}.md"

# By category
ls .opencode/agent/{category}/

# All agents
find .opencode/agent -name "*.md" -not -path "*/subagents/*"
```

### Найти файл теста

```bash
# By agent
ls evals/agents/{category}/{agent}/tests/

# All tests
find evals/agents -name "*.yaml"
```

### Найти контекстный файл

```bash
# By category
ls .opencode/context/{category}/

# All context
find .opencode/context -name "*.md"
```

### Найти скрипт

```bash
# By purpose
ls scripts/{purpose}/

# All scripts
find scripts -name "*.sh"
```

---

## Связанные файлы

- **Быстрый старт**: `quick-start.md`
- **Категории**: `core-concepts/categories.md`
- **Команды**: `lookup/commands.md`

---

**Последнее обновление**: 2025-12-10  
**Версия**: 0.5.0
