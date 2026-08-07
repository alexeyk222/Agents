<!-- Context: openagents-repo/examples | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Пример context bundle: создание агента Data Analyst

Сессия: 20250121-143022-a4f2
Создано: 2025-01-21T14:30:22Z
Для: TaskManager
Статус: in_progress

## Обзор задачи

Создать нового агента-аналитика данных для репозитория OpenAgents Control. Агент специализируется на задачах анализа данных: визуализации, статистическом анализе и преобразовании данных.

## Запрос пользователя

"Создай нового агента-аналитика данных, который помогает с анализом данных, визуализацией и статистическими задачами"

## Релевантные стандарты (загрузите перед началом)

**Базовые стандарты**:
- `.opencode/context/core/standards/code-quality.md` → модульные функциональные паттерны кода
- `.opencode/context/core/standards/test-coverage.md` → требования к тестированию и TDD
- `.opencode/context/core/standards/documentation.md` → стандарты документации

**Базовые процессы**:
- `.opencode/context/core/workflows/feature-breakdown.md` → методика декомпозиции задач

## Контекст репозитория (загрузите перед началом)

**Быстрый старт** (ВСЕГДА загружайте первым):
- `.opencode/context/openagents-repo/quick-start.md` → ориентация по репозиторию и частые команды

**Ключевые концепции** (загружайте по типу задачи):
- `.opencode/context/openagents-repo/core-concepts/agents.md` → как работают агенты
- `.opencode/context/openagents-repo/core-concepts/evals.md` → как работает тестирование
- `.opencode/context/openagents-repo/core-concepts/registry.md` → как работает registry
- `.opencode/context/openagents-repo/core-concepts/categories.md` → как устроена организация

**Руководства** (загружайте для конкретных workflows):
- `.opencode/context/openagents-repo/guides/adding-agent-basics.md` → пошаговое создание агента
- `.opencode/context/openagents-repo/guides/testing-agent.md` → workflow тестирования
- `.opencode/context/openagents-repo/guides/updating-registry.md` → workflow registry

## Ключевые требования

**Из стандартов**:
- Агент должен следовать модульным функциональным паттернам программирования
- Весь код должен быть тестируемым и поддерживаемым
- Документация должна быть краткой и содержательной
- Добавляйте примеры там, где они полезны

**Из контекста репозитория**:
- Файл агента должен находиться в `.opencode/agent/data/` (организация по категориям)
- Нужны корректные метаданные frontmatter (id, name, description, category, type, version и т. д.)
- Нужно следовать соглашению об именовании: `data-analyst.md` (kebab-case)
- Нужны tags для обнаружения
- Нужно указать tools и permissions
- Нужно зарегистрировать в `registry.json`

**Соглашения об именовании**:
- Имя файла: `data-analyst.md` (kebab-case)
- ID агента: `data-analyst`
- Категория: `data`
- Тип: `agent`

**Структура файлов**:
- Файл агента: `.opencode/agent/data/data-analyst.md`
- Eval-директория: `evals/agents/data/data-analyst/`
- Eval config: `evals/agents/data/data-analyst/config/eval-config.yaml`
- Eval tests: `evals/agents/data/data-analyst/tests/`
- README: `evals/agents/data/data-analyst/README.md`

## Технические ограничения

- Использовать организацию по категориям (категория data)
- Добавить корректные метаданные frontmatter
- Указать нужные tools (read, write, bash и т. д.)
- Определить permissions для чувствительных операций
- Добавить temperature (0.1-0.3 для аналитических задач)
- Следовать структуре промпта агента (context, role, task, instructions)
- Eval-тесты должны быть в формате YAML
- Запись registry должна соответствовать схеме

## Файлы для создания/изменения

**Создать**:
- `.opencode/agent/data/data-analyst.md` - основное определение агента с frontmatter и промптом
- `evals/agents/data/data-analyst/config/eval-config.yaml` - конфигурация eval
- `evals/agents/data/data-analyst/tests/smoke-test.yaml` - базовый smoke test
- `evals/agents/data/data-analyst/tests/data-analysis-test.yaml` - тест возможностей анализа данных
- `evals/agents/data/data-analyst/README.md` - документация агента

**Изменить**:
- `registry.json` - добавить запись агента data-analyst
- `.opencode/context/navigation.md` - добавить контекст категории data, если нужно

## Критерии успеха

