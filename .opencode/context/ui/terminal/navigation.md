<!-- Context: ui/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Terminal UI-контекст

**Purpose**: Паттерны Terminal UI (TUI), CLI-анимации и дизайн интерфейсов командной строки

**Last Updated**: 2026-01-07

---

## Обзор

Эта подкатегория будет содержать паттерны и лучшие практики для терминальных UI на Ink, Blessed и нативных возможностях терминала.

---

## Планируемый контент

### Основные файлы (будущие)

| Файл | Описание | Приоритет |
|------|-------------|----------|
| `tui-patterns.md` | Паттерны и layouts компонентов Terminal UI | high |
| `cli-animations.md` | Терминальные анимации, spinner, progress bar | high |
| `ink-components.md` | Паттерны React Ink-компонентов | medium |
| `blessed-patterns.md` | Паттерны и widgets Blessed.js | medium |
| `terminal-styling.md` | ANSI colors, chalk, темы терминала | medium |

### Планируемые темы

- **Layout patterns**: boxes, borders, flexbox-like layouts
- **Интерактивные компоненты**: menus, forms, selects, inputs
- **Индикаторы прогресса**: spinner, progress bar, состояния загрузки
- **Терминальные анимации**: покадровые анимации, плавные transitions
- **Цвет и стилизация**: ANSI escape codes, chalk, gradient text
- **Обработка клавиатуры**: key bindings, shortcuts, navigation
- **Определение терминала**: определение возможностей, fallbacks

---

## Примеры библиотек

### React-based TUI
- **Ink** - React для CLI
- **Pastel** - React-like TUI-фреймворк

### Традиционный TUI
- **Blessed** - высокоуровневая библиотека терминального интерфейса
- **Blessed-contrib** - widgets для blessed (charts, gauges)
- **Terminal-kit** - комплексное управление терминалом

### Стилизация
- **Chalk** - стилизация строк в терминале
- **Gradient-string** - градиентные цвета в терминале
- **Boxen** - создание box в терминале

### Progress/Animation
- **Ora** - аккуратные терминальные spinner
- **CLI-progress** - progress bar
- **Listr** - терминальные списки задач

---

## Использование

**Когда подкатегория будет наполнена**, используйте ее для:
- создания CLI-инструментов с богатыми интерфейсами
- терминальных dashboard
- интерактивных приложений командной строки
- добавления анимаций и индикаторов прогресса в CLI

---

## Связанные категории

- `ui/web/` - паттерны Web UI
- `development/` - общие паттерны разработки

---

## Статус

⏳ **Заглушка** - эта подкатегория запланирована, но пока не наполнена.

Чтобы добавить контент, следуйте принципам MVI:
1. Выделите ключевые концепции (1-3 предложения)
2. Перечислите ключевые пункты (3-5 пунктов)
3. Дайте минимальный пример
4. Добавьте ссылку на полную документацию

---

## Используется

**Agents**: cli-developer, terminal-specialist, devops-specialist (планируется)
