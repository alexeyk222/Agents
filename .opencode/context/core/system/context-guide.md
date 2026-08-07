<!-- Context: core/context-guide | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство по системе контекста

## Краткая справка

**Золотое правило**: Загружайте контекст, когда он нужен, а не заранее (ленивая загрузка)

**Ключевой принцип**: Используйте индекс контекста для обнаружения, загружайте конкретные файлы по необходимости

**Расположение индекса**: `.opencode/context/navigation.md` - Быстрая карта всех контекстов

**Структура**: standards/ (качество + анализ), workflows/ (процесс + ревью), system/ (внутреннее)

**Расположение сессии**: `.tmp/sessions/{timestamp}-{task-slug}/context.md`

---

## Обзор

Контекстные файлы дают правила и шаблоны для конкретных задач. Используйте индекс для эффективного обнаружения и ленивой загрузки, чтобы prompts оставались компактными.

## Система индекса контекста

**Центральный индекс**: `.opencode/context/navigation.md` - Сверхкомпактная карта всех контекстов

Индекс содержит:
- Быструю карту типовых задач (код, docs, тесты, ревью, делегирование)
- Триггеры/ключевые слова для каждого контекста
- Зависимости между контекстами
- Уровни приоритета (critical, high, medium)

### Доступные контекстные файлы

Все файлы находятся в `.opencode/context/core/` с организованными подпапками:

### Стандарты (правила качества + анализ)
- `standards/code-quality.md` - Принципы модульного, функционального кода [critical]
- `standards/documentation.md` - Стандарты документации [critical]
- `standards/test-coverage.md` - Стандарты тестирования [critical]
- `standards/security-patterns.md` - Базовые паттерны (обработка ошибок, безопасность) [high]
- `standards/code-analysis.md` - Фреймворк анализа [high]

### Рабочие процессы (шаблоны процессов + ревью)
- `workflows/task-delegation-basics.md` - Шаблон делегирования [high]
- `workflows/feature-breakdown.md` - Декомпозиция сложной задачи [high]
- `workflows/session-management.md` - Жизненный цикл сессии [medium]
- `workflows/code-review.md` - Правила ревью кода [high]

## Как использовать индекс

**Шаг 1: Проверьте быструю карту** (для типовых задач)
- Задача по коду? → Загрузить `standards/code-quality.md`
- Задача по docs? → Загрузить `standards/documentation.md`
- Задача по ревью? → Загрузить `workflows/code-review.md`

**Шаг 2: Загрузите индекс** (для сопоставления ключевых слов)
- Загрузить `.opencode/context/navigation.md`
- Просканировать триггеры, чтобы найти релевантные контексты
- Загружать конкретные контекстные файлы по необходимости

**Шаг 3: Загрузите зависимости**
- Проверить `deps:` в индексе
- Загрузить зависимые контексты для полных правил

**Преимущества:**
- Нет раздувания prompt (индекс всего ~120 токенов)
- Загружается только релевантное
- Быстрее для простых задач
- Понятное отслеживание зависимостей

## Когда использовать каждый файл

### .opencode/context/core/standards/code-quality.md
- Написание нового кода
- Изменение существующего кода
- Следование модульным/функциональным паттернам
- Принятие архитектурных решений

### .opencode/context/core/standards/documentation.md
- Написание README-файлов
- Создание API-документации
- Добавление комментариев к коду

### .opencode/context/core/standards/test-coverage.md
- Написание новых тестов
- Запуск наборов тестов
- Отладка падающих тестов

### .opencode/context/core/standards/security-patterns.md
- Обработка ошибок
- Паттерны безопасности
- Типовые паттерны кода

### .opencode/context/core/standards/code-analysis.md
- Анализ паттернов кодовой базы
- Расследование багов
- Оценка архитектуры

### .opencode/context/core/workflows/task-delegation-basics.md
- Делегирование general agent
- Создание контекста задачи
- Координация нескольких файлов

### .opencode/context/core/workflows/feature-breakdown.md
- Задачи с 4+ файлами
- Оценка трудозатрат >60 минут
- Сложные зависимости

### .opencode/context/core/workflows/session-management.md
- Жизненный цикл сессии
- Процедуры очистки
- Изоляция сессий

### .opencode/context/core/workflows/code-review.md
- Ревью кода
- Аудит кода
- Обратная связь по PR

## Временный контекст (для сессии)

При делегировании создавайте сфокусированный контекст задачи:

**Расположение**: `.tmp/sessions/{timestamp}-{task-slug}/context.md`

**Структура**:
```markdown
# Task Context: {Task Name}

Session ID: {id}
Created: {timestamp}
Status: in_progress

## Current Request
{What user asked for}

## Requirements
- {requirement 1}
- {requirement 2}

## Decisions Made
- {decision 1}

## Files to Modify/Create
- {file 1} - {purpose}

## Static Context Available
- .opencode/context/core/standards/code-quality.md
- .opencode/context/core/standards/test-coverage.md

## Constraints/Notes
{Important context}

## Progress
- [ ] {task 1}
- [ ] {task 2}

---
**Instructions for Subagent:**
{Specific instructions}
```

## Управление сессиями

### Структура сессии
```
.tmp/sessions/{session-id}/
├── context.md          # Task context
├── notes.md            # Working notes
└── artifacts/          # Generated files
```

### Формат ID сессии
`{timestamp}-{random-4-chars}`
Пример: `20250119-143022-a4f2`

### Очистка
- Спрашивайте пользователя перед удалением файлов сессии
- Удаляйте после завершения задачи
- Сохраняйте, если пользователь хочет проверить

## Лучшие практики

✅ Используйте индекс для обнаружения контекста
✅ Загружайте только релевантные контекстные файлы
✅ Проверяйте зависимости в индексе
✅ Создавайте временный контекст при делегировании
✅ Очищайте сессии после завершения
✅ По возможности ссылайтесь на конкретные секции
✅ Держите временный контекст сфокусированным и кратким

**Золотое правило**: Загружайте контекст, когда он нужен, а не заранее.
