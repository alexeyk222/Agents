<!-- Context: workflows/design-iteration-overview | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Рабочий процесс итераций дизайна — обзор

## Обзор

Структурированный 4-этапный workflow для создания UI-дизайнов и итераций по ним. Процесс обеспечивает осмысленные дизайн-решения с одобрением пользователя на каждом этапе.

## Краткая справка

**Этапы**: макет → тема → анимация → реализация
**Одобрение**: требуется между каждым этапом
**Выход**: один HTML-файл на итерацию дизайна
**Расположение**: папка `design_iterations/`

---

## Когда использовать этот workflow

### Делегируйте OpenFrontendSpecialist, когда:

**✅ НАСТОЯТЕЛЬНО РЕКОМЕНДУЕТСЯ** делегировать для:
- **Новой UI/UX-дизайн работы** - landing pages, dashboards, интерфейсы приложений
- **Создания дизайн-систем** - библиотеки компонентов, системы тем, style guides
- **Сложных макетов** - multi-column grids, responsive designs, сложные структуры
- **Визуальной полировки** - анимации, transitions, micro-interactions
- **Работы с фокусом на бренде** - маркетинговые страницы, product showcases, hero sections
- **UI с критичной доступностью** - формы, навигация, интерактивные компоненты

**Зачем делегировать?**
- OpenFrontendSpecialist следует 4-этапному workflow дизайна (Layout → Theme → Animation → Implementation)
- Обеспечивает осмысленные дизайн-решения с точками одобрения
- Создает отполированный, доступный, production-ready UI
- Учитывает responsive design, цвета OKLCH, семантический HTML
- Создает однофайловые HTML-прототипы для быстрых итераций

### Выполняйте напрямую, когда:

**⚠️ Только простые случаи**:
- Небольшие обновления текста/контента в существующем UI
- Малые CSS-правки (цвета, отступы, шрифты)
- Добавление простых utility-классов
- Обновление props существующих компонентов
- Исправления багов в существующем UI-коде

### Паттерн делегирования

```javascript
// For UI design work
task(
  subagent_type="OpenFrontendSpecialist",
  description="Design {feature} UI",
  prompt="Design a {feature} following the 4-stage workflow:
  
  Requirements:
  - {requirement 1}
  - {requirement 2}
  
  Context: {what this UI is for}
  
  Follow the design iteration workflow:
  1. Layout (ASCII wireframe)
  2. Theme (design system, colors)
  3. Animation (micro-interactions)
  4. Implementation (single HTML file)
  
  Request approval between each stage."
)
```

### Примеры сценариев

| Сценарий | Действие | Почему |
|----------|--------|-----|
| "Create a landing page for our SaaS product" | ✅ Делегировать OpenFrontendSpecialist | Сложный UI-дизайн, нужен 4-этапный workflow |
| "Design a user dashboard with charts" | ✅ Делегировать OpenFrontendSpecialist | Сложный макет, визуальный дизайн, взаимодействия |
| "Build a component library with our brand" | ✅ Делегировать OpenFrontendSpecialist | Работа с дизайн-системой, нужна экспертиза по темам |
| "Fix button color from blue to green" | ⚠️ Выполнить напрямую | Простое CSS-изменение |
| "Update hero text content" | ⚠️ Выполнить напрямую | Только обновление контента |

---

## Связанные файлы

- [Файл плана дизайна](./design-iteration-plan-file.md) - ОБЯЗАТЕЛЬНЫЙ шаблон плана
- [Этап 1: Макет](./design-iteration-stage-layout.md)
- [Этап 2: Тема](./design-iteration-stage-theme.md)
- [Этап 3: Анимация](./design-iteration-stage-animation.md)
- [Этап 4: Реализация](./design-iteration-stage-implementation.md)
- [Генерация визуального контента](./design-iteration-visual-content.md)
- [Лучшие практики](./design-iteration-best-practices.md)
- [Итерации плана](./design-iteration-plan-iterations.md)
