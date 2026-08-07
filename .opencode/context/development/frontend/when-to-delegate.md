<!-- Context: development/frontend/when-to-delegate | Priority: high | Version: 1.0 | Updated: 2026-01-30 -->
# Когда делегировать frontend-specialist

## Обзор

Чёткие критерии: когда делегировать frontend/UI-задачи подагенту **frontend-specialist**, а когда выполнять напрямую.

## Краткая памятка

**Делегируйте frontend-specialist, когда нужны**:
- UI/UX-дизайн (вайрфреймы, темы, анимации)
- Реализация дизайн-системы
- Сложные адаптивные макеты
- Анимации и микровзаимодействия
- Итерации визуального дизайна

**Выполняйте напрямую, когда это**:
- Простые правки HTML/CSS
- Обновление одного компонента
- Исправления багов в существующем UI
- Небольшие правки стилей

---

## Матрица решений

### ✅ ДЕЛЕГИРОВАТЬ frontend-specialist

| Сценарий | Почему делегировать | Пример |
|----------|--------------|---------|
| **Новый UI с нуля** | Нужен поэтапный workflow (макет → тема → анимация → реализация) | "Создайте лендинг для нашего продукта" |
| **Работа с дизайн-системой** | Нужны ContextScout для стандартов и ExternalScout для UI-библиотек | "Реализуйте нашу дизайн-систему с Tailwind + Shadcn" |
| **Сложные адаптивные макеты** | Нужен mobile-first-подход для разных брейкпоинтов | "Соберите дашборд с боковой панелью, карточками и адаптивной сеткой" |
| **Реализация анимаций** | Нужны паттерны анимации и оптимизация производительности | "Добавьте плавные переходы и микровзаимодействия в UI" |
| **Многоэтапные итерации дизайна** | Нужно версионирование (каталог `design_iterations/`) | "Спроектируйте оформление заказа из 3 шагов" |
| **Создание темы** | Нужны цвета OKLCH и кастомные CSS-свойства | "Создайте тёмную тему для приложения" |
| **Интеграция библиотеки компонентов** | Нужен ExternalScout для актуальной документации (Flowbite, Radix и т. д.) | "Интегрируйте компоненты Flowbite в наше приложение" |
| **UI с фокусом на доступность** | Нужны соответствие WCAG и ARIA-атрибуты | "Создайте доступную форму с корректными подписями и валидацией" |

### ⚠️ ВЫПОЛНЯТЬ НАПРЯМУЮ (не делегировать)

| Сценарий | Почему напрямую | Пример |
|----------|------------|---------|
| **Простые правки HTML** | Один файл, прямое изменение | "Измените текст кнопки с 'Submit' на 'Send'" |
| **Небольшие правки CSS** | Малое изменение стилей | "Сделайте отступ заголовка 20px вместо 16px" |
| **Исправления багов** | Исправление существующего кода, не новый дизайн | "Исправьте сломанную ссылку в подвале" |
| **Обновления контента** | Изменение текста, изображений или данных | "Обновите текст hero-секции" |
| **Обновление одного компонента** | Изменение одного существующего компонента | "Добавьте новый prop в компонент Button" |
| **Быстрые прототипы** | Одноразовый код для проверки идеи | "Создайте быстрый HTML-макет для проверки идеи" |

---

## Чеклист делегирования

Перед делегированием frontend-specialist убедитесь:

- [ ] **Задача сфокусирована на UI/дизайне** (не backend, логика или данные)
- [ ] **Нужна дизайн-экспертиза** (макет, тема, анимации)
- [ ] **Полезен поэтапный workflow** (макет → тема → анимация → реализация)
- [ ] **Нужно найти контекст** (дизайн-системы, UI-библиотеки, стандарты)
- [ ] **Пользователь подтвердил подход** (никогда не делегируйте до подтверждения)

---

## Как делегировать

### Шаг 1: найти контекст (опционально, но рекомендуется)

Если не уверены, какой контекст нужен frontend-specialist:

