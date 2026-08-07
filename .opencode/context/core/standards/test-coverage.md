<!-- Context: standards/tests | Priority: critical | Version: 2.0 | Updated: 2025-01-21 -->

# Стандарты тестирования

## Краткая справка

**Золотое правило**: Если это сложно тестировать — отрефакторьте

**Паттерн AAA**: Arrange → Act → Assert

**Тестируйте** (✅ делайте):
- Основной сценарий, крайние случаи, ошибки
- Бизнес-логику, публичные API

**Не тестируйте** (❌ не делайте):
- Сторонние библиотеки, внутренности фреймворка
- Простые getters/setters, приватные детали

**Покрытие**: критическое (100%), высокое (90%+), среднее (80%+)

---

## Принципы

**Тестируйте поведение, а не реализацию**: Фокус на том, что делает код, а не как
**Держите тесты простыми**: Один assert на тест, ясные имена, минимум настройки
**Независимые тесты**: Без общего состояния, запуск в любом порядке
**Быстрые и надежные**: Быстро выполняются, не flaky, детерминированы

## Структура теста (паттерн AAA)

```javascript
test('calculateTotal returns sum of item prices', () => {
  // Arrange - Set up test data
  const items = [{ price: 10 }, { price: 20 }, { price: 30 }];
  
  // Act - Execute code
  const result = calculateTotal(items);
  
  // Assert - Verify result
  expect(result).toBe(60);
});
```

## Что тестировать

### ✅ Что тестировать
- Основной сценарий (нормальное использование)
- Крайние случаи (границы, пустые значения, null, undefined)
- Ошибки (некорректный ввод, сбои)
- Бизнес-логику (ключевая функциональность)
- Публичные API (экспортируемые функции)

### ❌ Что не тестировать
- Сторонние библиотеки
- Внутренности фреймворка
- Простые getters/setters
- Приватные детали реализации

## Цели покрытия

1. **Критическое**: Бизнес-логика, преобразования данных (100%)
2. **Высокое**: Публичные API, пользовательские фичи (90%+)
3. **Среднее**: Утилиты, helpers (80%+)
4. **Низкое**: Простые обертки, конфиги (опционально)

## Тестирование чистых функций

```javascript
function add(a, b) { return a + b; }

test('add returns sum', () => {
  expect(add(2, 3)).toBe(5);
  expect(add(-1, 1)).toBe(0);
  expect(add(0, 0)).toBe(0);
});
```

## Тестирование с зависимостями

```javascript
// Testable with dependency injection
function createUserService(database) {
  return {
    getUser: (id) => database.findById('users', id)
  };
}

// Test with mock
test('getUser retrieves from database', () => {
  const mockDb = {
    findById: jest.fn().mockReturnValue({ id: 1, name: 'John' })
  };
  
  const service = createUserService(mockDb);
  const user = service.getUser(1);
  
  expect(mockDb.findById).toHaveBeenCalledWith('users', 1);
  expect(user).toEqual({ id: 1, name: 'John' });
});
```

## Именование тестов

```javascript
// ✅ Good: Descriptive, clear expectation
test('calculateDiscount returns 10% off for premium users', () => {});
test('validateEmail returns false for invalid format', () => {});
test('createUser throws error when email exists', () => {});

// ❌ Bad: Vague, unclear
test('it works', () => {});
test('test user', () => {});
```

## Лучшие практики

✅ Тестируйте одну вещь в одном тесте
✅ Используйте описательные имена тестов
✅ Держите тесты независимыми
✅ Мокайте внешние зависимости
✅ Тестируйте крайние случаи и ошибки
✅ Делайте тесты читаемыми
✅ Запускайте тесты часто
✅ Сразу исправляйте падающие тесты

**Золотое правило**: Если это сложно тестировать — отрефакторьте.
