<!-- Context: workflows/design-iteration-stage-implementation | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Этап 4: Реализация

**Назначение**: сгенерировать полный HTML-файл со всеми компонентами

## Процесс

1. Прочитать файл плана дизайна из `.tmp/design-plans/{name}.md`
2. Просмотреть все утвержденные решения этапов 1-3
3. Собрать отдельные UI-компоненты
4. Интегрировать CSS темы
5. Добавить анимации и взаимодействия
6. Объединить в один HTML-файл
7. Проверить адаптивное поведение
8. Сохранить в папку `design_iterations`
9. **Обновить файл плана** путями выходных файлов
10. Показать пользователю для проверки
11. **Обновить файл плана** обратной связью пользователя и финальным статусом одобрения

## Результат

- Полный HTML-файл со встроенным или подключенным CSS
- Обновленный файл плана с завершенным этапом 4 и документированными выходными файлами

## Организация файлов

```
design_iterations/
├── theme_1.css              # Theme file from Stage 2
├── dashboard_1.html         # Initial design
├── dashboard_1_1.html       # First iteration
├── dashboard_1_2.html       # Second iteration
├── chat_ui_1.html           # Different design
└── chat_ui_1_1.html         # Iteration of chat UI
```

## Правила именования

| Тип | Формат | Пример |
|------|--------|---------|
| Начальный дизайн | `{name}_1.html` | `table_1.html` |
| Первая итерация | `{name}_1_1.html` | `table_1_1.html` |
| Вторая итерация | `{name}_1_2.html` | `table_1_2.html` |
| Новый дизайн | `{name}_2.html` | `table_2.html` |

## Чеклист реализации

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Design Name</title>
  
  <!-- ✅ Preconnect to external resources -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <!-- ✅ Load fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- ✅ Load Tailwind (script tag, not stylesheet) -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- ✅ Load Flowbite if needed -->
  <link href="https://cdn.jsdelivr.net/npm/flowbite@2.0.0/dist/flowbite.min.css" rel="stylesheet">
  
  <!-- ✅ Load icons -->
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  
  <!-- ✅ Link theme CSS -->
  <link rel="stylesheet" href="theme_1.css">
  
  <!-- ✅ Custom styles with !important for overrides -->
  <style>
    body {
      font-family: 'Inter', sans-serif !important;
      color: var(--foreground) !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
      font-weight: 600 !important;
    }
    
    /* Custom animations */
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
      animation: fadeIn 300ms ease-out;
    }
  </style>
</head>
<body>
  <!-- ✅ Semantic HTML structure -->
  <header>
    <!-- Header content -->
  </header>
  
  <main>
    <!-- Main content -->
  </main>
  
  <footer>
    <!-- Footer content -->
  </footer>
  
  <!-- ✅ Load Flowbite JS if needed -->
  <script src="https://cdn.jsdelivr.net/npm/flowbite@2.0.0/dist/flowbite.min.js"></script>
  
  <!-- ✅ Initialize icons -->
  <script>
    lucide.createIcons();
  </script>
  
  <!-- ✅ Custom JavaScript -->
  <script>
    // Interactive functionality
  </script>
</body>
</html>
```

## Лучшие практики

✅ **Делайте**:
- Используйте один HTML-файл на дизайн
- Загружайте Tailwind через тег script
- Ссылайтесь на CSS-файл темы
- Используйте `!important` для переопределений фреймворка
- Проверяйте адаптивное поведение
- Добавляйте alt-текст для изображений
- Используйте семантический HTML

❌ **Не делайте**:
- Не разбивайте на несколько файлов
- Не загружайте Tailwind как stylesheet
- Не инлайните все стили
- Не пропускайте атрибуты доступности
- Не используйте выдуманные URL изображений
- Не используйте «div-суп» (несемантический HTML)

## Точка одобрения

"Пожалуйста, проверьте дизайн. Нужны изменения или итерации?"

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Этап 3: Анимация](./design-iteration-stage-animation.md)
- [Лучшие практики](./design-iteration-best-practices.md)
- [Процесс итераций](./design-iteration-plan-iterations.md)
