<!-- Context: workflows/design-iteration-stage-theme | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Этап 2: дизайн темы

**Назначение**: определить цвета, типографику, отступы и визуальный стиль

## Процесс

1. Прочитать файл плана дизайна из `.tmp/design-plans/{name}.md`
2. Просмотреть утвержденный макет этапа 1
3. Выбрать дизайн-систему (neo-brutalism, modern dark, custom)
4. Выбрать цветовую палитру (избегать Bootstrap blue, если не запрошено)
5. Выбрать типографику (Google Fonts)
6. Определить отступы и тени
7. Сгенерировать CSS-файл темы
8. **Обновить файл плана** спецификациями темы
9. Показать тему пользователю для одобрения
10. **Обновить файл плана** обратной связью пользователя и статусом одобрения

## Результат

- CSS-файл темы, сохраненный в `design_iterations/theme_N.css`
- Обновленный файл плана с завершенным этапом 2

## Критерии выбора темы

| Стиль | Использовать когда | Избегать когда |
|-------|----------|------------|
| Neo-Brutalism | Креативные/арт-проекты, ретро-эстетика | Enterprise apps, accessibility-critical |
| Modern Dark | SaaS, инструменты разработчика, professional dashboards | Playful consumer apps |
| Custom | Специфичные требования бренда | Проекты с жестким лимитом времени |

## Пример результата

```
## Theme Design: Modern Professional

**Style Reference**: Vercel/Linear aesthetic
**Color Palette**: Monochromatic with accent
**Typography**: Inter (UI) + JetBrains Mono (code)
**Spacing**: 4px base unit
**Shadows**: Subtle, soft elevation

**Theme File**: design_iterations/theme_1.css

Key Design Decisions:
- Primary: Neutral gray for professional feel
- Accent: Subtle blue for interactive elements
- Radius: 0.625rem for modern, friendly feel
- Shadows: Soft, minimal elevation
- Fonts: System-like for familiarity
```

## Именование файлов

`theme_1.css`, `theme_2.css` и т. д.

## Лучшие практики

✅ **Делайте**:
- Ссылайтесь на файлы контекста дизайн-системы
- Используйте CSS custom properties
- Сохраняйте тему в отдельный файл
- Учитывайте доступность (контрастность)
- Избегайте Bootstrap blue, если не запрошено

❌ **Не делайте**:
- Не хардкодьте цвета в HTML
- Не используйте generic/заезженные цветовые схемы
- Не пропускайте проверку контраста
- Не смешивайте форматы цветов (держитесь OKLCH)

## Точка одобрения

"Эта тема соответствует вашему видению или нужны корректировки?"

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Этап 1: Макет](./design-iteration-stage-layout.md)
- [Этап 3: Анимация](./design-iteration-stage-animation.md)
- [Контекст дизайн-систем](../../ui/web/design-systems.md)
- [Стандарты UI-стилей](../../ui/web/ui-styling-standards.md)
