<!-- Context: openagents-repo/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Контекст репозитория OpenAgents Control

**Назначение**: контекстные файлы для репозитория OpenAgents Control

**Последнее обновление**: 2026-02-04

---

## Быстрая навигация

| Функция | Файлы | Назначение |
|----------|-------|---------|
| **Стандарты** | 2 файла | Стандарты создания агентов |
| **Концепции** | 6 файлов | Ключевые идеи и принципы |
| **Примеры** | 9 файлов | Рабочие примеры кода |
| **Руководства** | 14 файлов | Пошаговые процессы |
| **Справочник** | 11 файлов | Быстрые справочные таблицы |
| **Ошибки** | 2 файла | Частые проблемы и решения |
| **Возможности** | 3 файла | Документация возможностей и рефакторинг |
| **Плагины** | Система контекстных плагинов | Архитектура и возможности плагинов |

---

## Стандарты (создание агентов)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `standards/agent-frontmatter.md` | Валидный YAML frontmatter OpenCode | ⭐⭐⭐⭐⭐ |
| `standards/subagent-structure.md` | Стандартная структура файла субагента | ⭐⭐⭐⭐⭐ |

**Когда читать**: перед созданием или изменением файлов агентов

---

## Концепции (ключевые идеи)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `concepts/compatibility-layer.md` | Паттерн адаптера для AI-инструментов разработки | ⭐⭐⭐⭐⭐ |
| `concepts/subagent-testing-modes.md` | Standalone-тестирование и делегирование | ⭐⭐⭐⭐⭐ |
| `concepts/hooks-system.md` | Пользовательские команды жизненного цикла | ⭐⭐⭐⭐ |
| `concepts/agent-skills.md` | Skills, обучающие Claude задачам | ⭐⭐⭐⭐ |
| `concepts/subagents-system.md` | Специализированные AI-помощники | ⭐⭐⭐⭐ |

**Когда читать**: перед тестированием субагентов или работой с адаптерами инструментов

---

## Примеры (рабочий код)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `examples/baseadapter-pattern.md` | Паттерн Template Method для адаптеров инструментов | ⭐⭐⭐⭐⭐ |
| `examples/zod-schema-migration.md` | Миграция TypeScript на схемы Zod | ⭐⭐⭐⭐ |
| `examples/subagent-prompt-structure.md` | Оптимизированный шаблон промпта субагента | ⭐⭐⭐⭐ |

**Когда читать**: при создании адаптеров, схем или оптимизации промптов субагентов

---

## Руководства (пошагово)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `guides/compatibility-layer-workflow.md` | Разработка слоя совместимости для AI-инструментов | ⭐⭐⭐⭐⭐ |
| `guides/testing-subagents.md` | Как тестировать субагентов standalone | ⭐⭐⭐⭐⭐ |
| `guides/adding-agent-basics.md` | Как добавлять новых агентов (основы) | ⭐⭐⭐⭐ |
| `guides/adding-agent-testing.md` | Как добавлять тесты агентов | ⭐⭐⭐⭐ |
| `guides/adding-skill-basics.md` | Как добавлять OpenCode skills | ⭐⭐⭐⭐ |
| `guides/creating-skills.md` | Как создавать Claude Code skills | ⭐⭐⭐⭐ |
| `guides/creating-subagents.md` | Как создавать субагентов Claude Code | ⭐⭐⭐⭐ |
| `guides/testing-agent.md` | Как тестировать агентов | ⭐⭐⭐⭐ |
| `guides/external-libraries-workflow.md` | Как работать с зависимостями внешних библиотек | ⭐⭐⭐⭐ |
| `guides/github-issues-workflow.md` | Как работать с GitHub issues и project board | ⭐⭐⭐⭐ |
| `guides/npm-publishing.md` | Как публиковать пакет в npm | ⭐⭐⭐ |
| `guides/updating-registry.md` | Как обновлять registry | ⭐⭐⭐ |
| `guides/debugging.md` | Как диагностировать проблемы | ⭐⭐⭐ |
| `guides/resolving-installer-wildcard-failures.md` | Исправление wildcard-сбоев установки контекста | ⭐⭐⭐ |
| `guides/creating-release.md` | Как создавать релизы | ⭐⭐ |

**Когда читать**: при выполнении конкретных задач

---

