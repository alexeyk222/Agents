<!-- Context: visual-development | Priority: high | Version: 1.0 | Updated: 2025-01-27 -->
# Контекст визуальной разработки

**Назначение**: Создание визуального контента, UI-дизайн, генерация изображений и диаграмм

---

## Быстрые маршруты

| Тип задачи | Контекстный файл | Subagent | Инструменты |
|-----------|-------------|----------|-------|
| **Сгенерировать изображение/диаграмму** | Этот файл | Image Specialist | tool:gemini |
| **Отредактировать существующее изображение** | Этот файл | Image Specialist | tool:gemini |
| **UI-макет (статический)** | Этот файл | Image Specialist | tool:gemini |
| **Интерактивный UI-дизайн** | `workflows/design-iteration-overview.md` | - | - |
| **Дизайн-система** | `ui/web/design-systems.md` | - | - |
| **UI-стандарты** | `ui/web/ui-styling-standards.md` | - | - |
| **Паттерны анимации** | `ui/web/animation-patterns.md` | - | - |

---

## Возможности Image Specialist

### Что делает

Subagent **Image Specialist** использует Gemini Nano Banana AI, чтобы:

- ✅ **Генерировать изображения по текстовым описаниям** - Создавать оригинальные изображения, иллюстрации, графику
- ✅ **Редактировать существующие изображения** - Изменять, улучшать или трансформировать изображения
- ✅ **Анализировать изображения** - Описывать содержимое изображения, извлекать информацию
- ✅ **Создавать диаграммы** - Архитектурные диаграммы, flowcharts, визуализации систем
- ✅ **Проектировать макеты** - UI-макеты, wireframes, дизайн-концепты
- ✅ **Генерировать графику** - Графика для соцсетей, промоматериалы, иконки

### Когда делегировать

Делегируйте Image Specialist, когда пользователи просят:

**Ключевые слова для отслеживания**:
- "create image", "generate image", "make image"
- "diagram", "flowchart", "visualization"
- "mockup", "wireframe", "design concept"
- "graphic", "illustration", "icon"
- "edit image", "modify image", "enhance image"
- "screenshot", "visual", "picture"

**Типовые сценарии**:
1. **Архитектурные диаграммы** - Микросервисы, дизайн системы, инфраструктура
2. **UI-макеты** - дизайн dashboard, интерфейсы приложений, web layout
3. **Графика для соцсетей** - Анонсы, промо, брендированный контент
4. **Изображения для документации** - скриншоты tutorial, highlights фич, guides
5. **Презентации** - графика для слайдов, charts, визуальные материалы
6. **Маркетинговые assets** - изображения продукта, hero-графика, banners

### Как вызвать

```javascript
task(
  subagent_type="Image Specialist",
  description="[Brief 3-5 word description]",
  prompt="Context to load:
          - .opencode/context/core/visual-development.md
          
          Task: [Detailed visual requirement]
          
          Requirements:
          - Style: [Visual aesthetic - modern, minimalist, professional, etc.]
          - Dimensions: [Width x Height or aspect ratio]
          - Key Elements: [What must be included]
          - Colors: [Color scheme, brand colors, palette]
          - Format: [PNG, JPG, SVG preference]
          
          Output: [Expected deliverable and location]"
)
```

---

## Примеры сценариев

### 1. Архитектурная диаграмма

**Запрос пользователя**: «Создай диаграмму нашей микросервисной архитектуры»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Generate microservices architecture diagram",
  prompt="Create a technical architecture diagram showing:
          
          **Services**:
          - API Gateway (entry point)
          - Auth Service (authentication)
          - User Service (user management)
          - Order Service (order processing)
          - Payment Service (payment processing)
          - Notification Service (emails/SMS)
          
          **Infrastructure**:
          - PostgreSQL databases (one per service)
          - Redis cache (shared)
          - RabbitMQ message queue
          - AWS S3 (file storage)
          
          **External Services**:
          - Stripe (payments)
          - SendGrid (emails)
          - Twilio (SMS)
          
          **Style**: Clean, professional, modern tech diagram
          **Colors**: Blue for services, green for databases, orange for external
          **Format**: PNG, 1920x1080
          **Layout**: Left-to-right flow, clear connections
          
          Output: Save to docs/architecture-diagram.png"
)
```

---

### 2. UI-макет

**Запрос пользователя**: «Покажи, как может выглядеть dashboard»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Generate analytics dashboard mockup",
  prompt="Create a UI mockup for an analytics dashboard:
          
          **Layout**:
          - Top: Header with logo, navigation, user menu
          - Below header: 4 metric cards in a row
            * Total Users (with trend arrow)
            * Revenue (with percentage change)
            * Conversion Rate (with sparkline)
            * Active Sessions (with live indicator)
          - Middle: Large line chart showing 30-day trends
          - Bottom: Data table with recent transactions
          
          **Style**: Modern, professional SaaS aesthetic
          **Theme**: Dark mode with subtle gradients
          **Colors**: 
            - Background: Dark gray (#1e293b)
            - Cards: Slightly lighter (#334155)
            - Accent: Blue (#3b82f6)
            - Text: White/gray
          **Typography**: Clean sans-serif (Inter-style)
          **Format**: PNG, 1440x900
          
          Output: Save to design_iterations/dashboard_mockup.png"
)
```

