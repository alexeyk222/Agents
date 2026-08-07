<!-- Context: standards/intelligence | Priority: high | Version: 1.0 | Updated: 2025-01-12 -->

# Project Intelligence

> **Что**: Живая документация, связывающая бизнес-домен и техническую реализацию.
> **Зачем**: Быстрое понимание проекта и онбординг для разработчиков, агентов и стейкхолдеров.
> **Где**: `.opencode/context/project-intelligence/` (выделенная папка)

## Краткая справка

| Что нужно | Файл | Описание |
|---------------|------|-------------|
| Понять «зачем» | `business-domain.md` | Проблема, пользователи, ценность |
| Понять «как» | `technical-domain.md` | Стек, архитектура |
| Увидеть связь | `business-tech-bridge.md` | Маппинг бизнес → техника |
| Узнать контекст | `decisions-log.md` | Почему приняты решения |
| Текущее состояние | `living-notes.md` | Активные проблемы, долг, вопросы |

## Зачем это нужно

Проекты буксуют, когда:
- Бизнес-замысел теряется в коде
- Технические решения не документируются с контекстом
- Новые участники тратят недели вместо часов на понимание проекта
- Контекст хранится только в головах людей, которые могут уйти

Это помогает **бизнесу и технической команде говорить на одном языке**.

## Структура

```
.opencode/context/
├── project-intelligence/              # Project-specific context
│   ├── navigation.md                  # Quick overview & routes
│   ├── business-domain.md             # Business context, problems solved
│   ├── technical-domain.md            # Stack, architecture, decisions
│   ├── business-tech-bridge.md        # How business needs → solutions
│   ├── decisions-log.md               # Decisions with rationale
│   └── living-notes.md                # Active issues, technical debt
└── core/                              # Universal standards
```

## Чеклист онбординга

Для новых участников команды или агентов:

- [ ] Прочитать `navigation.md` (этот файл)
- [ ] Прочитать `business-domain.md`, чтобы понять «зачем»
- [ ] Прочитать `technical-domain.md`, чтобы понять «как»
- [ ] Изучить `business-tech-bridge.md`, чтобы увидеть связь
- [ ] Проверить `decisions-log.md` для контекста ключевых решений
- [ ] Изучить `living-notes.md` для текущего состояния
- [ ] Исследовать кодовую базу с загруженным контекстом

## Как поддерживать актуальность

| Триггер | Действие |
|---------|--------|
| Меняется бизнес-направление | Обновить `business-domain.md` |
| Новое техническое решение | Добавить в `decisions-log.md` |
| Новые проблемы или долг | Обновить `living-notes.md` |
| Запуск фичи | Обновить `business-tech-bridge.md` |
| Изменения стека | Обновить `technical-domain.md` |

**Полное руководство по управлению**: см. `.opencode/context/core/standards/project-intelligence-management.md`

## Интеграция с системой контекста

- **Ленивая загрузка**: сначала загружайте project intelligence при подключении к проекту
- **Слои**: затем загружайте стандарты и конкретный контекст по необходимости
- **Справка**: обзор системы см. в `.opencode/context/core/context-system.md`

## Связанные файлы

- **Руководство по управлению**: `.opencode/context/core/standards/project-intelligence-management.md`
- **Система контекста**: `.opencode/context/core/context-system.md`
- **Индекс стандартов**: `.opencode/context/core/standards/navigation.md`