```javascript
task(
  subagent_type="ContextScout",
  description="Find frontend design context",
  prompt="Find design system standards, UI component patterns, animation guidelines, and responsive breakpoint conventions for frontend work."
)
```

### Шаг 2: предложить подход

Покажите пользователю план:

```markdown
## План реализации

**Task**: Create landing page with hero section, features grid, and CTA

**Approach**: Delegate to frontend-specialist subagent

**Why**: 
- Requires design system implementation
- Needs responsive layout across breakpoints
- Includes animations and micro-interactions
- Benefits from staged workflow (layout → theme → animation → implement)

**Context Needed**:
- Design system standards (ui/web/design-systems.md)
- UI styling standards (ui/web/ui-styling-standards.md)
- Animation patterns (ui/web/animation-patterns.md)

**Approval needed before proceeding.**
```

### Шаг 3: получить подтверждение

Дождитесь явного подтверждения пользователя перед делегированием.

### Шаг 4: делегировать с контекстом

**Для простого делегирования** (сессия не нужна):

```javascript
task(
  subagent_type="frontend-specialist",
  description="Create landing page design",
  prompt="Context to load:
  - .opencode/context/ui/web/design-systems.md
  - .opencode/context/ui/web/ui-styling-standards.md
  - .opencode/context/ui/web/animation-basics.md
  
  Task: Create a landing page with:
  - Hero section with headline, subheadline, CTA button
  - Features grid (3 columns on desktop, 1 on mobile)
  - Smooth scroll animations
  
  Requirements:
  - Use Tailwind CSS + Flowbite
  - Mobile-first responsive design
  - Animations <400ms
  - Save to design_iterations/landing_1.html
  
  Follow your staged workflow:
  1. Layout (ASCII wireframe)
  2. Theme (CSS theme file)
  3. Animation (micro-interactions)
  4. Implement (HTML file)
  
  Request approval between each stage."
)
```

**Для сложного делегирования** (с сессией):

Сначала создайте файл контекста сессии, затем делегируйте с путём к сессии.

---

## Типовые паттерны

### Паттерн 1: новый лендинг

**Триггер**: пользователь просит новый лендинг, маркетинговую страницу или страницу продукта

**Решение**: ✅ делегировать frontend-specialist

**Почему**: нужен полный workflow дизайна (макет, тема, анимации, реализация)

**Пример**:
```
User: "Create a landing page for our SaaS product"
You: [Propose approach] → [Get approval] → [Delegate to frontend-specialist]
```

### Паттерн 2: реализация дизайн-системы

**Триггер**: пользователь хочет реализовать или обновить дизайн-систему

**Решение**: ✅ делегировать frontend-specialist

**Почему**: нужны ContextScout для стандартов и ExternalScout для документации UI-библиотеки

**Пример**:
```
User: "Implement our design system using Tailwind and Shadcn"
You: [Propose approach] → [Get approval] → [Delegate to frontend-specialist]
```

### Паттерн 3: интеграция библиотеки компонентов

**Триггер**: пользователь хочет интегрировать библиотеку UI-компонентов (Flowbite, Radix и т. д.)

**Решение**: ✅ делегировать frontend-specialist

**Почему**: нужны ExternalScout для актуальной документации и корректные паттерны интеграции

**Пример**:
```
User: "Add Flowbite components to our app"
You: [Propose approach] → [Get approval] → [Delegate to frontend-specialist]
```

### Паттерн 4: работа с анимациями

**Триггер**: пользователь хочет анимации, переходы или микровзаимодействия

**Решение**: ✅ делегировать frontend-specialist

**Почему**: нужны паттерны анимации и оптимизация производительности (<400ms)

**Пример**:
```
User: "Add smooth animations to the dashboard"
You: [Propose approach] → [Get approval] → [Delegate to frontend-specialist]
```

### Паттерн 5: простая правка HTML

**Триггер**: пользователь хочет изменить текст, исправить ссылку или обновить контент

**Решение**: ⚠️ выполнить напрямую (не делегировать)

**Почему**: простая правка, дизайн-работа не нужна

