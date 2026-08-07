<!-- Context: ui/web/animation-chat | Priority: medium | Version: 1.0 | Updated: 2025-12-09 -->
# Паттерны анимации Chat UI

Паттерны анимации для появления сообщений, индикаторов набора и взаимодействий в чате.

---

## Появление сообщения

```css
/* User message - slide from right */
.message-user {
  animation: slideInRight 400ms ease-out;
}
@keyframes slideInRight {
  from {
    transform: translateX(10px) translateY(20px);
    opacity: 0;
    scale: 0.9;
  }
  to {
    transform: translateX(0) translateY(0);
    opacity: 1;
    scale: 1;
  }
}

/* AI message - slide from left with bounce */
.message-ai {
  animation: slideInLeft 600ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
  animation-delay: 200ms;
}
@keyframes slideInLeft {
  from {
    transform: translateY(15px);
    opacity: 0;
    scale: 0.95;
  }
  to {
    transform: translateY(0);
    opacity: 1;
    scale: 1;
  }
}
```

**Микросинтаксис**:
```
userMsg: 400ms ease-out [Y+20→0, X+10→0, S0.9→1]
aiMsg: 600ms bounce [Y+15→0, S0.95→1] +200ms
```

---

## Индикатор набора

```css
.typing-indicator span {
  animation: typingDot 1400ms infinite;
}
.typing-indicator span:nth-child(2) { animation-delay: 200ms; }
.typing-indicator span:nth-child(3) { animation-delay: 400ms; }

@keyframes typingDot {
  0%, 60%, 100% {
    transform: translateY(0);
    opacity: 0.4;
  }
  30% {
    transform: translateY(-8px);
    opacity: 1;
  }
}
```

**Микросинтаксис**:
```
typing: 1400ms ∞ [Y±8, α0.4→1] stagger+200ms
```

---

## Микроинтеракции сообщений чата

```css
/* Message hover */
.message:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 200ms ease-out;
}

/* Message selection */
.message.selected {
  background-color: var(--accent);
  transform: scale(1.02);
  transition: all 200ms ease-out;
}
```

**Микросинтаксис**:
```
msgHover: 200ms [Y0→-2, shadow↗]
msgSelect: 200ms [bg→accent, S1→1.02]
```

---

## Связанные файлы

- [Основы анимации](./animation-basics.md) - базовые принципы
- [Анимации компонентов](./animation-components.md) - UI-компоненты
- [Анимации загрузки](./animation-loading.md) - состояния загрузки
