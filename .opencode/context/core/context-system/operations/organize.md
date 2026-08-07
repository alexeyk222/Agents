<!-- Context: core/organize | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Organize

**Назначение**: преобразовать плоские файлы контекста в структуру папок по функциям

**Последнее обновление**: 2026-01-06

---

## Когда использовать

- Миграция с плоской структуры на структуру по функциям
- Очистка неорганизованных каталогов контекста
- Разделение неоднозначных файлов на правильные категории
- Разрешение дублирующихся/конфликтующих файлов

---

## 8-этапный workflow

### Этап 1: сканирование
**Действие**: просканировать категорию на все файлы и определить структуру

**Выход**: список файлов с текущим типом структуры (плоская или организованная)

---

### Этап 2: категоризация
**Действие**: категоризировать каждый файл по функции

**Правила категоризации**:
- Объясняет концепцию? → `concepts/`
- Показывает рабочий код? → `examples/`
- Пошаговые инструкции? → `guides/`
- Справочные данные (таблицы, команды)? → `lookup/`
- Ошибки/проблемы? → `errors/`

**Выход**: план категоризации с отмеченными неоднозначными файлами

---

### Этап 3: разрешить конфликты (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать план категоризации и обработать конфликты

**Формат**:
```
Organizing {category}/ (23 files, flat structure)

Clear categorization (18 files):
  concepts/ (8):
    ✓ authentication.md → concepts/authentication.md
  
  examples/ (5):
    ✓ jwt-example.md → examples/jwt-example.md

Ambiguous files (5 - need your input):
  
  [?] api-design.md (contains concepts AND steps)
      → [A] Split: concepts/api-design.md + guides/api-design-guide.md
      → [B] Keep as concepts/api-design.md
      → [C] Keep as guides/api-design.md

Conflicts (2):
  
  [!] authentication.md → concepts/auth.md
      Target already exists (120 lines)
      → [J] Merge into existing
      → [K] Rename to concepts/authentication-v2.md
      → [L] Skip (keep flat)

Select resolutions (A J or 'auto'):
```

**Валидация**: ОБЯЗАТЕЛЬНО дождаться ввода пользователя

---

### Этап 4: предварительный просмотр (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать предварительный просмотр всех изменений

**Формат**:
```
Preview changes:

CREATE directories:
  {category}/concepts/
  {category}/examples/
  {category}/guides/
  {category}/lookup/
  {category}/errors/

MOVE files (18):
  authentication.md → concepts/authentication.md
  ... (17 more)

SPLIT files (3):
  api-design.md → concepts/api-design.md + guides/api-design-guide.md

MERGE files (2):
  authentication.md → concepts/auth.md (merge content)

UPDATE:
  {category}/README.md
  Fix 47 internal references

Dry-run? (yes/no/show-diff):
```

**Dry-run**: симулирует изменения без выполнения

**Валидация**: ОБЯЗАТЕЛЬНО получить одобрение перед продолжением

---

### Этап 5: резервная копия
**Действие**: создать резервную копию перед внесением изменений

**Расположение**: `.tmp/backup/organize-{category}-{timestamp}/`

**Назначение**: включить откат при необходимости

---

### Этап 6: выполнение
**Действие**: выполнить реорганизацию

**Процесс**:
1. Создать функциональные папки
2. Переместить файлы в правильные места
3. Разделить неоднозначные файлы, если запрошено
4. Слить конфликты, если запрошено

---

### Этап 7: обновление
**Действие**: обновить навигацию и исправить ссылки

**Процесс**:
1. Обновить навигационные таблицы в `README.md`
2. Исправить все внутренние ссылки на перемещенные файлы
3. Проверить, что все ссылки работают
4. Обновить даты "Last Updated"

---

### Этап 8: отчет
**Действие**: показать полные результаты

**Формат**:
```
✅ Organized X files into function folders
📁 Created Y new folders
🔀 Split Z ambiguous files
🔗 Fixed N references
💾 Backup: .tmp/backup/organize-{category}-{timestamp}/

Rollback available if needed.
```

---

## Разрешение конфликтов

### Неоднозначные файлы
Файл подходит нескольким категориям (например, содержит concepts И steps)

**Варианты**:
- Разделить на несколько файлов (рекомендуется)
- Оставить в основной категории
- Пользователь решает, какая категория основная

### Дублирующиеся цели
Целевой файл уже существует

**Варианты**:
- Слить содержимое в существующий файл
- Переименовать, чтобы избежать конфликта (например, -v2)
- Пропустить (оставить в плоской структуре)

### Авторазрешение
Агент предлагает лучший вариант на основе:
- Размера файла
- Анализа содержимого
- Существующей структуры

---

## Примеры

### Организовать плоский каталог
```bash
/context organize development/
```

### Сначала dry-run
```bash
/context organize development/ --dry-run
```

### Организовать несколько
```bash
/context organize development/
/context organize core/
```

---

## Критерии успеха

- [ ] Все файлы в функциональных папках (не плоско)?
- [ ] Неоднозначные файлы разрешены?
- [ ] Конфликты обработаны?
- [ ] `README.md` создан/обновлен?
- [ ] Все ссылки исправлены?
- [ ] Резервная копия создана?
- [ ] Пользователь одобрил изменения?

---

## Связанные материалы

- standards/structure.md - правила организации папок
- guides/workflows.md - интерактивные примеры
