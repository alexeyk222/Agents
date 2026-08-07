<!-- Context: workflows/design-iteration-visual-content | Priority: medium | Version: 1.0 | Updated: 2025-12-09 -->
# Генерация визуального контента

## Когда использовать Image Specialist

Делегируйте subagent **Image Specialist**, когда пользователи просят:

- **Диаграммы и визуализации**: архитектурные диаграммы, flowcharts, визуализации систем
- **UI-макеты и wireframes**: визуальные макеты, дизайн-концепты, previews интерфейса
- **Графика и assets**: графика для соцсетей, промо-изображения, иконки, иллюстрации
- **Редактирование изображений**: улучшение фото, модификации изображений, визуальные корректировки

## Паттерн вызова

```javascript
task(
  subagent_type="Image Specialist",
  description="Generate/edit visual content",
  prompt="Context to load:
          - .opencode/context/core/visual-development.md
          
          Task: [Specific visual requirement]
          
          Requirements:
          - [Visual style/aesthetic]
          - [Dimensions/format]
          - [Key elements to include]
          - [Color scheme/branding]
          
          Output: [Expected deliverable]"
)
```

## Примеры использования

### Диаграмма архитектуры

```javascript
task(
  subagent_type="Image Specialist",
  description="Generate microservices architecture diagram",
  prompt="Create a diagram showing:
          - 5 microservices (API Gateway, Auth, Orders, Payments, Notifications)
          - Database connections
          - Message queue (RabbitMQ)
          - External services (Stripe, SendGrid)
          
          Style: Clean, professional, modern
          Format: PNG, 1920x1080"
)
```

### UI-макет

```javascript
task(
  subagent_type="Image Specialist",
  description="Generate dashboard mockup",
  prompt="Create a mockup for an analytics dashboard:
          - Header with navigation
          - 4 metric cards (Users, Revenue, Conversion, Retention)
          - Line chart showing trends
          - Data table below
          
          Style: Modern, dark theme, professional
          Format: PNG, 1440x900"
)
```

### Графика для соцсетей

```javascript
task(
  subagent_type="Image Specialist",
  description="Generate product launch graphic",
  prompt="Create a social media graphic announcing new feature:
          - Bold headline: 'Introducing Real-Time Collaboration'
          - Subtext: 'Work together, ship faster'
          - Brand colors: #6366f1 (primary), #1e293b (dark)
          - Include abstract collaboration visual
          
          Format: PNG, 1200x630 (Twitter/LinkedIn)"
)
```

## Требуемые инструменты

- **tool:gemini** - Gemini Nano Banana AI для генерации/редактирования изображений
- Автоматически доступен в Developer profile

## Когда НЕ делегировать

**Вместо этого используйте design-iteration workflow**, когда:
- Создаете интерактивные HTML/CSS-дизайны
- Собираете полноценные UI-реализации
- Выполняете итерации существующих HTML-файлов
- Нужен адаптивный, production-ready код

**Используйте image-specialist**, когда:
- Нужны статичные визуальные assets
- Создаете диаграммы или иллюстрации
- Генерируете mockups для презентации
- Нужны быстрые визуальные концепции без кода

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Визуальная разработка](../visual-development.md)
