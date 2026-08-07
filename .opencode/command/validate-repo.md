# Validate Repository

Комплексная команда валидации, которая проверяет весь repository OpenAgents Control на согласованность между CLI, документацией, registry и components.

## Использование

```bash
/validate-repo
```

## Что проверяет команда

Эта команда выполняет комплексную проверку следующих областей:

1. **Целостность Registry**

   * Проверка синтаксиса JSON
   * Полнота определений components
   * Корректность ссылок на пути файлов
   * Корректность объявлений dependencies

2. **Существование Components**

   * Все agents существуют по указанным путям
   * Все subagents существуют по указанным путям
   * Все commands существуют по указанным путям
   * Все tools существуют по указанным путям
   * Все plugins существуют по указанным путям
   * Все context-файлы существуют по указанным путям
   * Все config-файлы существуют по указанным путям

3. **Согласованность Profiles**

   * Количество components соответствует документации
   * Описания profiles корректны
   * Все dependencies удовлетворены
   * Отсутствуют дублирующиеся components

4. **Точность документации**

   * Количество components в README соответствует registry
   * Ссылки в документации OpenAgent корректны
   * Ссылки на context-файлы корректны
   * Installation guide актуален

5. **Структура Context Files**

   * Все упомянутые context-файлы существуют
   * Организация context-файлов корректна
   * Отсутствуют orphaned context-файлы

6. **Cross-References**

   * Dependencies агентов существуют
   * Ссылки на subagents корректны
   * Ссылки на commands корректны
   * Dependencies tools удовлетворены

## Результат

Команда создаёт подробный отчёт, показывающий:

* ✅ Что корректно и успешно прошло validation
* ⚠️ Предупреждения о потенциальных проблемах
* ❌ Ошибки, которые необходимо исправить
* 📊 Сводную статистику

## Инструкции

Ты — специалист по validation. Твоя задача — комплексно проверить repository OpenAgents Control на согласованность и корректность.

### Шаг 1: Проверить Registry JSON

1. Прочитать и распарсить `registry.json`
2. Проверить синтаксис JSON
3. Проверить структуру schema:

   * Поле `version` существует
   * Поле `repository` существует
   * Объект `categories` существует
   * Объект `components` существует и содержит все типы
   * Объект `profiles` существует
   * Объект `metadata` существует

### Шаг 2: Проверить определения Components

Для каждого типа component (`agents`, `subagents`, `commands`, `tools`, `plugins`, `contexts`, `config`):

1. Проверить обязательные поля:

   * `id` — уникальный
   * `name`
   * `type`
   * `path`
   * `description`
   * `tags` — массив
   * `dependencies` — массив
   * `category`

2. Проверить, что файл существует по указанному `path`

3. Проверить наличие duplicate IDs

4. Убедиться, что `category` присутствует среди определённых categories

### Шаг 3: Проверить Profiles

Для каждого profile (`essential`, `developer`, `business`, `full`, `advanced`):

1. Подсчитать количество components в profile
2. Проверить, что все ссылки на components существуют в секции `components`
3. Убедиться, что все dependencies удовлетворены
4. Проверить отсутствие дублирующихся components

### Шаг 4: Сверить с документацией

1. **navigation.md**:

   * Извлечь количество components из описаний profiles
   * Сравнить с фактическими значениями в registry
   * Проверить, что описания profiles соответствуют описаниям в registry

2. **docs/agents/openagent.md**:

   * Проверить упомянутые delegation criteria
   * Проверить ссылки на context-файлы
   * Проверить описания workflows

3. **docs/getting-started/installation.md**:

   * Проверить описания profiles
   * Проверить installation commands

### Шаг 5: Проверить структуру Context Files

1. Получить список всех файлов в `.opencode/context/`
2. Сверить их с context entries в registry
3. Найти orphaned files — существуют, но отсутствуют в registry
4. Найти missing files — указаны в registry, но не существуют
5. Проверить структуру:

   * Файлы `core/standards/`
   * Файлы `core/workflows/`
   * Файлы `core/system/`
   * Файлы `project/`

### Шаг 6: Проверить Dependencies

Для каждого component с dependencies:

1. Распарсить строку dependency в формате `type:id`
2. Убедиться, что указанный component существует
3. Проверить наличие circular dependencies
4. Проверить полноту dependency chain

### Шаг 7: Сформировать отчёт

Создай комплексный отчёт со следующими разделами:

#### ✅ Успешно проверено

* Синтаксис Registry JSON
* Существование файлов components
* Целостность profiles
* Точность документации
* Структура context-файлов
* Dependency chains

#### ⚠️ Предупреждения

* Orphaned files — существуют, но нигде не упоминаются
* Unused components — определены, но не входят ни в один profile
* Отсутствующие descriptions или tags
* Устаревшие даты metadata

#### ❌ Ошибки

* Отсутствующие файлы
* Сломанные dependencies
* Некорректный JSON
* Несовпадение количества components
* Сломанные ссылки в документации
* Duplicate component IDs

#### 📊 Статистика

* Всего components: X
* Всего profiles: X
* Всего context-файлов: X
* Разбивка количества components по profiles
* Процент file coverage

