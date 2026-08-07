<!-- Context: development/design-systems | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Дизайн-системы

## Обзор

Этот файл содержит переиспользуемые паттерны дизайн-систем, шаблоны тем и цветовые системы для frontend-дизайна. Используйте их как стартовую точку для цельных профессиональных UI.

## Краткая справка

**Формат цвета**: OKLCH (перцептуально равномерное цветовое пространство)
**Переменные темы**: CSS custom properties (--variable-name)
**Источники шрифтов**: Google Fonts
**Responsive**: все дизайны должны быть mobile-first responsive

---

## Паттерны тем

### Стиль Neo-Brutalism

**Характеристики**: эстетика web-дизайна 90-х, жирные borders, flat shadows, высокий контраст

**Сценарии**:
- Retro/vintage-приложения
- Смелые интерфейсы с ярким характером
- Арт/creative portfolios
- Игровые consumer apps

**Шаблон темы**:

```css
:root {
  /* Colors - High contrast, bold */
  --background: oklch(1.0000 0 0);
  --foreground: oklch(0 0 0);
  --card: oklch(1.0000 0 0);
  --card-foreground: oklch(0 0 0);
  --popover: oklch(1.0000 0 0);
  --popover-foreground: oklch(0 0 0);
  --primary: oklch(0.6489 0.2370 26.9728);
  --primary-foreground: oklch(1.0000 0 0);
  --secondary: oklch(0.9680 0.2110 109.7692);
  --secondary-foreground: oklch(0 0 0);
  --muted: oklch(0.9551 0 0);
  --muted-foreground: oklch(0.3211 0 0);
  --accent: oklch(0.5635 0.2408 260.8178);
  --accent-foreground: oklch(1.0000 0 0);
  --destructive: oklch(0 0 0);
  --destructive-foreground: oklch(1.0000 0 0);
  --border: oklch(0 0 0);
  --input: oklch(0 0 0);
  --ring: oklch(0.6489 0.2370 26.9728);
  
  /* Chart colors */
  --chart-1: oklch(0.6489 0.2370 26.9728);
  --chart-2: oklch(0.9680 0.2110 109.7692);
  --chart-3: oklch(0.5635 0.2408 260.8178);
  --chart-4: oklch(0.7323 0.2492 142.4953);
  --chart-5: oklch(0.5931 0.2726 328.3634);
  
  /* Sidebar */
  --sidebar: oklch(0.9551 0 0);
  --sidebar-foreground: oklch(0 0 0);
  --sidebar-primary: oklch(0.6489 0.2370 26.9728);
  --sidebar-primary-foreground: oklch(1.0000 0 0);
  --sidebar-accent: oklch(0.5635 0.2408 260.8178);
  --sidebar-accent-foreground: oklch(1.0000 0 0);
  --sidebar-border: oklch(0 0 0);
  --sidebar-ring: oklch(0.6489 0.2370 26.9728);
  
  /* Typography */
  --font-sans: DM Sans, sans-serif;
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: Space Mono, monospace;
  
  /* Border radius - Sharp corners */
  --radius: 0px;
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  
  /* Shadows - Bold, offset shadows */
  --shadow-2xs: 4px 4px 0px 0px hsl(0 0% 0% / 0.50);
  --shadow-xs: 4px 4px 0px 0px hsl(0 0% 0% / 0.50);
  --shadow-sm: 4px 4px 0px 0px hsl(0 0% 0% / 1.00), 4px 1px 2px -1px hsl(0 0% 0% / 1.00);
  --shadow: 4px 4px 0px 0px hsl(0 0% 0% / 1.00), 4px 1px 2px -1px hsl(0 0% 0% / 1.00);
  --shadow-md: 4px 4px 0px 0px hsl(0 0% 0% / 1.00), 4px 2px 4px -1px hsl(0 0% 0% / 1.00);
  --shadow-lg: 4px 4px 0px 0px hsl(0 0% 0% / 1.00), 4px 4px 6px -1px hsl(0 0% 0% / 1.00);
  --shadow-xl: 4px 4px 0px 0px hsl(0 0% 0% / 1.00), 4px 8px 10px -1px hsl(0 0% 0% / 1.00);
  --shadow-2xl: 4px 4px 0px 0px hsl(0 0% 0% / 2.50);
  
  /* Spacing */
  --tracking-normal: 0em;
  --spacing: 0.25rem;
}
```

---

### Стиль Modern Dark Mode

