<!-- Context: core/mvi | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Принцип MVI (минимально жизнеспособная информация)

**Назначение**: извлекать только ключевые идеи, а не подробные объяснения

**Последнее обновление**: 2026-01-06

---

## Ключевая идея

Извлекайте **минимум информации**, достаточный AI-агенту для понимания и применения концепции:
- Ключевая идея (1-3 предложения)
- Ключевые моменты (3-5 пунктов)
- Минимальный рабочий пример
- Ссылка на полную документацию

**Цель**: сканируется за <30 секунд. Ссылайтесь на полную документацию, не дублируйте ее.

---

## Формула

```
Core Concept (1-3 sentences)
  ↓
Key Points (3-5 bullets)
  ↓
Quick Example (5-10 lines)
  ↓
Reference Link (full docs)
  ↓
Related Files (cross-refs)
```

---

## Что извлекать ✅

- **Ключевые определения** - что это (1-3 предложения)
- **Ключевые свойства** - важные характеристики (3-5 пунктов)
- **Минимальный пример** - самый простой рабочий код (5-10 строк)
- **Распространенные паттерны** - как обычно используется (2-3 пункта)
- **Критичные подводные камни** - обязательные к знанию проблемы (1–2 пункта)
- **Ссылки** - где узнать больше

---

## Что пропускать ❌

- **Многословные объяснения** - вместо этого дайте ссылку на документацию
- **Полную API-документацию** - кратко резюмируйте + дайте ссылку
- **Детали реализации** - покажите минимальный пример + ссылку
- **Исторический контекст** - только если критичен для понимания
- **Маркетинговый текст** - только факты
- **Дублирующую информацию** - скажите один раз, дальше ссылайтесь

---

## Пример: аутентификация JWT

### ❌ Слишком многословно (400+ строк)
```markdown
# JWT Authentication

JSON Web Tokens (JWT) are an open standard (RFC 7519) that defines 
a compact and self-contained way for securely transmitting information 
between parties as a JSON object. This information can be verified and 
trusted because it is digitally signed. JWTs can be signed using a 
secret (with the HMAC algorithm) or a public/private key pair using RSA 
or ECDSA.

[... 400 more lines of explanation, examples, edge cases ...]
```

### ✅ Соответствует MVI (~50 строк)
```markdown
# Concept: JWT Authentication

**Core Idea**: Stateless authentication using JSON Web Tokens signed 
with a secret key. Token contains user data (payload) that server can 
trust because signature is verified.

**Key Points**:
- Token has 3 parts: header.payload.signature (Base64 encoded)
- Server verifies signature to trust payload without database lookup
- No session storage needed (stateless)
- Tokens expire (include `exp` claim)
- Store in httpOnly cookie or Authorization header

**Quick Example**:
```js
// Sign token
const token = jwt.sign(
  { userId: 123, role: 'admin' }, 
  SECRET_KEY, 
  { expiresIn: '1h' }
)

// Verify token
const decoded = jwt.verify(token, SECRET_KEY)
console.log(decoded.userId) // 123
```

**Reference**: https://jwt.io/introduction

**Related**: 
- examples/jwt-auth-example.md
- guides/implementing-jwt.md
- errors/auth-errors.md
```

---

## Ограничения размера файлов

<rule id="size_limits" enforcement="strict">
  - Файлы Concept: максимум 100 строк
  - Файлы Example: максимум 80 строк
  - Файлы Guide: максимум 150 строк
  - Файлы Lookup: максимум 100 строк
  - Файлы Error: максимум 150 строк
  - Файлы README: максимум 100 строк
</rule>

**Почему**: заставляет быть краткими. Если нужно больше, разбейте на несколько файлов или дайте ссылку на внешнюю документацию.

---

## Чеклист валидации

Перед созданием файла контекста проверьте:

- [ ] Ключевая идея занимает 1-3 предложения?
- [ ] Ключевые моменты — 3-5 пунктов?
- [ ] Пример содержит <10 строк кода?
- [ ] Ссылка на источник добавлена?
- [ ] Файл <200 строк всего?
- [ ] Файл можно просмотреть за <30 секунд?

Если любой ответ — «нет», сожмите сильнее.

---

## Связанные материалы

- structure.md - где размещать файлы
- compact.md - как минимизировать
- templates.md - стандартные форматы
- creation.md - правила создания файлов
