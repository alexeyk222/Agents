<!-- Context: workflows/design-iteration-best-practices | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Лучшие практики итераций дизайна

## Процесс итераций

### Когда создавать итерации

**Создавайте новую итерацию** (`{name}_1_1.html`), когда:
- Пользователь просит изменения в существующем дизайне
- Дорабатываете по обратной связи
- Нужны варианты A/B-тестирования
- Выполняется progressive enhancement

**Создавайте новый дизайн** (`{name}_2.html`), когда:
- Запрошен полный редизайн
- Нужен другой подход/стиль
- Нужна альтернативная структура макета

### Workflow итераций

```
User: "Can you make the buttons larger and change the color?"

1. Read current file: dashboard_1.html
2. Make requested changes
3. Save as: dashboard_1_1.html
4. Present changes to user

User: "Perfect! Now can we add a sidebar?"

1. Read current file: dashboard_1_1.html
2. Add sidebar component
3. Save as: dashboard_1_2.html
4. Present changes to user
```

---

## Управление файлами

### Структура папки

```
design_iterations/
├── theme_1.css
├── theme_2.css
├── landing_1.html
├── landing_1_1.html
├── landing_1_2.html
├── dashboard_1.html
├── dashboard_1_1.html
└── README.md (optional: design notes)
```

### Контроль версий

**Отслеживание итераций**:
- Начальная: `design_1.html`
- Итерация 1: `design_1_1.html`
- Итерация 2: `design_1_2.html`
- Итерация 3: `design_1_3.html`

**Новая major-версия**:
- Полный редизайн: `design_2.html`
- Затем итерации: `design_2_1.html`, `design_2_2.html`

---

## Паттерны коммуникации

### Переходы между этапами

**После макета**:
```
"Here's the proposed layout structure. The design uses a [description].
Would you like to proceed with this layout, or should we make adjustments?"
```

**После темы**:
```
"I've created a [style] theme with [key features]. The theme file is saved as theme_N.css.
Does this match your vision, or would you like to adjust colors/typography?"
```

**После анимации**:
```
"Here's the animation plan using [timing/style]. All animations are optimized for performance.
Are these animations appropriate, or should we adjust the timing/effects?"
```

**После реализации**:
```
"I've created the complete design as {filename}.html. The design includes [key features].
Please review and let me know if you'd like any changes or iterations."
```

### Запросы на итерации

**Пользователь просит изменение**:
```
"I'll update the design with [changes] and save it as {filename}_N.html.
This preserves the previous version for reference."
```

---

## Чеклист качества

Перед показом каждого этапа:

**Этап макета**:
- [ ] ASCII wireframe понятен и детален
- [ ] Компоненты хорошо организованы
- [ ] Адаптивное поведение спланировано
- [ ] Запрошено одобрение пользователя

**Этап темы**:
- [ ] Файл темы создан и сохранен
- [ ] Цвета используют формат OKLCH
- [ ] Шрифты загружены из Google Fonts
- [ ] Контрастность соответствует WCAG AA
- [ ] Запрошено одобрение пользователя

**Этап анимации**:
- [ ] Анимации документированы в micro-syntax
- [ ] Timing корректен (< 400ms)
- [ ] Производительность оптимизирована (transform/opacity)
- [ ] Доступность учтена
- [ ] Запрошено одобрение пользователя

**Этап реализации**:
- [ ] Создан один HTML-файл
- [ ] CSS темы подключен
- [ ] Tailwind загружен через тег script
- [ ] Иконки инициализированы
- [ ] Адаптивный дизайн протестирован
- [ ] Атрибуты доступности добавлены
- [ ] Изображения используют валидные placeholder URLs
- [ ] Использован семантический HTML
- [ ] Запрошена проверка пользователя

---

## Устранение неполадок

### Распространенные проблемы

**Проблема**: пользователь хочет пропустить этапы
**Решение**: объясните преимущества структурированного подхода, но адаптируйтесь, если он настаивает

**Проблема**: тема не соответствует видению пользователя
**Решение**: выполните итерацию файла темы, создайте `theme_2.css` с корректировками

**Проблема**: анимации кажутся слишком медленными/быстрыми
**Решение**: скорректируйте timing в micro-syntax и пересоздайте с новыми значениями

**Проблема**: дизайн не работает на mobile
**Решение**: проверьте responsive breakpoints, добавьте стили для мобильных устройств

**Проблема**: у цветов плохой контраст
**Решение**: используйте WCAG contrast checker, скорректируйте значения OKLCH lightness

---

## Ссылки

- [Контекст дизайн-систем](../../ui/web/design-systems.md)
- [Стандарты UI-стилей](../../ui/web/ui-styling-standards.md)
- [Основы анимации](../../ui/web/animation-basics.md)
- [ASCII Art Generator](https://www.asciiart.eu/)
- [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Этап 4: Реализация](./design-iteration-stage-implementation.md)
- [Итерации плана](./design-iteration-plan-iterations.md)