---

### 3. Графика для соцсетей

**Запрос пользователя**: «Создай графику для анонса новой фичи»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Generate feature announcement graphic",
  prompt="Create a social media graphic for feature launch:
          
          **Content**:
          - Main headline: 'Introducing Real-Time Collaboration'
          - Subheadline: 'Work together, ship faster'
          - Small text: 'Available now for all teams'
          
          **Visual Elements**:
          - Abstract illustration of people collaborating
          - Subtle geometric shapes in background
          - Modern, energetic feel
          
          **Brand Colors**:
          - Primary: #6366f1 (indigo)
          - Secondary: #8b5cf6 (purple)
          - Background: White with gradient
          - Text: Dark gray (#1e293b)
          
          **Format**: PNG, 1200x630 (optimized for Twitter/LinkedIn)
          **Style**: Modern, professional, eye-catching
          
          Output: Save to marketing/feature-launch-social.png"
)
```

---

### 4. Flowchart / диаграмма процесса

**Запрос пользователя**: «Сделай диаграмму user onboarding flow»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Generate user onboarding flowchart",
  prompt="Create a flowchart showing user onboarding process:
          
          **Steps**:
          1. User signs up (email/password)
          2. Email verification sent
          3. User clicks verification link
          4. Profile setup (name, company, role)
          5. Choose plan (Free/Pro/Enterprise)
          6. Payment (if Pro/Enterprise)
          7. Onboarding tutorial (5 steps)
          8. Dashboard access
          
          **Decision Points**:
          - Email verified? (Yes → Continue, No → Resend)
          - Plan selected? (Free → Skip payment, Paid → Payment)
          - Payment successful? (Yes → Continue, No → Retry)
          
          **Style**: Clean flowchart with standard symbols
          **Colors**: 
            - Start/End: Green
            - Process: Blue
            - Decision: Yellow
            - Error: Red
          **Format**: PNG, 1600x1200
          **Layout**: Top-to-bottom flow
          
          Output: Save to docs/onboarding-flow.png"
)
```

---

### 5. Иконка/иллюстрация

