# Формат frontmatter

**Назначение**: формат HTML-комментария frontmatter для всех файлов контекста

**Последнее обновление**: 2026-01-27

---

## Формат

<rule id="frontmatter_required" enforcement="strict">
  ВСЕ файлы контекста ДОЛЖНЫ начинаться с:
  
  ```markdown
  <!-- Context: {category}/{function} | Priority: {level} | Version: X.Y | Updated: YYYY-MM-DD -->
  ```
</rule>

---

## Компоненты

**Category/Function**: `{category}/{function}`
- Примеры: `ecommerce/concepts`, `development/examples`, `core/standards`
- Category = домен (ecommerce, payments, development)
- Function = тип файла (concepts, examples, guides, lookup, errors)

**Priority**: `critical` | `high` | `medium` | `low`
- critical: 80% сценариев (бизнес-логика, ключевые концепции)
- high: 15% сценариев (типовые процессы, примеры)
- medium: 4% сценариев (крайние случаи)
- low: 1% сценариев (редкие сценарии)

**Version**: `X.Y` (начинайте с 1.0, повышайте при изменениях)

**Updated**: `YYYY-MM-DD` (ISO 8601, должно совпадать с разделом metadata)

---

## Примеры

```markdown
<!-- Context: ecommerce/concepts | Priority: critical | Version: 1.0 | Updated: 2026-01-27 -->
<!-- Context: payments/guides | Priority: high | Version: 1.2 | Updated: 2026-01-27 -->
<!-- Context: development/examples | Priority: medium | Version: 1.0 | Updated: 2026-01-27 -->
```

---

## Валидация

- [ ] Frontmatter находится на первой строке?
- [ ] Формат точный: `<!-- Context: ... -->`?
- [ ] Priority равен critical|high|medium|low?
- [ ] Version имеет формат X.Y?
- [ ] Дата имеет формат YYYY-MM-DD?

---

## Связанные материалы

- structure.md - организация файлов
- templates.md - шаблоны файлов
- codebase-references.md - ссылки на код
