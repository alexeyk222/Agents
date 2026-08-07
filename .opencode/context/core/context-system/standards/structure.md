<!-- Context: core/structure | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Структура контекста

**Назначение**: организация папок по функции для удобного поиска

**Последнее обновление**: 2026-01-06

---

## Основная структура

<rule id="function_structure" enforcement="strict">
  ВСЕГДА организуйте по функции (что делает информация), а не только по теме.
  
  Обязательные папки:
  - concepts/  - основные идеи, определения, «что это?»
  - examples/  - минимальный рабочий код
  - guides/    - пошаговые процессы
  - lookup/    - справочные таблицы, команды, пути
  - errors/    - типовые проблемы, подводные камни, исправления
</rule>

```
.opencode/context/{category}/
├── navigation.md              # Navigation map (REQUIRED)
├── concepts/              # What it is
│   └── {topic}.md
├── examples/              # Working code
│   └── {example}.md
├── guides/                # How to do it
│   └── {guide}.md
├── lookup/                # Quick reference
│   └── {reference}.md
└── errors/                # Common issues
    └── {framework}.md
```

---

## Назначение папок

### concepts/
**Назначение**: основные идеи, определения, «что это?»

**Содержит**:
- Фундаментальные концепции
- Дизайн-паттерны
- Архитектурные решения
- Системные принципы

**Примеры**:
- `concepts/authentication.md`
- `concepts/state-management.md`
- `concepts/mvi-principle.md`

---

### examples/
**Назначение**: минимальные рабочие примеры кода

**Содержит**:
- Сниппеты кода, работающие как есть
- Минимальные воспроизведения
- Типовые паттерны в действии

**Примеры**:
- `examples/jwt-auth-example.md`
- `examples/react-hooks-example.md`
- `examples/api-call-example.md`

**Правило**: примеры должны быть <30 строк кода и полностью функциональными

---

### guides/
**Назначение**: пошаговые процессы, «как сделать X»

**Содержит**:
- Нумерованные процедуры
- Инструкции по настройке
- Процессы реализации
- Руководства по миграции

**Примеры**:
- `guides/setting-up-auth.md`
- `guides/deploying-api.md`
- `guides/migrating-to-v2.md`

**Правило**: шаги должны быть практическими, а не теоретическими

---

### lookup/
**Назначение**: справочные таблицы, команды, пути

**Содержит**:
- Списки команд
- Расположения файлов
- API-endpoints
- Опции конфигурации
- Горячие клавиши

**Примеры**:
- `lookup/cli-commands.md`
- `lookup/file-locations.md`
- `lookup/api-endpoints.md`

**Правило**: должен быть в формате таблиц/списков (быстро просматриваемым)

---

### errors/
**Назначение**: типовые ошибки, подводные камни, крайние случаи

**Содержит**:
- Сообщения об ошибках + исправления
- Типовые ловушки
- Крайние случаи
- Устранение неполадок

**Примеры**:
- `errors/react-errors.md`
- `errors/nextjs-build-errors.md`
- `errors/auth-errors.md`

**Правило**: группируйте по фреймворку/теме, а не один файл на ошибку

---

## Требование `navigation.md`

<rule id="readme_required" enforcement="strict">
  В каждой категории контекста ОБЯЗАН быть navigation.md в корне с:
  1. Purpose (1–2 предложения)
  2. Навигационными таблицами для каждой функциональной папки
  3. Уровнями приоритета (critical/high/medium/low)
  4. Стратегией загрузки (что загружать для типовых задач)
</rule>

**Пример**:
```markdown
# Development Context

**Purpose**: Core development patterns, errors, and examples

---

## Быстрая навигация

### Concepts
| File | Description | Priority |
|------|-------------|----------|
| concepts/auth.md | Authentication patterns | critical |

### Examples
| File | Description | Priority |
|------|-------------|----------|
| examples/jwt.md | JWT auth example | high |

### Errors
| File | Description | Priority |
|------|-------------|----------|
| errors/react.md | Common React errors | high |

---

## Loading Strategy

**For auth work**: 
1. Load concepts/auth.md
2. Load examples/jwt.md
3. Reference guides/setup-auth.md if needed
```

---

## Правила категоризации

При организации файла спросите:

| Вопрос | Папка |
|----------|--------|
| Объясняет **что** что-то такое? | `concepts/` |
| Показывает **рабочий код**? | `examples/` |
| Объясняет, **как сделать** что-то? | `guides/` |
| Это **справочные** данные? | `lookup/` |
| Документирует **ошибку/проблему**? | `errors/` |

---

## Антипаттерны ❌

### ❌ Плоская структура
```
development/
├── authentication.md
├── jwt-example.md
├── setting-up-auth.md
├── auth-errors.md
└── api-endpoints.md
```
**Проблема**: трудно находить. `authentication.md` — концепция или руководство?

### ✅ По функциям
```
development/
├── navigation.md
├── concepts/
│   └── authentication.md
├── examples/
│   └── jwt-example.md
├── guides/
│   └── setting-up-auth.md
├── lookup/
│   └── api-endpoints.md
└── errors/
    └── auth-errors.md
```
**Преимущество**: назначение файла сразу понятно по расположению

---

## Валидация

Перед коммитом структуры контекста:

- [ ] У всех категорий есть `navigation.md`?
- [ ] Файлы находятся в функциональных папках (не плоско)?
- [ ] В README есть навигационные таблицы?
- [ ] Уровни приоритета назначены?
- [ ] Стратегия загрузки задокументирована?

---

## Связанные материалы

- mvi-principle.md - что извлекать
- templates.md - форматы файлов
- creation.md - как создавать файлы
