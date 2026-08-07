<!-- Context: ui/web/animation-advanced | Priority: medium | Version: 1.0 | Updated: 2025-12-09 -->
# Продвинутые паттерны анимации

Рецепты, лучшие практики, микроинтеракции и требования доступности.

---

## Переходы страниц

### Смена маршрутов

```css
/* Page fade out */
.page-exit {
  animation: fadeOut 200ms ease-in;
}
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

/* Page fade in */
.page-enter {
  animation: fadeIn 300ms ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

**Микросинтаксис**:
```
pageExit: 200ms ease-in [α1→0]
pageEnter: 300ms ease-out [α0→1]
```

---

## Микроинтеракции

### Hover-эффекты

```css
/* Link underline slide */
.link {
  position: relative;
}
.link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 250ms ease-out;
}
.link:hover::after {
  width: 100%;
}
```

**Микросинтаксис**:
```
linkHover: 250ms ease-out [width0→100%]
```

### Toggle switch

```css
/* Toggle slide */
.toggle-switch {
  transition: background-color 200ms ease-out;
}
.toggle-switch .thumb {
  transition: transform 200ms ease-out;
}
.toggle-switch.on .thumb {
  transform: translateX(20px);
}
```

**Микросинтаксис**:
```
toggle: 200ms ease-out [X0→20, bg→accent]
```

---

## Рецепты анимации

### Полная система анимации Chat UI

```
## Core Message Flow
userMsg: 400ms ease-out [Y+20→0, X+10→0, S0.9→1]
aiMsg: 600ms bounce [Y+15→0, S0.95→1] +200ms
typing: 1400ms ∞ [Y±8, α0.4→1] stagger+200ms
status: 300ms ease-out [α0.6→1, S1→1.05→1]

## Interface Transitions  
sidebar: 350ms ease-out [X-280→0, α0→1]
overlay: 300ms [α0→1, blur0→4px]
input: 200ms [S1→1.01, shadow+ring] focus
input: 150ms [S1.01→1, shadow-ring] blur

## Button Interactions
sendBtn: 150ms [S1→0.95→1, R±2°] press
sendBtn: 200ms [S1→1.05, shadow↗] hover
ripple: 400ms [S0→2, α1→0]

## Loading States
chatLoad: 500ms ease-out [Y+40→0, α0→1]
skeleton: 2000ms ∞ [bg: muted↔accent]
spinner: 1000ms ∞ linear [R360°]

## Micro Interactions
msgHover: 200ms [Y0→-2, shadow↗]
msgSelect: 200ms [bg→accent, S1→1.02]
error: 400ms [X±5] shake
success: 600ms bounce [S0→1.2→1, R360°]

## Scroll & Navigation
autoScroll: 400ms smooth
scrollHint: 800ms ∞×3 [Y±5]
```

---

## Лучшие практики

### Делайте ✅

- Держите большинство анимаций короче 400ms
- Используйте `transform` и `opacity` для 60fps
- Задавайте цель каждой анимации
- Используйте ease-out для появления, ease-in для выхода
- Тестируйте на слабых устройствах
- Учитывайте `prefers-reduced-motion`
- Делайте stagger для списков (задержка 50-100ms)
- Используйте одинаковую длительность для похожих взаимодействий

### Не делайте ❌

- Не анимируйте width/height (используйте scale)
- Не используйте анимации дольше 800ms
- Не анимируйте слишком много элементов одновременно
- Не добавляйте анимации без цели
- Не игнорируйте настройки доступности
- Не используйте резкие или отвлекающие анимации
- Не анимируйте каждое взаимодействие
- Не используйте сложный easing для простых действий

---

## Доступность

### Reduced Motion

```css
/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Индикаторы фокуса

```css
/* Always animate focus states */
:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
  transition: outline-offset 150ms ease-out;
}
```

---

## Ссылки

- [Web Animation API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
- [CSS Easing Functions](https://easings.net/)
- [Animation Performance](https://web.dev/animations-guide/)
- [Reduced Motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

---

## Связанные файлы

- [Основы анимации](./animation-basics.md) - базовые принципы
- [Анимации компонентов](./animation-components.md) - распространенные UI-паттерны
- [Анимации загрузки](./animation-loading.md) - состояния загрузки
