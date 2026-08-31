Данный форк создан для быстрого погружения в архитектуру ИИ-агентов без языкового барьера. Все термины переведены, что позволяет сфокусироваться на логике LLM-систем. Репозиторий служит наглядным примером harness-упряжки: изучите его, чтобы написать собственный, более эффективный инструмент с чистого листа.

# OpenAgents Control (OAC)

OAC — конфигурационный слой для [OpenCode](https://opencode.ai): набор Markdown-промптов, специализированных агентов, команд и контекстных файлов. Его задача — сделать работу AI-агента предсказуемой: сначала понять проект и его правила, затем предложить план, получить подтверждение и только после этого выполнять изменения.

Проект удобно использовать как локальную папку `.opencode/` внутри репозитория. Тогда командные правила и знания о проекте живут рядом с кодом, версионируются Git и доступны всей команде.

## Что даёт OAC

- **Контекст проекта.** Агент сначала загружает подходящие правила: стиль кода, тестирования, документации, безопасности и архитектуры.
- **Разделение ролей.** Основной агент передаёт специализированные части задачи агентам для поиска контекста, реализации, тестирования, ревью и сборки.
- **Контроль изменений.** В промптах предусмотрен цикл «анализ → план → подтверждение → выполнение → проверка».
- **Редактируемые правила.** Поведение агентов описано обычными `.md`-файлами. Их можно адаптировать под процессы команды без разработки плагина.
- **Минимальный контекст.** База знаний организована по принципу MVI: агент подгружает только файлы, нужные для текущей задачи.
- **Honcho.** Интеграция с межсессионной памятью. https://honcho.dev/

## Как это работает

```text
Запрос разработчика
        ↓
ContextScout находит правила и примеры проекта
        ↓
Основной агент формирует план
        ↓
Подтверждение пользователя
        ↓
Реализация и делегирование специалистам
        ↓
Тесты / сборка / ревью
        ↓
Результат и краткий отчёт
```

## Быстрый старт

### 1. Подготовьте окружение

Нужны установленный [OpenCode CLI](https://opencode.ai/docs), Git и Node.js. Для встроенного CLI управления задачами также нужен `npx ts-node` (при первом запуске `npx` может предложить его скачать).

Разместите эту папку в корне целевого проекта:

```text
my-project/
├── .opencode/       # этот репозиторий
├── src/
└── package.json
```

Установите npm-зависимость, если она ещё не установлена:

```bash
cd .opencode
npm install
```

### 2. Запустите агента

Из корня проекта:

```bash
opencode --agent OpenAgent
```

`OpenAgent` подходит для вопросов, небольших задач и знакомства с системой. Для сложной разработки, проектирования или рефакторинга используйте:

```bash
opencode --agent OpenCoder
```

Пример запроса:

```text
Добавь endpoint профиля пользователя. Сначала изучи существующие API-паттерны,
предложи план и жди моего подтверждения перед изменением файлов.
```

### 3. Добавьте знания о своём проекте

В сессии OpenCode запустите:

```text
/add-context
```

Команда собирает стек, примеры API и компонентов, соглашения по именованию, правила качества и требования безопасности. Результат сохраняется в `context/project-intelligence/` и становится доступен агентам в следующих задачах.

## Основные агенты

| Агент | Когда использовать | Роль |
|---|---|---|
| `OpenCoder` | Новая фича, архитектура, многофайловый рефакторинг | Координатор разработки с обязательными проверками. |
| `ContextScout` | Перед новой задачей | Находит подходящие локальные стандарты и примеры. |
| `ExternalScout` | Внешняя библиотека или API | Ищет актуальную внешнюю документацию. |
| `TaskManager` | Большая фича с зависимостями | Делит работу на атомарные подзадачи. |
| `ScientificAgent` | Научный анализ, ML, статистика, базы, cheminformatics, симуляции и публикации | Выбирает минимальный набор scientific skills и выполняет воспроизводимый workflow. |
| `CoderAgent` | Реализация утверждённой части работы | Пишет код в заданных границах. |
| `TestEngineer` | Проверка поведения | Создаёт и запускает тесты. |
| `CodeReviewer` | Контроль качества и рисков | Делает ревью без изменения кода. |
| `BuildAgent` | Финальная техническая проверка | Выполняет type-check и сборку, только сообщает результат. |
| `DocWriter` | Документация | Создаёт и поддерживает документацию. |

Промпты и права агентов находятся в [`agent/`](agent/). Главные агенты могут делегировать работу только разрешённым специалистам.

## Научный профиль

`ScientificAgent` использует 87 skills, vendored непосредственно в
[`skills/`](.opencode/skills/): ML/deep learning, анализ и методология, научная
коммуникация, cheminformatics/drug discovery, анализ и визуализация данных,
научные базы, документы, инженерные симуляции и research methodology/grants.
Соседний checkout `scientific-agent-skills/` для работы OAC не требуется.

```text
OpenCoder → scientific navigation → ScientificAgent → 1 основной + до 2 вспомогательных skills
```

Состав профиля и закреплённая версия upstream находятся в
[`config/scientific-skills.json`](.opencode/config/scientific-skills.json), а OpenCode
подключает только эти каталоги через [`opencode.json`](.opencode/opencode.json). Главный
агент не загружает научные skills сам: чисто научную работу он делегирует
`ScientificAgent`, а mixed-задачи делит через `TaskManager` между научными и
программными подзадачами.

Полностью локальные вычисления не требуют отдельного согласования. Контроль
строится по типу действия (`local`, `network-read`, `external-write`, `hardware`),
без классификации локальных данных. Девять skills, способных инициировать более
широкий research/publishing workflow, отмечены `review_required` и требуют
подтверждения при загрузке. Vendored skills считаются read-only; результаты
создаются в рабочем проекте или `.tmp/scientific-runs/`. Manifest сохраняет
upstream repository, version и commit для воспроизводимого обновления.
Лицензия коллекции сохранена в
[`skills/SCIENTIFIC-AGENT-SKILLS-LICENSE.md`](.opencode/skills/SCIENTIFIC-AGENT-SKILLS-LICENSE.md);
у отдельных skills могут быть собственные условия в `SKILL.md` или `LICENSE*`.

Проверить профиль после обновления vendored-копий или manifest:

```bash
python3 .opencode/scripts/validate-scientific-integration.py
```

## Проектные прикладные skills

Три project-local skill находятся рядом с vendored-профилем, но учитываются
отдельно в [`.opencode/config/project-skills.json`](.opencode/config/project-skills.json):

- `jupyter-notebook` — создание и проверка `.ipynb`, а также ограниченный
  безопасный workflow для JupyterHub REST API;
- `sql-queries` — написание, проверка и оптимизация SQL с учётом диалекта,
  схемы, cardinality и границ live-мутаций;
- `pdf-authoring` — создание PDF и обязательная визуальная проверка рендера.

Они явно разрешены только `OpenCoder`, `CoderAgent` и `ScientificAgent`.
`pdf-authoring` отвечает за создание итогового документа, а scientific skill
`pdf` — за extraction, OCR, forms и преобразование существующих PDF.

## Команды

| Команда | Назначение |
|---|---|
| `/add-context` | Собрать и сохранить паттерны конкретного проекта. |
| `/context` | Извлечь, упорядочить или обновить базу контекста. |
| `/analyze-patterns` | Найти повторения, похожие реализации и возможности рефакторинга. |
| `/clean` | Очистить код: форматирование, импорты, lint и типы. |
| `/optimize` | Проанализировать производительность и безопасность. |
| `/test` | Запустить pipeline типов, линтера и тестов. |
| `/commit` | Подготовить conventional commit. |
| `/validate-repo` | Проверить согласованность файлов OAC. |
| `/check-context-deps` | Проверить связи агентов с контекстными файлами. |
| `/validate-scientific-skills` | Проверить manifest, пути, permissions, navigation и pinned upstream научного профиля. |

Полные инструкции команд находятся в [`command/`](command/).

## Структура

```text
.opencode/
  ├── agent/                              # Промпты и права AI-агентов
  │   ├── core/
  │   │   └── opencoder.md                # Главный агент для сложной разработки,
  │   │                                   # архитектуры и многофайловых изменений.
  │   │
  │   └── subagents/                      # Специалисты, которым главные агенты делегируют работу
  │       ├── core/
  │       │   ├── contextscout.md         # Находит релевантный контекст и стандарты проекта.
  │       │   ├── externalscout.md        # Ищет актуальную документацию внешних библиотек.
  │       │   ├── task-manager.md         # Декомпозирует большую задачу на подзадачи и зависимости.
  │       │   └── documentation.md        # Создаёт и обновляет техническую документацию.
  │       ├── code/
  │       │   ├── coder-agent.md          # Реализует код по утверждённому плану.
  │       │   ├── test-engineer.md        # Пишет и проверяет тесты.
  │       │   ├── reviewer.md             # Выполняет code review без изменения кода.
  │       │   └── build-agent.md          # Запускает type-check и build, только сообщает ошибки.
  │       ├── development/
  │       │   ├── frontend-specialist.md  # Специалист по frontend/UI-задачам.
  │       │   └── devops-specialist.md    # Специалист по CI/CD, контейнерам и инфраструктуре.
  │       ├── science/
  │       │   └── scientific-agent.md     # Исполняет выбранные scientific skills.
  │       └── system-builder/
  │           └── context-organizer.md    # Организует, сжимает и поддерживает базу контекста.
  │
  ├── command/                            # Slash-команды для типовых операций
  │   ├── add-context.md                  # Интерактивно собирает паттерны проекта
  │   │                                   # и формирует Project Intelligence.
  │   ├── analyze-patterns.md             # Ищет повторяющиеся паттерны, дублирование,
  │   │                                   # похожие реализации и точки рефакторинга.
  │   ├── clean.md                        # Описывает очистку кода: форматирование,
  │   │                                   # импорты, lint, типы, debug-код.
  │   ├── commit.md                       # Создаёт conventional commit с emoji.
  │   ├── context.md                      # Управляет знаниями: harvest, extract,
  │   │                                   # organize и update контекстных файлов.
  │   ├── optimize.md                     # Анализирует производительность и безопасность.
  │   ├── test.md                         # Запускает типы, lint и тесты.
  │   ├── validate-repo.md                # Проверяет согласованность компонентов,
  │   │                                   # документации и связей в OAC.
  │   ├── validate-scientific-skills.md   # Проверяет интеграцию научного профиля.
  │   └── openagents/
  │       └── check-context-deps.md       # Ищет сломанные/необъявленные зависимости
  │                                       # между агентами и контекстными файлами.
  │
  ├── config/
  │   ├── agent-metadata.json             # Центральный реестр метаданных агентов.
  │   ├── project-skills.json             # Три общих project-local support skills.
  │   ├── scientific-skills.json          # Manifest 87 skills, категории и execution modes.
  │   └── scientific-skill-requirements.toml # Изолированные runtime-зависимости skills.
  │
  ├── context/                            # База знаний, загружаемая агентами по необходимости
  │   ├── navigation.md                   # Главная карта всей базы контекста.
  │   │
  │   ├── core/                           # Общие правила работы любых агентов
  │   │   ├── navigation.md               # Навигация по базовому контексту.
  │   │   ├── essential-patterns.md       # Общие инженерные паттерны.
  │   │   ├── visual-development.md       # Базовые правила визуальной разработки.
  │   │   ├── config/
  │   │   │   ├── paths.json              # Локальный/глобальный путь к контексту.
  │   │   │   └── navigation.md           # Описание конфигурации.
  │   │   ├── standards/                  # Нормы качества и соглашения
  │   │   │   ├── code-quality.md         # Качество кода.
  │   │   │   ├── code-analysis.md        # Анализ существующего кода.
  │   │   │   ├── test-coverage.md        # Тестирование и покрытие.
  │   │   │   ├── documentation.md        # Стиль и структура документации.
  │   │   │   ├── security-patterns.md    # Базовые практики безопасности.
  │   │   │   ├── typescript.md           # Стандарты TypeScript.
  │   │   │   ├── csharp.md               # Стандарты C#.
  │   │   │   ├── csharp-project-structure.md # Структура C#-проекта.
  │   │   │   ├── project-intelligence.md # Как хранить знания о проекте.
  │   │   │   └── project-intelligence-management.md # Их сопровождение.
  │   │   ├── workflows/                  # Регламент выполнения задач
  │   │   │   ├── code-review.md, review.md      # Процесс ревью.
  │   │   │   ├── feature-breakdown.md           # Декомпозиция фичи.
  │   │   │   ├── delegation.md,
  │   │   │   │   task-delegation-*.md           # Делегирование и кэширование контекста.
  │   │   │   ├── component-planning.md          # Планирование компонентов.
  │   │   │   ├── session-management.md          # Продолжение и завершение сессий.
  │   │   │   ├── external-context-*.md,
  │   │   │   │   external-libraries-*.md        # Работа с внешними источниками и пакетами.
  │   │   │   └── design-iteration-*.md          # Цикл UI-дизайна:
  │   │   │                                       # layout → theme → animation → implementation.
  │   │   ├── task-management/             # Формат и жизненный цикл задач
  │   │   │   ├── standards/task-schema.md # JSON-схема задачи/подзадачи.
  │   │   │   ├── guides/*.md              # Декомпозиция и ведение задач.
  │   │   │   └── lookup/task-commands.md  # Справочник Task CLI.
  │   │   ├── system/                      # Правила разрешения путей и загрузки контекста.
  │   │   └── context-system/              # «Операционная система» базы знаний:
  │   │       ├── standards/*.md           # MVI, frontmatter, структура, шаблоны.
  │   │       ├── guides/*.md              # Создание, сжатие и навигация контекста.
  │   │       ├── operations/*.md          # Extract, Harvest, Organize, Update, Migrate, Error.
  │   │       ├── examples/*.md            # Примеры навигационных файлов.
  │   │       └── CHANGELOG.md             # История изменений системы.
  │   │
  │   ├── development/                     # Знания по разработке
  │   │   ├── navigation.md и *-navigation.md # Маршруты для backend, frontend,
  │   │   │                                    # fullstack, data, infrastructure, UI, интеграций.
  │   │   ├── principles/
  │   │   │   ├── api-design.md            # Проектирование API.
  │   │   │   └── clean-code.md            # Clean Code.
  │   │   ├── frontend/when-to-delegate.md # Когда передавать задачу frontend-специалисту.
  │   │   └── ai/mastra-ai/                # Справочник интеграции Mastra:
  │   │       ├── concepts/*.md            # Agents, Tools, Workflows, Storage, Evals.
  │   │       ├── guides/*.md              # Сборка, тестирование, структура workflow.
  │   │       ├── examples/*.md            # Пример document workflow.
  │   │       ├── errors/*.md              # Ошибки Mastra.
  │   │       └── lookup/*.md              # Конфигурация Mastra.
  │   │
  │   ├── scientific/                      # Маршрутизация по девяти научным категориям.
  │   │   └── */navigation.md              # Индексы skills без загрузки их полного текста.
  │   │
  │   ├── ui/                              # UI/UX-контекст
  │   │   ├── terminal/navigation.md       # Терминальный интерфейс.
  │   │   └── web/                         # Web UI:
  │   │       ├── react-patterns.md, ui-styling-standards.md, design-systems.md
  │   │       ├── animation-*.md           # Анимации компонентов, форм, загрузок и чата.
  │   │       └── design/                  # Scrollytelling и scroll-анимации:
  │   │           ├── concepts/
  │   │           ├── guides/
  │   │           ├── examples/
  │   │           └── lookup/
  │   │
  │   ├── project-intelligence/            # Память о конкретном продукте:
  │   │   ├── business-domain.md           # Бизнес-домен.
  │   │   ├── technical-domain.md          # Технологии и инженерные соглашения.
  │   │   ├── business-tech-bridge.md      # Связь требований бизнеса с реализацией.
  │   │   ├── decisions-log.md             # Архитектурные решения.
  │   │   └── living-notes.md              # Живые рабочие заметки.
  │   │
  │   └── openagents-repo/                 # Документация именно по развитию OAC
  │       ├── quick-start.md               # Быстрый старт.
  │       ├── core-concepts/*.md           # Агенты, метаданные, registry, evals, категории.
  │       ├── guides/*.md                  # Добавление агента/skill, тестирование,
  │       │                                 # релизы, npm, GitHub Issues, отладка.
  │       ├── lookup/*.md                  # Команды, файловая карта и тестовые команды.
  │       ├── examples/*.md                # Примеры context bundle и промптов субагентов.
  │       ├── blueprints/, templates/      # Шаблоны context bundle.
  │       ├── errors/                      # Ошибки прав инструментов.
  │       ├── quality/                     # Проверка зависимостей registry.
  │       └── plugins/context/             # Архитектура плагинов OpenCode:
  │                                       # lifecycle, events, tools, skills, agents.
  │
  ├── skills/                              # Исполняемые навыки для агентов
  │   ├── context7/                        # Получение актуальной документации библиотек:
  │   │   ├── SKILL.md                     # Инструкция по API Context7.
  │   │   ├── README.md                    # Быстрый сценарий применения.
  │   │   ├── library-registry.md          # Поддерживаемые библиотеки и шаблоны запросов.
  │   │   └── navigation.md                # Навигация по skill.
  │   ├── task-management/                 # Реальная CLI-реализация управления задачами:
  │       ├── SKILL.md                     # Контракт skill и JSON-модель задач.
  │       ├── router.sh                    # Bash-точка входа.
  │       └── scripts/task-cli.ts          # Команды status/next/parallel/deps/
  │                                       # blocked/complete/validate.
  │   ├── {87 scientific skills}/         # Vendored profile для ScientificAgent.
  │   └── SCIENTIFIC-AGENT-SKILLS-LICENSE.md # Лицензия исходной коллекции.
  │
  ├── tool/
  │   └── env/index.ts                     # TypeScript-утилита безопасной загрузки
  │                                       # переменных окружения из нескольких .env.
  │
  ├── scripts/
  │   └── validate-scientific-integration.py # Read-only проверка scientific + support профилей.
  ├── opencode.json                       # Project config и точные vendored skill paths.
  ├── README.md                            # Позиционирование OAC, установка и сценарии работы.
  ├── node_modules/                        # Установленные внешние зависимости; в презентацию
  │                                       # обычно не включают.
  └── env.example                          # Шаблон переменных Telegram/Gemini/MiniMax.

```

Подробная карта базы знаний начинается с [`context/navigation.md`](context/navigation.md). Для задач по коду ключевой файл — [`context/core/standards/code-quality.md`](context/core/standards/code-quality.md).

## Работа с контекстом

Контекст разрешается по принципу local-first:

1. Сначала `ContextScout` ищет `.opencode/context/core/navigation.md` внутри проекта.
2. Если локальной базы нет, для общих правил может использоваться глобальный путь `~/.config/opencode/context`.
3. `project-intelligence/` остаётся локальным: это знания именно вашего проекта.

Файл [`context/core/config/paths.json`](context/core/config/paths.json) позволяет изменить эти пути.

### Что стоит добавить первым

- используемый стек и версии ключевых библиотек;
- пример API endpoint и формат обработки ошибок;
- пример UI-компонента;
- соглашения по именованию файлов, сущностей и веток;
- правила тестирования и требования безопасности;
- принятые архитектурные решения.

Чем точнее эти сведения, тем меньше агенту приходится делать предположений.

## Управление крупными задачами

`TaskManager` сохраняет декомпозицию в `.tmp/tasks/` целевого проекта. Встроенный CLI показывает прогресс, готовые к запуску подзадачи и блокировки:

```bash
# Запускать из корня целевого проекта
bash .opencode/skills/task-management/router.sh status
bash .opencode/skills/task-management/router.sh next
bash .opencode/skills/task-management/router.sh blocked
bash .opencode/skills/task-management/router.sh validate
```

Формат файлов задач описан в [`context/core/task-management/standards/task-schema.md`](context/core/task-management/standards/task-schema.md).

## Адаптация под команду

1. Дополните `context/project-intelligence/` правилами проекта.
2. При необходимости измените Markdown-промпты в `agent/`.
3. Добавьте свои slash-команды в `command/`.
4. Проверьте связи между компонентами через `/check-context-deps`.
5. Закоммитьте `.opencode/` вместе с кодом проекта.

Не храните секреты в контексте или в Git. Для ключей используйте `.env`; пример имён переменных находится в [`env.example`](env.example).


## Лицензия

Исходная основа OAC распространяется по лицензии MIT. Перед публикацией форка добавьте в репозиторий собственный файл `LICENSE` с выбранными условиями использования.

## Иерархия Scientific Agent Skills

Дерево ниже показывает полный vendored-профиль `ScientificAgent`: какой skill
выбирать и зачем он нужен. Пометка `[review]` означает подтверждение перед
загрузкой skill. Обычно агент использует один основной и не более двух
вспомогательных skills.

```text
ScientificAgent (87 skills)
├── Machine Learning & Deep Learning (18)
│   ├── aeon — временные ряды: classification, regression, clustering и forecasting
│   ├── cirq — создание и симуляция квантовых схем в экосистеме Cirq
│   ├── pufferlib — высокопроизводительное reinforcement learning и vectorized environments
│   ├── pymc — Bayesian-модели, MCMC и probabilistic inference
│   ├── pymoo — многокритериальная оптимизация и Pareto-поиск
│   ├── pytorch-lightning — структурированное обучение и масштабирование PyTorch-моделей
│   ├── pennylane — differentiable quantum computing и quantum ML
│   ├── qiskit — квантовые схемы и вычисления в экосистеме IBM
│   ├── qutip — динамика открытых квантовых систем
│   ├── scikit-learn — классический ML, preprocessing, pipelines и evaluation
│   ├── scikit-survival — survival analysis с censored data
│   ├── shap — объяснение предсказаний и feature attribution
│   ├── stable-baselines3 — готовые алгоритмы reinforcement learning
│   ├── statsmodels — статистические модели, econometrics и time series
│   ├── timesfm-forecasting — прогнозирование временных рядов моделью TimesFM
│   ├── torch-geometric — graph neural networks на PyTorch Geometric
│   ├── transformers — transformer-модели, tokenizers, inference и fine-tuning
│   └── umap-learn — нелинейное снижение размерности и визуализация embeddings
├── Analysis & Scientific Methodology (12)
│   ├── experimental-design — планирование экспериментов, randomization и factorial design
│   ├── exploratory-data-analysis — первичное исследование данных и поиск проблем качества
│   ├── hypothesis-generation — формирование проверяемых научных гипотез
│   ├── hypogenic — автоматизированная генерация и оценка гипотез
│   ├── literature-review [review] — систематический поиск и evidence synthesis
│   ├── peer-review — структурированное рецензирование рукописей
│   ├── scientific-brainstorming — поиск исследовательских идей и направлений
│   ├── scientific-critical-thinking — проверка аргументов, допущений и причинности
│   ├── scientific-visualization — проектирование корректных научных графиков
│   ├── scientific-writing — подготовка manuscripts и научных отчётов
│   ├── statistical-analysis — выбор тестов, диагностика и интерпретация статистики
│   └── statistical-power — power analysis и расчёт размера выборки
├── Scientific Communication & Publishing (11)
│   ├── bgpt-paper-search — поиск научных публикаций и релевантных источников
│   ├── pyzotero — программная работа с библиотеками Zotero
│   ├── citation-management [review] — поиск, проверка и форматирование citations/BibTeX
│   ├── generate-image — генерация иллюстраций через поддерживаемые image APIs
│   ├── infographics [review] — создание научных инфографик
│   ├── latex-posters [review] — подготовка академических posters в LaTeX
│   ├── market-research-reports — evidence-based market research reports
│   ├── pptx-posters — создание научных posters в PowerPoint
│   ├── scientific-schematics [review] — научные схемы и объясняющие диаграммы
│   ├── scientific-slides [review] — исследовательские презентации и slide decks
│   └── venue-templates — адаптация материалов под journal, conference или grant venue
├── Cheminformatics & Drug Discovery (9)
│   ├── datamol — стандартизация молекул и удобные RDKit workflows
│   ├── deepchem — machine learning для chemistry и biology
│   ├── diffdock — предсказание molecular docking poses
│   ├── medchem — medicinal chemistry filters и compound analysis
│   ├── molfeat — molecular descriptors и featurization
│   ├── pytdc — datasets, benchmarks и oracles Therapeutics Data Commons
│   ├── rdkit — molecular I/O, fingerprints, descriptors и substructure search
│   ├── rowan — managed computational chemistry calculations
│   └── torchdrug — graph ML для molecules, proteins и drug discovery
├── Data Analysis & Visualization (9)
│   ├── dask — distributed и out-of-core вычисления
│   ├── geomaster [review] — geospatial AI и обработка пространственных данных
│   ├── geopandas — анализ векторных геоданных
│   ├── matplotlib — базовые scientific plots и figure composition
│   ├── networkx — построение и анализ графов
│   ├── polars — быстрые DataFrame workflows
│   ├── seaborn — статистическая визуализация
│   ├── uncertainty-and-units — единицы, propagation и uncertainty budgets
│   └── vaex — анализ очень больших табличных datasets
├── Scientific Databases (9)
│   ├── database-lookup — единая маршрутизация запросов к публичным научным базам
│   ├── depmap — cancer dependencies и cell-line datasets
│   ├── imaging-data-commons — поиск публичных cancer imaging datasets
│   ├── primekg — работа с Precision Medicine Knowledge Graph
│   ├── ncats-arax — biomedical knowledge graph и Translator ARAX
│   ├── usfiscaldata — получение данных U.S. Treasury Fiscal Data
│   ├── ontology-term-resolution — нормализация ontology terms, IDs и CURIE
│   ├── pathogen-variant-surveillance — анализ актуальных pathogen variants и lineages
│   └── hugging-science — scientific models и datasets на Hugging Face
├── Document Processing & Conversion (7)
│   ├── docx — чтение, создание и проверка Word/OOXML
│   ├── markitdown — преобразование документов в Markdown
│   ├── liteparse — структурный parsing сложных документов
│   ├── markdown-mermaid-writing — Markdown-документы, Mermaid и шаблоны
│   ├── pdf — PDF extraction, OCR, forms, generation и conversion
│   ├── pptx — создание и проверка PowerPoint/OOXML
│   └── xlsx [review] — создание, изменение и проверка Excel/OOXML
├── Engineering & Simulation (6)
│   ├── lab-hardware-cad — CAD-проекты лабораторного оборудования
│   ├── matlab — MATLAB analysis, scripts и numerical workflows
│   ├── fluidsim — computational fluid dynamics simulations
│   ├── openpiv — particle image velocimetry analysis
│   ├── simpy — discrete-event simulation
│   └── sympy — символьная математика и аналитические вычисления
└── Research Methodology & Grants (6)
    ├── paperclip — поиск full-text biomedical и regulatory literature
    ├── paperzilla — организация paper projects и recommendations
    ├── paper-lookup — поиск публикаций через academic APIs
    ├── research-grants — подготовка proposals, specific aims и budgets
    ├── research-lookup [review] — manuscript-ready evidence workflow
    └── scholar-evaluation — качественная оценка научных работ и исследователей
```

### Project-local support skills

Эти три skill не входят в число 87 и доступны только `OpenCoder`, `CoderAgent`
и `ScientificAgent`:

```text
Project support (3)
├── jupyter-notebook — воспроизводимые .ipynb и защищённые JupyterHub workflows
├── sql-queries — корректный SQL, cardinality, EXPLAIN и контроль мутаций
└── pdf-authoring — создание PDF, проверка шрифтов и визуальный QA всех страниц
```
