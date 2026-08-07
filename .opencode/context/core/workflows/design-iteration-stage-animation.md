<!-- Context: workflows/design-iteration-stage-animation | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Этап 3: дизайн анимаций

**Назначение**: определить micro-interactions и transitions

## Процесс

1. Прочитать файл плана дизайна из `.tmp/design-plans/{name}.md`
2. Просмотреть утвержденную тему этапа 2
3. Определить ключевые взаимодействия (hover, click, scroll)
4. Задать timing и easing анимаций
5. Спланировать состояния загрузки и transitions
6. Документировать анимации через micro-syntax
7. **Обновить файл плана** спецификациями анимаций
8. Показать план анимаций пользователю для одобрения
9. **Обновить файл плана** обратной связью пользователя и статусом одобрения

## Результат

- Спецификация анимаций в формате micro-syntax
- Обновленный файл плана с завершенным этапом 3

## Пример результата

```
## Animation Design: Smooth & Professional

### Button Interactions
hover: 200ms ease-out [Y0→-2, shadow↗]
press: 100ms ease-in [S1→0.95]
ripple: 400ms ease-out [S0→2, α1→0]

### Card Interactions
cardHover: 300ms ease-out [Y0→-4, shadow↗]
cardClick: 200ms ease-out [S1→1.02]

### Page Transitions
pageEnter: 300ms ease-out [α0→1, Y+20→0]
pageExit: 200ms ease-in [α1→0]

### Loading States
spinner: 1000ms ∞ linear [R360°]
skeleton: 2000ms ∞ [bg: muted↔accent]

### Micro-Interactions
inputFocus: 200ms ease-out [S1→1.01, ring]
linkHover: 250ms ease-out [underline 0→100%]

**Philosophy**: Subtle, purposeful animations that enhance UX without distraction
**Performance**: All animations use transform/opacity for 60fps
**Accessibility**: Respects prefers-reduced-motion
```

## Лучшие практики

✅ **Делайте**:
- Используйте micro-syntax для документации
- Держите анимации короче 400ms
- Используйте transform/opacity для производительности
- Учитывайте prefers-reduced-motion
- Делайте анимации осмысленными

❌ **Не делайте**:
- Не анимируйте width/height (используйте scale)
- Не создавайте отвлекающие анимации
- Не игнорируйте влияние на производительность
- Не пропускайте вопросы доступности

## Точка одобрения

"Эти анимации подходят вашему дизайну или нужно скорректировать?"

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Этап 2: Тема](./design-iteration-stage-theme.md)
- [Этап 4: Реализация](./design-iteration-stage-implementation.md)
- [Основы анимации](../../ui/web/animation-basics.md)
