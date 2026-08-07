<!-- Context: ui/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Web UI-контекст

**Purpose**: Web UI-паттерны, анимации, стандарты стилизации и дизайн React-компонентов

**Last Updated**: 2026-01-07

---

## Быстрая навигация

### Основные файлы

| Файл | Описание | Приоритет |
|------|-------------|----------|
| [animation-basics.md](animation-basics.md) | Основы анимации, длительность, easing | high |
| [animation-components.md](animation-components.md) | Анимации кнопок, карточек, modal, dropdown | high |
| [animation-chat.md](animation-chat.md) | Chat UI и анимации сообщений | medium |
| [animation-loading.md](animation-loading.md) | Skeleton, spinner, progress-анимации | medium |
| [animation-forms.md](animation-forms.md) | Анимации полей формы и валидации | medium |
| [animation-advanced.md](animation-advanced.md) | Рецепты, лучшие практики, доступность | medium |
| [ui-styling-standards.md](ui-styling-standards.md) | CSS-фреймворки, паттерны Tailwind, лучшие практики стилизации | high |
| [react-patterns.md](react-patterns.md) | Современные React-паттерны, hooks, дизайн компонентов | high |
| [design-systems.md](design-systems.md) | Принципы дизайн-систем и библиотеки компонентов | medium |
| [images-guide.md](images-guide.md) | Placeholder и responsive images | medium |
| [icons-guide.md](icons-guide.md) | Icon-системы (Lucide, Heroicons, FA) | medium |
| [fonts-guide.md](fonts-guide.md) | Загрузка и оптимизация шрифтов | medium |
| [cdn-resources.md](cdn-resources.md) | CDN-библиотеки и ресурсы | medium |

### Подкатегории

| Подкатегория | Описание | Путь |
|-------------|-------------|------|
| **design/** | Продвинутые дизайн-паттерны (scrollytelling, эффекты) | [design/navigation.md](design/navigation.md) |

---

## Стратегия загрузки

### Для общей работы с Web UI:
1. Загрузите `ui-styling-standards.md` (CSS-фреймворки, Tailwind)
2. Загрузите `react-patterns.md` (паттерны компонентов)
3. Смотрите `animation-patterns.md` (если нужны анимации)

### Для работы с анимациями:
1. Загрузите `animation-basics.md` (основы, длительность, easing)
2. Загрузите `animation-components.md` (анимации UI-компонентов)
3. Смотрите `animation-chat.md` для паттернов Chat UI
4. Смотрите `animation-advanced.md` для рецептов и доступности

### Для scroll-анимаций:
1. Перейдите в подкатегорию `design/`
2. Загрузите гайды по scroll-linked-анимациям

---

## Область

Эта подкатегория охватывает:
- ✅ CSS-анимации и transitions
- ✅ Tailwind CSS и utility-first-стилизацию
- ✅ Паттерны React-компонентов и hooks
- ✅ Дизайн-системы и библиотеки компонентов
- ✅ Библиотеки иконок и web fonts
- ✅ Scroll-linked-анимации (scrollytelling)
- ✅ Canvas-based rendering
- ✅ Паттерны Framer Motion

---

## Кратко о файлах

### animation-basics.md, animation-components.md, animation-chat.md, animation-loading.md, animation-forms.md, animation-advanced.md
CSS-анимации, микроинтеракции и UI-переходы, разделенные на фокусные модули.

**Ключевые темы**: микросинтаксис анимаций, производительность 60fps, reduced motion, анимации Chat UI, паттерны компонентов

### ui-styling-standards.md
Использование CSS-фреймворков, паттерны Tailwind CSS, responsive design и лучшие практики стилизации.

**Ключевые темы**: utility-first CSS, стилизация компонентов, responsive breakpoints, dark mode

### react-patterns.md
Современные React-паттерны: функциональные компоненты, hooks, управление состоянием и оптимизация производительности.

**Ключевые темы**: custom hooks, context API, code splitting, memoization

### design-systems.md
Принципы дизайн-систем, библиотеки компонентов и поддержание консистентности в приложениях.

**Ключевые темы**: design tokens, component APIs, документация, versioning

### images-guide.md, icons-guide.md, fonts-guide.md, cdn-resources.md
Управление дизайн-ассетами в web-приложениях, разбитое на фокусные гайды.

**Ключевые темы**: placeholder images, библиотеки иконок (Lucide, Heroicons), web fonts, CDN-ресурсы

---

## Связанные категории

- `ui/terminal/` - паттерны Terminal UI
- `development/` - общие паттерны разработки
- `product/` - продуктовый дизайн и UX-стратегия

---

## Используется

**Agents**: frontend-specialist, design-specialist, ui-developer, react-developer, animation-expert

---

## Статистика
- Основные файлы: 8
- Подкатегории: 1 (design/)
- **Всего context-файлов**: 8 + подкатегория design