### Шаг 8: Дать рекомендации

На основе найденных проблем предложи:

* Какие файлы нужно создать
* Какие registry entries добавить или удалить
* Какую документацию обновить
* Какие dependencies исправить

## Пример формата отчёта

```markdown
# Отчёт по валидации Repository OpenAgents Control

Сформировано: 2025-11-19 14:30:00

## Сводка

✅ 95% проверок пройдено
⚠️ Найдено 3 предупреждения
❌ Найдено 2 ошибки

---

## ✅ Успешно проверено

### Целостность Registry
✅ Синтаксис JSON корректен
✅ Все обязательные поля присутствуют
✅ Структура schema корректна

### Существование Components (найдено 45/47 файлов)
✅ Agents: 3/3 файлов существуют
✅ Subagents: 15/15 файлов существуют
✅ Commands: 8/8 файлов существуют
✅ Tools: 2/2 файлов существуют
✅ Plugins: 2/2 файлов существуют
✅ Contexts: 13/15 файлов существуют
✅ Config: 2/2 файлов существуют

### Согласованность Profiles
✅ Essential: 9 components (соответствует README)
✅ Developer: 29 components (соответствует README)
✅ Business: 15 components (соответствует README)
✅ Full: 35 components (соответствует README)
✅ Advanced: 42 components (соответствует README)

### Точность документации
✅ Количество components в README соответствует registry
✅ Документация OpenAgent актуальна
✅ Installation guide корректен

---

## ⚠️ Предупреждения (3)

1. **Orphaned Context File**
   - File: `.opencode/context/legacy/old-patterns.md`
   - Проблема: Файл существует, но не указан в registry
   - Рекомендация: Добавить в registry или удалить файл

2. **Unused Component**
   - Component: `workflow-orchestrator` (agent)
   - Проблема: Определён в registry, но не входит ни в один profile
   - Рекомендация: Добавить в profile или пометить как deprecated

3. **Устаревшая Metadata**
   - Поле: `metadata.lastUpdated`
   - Текущее значение: 2025-11-15
   - Рекомендация: Обновить до текущей даты

---

## ❌ Ошибки (2)

1. **Отсутствующий Context File**
   - Component: `context:advanced-patterns`
   - Ожидаемый путь: `.opencode/context/core/advanced-patterns.md`
   - Используется в: developer, full, advanced profiles
   - Действие: Создать файл или удалить ссылку из registry

2. **Сломанная Dependency**
   - Component: `agent:opencoder`
   - Dependency: `subagent:pattern-matcher`
   - Проблема: Dependency отсутствует в registry
   - Действие: Добавить отсутствующий subagent или исправить dependency reference

---

## 📊 Статистика

### Распределение Components
- Agents: 3
- Subagents: 15
- Commands: 8
- Tools: 2
- Plugins: 2
- Contexts: 15
- Config: 2
- **Всего: 47 components**

### Разбивка Profiles
- Essential: 9 components (19%)
- Developer: 29 components (62%)
- Business: 15 components (32%)
- Full: 35 components (74%)
- Advanced: 42 components (89%)

### File Coverage
- Всего файлов определено: 47
- Найдено файлов: 45 (96%)
- Отсутствует файлов: 2 (4%)
- Orphaned files: 1

### Состояние Dependencies
- Всего dependencies: 23
- Валидных dependencies: 22 (96%)
- Сломанных dependencies: 1 (4%)
- Circular dependencies: 0

---

## 🔧 Рекомендуемые действия

### Высокий приоритет (Errors)
1. Создать отсутствующий файл: `.opencode/context/core/advanced-patterns.md`
2. Исправить сломанную dependency в `opencoder`

### Средний приоритет (Warnings)
1. Удалить orphaned file или добавить его в registry
2. Добавить `workflow-orchestrator` в profile или пометить как deprecated
3. Обновить `metadata.lastUpdated` до 2025-11-19

### Низкий приоритет (Improvements)
1. Добавить больше tags к components для улучшения поиска
2. Рассмотреть добавление descriptions ко всем context-файлам
3. Задокументировать component categories в README

---

## Следующие шаги

1. Проверить и исправить все ❌ ошибки
2. При необходимости обработать ⚠️ предупреждения
3. Повторно запустить validation, чтобы подтвердить исправления
4. При необходимости обновить документацию

---

**Валидация завершена** ✓
```

## Примечания по реализации

Команда должна:

* Использовать bash/python для операций с файловой системой
* Парсить JSON с корректным error handling
* Генерировать отчёт в Markdown
* Быть non-destructive — только read-only validation
* Давать actionable recommendations
* Поддерживать verbose mode для подробного вывода

## Обработка ошибок

* Корректно обрабатывать отсутствующие файлы
* Продолжать validation даже при обнаружении ошибок
* Собрать все проблемы перед формированием отчёта
* Показывать понятные error messages с контекстом

## Производительность

* Выполняться менее чем за 30 секунд
* По возможности кэшировать чтение файлов
* Выполнять validation параллельно там, где это безопасно
* Показывать progress indicators для длительных операций