**Характеристики**: чистый, минимальный, профессиональный (эстетика Vercel/Linear)

**Сценарии**:
- SaaS-приложения
- Инструменты разработчика
- Профессиональные dashboard
- Enterprise-приложения
- Современные web apps

**Шаблон темы**:

```css
:root {
  /* Colors - Subtle, professional */
  --background: oklch(1 0 0);
  --foreground: oklch(0.1450 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.1450 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.1450 0 0);
  --primary: oklch(0.2050 0 0);
  --primary-foreground: oklch(0.9850 0 0);
  --secondary: oklch(0.9700 0 0);
  --secondary-foreground: oklch(0.2050 0 0);
  --muted: oklch(0.9700 0 0);
  --muted-foreground: oklch(0.5560 0 0);
  --accent: oklch(0.9700 0 0);
  --accent-foreground: oklch(0.2050 0 0);
  --destructive: oklch(0.5770 0.2450 27.3250);
  --destructive-foreground: oklch(1 0 0);
  --border: oklch(0.9220 0 0);
  --input: oklch(0.9220 0 0);
  --ring: oklch(0.7080 0 0);
  
  /* Chart colors - Monochromatic blues */
  --chart-1: oklch(0.8100 0.1000 252);
  --chart-2: oklch(0.6200 0.1900 260);
  --chart-3: oklch(0.5500 0.2200 263);
  --chart-4: oklch(0.4900 0.2200 264);
  --chart-5: oklch(0.4200 0.1800 266);
  
  /* Sidebar */
  --sidebar: oklch(0.9850 0 0);
  --sidebar-foreground: oklch(0.1450 0 0);
  --sidebar-primary: oklch(0.2050 0 0);
  --sidebar-primary-foreground: oklch(0.9850 0 0);
  --sidebar-accent: oklch(0.9700 0 0);
  --sidebar-accent-foreground: oklch(0.2050 0 0);
  --sidebar-border: oklch(0.9220 0 0);
  --sidebar-ring: oklch(0.7080 0 0);
  
  /* Typography - System fonts */
  --font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  
  /* Border radius - Rounded */
  --radius: 0.625rem;
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  
  /* Shadows - Subtle, soft */
  --shadow-2xs: 0 1px 3px 0px hsl(0 0% 0% / 0.05);
  --shadow-xs: 0 1px 3px 0px hsl(0 0% 0% / 0.05);
  --shadow-sm: 0 1px 3px 0px hsl(0 0% 0% / 0.10), 0 1px 2px -1px hsl(0 0% 0% / 0.10);
  --shadow: 0 1px 3px 0px hsl(0 0% 0% / 0.10), 0 1px 2px -1px hsl(0 0% 0% / 0.10);
  --shadow-md: 0 1px 3px 0px hsl(0 0% 0% / 0.10), 0 2px 4px -1px hsl(0 0% 0% / 0.10);
  --shadow-lg: 0 1px 3px 0px hsl(0 0% 0% / 0.10), 0 4px 6px -1px hsl(0 0% 0% / 0.10);
  --shadow-xl: 0 1px 3px 0px hsl(0 0% 0% / 0.10), 0 8px 10px -1px hsl(0 0% 0% / 0.10);
  --shadow-2xl: 0 1px 3px 0px hsl(0 0% 0% / 0.25);
  
  /* Spacing */
  --tracking-normal: 0em;
  --spacing: 0.25rem;
}
```

---

## Система типографики

### Рекомендуемые семейства шрифтов

**Monospace fonts** (код, технические интерфейсы):
- JetBrains Mono
- Fira Code
- Source Code Pro
- IBM Plex Mono
- Roboto Mono
- Space Mono
- Geist Mono

**Sans-serif fonts** (UI, body text):
- Inter
- Roboto
- Open Sans
- Poppins
- Montserrat
- Outfit
- Plus Jakarta Sans
- DM Sans
- Geist
- Space Grotesk

**Display/decorative fonts**:
- Oxanium
- Architects Daughter

**Serif fonts** (редакционные, формальные):
- Merriweather
- Playfair Display
- Lora
- Source Serif Pro
- Libre Baskerville

### Загрузка шрифтов

Всегда используйте Google Fonts для консистентности и надежности:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## Рекомендации по цветовой системе

### Цветовое пространство OKLCH

Используйте OKLCH для перцептуально равномерных цветов:
- **L** (Lightness): 0-1 (0 = черный, 1 = белый)
- **C** (Chroma): 0-0.4 (насыщенность)
- **H** (Hue): 0-360 (угол цвета)