**Пример**:
```
User: "Change the button text to 'Get Started'"
You: [Edit the HTML file directly]
```

### Паттерн 6: исправление CSS-бага

**Триггер**: пользователь сообщает о баге стилей или сломанной вёрстке

**Решение**: ⚠️ выполнить напрямую (не делегировать)

**Почему**: это исправление бага, а не новая дизайн-работа

**Пример**:
```
User: "The header is overlapping the content on mobile"
You: [Read the CSS, fix the issue directly]
```

---

## Красные флаги (не делегировать)

❌ **Пользователю нужно быстрое исправление** → выполнить напрямую  
❌ **Задача про backend/логику** → неправильный подагент (используйте coder-agent или выполните напрямую)  
❌ **Задача — изменение одной строки** → выполнить напрямую  
❌ **Задача — обновление контента** → выполнить напрямую  
❌ **Задача — тестирование/валидация** → неправильный подагент (используйте tester)  
❌ **Задача — code review** → неправильный подагент (используйте reviewer)  

---

## Зелёные флаги (делегировать)

✅ **Пользователь хочет новый UI-дизайн** → делегировать  
✅ **Задача включает дизайн-системы** → делегировать  
✅ **Нужны адаптивные макеты** → делегировать  
✅ **Есть анимации** → делегировать  
✅ **Нужна интеграция UI-библиотеки** → делегировать  
✅ **Полезен поэтапный workflow** → делегировать  
✅ **Нужна дизайн-экспертиза** → делегировать  

---

## Возможности frontend-specialist

**Что хорошо делает**:
- Создаёт полноценные UI-дизайны с нуля
- Реализует дизайн-системы (Tailwind, Shadcn, Flowbite)
- Строит адаптивные макеты (mobile-first)
- Добавляет анимации и микровзаимодействия
- Интегрирует библиотеки UI-компонентов
- Создаёт темы с цветами OKLCH
- Следует поэтапному workflow (макет → тема → анимация → реализация)
- Версионирует дизайны (каталог `design_iterations/`)

**Чего не делает**:
- Backend-логика или интеграция API
- Запросы к базе данных или обработка данных
- Тестирование или валидация
- Ревью кода или рефакторинг
- Простые правки HTML/CSS (избыточно)
- Обновления контента (только изменения текста)

---

## Файлы контекста, которые использует frontend-specialist

frontend-specialist автоматически загрузит их через ContextScout:

**Дизайн-система**:
- `ui/web/design-systems.md` - шаблоны тем, цветовые системы
- `ui/web/ui-styling-standards.md` - Tailwind, Flowbite, адаптивный дизайн
- `ui/web/design-assets.md` - изображения, иконки, шрифты

**Паттерны**:
- `ui/web/animation-patterns.md` - синтаксис анимаций, микровзаимодействия
- `development/frontend/react/react-patterns.md` - паттерны React (если проект на React)

**Рабочие процессы**:
- `core/workflows/design-iteration-overview.md` - workflow итераций дизайна

---

## Лучшие практики

### Что делать ✅

- ✅ **Предложите подход до делегирования** - сначала покажите пользователю план
- ✅ **Получите подтверждение** - не делегируйте без подтверждения пользователя
- ✅ **Дайте контекст** - перечислите файлы контекста, которые должен загрузить подагент
- ✅ **Задайте чёткие требования** - укажите дизайн-систему, брейкпоинты, анимации
- ✅ **Используйте поэтапный workflow** - дайте frontend-specialist следовать процессу
- ✅ **Доверяйте специалисту** - он знает паттерны дизайна и лучшие практики

### Чего не делать ❌

- ❌ **Не делегируйте простые правки** - эффективнее выполнить напрямую
- ❌ **Не пропускайте подтверждение** - всегда сначала получайте подтверждение пользователя
- ❌ **Не делегируйте backend-работы** - это неправильный подагент
- ❌ **Не микроменеджерите** - дайте специалисту следовать своему workflow
- ❌ **Не делегируйте без контекста** - предоставьте файлы контекста для загрузки
- ❌ **Не делегируйте исправления багов** - выполняйте напрямую, если это не дизайн-проблема

