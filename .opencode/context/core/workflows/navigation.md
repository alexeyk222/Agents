<!-- Context: core/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по базовым рабочим процессам

**Назначение**: рабочие процессы для распространенных задач разработки

---

## Файлы

| Файл | Тема | Приоритет | Когда загружать |
|------|-------|----------|-----------|
| `code-review.md` | Процесс ревью кода | ⭐⭐⭐⭐ | Ревью кода |
| `task-delegation-basics.md` | Основной workflow делегирования | ⭐⭐⭐⭐ | Использование task tool |
| `task-delegation-specialists.md` | Кому и когда делегировать | ⭐⭐⭐⭐ | Выбор специалиста |
| `task-delegation-caching.md` | Кэширование контекста | ⭐⭐⭐ | Повторяющиеся задачи |
| `external-libraries-workflow.md` | Процесс внешних библиотек | ⭐⭐⭐⭐ | Внешние пакеты |
| `external-libraries-scenarios.md` | Распространенные сценарии | ⭐⭐⭐ | Нужны примеры |
| `external-libraries-faq.md` | Устранение неполадок | ⭐⭐⭐ | Ошибки/вопросы |
| `feature-breakdown.md` | Декомпозиция функций | ⭐⭐⭐⭐ | 4+ файла, сложные задачи |
| `session-management.md` | Управление сессиями | ⭐⭐⭐ | Очистка сессии |
| `design-iteration-overview.md` | Обзор workflow дизайна | ⭐⭐⭐⭐ | Начало работы над дизайном |
| `design-iteration-plan-file.md` | Шаблон плана дизайна | ⭐⭐⭐⭐ | Создание плана дизайна |
| `design-iteration-stage-layout.md` | Этап 1: макет | ⭐⭐⭐ | Дизайн макета |
| `design-iteration-stage-theme.md` | Этап 2: тема | ⭐⭐⭐ | Дизайн темы |
| `design-iteration-stage-animation.md` | Этап 3: анимация | ⭐⭐⭐ | Дизайн анимаций |
| `design-iteration-stage-implementation.md` | Этап 4: реализация | ⭐⭐⭐ | Реализация |
| `design-iteration-visual-content.md` | Генерация визуального контента | ⭐⭐ | Генерация изображений |
| `design-iteration-best-practices.md` | Лучшие практики и устранение неполадок | ⭐⭐⭐ | Проверка качества |
| `design-iteration-plan-iterations.md` | Итерации файла плана | ⭐⭐⭐ | Управление итерациями |

---

## Стратегия загрузки

**Для ревью кода**:
1. Загрузить `code-review.md` (high)
2. Зависит от: `../standards/code-quality.md`, `../standards/security-patterns.md`

**Для делегирования задач**:
1. Загрузить `task-delegation-basics.md` (high)
2. Загрузить `task-delegation-specialists.md` (при выборе агента)

**Для внешних библиотек**:
1. Загрузить `external-libraries-workflow.md` (high)
2. Смотреть примеры в `external-libraries-scenarios.md`

**Для сложных функций**:
1. Загрузить `feature-breakdown.md` (high)
2. Зависит от: `task-delegation-basics.md`

**Для управления сессиями**:
1. Загрузить `session-management.md` (medium)

---

## Связанные материалы

- **Стандарты** → `../standards/navigation.md`
- **Делегирование OpenAgents Control** → `../../openagents-repo/guides/subagent-invocation.md`