- [x] Файл агента создан с корректными метаданными frontmatter
- [x] Промпт агента следует установленным паттернам (context, role, task, instructions)
- [x] Структура eval-тестов создана с config и tests
- [x] Smoke test проходит
- [x] Тест анализа данных проходит
- [x] Запись registry добавлена и проходит валидацию
- [x] README-документация создана
- [x] Все скрипты валидации проходят

## Требования к валидации

**Скрипты для запуска**:
- `./scripts/registry/validate-registry.sh` - проверяет схему и записи registry.json
- `./scripts/validation/validate-test-suites.sh` - проверяет структуру eval-тестов

**Тесты для запуска**:
- `cd evals/framework && npm run eval:sdk -- --agent=data/data-analyst --pattern="smoke-test.yaml"` - запустить smoke test
- `cd evals/framework && npm run eval:sdk -- --agent=data/data-analyst` - запустить все тесты

**Ручные проверки**:
- Убедиться, что frontmatter содержит все обязательные поля
- Проверить, что tools и permissions подходят задаче
- Убедиться, что промпт понятный и следует стандартам
- Проверить, что eval-тесты содержательны

## Ожидаемый результат

**Результаты**:
- Рабочий агент-аналитик данных
- Полный eval test suite
- Запись registry
- Документация

**Формат**:
- Файл агента: Markdown с YAML frontmatter
- Eval config: формат YAML
- Eval tests: формат YAML с test cases
- README: Markdown-документация

## Отслеживание прогресса

- [ ] Контекст загружен и понят
- [ ] Файл агента создан с frontmatter
- [ ] Промпт агента написан
- [ ] Структура eval-директорий создана
- [ ] Eval config создан
- [ ] Smoke test создан
- [ ] Тест анализа данных создан
- [ ] README-документация создана
- [ ] Запись registry добавлена
- [ ] Скрипты валидации запущены
- [ ] Все тесты проходят
- [ ] Документация обновлена

---

## Инструкции для субагента

**ВАЖНО**: 
1. Загрузите ВСЕ контекстные файлы из секций "Релевантные стандарты" и "Контекст репозитория" ДО начала работы
2. Следуйте ВСЕМ требованиям из загруженного контекста
3. Применяйте соглашения об именовании и требования к структуре файлов
4. Валидируйте работу по требованиям к валидации
5. Обновляйте отслеживание прогресса по мере выполнения шагов

**Ваша задача**:
Создать полноценного агента-аналитика данных для репозитория OpenAgents Control, следуя всем установленным соглашениям и стандартам.

**Подход**:
1. **Загрузить контекст**: прочитать все указанные выше контекстные файлы, чтобы понять:
   - Как устроены агенты (core-concepts/agents.md)
   - Как добавить агента (guides/adding-agent-basics.md)
   - Стандарты кода (standards/code-quality.md)
   - Требования к тестированию (core-concepts/evals.md)

2. **Создать файл агента**:
   - Создать `.opencode/agent/data/data-analyst.md`
   - Добавить frontmatter со всеми обязательными метаданными
   - Написать промпт агента с:
      - секцией Context (system, domain, task, execution context)
      - определением роли
      - описанием задачи
      - инструкциями и workflow
      - tools и capabilities
      - примерами, если полезно

3. **Создать eval-структуру**:
   - Создать директорию: `evals/agents/data/data-analyst/`
   - Создать config: `config/eval-config.yaml`
   - Создать директорию tests: `tests/`
   - Создать smoke test: `tests/smoke-test.yaml`
   - Создать capability test: `tests/data-analysis-test.yaml`
   - Создать README: `README.md`

4. **Обновить registry**:
   - Добавить запись в `registry.json` по схеме
   - Включить: id, name, description, category, type, path, version, tags

5. **Валидировать**:
   - Запустить скрипты валидации
   - Запустить eval-тесты
   - Исправить найденные проблемы

**Ограничения**:
- Агент должен быть в категории `data`
- Нужно следовать паттернам функционального программирования
- Нужно добавить корректную обработку ошибок
- Нужно указать подходящие tools (read, write, bash для data tasks)
- Temperature должна быть 0.1-0.3 для аналитической точности
- Eval-тесты должны быть содержательными и проверять реальные capabilities

**Вопросы/уточнения**:
- Какие возможности анализа данных подчеркнуть? (визуализация, статистика, преобразование)
- Должен ли агент поддерживать конкретные форматы данных? (CSV, JSON, Parquet)
- Нужна ли интеграция с конкретными инструментами? (pandas, matplotlib и т. д.)
- Какой уровень статистического анализа нужен? (описательный, inferential, predictive)

**Примечание**: это пример context bundle. На практике субагент получит этот файл и выполнит задачу по инструкциям.
