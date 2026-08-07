<!-- Context: standards/docs | Priority: critical | Version: 2.0 | Updated: 2025-01-21 -->

# Стандарты документации

## Краткая справка

**Золотое правило**: Если пользователи дважды задают один вопрос — задокументируйте ответ

**Документируйте** (✅ делайте):
- ПОЧЕМУ были приняты решения
- Сложные алгоритмы/логику
- Публичные API, настройку, типовые сценарии

**Не документируйте** (❌ не делайте):
- Очевидный код (`i++` не требует комментария)
- Что делает код (это должно быть понятно из самого кода)

**Принципы**: Ориентация на аудиторию, показывайте вместо объяснений, поддерживайте актуальность

---

## Принципы

**Ориентация на аудиторию**: Пишите для пользователей (что/как), разработчиков (почему/когда), контрибьюторов (настройка/соглашения)
**Показывайте вместо объяснений**: Примеры кода, реальные сценарии, ожидаемый вывод
**Поддерживайте актуальность**: Обновляйте вместе с кодом, удаляйте устаревшее, помечайте deprecated

## Структура README

```markdown
# Project Name
Brief description (1-2 sentences)

## Features
- Key feature 1
- Key feature 2

## Installation
```bash
npm install package-name
```

## Быстрый старт
```javascript
const result = doSomething();
```

## Использование
[Detailed examples]

## API Reference
[If applicable]

## Contributing
[Link to CONTRIBUTING.md]

## License
[License type]
```

## Документация функций

```javascript
/**
 * Calculate total price including tax
 * 
 * @param {number} price - Base price
 * @param {number} taxRate - Tax rate (0-1)
 * @returns {number} Total with tax
 * 
 * @example
 * calculateTotal(100, 0.1) // 110
 */
function calculateTotal(price, taxRate) {
  return price * (1 + taxRate);
}
```

## Что документировать

### ✅ Делайте
- **ПОЧЕМУ** были приняты решения
- Сложные алгоритмы/логику
- Неочевидное поведение
- Публичные API
- Настройку/установку
- Типовые сценарии
- Известные ограничения
- Обходные решения (с объяснением)

### ❌ Не делайте
- Очевидный код (`i++` не требует комментария)
- Что делает код (это должно быть понятно из самого кода)
- Избыточную информацию
- Устаревшую/некорректную информацию

## Комментарии

### Хорошо
```javascript
// Calculate discount by tier (Bronze: 5%, Silver: 10%, Gold: 15%)
const discount = getDiscountByTier(customer.tier);

// HACK: API returns null instead of [], normalize it
const items = response.items || [];

// TODO: Use async/await when Node 18+ is minimum
```

### Плохо
```javascript
// Increment i
i++;

// Get user
const user = getUser();
```

## Документация API

```markdown
### POST /api/users
Create a new user

**Request:**
```json
{ "name": "John", "email": "john@example.com" }
```

**Response:**
```json
{ "id": "123", "name": "John", "email": "john@example.com" }
```

**Errors:**
- 400 - Invalid input
- 409 - Email exists
```

## Лучшие практики

✅ Объясняйте ПОЧЕМУ, а не только ЧТО
✅ Добавляйте рабочие примеры
✅ Показывайте ожидаемый вывод
✅ Описывайте обработку ошибок
✅ Используйте согласованную терминологию
✅ Держите структуру предсказуемой
✅ Обновляйте при изменениях кода

**Золотое правило**: Если пользователи дважды задают один вопрос — задокументируйте ответ.
