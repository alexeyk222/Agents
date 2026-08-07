<!-- Context: development/ui-styling-standards | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Стандарты UI-стилизации

## Обзор

Стандарты и соглашения для CSS-фреймворков, responsive design и лучших практик стилизации во frontend-разработке.

## Краткая справка

**Фреймворк**: Tailwind CSS + Flowbite (по умолчанию)
**Подход**: mobile-first responsive
**Формат**: utility-first CSS
**Специфичность**: используйте `!important` для override при необходимости

---

## Соглашения CSS-фреймворков

### Tailwind CSS

**Способ загрузки** (предпочтительно):

```html
<!-- ✅ Use CDN script tag -->
<script src="https://cdn.tailwindcss.com"></script>
```

**Избегайте**:

```html
<!-- ❌ Don't use stylesheet link -->
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
```

**Почему**: script tag включает JIT-компиляцию и настройку

### Flowbite

**Способ загрузки**:

```html
<!-- Flowbite CSS -->
<link href="https://cdn.jsdelivr.net/npm/flowbite@2.0.0/dist/flowbite.min.css" rel="stylesheet">

<!-- Flowbite JS -->
<script src="https://cdn.jsdelivr.net/npm/flowbite@2.0.0/dist/flowbite.min.js"></script>
```

**Использование**: Flowbite — библиотека компонентов по умолчанию, если пользователь не указал другое

**Доступные компоненты**:
- Кнопки, формы, модальные окна
- Навигация, dropdown, tabs
- Cards, alerts, badges
- Таблицы, pagination
- Tooltips, popovers

---

## Требования к responsive design

### Подход mobile-first

**Правило**: ВСЕ дизайны ДОЛЖНЫ быть responsive

**Breakpoints** (значения Tailwind по умолчанию):

```css
/* Mobile first - base styles apply to mobile */
.element { }

/* Small devices (640px and up) */
@media (min-width: 640px) { }  /* sm: */

/* Medium devices (768px and up) */
@media (min-width: 768px) { }  /* md: */

/* Large devices (1024px and up) */
@media (min-width: 1024px) { } /* lg: */

/* Extra large devices (1280px and up) */
@media (min-width: 1280px) { } /* xl: */

/* 2XL devices (1536px and up) */
@media (min-width: 1536px) { } /* 2xl: */
```

**Синтаксис Tailwind**:

```html
<!-- Mobile: stack, Desktop: side-by-side -->
<div class="flex flex-col md:flex-row">
  <div class="w-full md:w-1/2">Left</div>
  <div class="w-full md:w-1/2">Right</div>
</div>

<!-- Mobile: full width, Desktop: constrained -->
<div class="w-full lg:w-3/4 xl:w-1/2 mx-auto">
  Content
</div>
```

### Требования к тестированию

✅ Тестируйте минимум на breakpoints: 375px, 768px, 1024px, 1440px
✅ Проверяйте touch targets (минимум 44x44px)
✅ Проверяйте читаемость текста на всех размерах
✅ Убедитесь, что изображения корректно масштабируются
✅ Тестируйте навигацию на mobile

---

## Рекомендации по цветовой палитре

### Избегайте Bootstrap Blue