## Справочник (быстрые ссылки)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `lookup/tool-feature-parity.md` | Сравнение возможностей AI-инструментов для кода | ⭐⭐⭐⭐⭐ |
| `lookup/compatibility-layer-structure.md` | Структура файлов пакета совместимости | ⭐⭐⭐⭐⭐ |
| `lookup/subagent-test-commands.md` | Команды тестирования субагентов | ⭐⭐⭐⭐⭐ |
| `lookup/hook-events.md` | Справочник всех событий hooks | ⭐⭐⭐⭐ |
| `lookup/skill-metadata.md` | Поля frontmatter в SKILL.md | ⭐⭐⭐⭐ |
| `lookup/skills-comparison.md` | Skills и альтернативы | ⭐⭐⭐⭐ |
| `lookup/builtin-subagents.md` | Субагенты по умолчанию (Explore, Plan) | ⭐⭐⭐⭐ |
| `lookup/subagent-frontmatter.md` | Поля конфигурации субагента | ⭐⭐⭐⭐ |
| `lookup/file-locations.md` | Где расположены файлы | ⭐⭐⭐⭐ |
| `lookup/commands.md` | Доступные slash-команды | ⭐⭐⭐ |

**Когда читать**: для быстрого поиска команд и сравнения возможностей

---

## Ошибки (диагностика)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `errors/tool-permission-errors.md` | Проблемы с правами инструментов | ⭐⭐⭐⭐⭐ |
| `errors/skills-errors.md` | Skills не срабатывают или не загружаются | ⭐⭐⭐⭐ |

**Когда читать**: когда тесты падают из-за ошибок прав

---

## Ключевые концепции (основа)

| Файл | Тема | Приоритет |
|------|-------|----------|
| `core-concepts/agents.md` | Как работают агенты | ⭐⭐⭐⭐⭐ |
| `core-concepts/evals.md` | Как работает тестирование | ⭐⭐⭐⭐⭐ |
| `core-concepts/registry.md` | Как работает registry | ⭐⭐⭐⭐ |
| `core-concepts/categories.md` | Как устроена организация | ⭐⭐⭐ |

**Когда читать**: при первом знакомстве с репозиторием

---

## Стратегия загрузки

### Для тестирования субагентов:
1. Загрузите `concepts/subagent-testing-modes.md` (понять режимы)
2. Загрузите `guides/testing-subagents.md` (пошагово)
3. Используйте `lookup/subagent-test-commands.md` (команды)
4. Если есть ошибки: загрузите `errors/tool-permission-errors.md`

### Для создания агентов:
1. Загрузите `standards/agent-frontmatter.md` (валидный YAML frontmatter)
2. Загрузите `standards/subagent-structure.md` (структура файла)
3. Загрузите `core-concepts/agents.md` (понять систему)
4. Загрузите `guides/adding-agent-basics.md` (пошагово)
5. **Если используете внешние библиотеки**: загрузите `guides/external-libraries-workflow.md` (получить docs)
6. Загрузите `examples/subagent-prompt-structure.md` (если это субагент)
7. Загрузите `guides/testing-agent.md` (валидация)

### Для управления issues:
1. Загрузите `guides/github-issues-workflow.md` (понять процесс)
2. Создавайте issues с корректными labels и шаблонами
3. Добавляйте их на доску проекта для отслеживания
4. Обрабатывайте запросы системно

### Для отладки:
1. Загрузите `guides/debugging.md` (общий подход)
2. Загрузите конкретный файл ошибки из `errors/`
3. Используйте `lookup/file-locations.md` (поиск файлов)

---

## Соответствие размерам файлов

Все файлы следуют принципу MVI (<200 строк):

- ✅ Стандарты: <200 строк
- ✅ Концепции: <100 строк
- ✅ Примеры: <100 строк
- ✅ Руководства: <150 строк
- ✅ Справочник: <100 строк
- ✅ Ошибки: <150 строк

---

## Связанный контекст

- `../core/` - базовый системный контекст (стандарты, паттерны)
- `../core/context-system/` - система управления контекстом
- `quick-start.md` - 2-минутная ориентация по репозиторию
- `../content-creation/navigation.md` - принципы создания контента
- `plugins/context/navigation.md` - контекст системы плагинов
- `features/navigation.md` - документация возможностей и руководства по рефакторингу

---

## Вклад

При добавлении новых контекстных файлов:

1. Следуйте принципу MVI (<200 строк)
2. Используйте функциональную организацию (concepts/, examples/, guides/, lookup/, errors/)
3. Обновите навигацию в этом README.md
4. Добавьте перекрестные ссылки на связанные файлы
5. Проверьте через `/context validate`
