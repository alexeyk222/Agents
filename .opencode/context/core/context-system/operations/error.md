<!-- Context: core/error | Priority: medium | Version: 1.0 | Updated: 2026-02-15 -->

# Операция Error

**Назначение**: добавлять повторяющиеся ошибки в базу знаний с дедупликацией

**Последнее обновление**: 2026-01-06

---

## Когда использовать

- Одна и та же ошибка встречалась несколько раз
- Нужно документировать решение для команды
- Формируется база знаний по ошибкам
- Нужно предотвратить повторную отладку

---

## 6-этапный workflow

### Этап 1: найти существующие
**Действие**: найти похожие/связанные ошибки

**Процесс**:
1. Искать сообщение ошибки во всех файлах `errors/`
2. Найти похожие ошибки (нечеткое совпадение)
3. Найти связанные ошибки (та же категория)

**Формат**:
```
Searching for: "Cannot read property 'map' of undefined"

Found 1 similar error:
  📄 development/errors/react-errors.md (Line 45)
     ## Error: Cannot read property 'X' of undefined
     Covers: General undefined property access
     Frequency: common

Found 2 related errors:
  📄 development/errors/react-errors.md
     ## Error: Cannot read property 'length' of undefined
     ## Error: Undefined is not an object
```

---

### Этап 2: проверить дублирование (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать варианты дедупликации

**Формат**:
```
Options:
  [A] Add as new error to react-errors.md
      (Specific case: 'map' on undefined array)
  
  [B] Update existing 'Cannot read property X' error
      (Add 'map' as common example)
  
  [C] Skip (already covered sufficiently)

Which framework/category?
  [1] React (react-errors.md)
  [2] JavaScript (js-errors.md)
  [3] General (common-errors.md)
  [4] Create new: ___

Select option + category (e.g., 'B 1'):
```

**Валидация**: ОБЯЗАТЕЛЬНО дождаться ввода пользователя

---

### Этап 3: предварительный просмотр (ТРЕБУЕТСЯ ОДОБРЕНИЕ)
**Действие**: показать полную запись ошибки перед добавлением

**Формат**:
```
Would update development/errors/react-errors.md:

Current (Line 45):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Error: Cannot read property 'X' of undefined

**Symptom**:
```
TypeError: Cannot read property 'X' of undefined
```

**Cause**: Attempting to access property on undefined/null object.

**Solution**:
1. Add null check
2. Use optional chaining (?.)
3. Provide default value

**Code**:
```jsx
// ❌ Before
const value = obj.property

// ✅ After
const value = obj?.property ?? 'default'
```

**Prevention**: Always validate data exists
**Frequency**: common
**Reference**: [Link]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Proposed update:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## Error: Cannot read property 'X' of undefined

**Symptom**:
```
TypeError: Cannot read property 'X' of undefined
TypeError: Cannot read property 'map' of undefined  ← NEW
TypeError: Cannot read property 'length' of undefined  ← NEW
```

**Cause**: Attempting to access property on undefined/null object.
Common with array methods (map, filter) when data hasn't loaded.  ← NEW

**Solution**:
1. Add null check
2. Use optional chaining (?.)
3. Provide default value (especially for arrays)  ← UPDATED

**Code**:
```jsx
// ❌ Before
const value = obj.property
const items = data.map(item => item.name)  ← NEW

// ✅ After
const value = obj?.property ?? 'default'
const items = (data || []).map(item => item.name)  ← NEW
```

**Prevention**: Always validate data exists. For arrays, provide empty array default.  ← UPDATED
**Frequency**: common
**Reference**: [Link]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File size: 98 lines → 105 lines (under 150 limit ✓)

Approve? (yes/no/edit):
```

**Режим edit**: разрешить изменение перед добавлением

**Валидация**: ОБЯЗАТЕЛЬНО получить одобрение перед продолжением

---

### Этап 4: добавить/обновить
**Действие**: добавить или обновить запись ошибки

**Процесс**:
1. Добавить/обновить ошибку в целевом файле
2. Следовать формату шаблона ошибок
3. Поддерживать размер файла <150 строк
4. Обновить дату "Last Updated"

**Формат шаблона**:
```markdown
## Error: {Name}

**Symptom**: [Error message]
**Cause**: [Why - 1-2 sentences]
**Solution**: [Steps]
**Code**: [Before/After example]
**Prevention**: [How to avoid]
**Frequency**: common/occasional/rare
**Reference**: [Link]
```

---

### Этап 5: обновить навигацию
**Действие**: обновить `README.md` и добавить перекрестные ссылки

**Процесс**:
1. Обновить `README.md`, если создан новый файл
2. Добавить перекрестные ссылки к связанным ошибкам
3. Добавить ссылки из связанных concepts/examples

---

### Этап 6: отчет
**Действие**: показать результаты

**Формат**:
```
✅ Added error to {category}/errors/{file}.md
🔗 Cross-referenced with X related errors
📊 Updated README.md (if needed)

Changes:
  - Updated existing error entry
  - Added 'map' and 'length' examples
  - File size: 105 lines (under 150 limit)
```

---

## Стратегия дедупликации

### Похожие ошибки
Одна корневая причина, разные проявления
→ **Обновить существующую**, добавив новые примеры

### Связанные ошибки
Разные причины, одна категория
→ Добавить **перекрестную ссылку** между ошибками

### Дублирующиеся ошибки
Та же самая ошибка уже документирована
→ **Пропустить** (уже покрыто)

### Новые ошибки
Уникальная ошибка еще не документирована
→ **Добавить как новую** запись ошибки

---

## Группировка ошибок

Группируйте ошибки по фреймворку/теме в одном файле:
- `react-errors.md` - все ошибки React
- `nextjs-errors.md` - все ошибки Next.js
- `auth-errors.md` - все ошибки аутентификации

**Не создавайте**: один файл на ошибку (слишком гранулярно)

---

## Примеры

### Добавить новую ошибку
```bash
/context error for "hooks can only be called inside components"
```

### Добавить распространенную ошибку
```bash
/context error for "Cannot read property 'map' of undefined"
```

### Добавить ошибку фреймворка
```bash
/context error for "Hydration failed in Next.js"
```

---

## Критерии успеха

- [ ] Поиск похожих ошибок выполнен?
- [ ] Варианты дедупликации показаны?
- [ ] Предварительный просмотр показан?
- [ ] Пользователь одобрил?
- [ ] Ошибка следует формату шаблона?
- [ ] Размер файла <150 строк?
- [ ] Перекрестные ссылки добавлены?
- [ ] `README.md` обновлен (если новый файл)?

---

## Связанные материалы

- standards/templates.md - формат шаблона ошибок
- guides/workflows.md - интерактивные примеры
