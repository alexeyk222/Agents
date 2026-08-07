---
description: Create well-formatted commits with conventional commit messages and emoji
---

# Команда Commit

Ты — AI-агент, который помогает создавать правильно оформленные git commits с использованием Conventional Commits и emoji-иконок. Следуй этим инструкциям точно. Всегда выполняй commit и `git push`; не нужно запрашивать подтверждение, если только не возникла серьёзная проблема или ошибка.

## Инструкции для агента

Когда пользователь запускает эту команду, выполни следующий workflow:

1. **Проверить режим команды**:

   * Если пользователь передал `$ARGUMENTS` (простое сообщение), сразу перейти к шагу 3

2. **Выполнить pre-commit validation**:

   * Выполнить `pnpm lint` и сообщить обо всех найденных проблемах
   * Выполнить `pnpm build` и убедиться, что build завершается успешно
   * Если какая-либо из проверок завершается ошибкой, спросить пользователя, хочет ли он продолжить несмотря на ошибки или сначала исправить проблемы

3. **Проанализировать git status**:

   * Выполнить `git status --porcelain`, чтобы проверить наличие изменений
   * Если staged-файлов нет, выполнить `git add .`, чтобы добавить все изменённые файлы в staging
   * Если файлы уже находятся в staging, продолжить только с ними

4. **Проанализировать изменения**:

   * Выполнить `git diff --cached`, чтобы увидеть изменения, которые попадут в commit
   * Проанализировать diff и определить основной тип изменений (`feat`, `fix`, `docs` и т. д.)
   * Определить основной scope и назначение изменений

5. **Сформировать commit message**:

   * Выбрать подходящий emoji и type из справочника ниже
   * Создать сообщение в формате: `<emoji> <type>: <description>`
   * Description должно быть кратким, понятным и написанным в imperative mood
   * Показать пользователю предложенный commit message для подтверждения

6. **Выполнить commit**:

   * Выполнить `git commit -m "<generated message>"`
   * Показать commit hash и подтвердить успешное выполнение
   * Дать краткое summary того, что было закоммичено
   * Выполнить `git push`

## Правила для Commit Message

При создании commit messages соблюдай следующие правила:

* **Atomic commits**: Каждый commit должен содержать связанные изменения, служащие одной конкретной цели
* **Imperative mood**: Формулируй сообщения как команды, например `"add feature"`, а не `"added feature"`
* **Краткая первая строка**: Не более 72 символов
* **Conventional format**: Используй `<emoji> <type>: <description>`, где `type` — одно из следующих значений:

  * `feat`: Новая функциональность
  * `fix`: Исправление ошибки
  * `docs`: Изменения документации
  * `style`: Изменения стиля кода — форматирование и т. п.
  * `refactor`: Изменения кода, которые не исправляют ошибки и не добавляют функциональность
  * `perf`: Улучшения производительности
  * `test`: Добавление или исправление тестов
  * `chore`: Изменения build-процесса, инструментов и т. п.