---

## Примеры

### Пример 1: лендинг (делегировать)

**Запрос пользователя**: "Создайте лендинг для нашего SaaS-продукта с hero-секцией, блоком преимуществ и ценами"

**Ваш ответ**:
```markdown
## План реализации

**Task**: Create SaaS landing page

**Approach**: Delegate to frontend-specialist subagent

**Why**:
- Requires full design workflow (layout, theme, animations)
- Needs responsive design across breakpoints
- Benefits from design system standards

**Context Needed**:
- Design system standards
- UI styling standards
- Animation patterns

**Approval needed before proceeding.**
```

**После подтверждения**:
```javascript
task(
  subagent_type="frontend-specialist",
  description="Create SaaS landing page",
  prompt="Context to load:
  - .opencode/context/ui/web/design-systems.md
  - .opencode/context/ui/web/ui-styling-standards.md
  - .opencode/context/ui/web/animation-basics.md
  
  Task: Create a SaaS landing page with:
  - Hero section (headline, subheadline, CTA)
  - Features section (3-column grid)
  - Pricing section (3 tiers)
  - Footer
  
  Requirements:
  - Tailwind CSS + Flowbite
  - Mobile-first responsive
  - Smooth scroll animations
  - Modern design system
  
  Follow staged workflow and request approval between stages."
)
```

### Пример 2: изменение текста кнопки (напрямую)

**Запрос пользователя**: "Измените текст кнопки 'Submit' на 'Send Message'"

**Ваш ответ**:
```markdown
I'll update the button text directly.
```

**Действие**: прочитайте HTML-файл, измените текст кнопки, готово. Делегирование не нужно.

---

### Пример 3: реализация дизайн-системы (делегировать)

**Запрос пользователя**: "Реализуйте нашу дизайн-систему с компонентами Tailwind и Shadcn"

**Ваш ответ**:
```markdown
## План реализации

**Task**: Implement design system with Tailwind + Shadcn

**Approach**: Delegate to frontend-specialist subagent

**Why**:
- Requires UI library integration (Shadcn)
- Needs ExternalScout for current Shadcn docs
- Benefits from design system standards

**Context Needed**:
- Design system standards
- UI styling standards
- External docs (Shadcn)

**Approval needed before proceeding.**
```

**После подтверждения**:
```javascript
task(
  subagent_type="frontend-specialist",
  description="Implement Tailwind + Shadcn design system",
  prompt="Context to load:
  - .opencode/context/ui/web/design-systems.md
  - .opencode/context/ui/web/ui-styling-standards.md
  
  Task: Implement design system using Tailwind CSS and Shadcn/ui
  
  Requirements:
  - Call ExternalScout for current Shadcn docs
  - Set up Tailwind config
  - Integrate Shadcn components
  - Create theme file with OKLCH colors
  - Document component usage
  
  Follow staged workflow and request approval between stages."
)
```

---

## Итог

**Делегируйте frontend-specialist, когда нужны**:
- Новый UI-дизайн с нуля
- Реализация дизайн-системы
- Сложные адаптивные макеты
- Работа с анимациями
- Интеграция UI-библиотеки
- Многоэтапные итерации дизайна

**Выполняйте напрямую, когда это**:
- Простые правки HTML/CSS
- Исправления багов
- Обновления контента
- Обновление одного компонента
- Быстрые прототипы

**Всегда**:
- Сначала предлагайте подход
- Получайте подтверждение пользователя
- Предоставляйте файлы контекста
- Доверяйте workflow специалиста

---

## Связанный контекст

- **Агент frontend-specialist** → `../../../agent/subagents/development/frontend-specialist.md`
- **Дизайн-системы** → `../../ui/web/design-systems.md`
- **Стандарты UI-стилизации** → `../../ui/web/ui-styling-standards.md`
- **Паттерны анимации** → `../../ui/web/animation-patterns.md`
- **Рабочий процесс делегирования** → `../../core/workflows/task-delegation-basics.md`
- **Паттерны React** → `react/react-patterns.md`
