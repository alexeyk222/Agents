<!-- Context: core/codebase-references | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Ссылки на кодовую базу

**Назначение**: связывать файлы контекста с фактической реализацией в коде

**Последнее обновление**: 2026-01-27

---

## Основной принцип

<rule id="link_to_code" enforcement="critical">
  ВСЕ файлы контекста ДОЛЖНЫ по возможности включать раздел `📂 Codebase References` со ссылками на релевантный код.
  Используйте разделы, подходящие вашему типу контекста (не всем файлам нужны все разделы).
</rule>

**Почему**: агентам нужно находить фактическую реализацию, а не только читать о ней.

---

## Типы разделов (используйте релевантное)

### Контекст бизнес-домена
```markdown
**Business Logic**: (MOST IMPORTANT for business domains)
- `src/orders/rules/validation-rules.ts` - Order validation business rules

**Implementation**:
- `src/orders/order-processor.ts` - Main order processing logic

**Models/Types**:
- `src/orders/models/order.model.ts` - Order data model

**Tests**:
- `src/orders/__tests__/processor.test.ts` - Order processing tests

**Configuration**:
- `config/orders.config.ts` - Order processing config
```

### Технический/кодовый контекст
```markdown
**Implementation**: (MOST IMPORTANT for technical contexts)
- `src/auth/jwt-handler.ts` - JWT authentication implementation

**Examples**:
- `src/auth/examples/jwt-example.ts` - Working JWT example

**Types**:
- `src/auth/types/jwt-payload.ts` - JWT payload types

**Tests**:
- `src/auth/__tests__/jwt.test.ts` - JWT tests
```

### Контекст стандартов/качества
```markdown
**Validation/Enforcement**: (MOST IMPORTANT for standards)
- `scripts/validate-code-quality.ts` - Code quality validator
- `eslint.config.js` - ESLint rules

**Examples**:
- `examples/good-code.ts` - Good code example
- `examples/bad-code.ts` - Anti-pattern example

**Tests**:
- `tests/code-quality.test.ts` - Quality validation tests
```

### Операционный контекст
```markdown
**Scripts/Tools**: (MOST IMPORTANT for operations)
- `scripts/deploy.sh` - Deployment script
- `scripts/monitor.ts` - Monitoring setup

**Configuration**:
- `config/deployment.config.ts` - Deployment configuration
- `.github/workflows/deploy.yml` - CI/CD workflow
```

---

## Правила

<rule id="path_format" enforcement="strict">
  1. Используйте пути относительно проекта (src/..., не /Users/...)
  2. Используйте прямые слэши (/)
  3. Указывайте расширение файла (.ts, .js, .sh)
  4. Давайте краткое описание (3-10 слов) для каждого файла
  5. Проверяйте, что файлы существуют (предупреждайте, если не найдены)
  6. Используйте только релевантные разделы (не всем файлам нужны все разделы)
</rule>

---

## Примеры

**Бизнес-контекст**:
```markdown
## 📂 Codebase References

**Business Logic**:
- `src/payments/rules/validation-rules.ts` - Card validation rules
- `src/payments/rules/fraud-detection.ts` - Fraud detection logic

**Implementation**:
- `src/payments/payment-processor.ts` - Main payment processing

**Tests**:
- `src/payments/__tests__/processor.test.ts` - Payment tests
```

**Технический контекст**:
```markdown
## 📂 Codebase References

**Implementation**:
- `src/auth/jwt-handler.ts` - JWT authentication

**Examples**:
- `examples/jwt-auth.ts` - Working example

**Tests**:
- `src/auth/__tests__/jwt.test.ts` - JWT tests
```

---

## Валидация

- [ ] Есть раздел "📂 Codebase References"?
- [ ] Включен самый важный раздел для типа контекста?
- [ ] Пути указаны относительно проекта?
- [ ] Пути включают расширения?
- [ ] У каждого пути есть описание 3-10 слов?

---

## Связанные материалы

- frontmatter.md - формат frontmatter
- templates.md - шаблоны файлов
- structure.md - организация файлов
- templates/ - шаблоны файлов со ссылками на кодовую базу