**Запрос пользователя**: «Создай иконку для фичи загрузки файлов»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Generate file upload icon",
  prompt="Create a modern icon for file upload feature:
          
          **Concept**: Cloud with upward arrow
          **Style**: 
            - Minimalist, clean lines
            - Rounded corners
            - Flat design (no gradients)
          **Colors**: 
            - Primary: #3b82f6 (blue)
            - Accent: #60a5fa (lighter blue)
          **Size**: 512x512px (will be scaled down)
          **Format**: PNG with transparent background
          **Usage**: App UI, documentation, marketing
          
          Output: Save to assets/icons/upload-icon.png"
)
```

---

### 6. Редактирование изображения

**Запрос пользователя**: «Сделай этот скриншот более профессиональным»

**Вызов**:
```javascript
task(
  subagent_type="Image Specialist",
  description="Enhance screenshot for documentation",
  prompt="Edit the existing screenshot at docs/raw-screenshot.png:
          
          **Enhancements Needed**:
          - Add subtle drop shadow for depth
          - Round the corners (8px radius)
          - Add a thin border (#e5e7eb)
          - Increase contrast slightly
          - Ensure text is crisp and readable
          
          **Optional**:
          - Add subtle gradient background
          - Highlight key UI elements with arrows/boxes
          
          **Output Format**: PNG, maintain original dimensions
          **Quality**: High (for documentation)
          
          Output: Save to docs/enhanced-screenshot.png"
)
```

---

## Дерево решений: Image Specialist и Design Iteration

Используйте это дерево решений, чтобы выбрать подход:

```
User needs visual content
    ↓
Is it interactive/responsive HTML/CSS?
    ↓
  YES → Use design-iteration-overview.md workflow
    |    - Create HTML files
    |    - Iterate on designs
    |    - Production-ready code
    ↓
  NO → Is it a static visual asset?
    ↓
  YES → Use Image Specialist
    |    - Diagrams
    |    - Mockups (non-interactive)
    |    - Graphics
    |    - Illustrations
    ↓
  NO → Clarify requirements with user
```

### Краткая справка

| Нужно | Использовать |
|------|-----|
| **Интерактивный dashboard** | design-iteration-overview.md |
| **Dashboard mockup (статическое изображение)** | Image Specialist |
| **Responsive landing page** | design-iteration-overview.md |
| **Hero-графика для landing page** | Image Specialist |
| **Рабочий HTML-прототип** | design-iteration-overview.md |
| **Архитектурная диаграмма** | Image Specialist |
| **Библиотека UI-компонентов** | design-iteration-overview.md |
| **Графика для соцсетей** | Image Specialist |

---

## Инструменты и зависимости

### Обязательный инструмент

**tool:gemini** - Gemini Nano Banana AI
- Автоматически включен в профиль Developer
- Требует переменную окружения GEMINI_API_KEY
- Получить API key: https://makersuite.google.com/app/apikey

### Конфигурация

Добавьте в файл `.env`:
```bash
GEMINI_API_KEY=your_api_key_here
```

### Возможности

- **Text-to-Image**: Генерация изображений по описаниям
- **Image-to-Image**: Редактирование и трансформация существующих изображений
- **Image Analysis**: Описание и анализ содержимого изображения
- **Multiple Formats**: Поддержка PNG, JPG, WebP
- **High Resolution**: До 2048x2048 пикселей

---

## Лучшие практики

### Написание эффективных prompt-запросов

✅ **Делайте**:
- Конкретно указывайте размеры и формат
- Ясно описывайте визуальный стиль (modern, minimalist, professional)
- Указывайте цвета hex-кодами или названиями
- Добавляйте ключевые элементы, которые должны быть на изображении
- Указывайте предполагаемый сценарий использования
- Давайте контекст бренда/эстетики

❌ **Не делайте**:
- Не используйте расплывчатые описания («сделай красиво»)
- Не забывайте указывать размеры
- Не полагайтесь на предпочтения стиля по умолчанию
- Не пропускайте спецификацию цветов
- Не забывайте место вывода

### Пример: хороший и плохой prompt-запрос

**❌ Плохой prompt-запрос**:
```
"Create a diagram of our system"
```

**✅ Хороший prompt-запрос**:
```
"Create a technical architecture diagram showing:
- 3 microservices (API, Auth, Database)
- AWS infrastructure (EC2, RDS, S3)
- External APIs (Stripe, SendGrid)

Style: Clean, professional, modern
Colors: Blue for services, green for databases
Format: PNG, 1920x1080
Layout: Left-to-right flow with clear connections

Output: docs/system-architecture.png"
```

---

## Чеклист качества

Перед делегированием Image Specialist:

- [ ] Запрос пользователя явно требует визуального контента
- [ ] Подтверждено, что подходит статическое изображение (не interactive HTML)
- [ ] Собраны требования: стиль, размеры, цвета, элементы
- [ ] Указаны формат и место вывода
- [ ] Подтверждено, что tool:gemini доступен в профиле
- [ ] Подготовлен подробный prompt-запрос со всеми спецификациями

После получения результата:

- [ ] Изображение соответствует требованиям
- [ ] Размеры и формат корректны
- [ ] Визуальный стиль соответствует запросу
- [ ] Все ключевые элементы включены
- [ ] Изображение сохранено в указанное место
- [ ] Пользователь доволен результатом

---

## Устранение неполадок

### Типовые проблемы

**Проблема**: Сгенерированное изображение не соответствует ожиданиям
**Решение**: Уточнить prompt-запрос конкретными деталями, дать референсы

**Проблема**: Низкое качество изображения
**Решение**: Запросить более высокое разрешение, указать требования к качеству в prompt-запросе

**Проблема**: Цвета не соответствуют бренду
**Решение**: Дать точные hex-коды, сослаться на brand guidelines

**Проблема**: Layout перегружен
**Решение**: Упростить требования, указать четкую иерархию и отступы

**Проблема**: Текст на изображении не читается
**Решение**: Запросить более крупный текст, высокий контраст, более ясную типографику

---

## Связанный контекст

- **Workflow UI-дизайна**: `.opencode/context/core/workflows/design-iteration-overview.md`
- **Дизайн-системы**: `.opencode/context/ui/web/design-systems.md`
- **Стандарты UI-стилей**: `.opencode/context/ui/web/ui-styling-standards.md`
- **Паттерны анимации**: `.opencode/context/ui/web/animation-basics.md`, `.opencode/context/ui/web/animation-advanced.md`
- **Руководство по вызову subagent**: `.opencode/context/openagents-repo/guides/subagent-invocation.md`
- **Возможности агентов**: `.opencode/context/openagents-repo/core-concepts/agents.md`

---

## Ключевые слова для discovery

**ContextScout должен находить этот файл, когда пользователи упоминают**:

- image, images, picture, photo, graphic
- diagram, flowchart, visualization, chart
- mockup, wireframe, design, concept
- illustration, icon, asset, visual
- generate, create, make, design
- screenshot, capture, render
- architecture, system, flow, process
- social media, marketing, promotional
- edit, modify, enhance, transform
- UI, interface, dashboard, layout

---

## История версий

- **v1.0** (2025-01-27): Первичное создание с полными сценариями и примерами
