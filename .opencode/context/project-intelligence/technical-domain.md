<!-- Context: project-intelligence/technical | Priority: high | Version: 1.0 | Updated: 2025-01-12 -->

# Технический домен

> Документируйте техническую основу, архитектуру и ключевые решения.

## Краткая справка

- **Назначение**: понять, как проект работает технически
- **Обновлять когда**: появляются новые функции, рефакторинг или изменения технологического стека
- **Аудитория**: разработчики, DevOps, технические стейкхолдеры

## Основной стек

| Слой | Технология | Версия | Обоснование |
|-------|-----------|---------|-----------|
| Язык | [e.g., TypeScript] | [Version] | [Why this language] |
| Фреймворк | [e.g., Node.js] | [Version] | [Why this framework] |
| База данных | [e.g., PostgreSQL] | [Version] | [Why this database] |
| Инфраструктура | [e.g., AWS, Vercel] | [N/A] | [Why this infra] |
| Ключевые библиотеки | [List important ones] | [Versions] | [Why each matters] |

## Архитектурный паттерн

```
Type: [Monolith | Microservices | Serverless | Agent-based | Hybrid]
Pattern: [Brief description]
Diagram: [Link to architecture diagram if exists]
```

### Почему эта архитектура?

[Explain the business and technical reasons for this architecture choice. What problem does this architecture solve? What were alternatives considered?]

## Структура проекта

```
[Project Root]
├── src/                    # Исходный код
├── tests/                  # Тестовые файлы
├── docs/                   # Документация
├── scripts/                # Скрипты сборки/деплоя
└── [Other key directories]
```

**Ключевые директории**:
- `src/` - Содержит всю логику приложения, организованную по [module/feature/domain]
- `tests/` - [How tests are organized]
- `docs/` - [What documentation lives here]

## Ключевые технические решения

| Решение | Обоснование | Влияние |
|----------|-----------|--------|
| [Decision 1] | [Why this choice] | [What it enables] |
| [Decision 2] | [Why this choice] | [What it enables] |

Полную историю решений с альтернативами см. в `decisions-log.md`.

## Точки интеграции

| Система | Назначение | Протокол | Направление |
|--------|---------|----------|-----------|
| [API 1] | [What it does] | [REST/GraphQL/gRPC] | [Inbound/Outbound] |
| [Database] | [What it stores] | [PostgreSQL/Mongo/etc] | [Internal] |
| [Service] | [What it provides] | [HTTP/gRPC] | [Outbound] |

## Технические ограничения

| Ограничение | Источник | Влияние |
|------------|--------|--------|
| [Legacy systems] | [Business/Tech] | [What limitation it creates] |
| [Compliance] | [Regulation] | [What must be followed] |
| [Performance] | [SLAs] | [What must be met] |

## Среда разработки

```
Setup: [Quick setup command or link]
Requirements: [What developers need installed]
Local Dev: [How to run locally]
Testing: [How to run tests]
```

## Деплой

```
Environment: [Production/Staging/Development]
Platform: [Where it deploys]
CI/CD: [Pipeline used]
Monitoring: [Tools for observability]
```

## Чеклист онбординга

- [ ] Знать основной технологический стек
- [ ] Понимать архитектурный паттерн и почему он выбран
- [ ] Знать ключевые директории проекта и их назначение
- [ ] Понимать основные технические решения и их обоснование
- [ ] Знать точки интеграции и зависимости
- [ ] Уметь настроить локальную среду разработки
- [ ] Знать, как запускать тесты и деплой

## Связанные файлы

- `business-domain.md` - Почему существует эта техническая основа
- `business-tech-bridge.md` - Как бизнес-потребности связаны с техническими решениями
- `decisions-log.md` - Полная история решений с контекстом