**Правило**: НИКОГДА не используйте типовой Bootstrap blue (#007bff), если это явно не запрошено

**Почему**: заезженный, без характера, выглядит устаревшим

**Альтернативы**:

```css
/* Instead of Bootstrap blue */
--bootstrap-blue: #007bff; /* ❌ Avoid */

/* Use contextual colors */
--primary: oklch(0.6489 0.2370 26.9728);    /* Vibrant orange */
--accent: oklch(0.5635 0.2408 260.8178);     /* Rich purple */
--info: oklch(0.6200 0.1900 260);            /* Modern blue */
--success: oklch(0.7323 0.2492 142.4953);    /* Fresh green */
```

### Правила использования цвета

1. **Семантические имена**: используйте `--primary`, `--accent`, а не `--blue`, `--red`
2. **Соответствие бренду**: выбирайте цвета под характер проекта
3. **Проверка контраста**: обеспечьте соответствие WCAG AA (минимум 4.5:1)
4. **Консистентность**: везде используйте theme variables

---

## Контраст background/foreground

### Правило контраста

**При дизайне компонентов или постеров**:

- **Светлый компонент** → темный фон
- **Темный компонент** → светлый фон

**Почему**: повышает видимость и создает визуальную иерархию

**Примеры**:

```html
<!-- Light card on dark background -->
<div class="bg-gray-900 p-8">
  <div class="bg-white text-gray-900 p-6 rounded-lg">
    Light card content
  </div>
</div>

<!-- Dark card on light background -->
<div class="bg-gray-50 p-8">
  <div class="bg-gray-900 text-white p-6 rounded-lg">
    Dark card content
  </div>
</div>
```

### Правила для отдельных компонентов

**Posters/Hero sections**:
- Используйте высокий контраст для читаемости
- Добавляйте overlay gradients для текста поверх изображений
- Тестируйте на реальном контенте

**Cards/Panels**:
- Мягкая глубина через shadows
- Четкая граница между card и background
- Консистентный padding

---

## CSS specificity и overrides

### Использование !important

**Правило**: используйте `!important` для свойств, которые могут перезаписать Tailwind или Flowbite

**Частые случаи**:

```css
/* Typography overrides */
h1 {
  font-size: 2.5rem !important;
  font-weight: 700 !important;
  line-height: 1.2 !important;
}

body {
  font-family: 'Inter', sans-serif !important;
  color: var(--foreground) !important;
}

/* Component overrides */
.custom-button {
  background-color: var(--primary) !important;
  border-radius: var(--radius) !important;
}
```

**Когда НЕ использовать**:

```css
/* ❌ Don't use for everything */
.element {
  margin: 1rem !important;
  padding: 1rem !important;
  display: flex !important;
}

/* ✅ Use Tailwind utilities instead */
<div class="m-4 p-4 flex">
```

### Лучшие практики specificity

1. **Предпочитайте utility classes** вместо custom CSS
2. **Используйте !important умеренно** — только для override фреймворка
3. **Скоупьте custom styles**, чтобы избежать конфликтов
4. **Используйте CSS custom properties** для темизации

---

## Layout-паттерны

### Flexbox (предпочтительно для 1D layouts)

```html
<!-- Horizontal layout -->
<div class="flex items-center gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Vertical layout -->
<div class="flex flex-col gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Centered content -->
<div class="flex items-center justify-center min-h-screen">
  <div>Centered content</div>
</div>
```

### Grid (предпочтительно для 2D layouts)

```html
<!-- Responsive grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div>Card 1</div>
  <div>Card 2</div>
  <div>Card 3</div>
</div>

<!-- Dashboard layout -->
<div class="grid grid-cols-12 gap-4">
  <aside class="col-span-12 lg:col-span-3">Sidebar</aside>
  <main class="col-span-12 lg:col-span-9">Content</main>
</div>
```

### Паттерны контейнеров

```html
<!-- Centered container with max width -->
<div class="container mx-auto px-4 max-w-7xl">
  Content
</div>

<!-- Full-width section with contained content -->
<section class="w-full bg-gray-50">
  <div class="container mx-auto px-4 py-12 max-w-6xl">
    Content
  </div>
</section>
```

---

## Стандарты типографики

### Иерархия

```html
<!-- Heading scale -->
<h1 class="text-4xl md:text-5xl lg:text-6xl font-bold">Main Heading</h1>
<h2 class="text-3xl md:text-4xl font-semibold">Section Heading</h2>
<h3 class="text-2xl md:text-3xl font-semibold">Subsection</h3>
<h4 class="text-xl md:text-2xl font-medium">Minor Heading</h4>

<!-- Body text -->
<p class="text-base md:text-lg leading-relaxed">Body text</p>
<p class="text-sm text-gray-600">Secondary text</p>
<p class="text-xs text-gray-500">Caption text</p>
```

### Загрузка шрифтов

**Всегда используйте Google Fonts**:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Применяйте в CSS**:

```css
body {
  font-family: 'Inter', sans-serif !important;
}
```

### Читаемость

- **Длина строки**: оптимально 60-80 символов
- **Line height**: 1.5-1.75 для body text
- **Размер шрифта**: минимум 16px для body text
- **Контраст**: минимум 4.5:1 для обычного текста

---

## Паттерны стилизации компонентов

### Buttons

```html
<!-- Primary button -->
<button class="bg-primary text-primary-foreground px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity">
  Primary Action
</button>

<!-- Secondary button -->
<button class="bg-secondary text-secondary-foreground px-6 py-3 rounded-lg font-medium hover:bg-secondary/80 transition-colors">
  Secondary Action
</button>

<!-- Outline button -->
<button class="border-2 border-primary text-primary px-6 py-3 rounded-lg font-medium hover:bg-primary hover:text-primary-foreground transition-all">
  Outline Action
</button>
```

### Cards

```html
<!-- Basic card -->
<div class="bg-card text-card-foreground rounded-lg shadow-md p-6">
  <h3 class="text-xl font-semibold mb-2">Card Title</h3>
  <p class="text-muted-foreground">Card content</p>
</div>

<!-- Interactive card -->
<div class="bg-card text-card-foreground rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer">
  <h3 class="text-xl font-semibold mb-2">Interactive Card</h3>
  <p class="text-muted-foreground">Hover for effect</p>
</div>
```

### Forms

```html
<!-- Input field -->
<div class="space-y-2">
  <label class="block text-sm font-medium">Email</label>
  <input 
    type="email" 
    class="w-full px-4 py-2 border border-input rounded-lg focus:ring-2 focus:ring-ring focus:border-transparent transition-all"
    placeholder="you@example.com"
  >
</div>

<!-- Textarea -->
<div class="space-y-2">
  <label class="block text-sm font-medium">Message</label>
  <textarea 
    class="w-full px-4 py-2 border border-input rounded-lg focus:ring-2 focus:ring-ring focus:border-transparent transition-all resize-none"
    rows="4"
    placeholder="Your message..."
  ></textarea>
</div>
```

---

## Стандарты доступности

### ARIA Labels

```html
<!-- Button with icon -->
<button aria-label="Close dialog">
  <svg>...</svg>
</button>

<!-- Navigation -->
<nav aria-label="Main navigation">
  <ul>...</ul>
</nav>
```

### Semantic HTML

```html
<!-- ✅ Use semantic elements -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<article>...</article>
<aside>...</aside>
<footer>...</footer>

<!-- ❌ Avoid div soup -->
<div class="header">...</div>
<div class="nav">...</div>
<div class="main">...</div>
```

### Состояния фокуса

```css
/* Always provide visible focus states */
button:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

/* Tailwind utility */
<button class="focus:ring-2 focus:ring-ring focus:ring-offset-2">
  Button
</button>
```

---

## Оптимизация производительности

### Загрузка CSS

```html
<!-- Preconnect to font sources -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Preload critical fonts -->
<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
```

### Оптимизация изображений

```html
<!-- Responsive images -->
<img 
  src="image-800.jpg" 
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
  alt="Description"
  loading="lazy"
>
```

### Critical CSS

```html
<!-- Inline critical CSS -->
<style>
  /* Above-the-fold styles */
  body { margin: 0; font-family: system-ui; }
  .hero { min-height: 100vh; }
</style>

<!-- Load full CSS async -->
<link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'">
```

---

## Лучшие практики

### Делайте ✅

- Используйте utility classes Tailwind для быстрой разработки
- Загружайте Tailwind через script tag для JIT-компиляции
- Используйте Flowbite как библиотеку компонентов по умолчанию
- Делайте все дизайны mobile-first responsive
- Тестируйте на нескольких breakpoints
- Используйте semantic HTML elements
- Добавляйте ARIA labels для интерактивных элементов
- Используйте CSS custom properties для темизации
- Применяйте `!important` для framework overrides
- Обеспечивайте корректный цветовой контраст (WCAG AA)

### Не делайте ❌

- Не используйте Bootstrap blue без явного запроса
- Не загружайте Tailwind как stylesheet
- Не пропускайте responsive design
- Не используйте div soup (используйте semantic HTML)
- Не забывайте focus states
- Не хардкодьте цвета (используйте theme variables)
- Не пропускайте тестирование доступности
- Не используйте маленькие touch targets (<44px)
- Не смешивайте форматы цветов
- Не злоупотребляйте `!important`

---

## Альтернативы фреймворков

Если пользователь просит другой фреймворк:

**Bootstrap**:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

**Bulma**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
```

**Foundation**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/css/foundation.min.css">
<script src="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/js/foundation.min.js"></script>
```

---

## Ссылки

- [Документация Tailwind CSS](https://tailwindcss.com/docs)
- [Компоненты Flowbite](https://flowbite.com/docs/getting-started/introduction/)
- [Рекомендации WCAG](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
