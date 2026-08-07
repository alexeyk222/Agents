<!-- Context: development/testing | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: тестирование Mastra

**Назначение**: Как запускать и проверять компоненты Mastra в этом проекте.

**Обновлено**: 2026-01-09

---

## Основная идея
Тестирование в этом проекте делится на тесты уровня tools и полные интеграционные тесты workflows. Используйте готовые npm-скрипты для быстрой проверки.

## Ключевые пункты
- **Тесты tools**: проверяют отдельные tools изолированно (например, `npm run test:playbook`).
- **Тесты workflows**: запускают полные end-to-end-сценарии (например, `npm run test:workflow`).
- **Базовые тесты**: сравнивают текущие показатели с известным baseline-значением (`npm run test:baseline`).
- **Наблюдаемость**: используйте `npm run traces` после тестов, чтобы посмотреть детали выполнения в базе данных.

## Быстрый пример
```bash
# Проверить конкретный tool
npm run test:calculator

# Запустить полный validity workflow
npm run validity:workflow

# Посмотреть результаты последнего запуска
npm run traces
```

**Источник**: `package.json` scripts, каталог `scripts/`
**Связано**:
- concepts/core.md
- lookup/mastra-config.md