**Формат**: `oklch(L C H)`

**Пример**: `oklch(0.6489 0.2370 26.9728)` = яркий оранжевый

### Правила цветовой палитры

1. **Избегайте Bootstrap Blue**: если явно не запрошено, избегайте типового blue (#007bff)
2. **Семантические цвета**: используйте осмысленные имена цветов (--primary, --destructive, --success)
3. **Контраст**: обеспечьте соответствие WCAG AA (4.5:1 для текста)
4. **Консистентность**: используйте theme variables, а не hardcoded colors

### Сочетание background/foreground

**Правило**: background должен контрастировать с контентом

- Светлый компонент → темный background
- Темный компонент → светлый background
- Обеспечивает видимость и визуальную иерархию

---

## Система shadows

### Шкала shadows

Shadows создают глубину и иерархию:

- `--shadow-2xs`: минимальная elevation (1-2px)
- `--shadow-xs`: легкий lift (2-3px)
- `--shadow-sm`: маленькие cards (3-4px)
- `--shadow`: elevation по умолчанию (4-6px)
- `--shadow-md`: средние cards (6-8px)
- `--shadow-lg`: modals, dropdowns (8-12px)
- `--shadow-xl`: floating panels (12-16px)
- `--shadow-2xl`: максимальная elevation (16-24px)

### Стили shadows

**Soft shadows** (Modern):
```css
box-shadow: 0 1px 3px 0px hsl(0 0% 0% / 0.10);
```

**Hard shadows** (Neo-brutalism):
```css
box-shadow: 4px 4px 0px 0px hsl(0 0% 0% / 1.00);
```

---

## Система spacing

### Базовая единица

Используйте `--spacing: 0.25rem` (4px) как базовую единицу

### Шкала

- 1x = 0.25rem (4px)
- 2x = 0.5rem (8px)
- 3x = 0.75rem (12px)
- 4x = 1rem (16px)
- 6x = 1.5rem (24px)
- 8x = 2rem (32px)
- 12x = 3rem (48px)
- 16x = 4rem (64px)

---

## Система border radius

### Шкала radius

```css
--radius-sm: calc(var(--radius) - 4px);
--radius-md: calc(var(--radius) - 2px);
--radius-lg: var(--radius);
--radius-xl: calc(var(--radius) + 4px);
```

### Частые значения

- **Sharp** (Neo-brutalism): `--radius: 0px`
- **Subtle** (Modern): `--radius: 0.375rem` (6px)
- **Rounded** (Friendly): `--radius: 0.625rem` (10px)
- **Pill** (Buttons): `--radius: 9999px`

---

## Рекомендации по использованию

### Когда использовать каждую тему

**Neo-Brutalism**:
- ✅ Креативные/арт-проекты
- ✅ Retro/vintage-эстетика
- ✅ Смелые выразительные дизайны
- ❌ Enterprise/corporate-приложения
- ❌ Интерфейсы с критичной доступностью

**Modern Dark Mode**:
- ✅ SaaS-приложения
- ✅ Инструменты разработчика
- ✅ Профессиональные dashboard
- ✅ Enterprise-приложения
- ✅ Интерфейсы с критичной доступностью

### Кастомизация

1. Начните с базового шаблона темы
2. Настройте primary/accent colors под бренд
3. Измените radius для нужного ощущения
4. Настройте shadows под нужную глубину
5. Проверяйте contrast ratios для доступности

---

## Лучшие практики

✅ **Используйте CSS custom properties** для всех значений темы
✅ **Тестируйте light и dark modes**, если применимо
✅ **Проверяйте цветовой контраст** (минимум WCAG AA)
✅ **Используйте семантические имена цветов** (--primary, не --blue)
✅ **Загружайте шрифты из Google Fonts** для надежности
✅ **Применяйте консистентный spacing** через шкалу spacing
✅ **Тестируйте responsive behavior** на всех breakpoints

❌ **Не хардкодьте цвета** в компонентах
❌ **Не используйте generic blue** (#007bff) без причины
❌ **Не смешивайте форматы цветов** (держитесь OKLCH)
❌ **Не пропускайте contrast testing**
❌ **Не используйте слишком много font families** (максимум 2-3)

---

## Ссылки

- [OKLCH Color Picker](https://oklch.com/)
- [Google Fonts](https://fonts.google.com/)
- [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Tailwind CSS Colors](https://tailwindcss.com/docs/customizing-colors)
