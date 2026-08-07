<!-- Context: ui/web/animation-basics | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Основы анимации

## Обзор

Стандарты и паттерны для UI-анимаций, микроинтеракций и переходов. Анимации должны ощущаться естественно, иметь цель и улучшать UX без отвлечения.

## Краткая справка

**Длительность**: 150-400ms для большинства взаимодействий
**Easing**: ease-out для появления, ease-in для выхода
**Цель**: у каждой анимации должна быть понятная задача
**Производительность**: используйте transform и opacity для 60fps

---

## Микросинтаксис анимаций

### Правила записи

**Формат**: `element: duration easing [properties] modifiers`

**Символы**:
- `→` = переход от → к
- `±` = колебание/тряска
- `↗` = увеличение
- `↘` = уменьшение
- `∞` = бесконечный цикл
- `×N` = повторить N раз
- `+Nms` = задержка на N миллисекунд

**Свойства**:
- `Y` = translateY
- `X` = translateX
- `S` = scale
- `R` = rotate
- `α` = opacity
- `bg` = background

**Пример**: `button: 200ms ease-out [S1→1.05, α0.8→1]`
- Кнопка масштабируется с 1 до 1.05 и меняет opacity с 0.8 до 1 за 200ms с ease-out

---

## Базовые принципы анимации

### Стандарты длительности

```
Ultra-fast:  100-150ms  (micro-feedback, hover states)
Fast:        150-250ms  (button clicks, toggles)
Standard:    250-350ms  (modals, dropdowns, navigation)
Moderate:    350-500ms  (page transitions, complex animations)
Slow:        500-800ms  (dramatic reveals, storytelling)
```

### Функции easing

```css
/* Entrances - start slow, end fast */
ease-out: cubic-bezier(0, 0, 0.2, 1);

/* Exits - start fast, end slow */
ease-in: cubic-bezier(0.4, 0, 1, 1);

/* Both - smooth throughout */
ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);

/* Bounce - playful, attention-grabbing */
bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);

/* Elastic - spring-like */
elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6);
```

### Рекомендации по производительности

**Анимации 60fps** (GPU-ускорение):
- ✅ `transform` (translate, scale, rotate)
- ✅ `opacity`
- ✅ `filter` (осторожно)

**Избегайте** (вызывает reflow/repaint):
- ❌ `width`, `height`
- ❌ `top`, `left`, `right`, `bottom`
- ❌ `margin`, `padding`

---

## Связанные файлы

- [Анимации компонентов](./animation-components.md) - распространенные UI-паттерны
- [Анимации загрузки](./animation-loading.md) - состояния загрузки
- [Продвинутые анимации](./animation-advanced.md) - рецепты и лучшие практики