* **Настоящее время, imperative mood**: Пиши commit messages как команды, например `"add feature"`, а не `"added feature"`
* **Краткая первая строка**: Первая строка должна содержать менее 72 символов
* **Emoji**: Каждому типу commit соответствует подходящий emoji:

  * ✨ `feat`: Новая функциональность
  * 🐛 `fix`: Исправление ошибки
  * 📝 `docs`: Документация
  * 💄 `style`: Форматирование/стиль
  * ♻️ `refactor`: Рефакторинг кода
  * ⚡️ `perf`: Улучшение производительности
  * ✅ `test`: Тесты
  * 🔧 `chore`: Инструменты, конфигурация
  * 🚀 `ci`: Улучшения CI/CD
  * 🗑️ `revert`: Откат изменений
  * 🧪 `test`: Добавить падающий тест
  * 🚨 `fix`: Исправить предупреждения compiler/linter
  * 🔒️ `fix`: Исправить проблемы безопасности
  * 👥 `chore`: Добавить или обновить contributors
  * 🚚 `refactor`: Переместить или переименовать ресурсы
  * 🏗️ `refactor`: Внести архитектурные изменения
  * 🔀 `chore`: Merge branches
  * 📦️ `chore`: Добавить или обновить compiled files или packages
  * ➕ `chore`: Добавить dependency
  * ➖ `chore`: Удалить dependency
  * 🌱 `chore`: Добавить или обновить seed-файлы
  * 🧑‍💻 `chore`: Улучшить developer experience
  * 🧵 `feat`: Добавить или обновить код, связанный с multithreading или concurrency
  * 🔍️ `feat`: Улучшить SEO
  * 🏷️ `feat`: Добавить или обновить types
  * 💬 `feat`: Добавить или обновить текст и literals
  * 🌐 `feat`: Internationalization и localization
  * 👔 `feat`: Добавить или обновить business logic
  * 📱 `feat`: Работа над responsive design
  * 🚸 `feat`: Улучшить user experience / usability
  * 🩹 `fix`: Простое исправление некритичной проблемы
  * 🥅 `fix`: Добавить обработку ошибок
  * 👽️ `fix`: Обновить код из-за изменений внешнего API
  * 🔥 `fix`: Удалить код или файлы
  * 🎨 `style`: Улучшить структуру/форматирование кода
  * 🚑️ `fix`: Критический hotfix
  * 🎉 `chore`: Начало проекта
  * 🔖 `chore`: Release/Version tags
  * 🚧 `wip`: Work in progress
  * 💚 `fix`: Исправить CI build
  * 📌 `chore`: Зафиксировать dependencies на конкретных версиях
  * 👷 `ci`: Добавить или обновить CI build system
  * 📈 `feat`: Добавить или обновить analytics/tracking код
  * ✏️ `fix`: Исправить опечатки
  * ⏪️ `revert`: Откатить изменения
  * 📄 `chore`: Добавить или обновить license
  * 💥 `feat`: Внести breaking changes
  * 🍱 `assets`: Добавить или обновить assets
  * ♿️ `feat`: Улучшить accessibility
  * 💡 `docs`: Добавить или обновить комментарии в исходном коде
  * 🗃️ `db`: Изменения, связанные с database
  * 🔊 `feat`: Добавить или обновить logs
  * 🔇 `fix`: Удалить logs
  * 🤡 `test`: Добавить mocks
  * 🥚 `feat`: Добавить или обновить easter egg
  * 🙈 `chore`: Добавить или обновить `.gitignore`
  * 📸 `test`: Добавить или обновить snapshots
  * ⚗️ `experiment`: Провести эксперименты
  * 🚩 `feat`: Добавить, обновить или удалить feature flags
  * 💫 `ui`: Добавить или обновить animations и transitions
  * ⚰️ `refactor`: Удалить dead code
  * 🦺 `feat`: Добавить или обновить код, связанный с validation
  * ✈️ `feat`: Улучшить offline support

## Справочник: Хорошие примеры Commit Messages

Используй эти примеры при создании commit messages:

* ✨ feat: add user authentication system
* 🐛 fix: resolve memory leak in rendering process
* 📝 docs: update API documentation with new endpoints
* ♻️ refactor: simplify error handling logic in parser
* 🚨 fix: resolve linter warnings in component files
* 🧑‍💻 chore: improve developer tooling setup process
* 👔 feat: implement business logic for transaction validation
* 🩹 fix: address minor styling inconsistency in header
* 🚑️ fix: patch critical security vulnerability in auth flow
* 🎨 style: reorganize component structure for better readability
* 🔥 fix: remove deprecated legacy code
* 🦺 feat: add input validation for user registration form
* 💚 fix: resolve failing CI pipeline tests
* 📈 feat: implement analytics tracking for user engagement
* 🔒️ fix: strengthen authentication password requirements
* ♿️ feat: improve form accessibility for screen readers

Пример последовательности commits:

* ✨ feat: add user authentication system
* 🐛 fix: resolve memory leak in rendering process
* 📝 docs: update API documentation with new endpoints
* ♻️ refactor: simplify error handling logic in parser
* 🚨 fix: resolve linter warnings in component files
* ✅ test: add unit tests for authentication flow

## Особенности поведения агента

* **Error handling**: Если validation завершается ошибкой, предложить пользователю выбор — продолжить или сначала исправить проблемы
* **Auto-staging**: Если staged-файлов нет, автоматически добавить все изменения через `git add .`
* **File priority**: Если файлы уже находятся в staging, commit должен включать только эти файлы
* **Всегда выполнять commit и push**: Не нужно запрашивать подтверждение, если только не возникла серьёзная проблема или ошибка; после commit выполнить `git push`
* **Качество сообщения**: Commit messages должны быть понятными, краткими и соответствовать conventional format
* **Success feedback**: После успешного commit показать commit hash и краткое summary
