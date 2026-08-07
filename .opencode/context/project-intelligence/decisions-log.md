<!-- Context: project-intelligence/decisions | Priority: high | Version: 1.0 | Updated: 2025-01-12 -->

# Журнал решений

> Фиксируйте ключевые архитектурные и бизнес-решения с полным контекстом. Это предотвращает споры в стиле «почему так сделали?».

## Краткая справка

- **Назначение**: документировать решения, чтобы будущие участники команды понимали контекст
- **Формат**: каждое решение отдельной записью
- **Статус**: Decided | Pending | Under Review | Deprecated

## Шаблон решения

```markdown
## [Decision Title]

**Date**: YYYY-MM-DD
**Status**: [Decided/Pending/Under Review/Deprecated]
**Owner**: [Who owns this decision]

### Context
[What situation prompted this decision? What was the problem or opportunity?]

### Decision
[What was decided? Be specific about the choice made.]

### Rationale
[Why this decision? What were the alternatives and why were they rejected?]

### Alternatives Considered
| Alternative | Pros | Cons | Why Rejected? |
|-------------|------|------|---------------|
| [Alt 1] | [Pros] | [Cons] | [Why not chosen] |
| [Alt 2] | [Pros] | [Cons] | [Why not chosen] |

### Impact
**Positive**: [What this enables or improves]
**Negative**: [What trade-offs or limitations this creates]
**Risk**: [What could go wrong]

### Related
- [Links to related decisions, PRs, issues, or documentation]
```

---

## Решение: [Title]

**Дата**: YYYY-MM-DD
**Статус**: [Status]
**Владелец**: [Owner]

### Контекст
[What was happening? Why did we need to decide?]

### Решение
[What we decided]

### Обоснование
[Why this was the right choice]

### Рассмотренные альтернативы
| Альтернатива | Плюсы | Минусы | Почему отклонено? |
|-------------|------|------|---------------|
| [Option A] | [Good things] | [Bad things] | [Reason] |
| [Option B] | [Good things] | [Bad things] | [Reason] |

### Влияние
- **Положительное**: [What we gain]
- **Отрицательное**: [What we trade off]
- **Риск**: [What to watch for]

### Связанные материалы
- [Link to PR #000]
- [Link to issue #000]
- [Link to documentation]

---

## Решение: [Title]

**Дата**: YYYY-MM-DD
**Статус**: [Status]
**Владелец**: [Owner]

### Контекст
[What was happening?]

### Решение
[What we decided]

### Обоснование
[Why this was right]

### Рассмотренные альтернативы
| Альтернатива | Плюсы | Минусы | Почему отклонено? |
|-------------|------|------|---------------|
| [Option A] | [Good things] | [Bad things] | [Reason] |

### Влияние
- **Положительное**: [What we gain]
- **Отрицательное**: [What we trade off]

### Связанные материалы
- [Link]

---

## Устаревшие решения

Решения, которые позже были отменены (для исторического контекста):

| Решение | Дата | Заменено на | Почему |
|----------|------|-------------|-----|
| [Old decision] | [Date] | [New decision] | [Reason] |

## Чеклист онбординга

- [ ] Понимать философию ключевых архитектурных выборов
- [ ] Знать, почему конкретные технологии выбраны вместо альтернатив
- [ ] Понимать сделанные компромиссы
- [ ] Знать, где искать контекст решений при вопросах
- [ ] Понимать, какие решения ожидают принятия и почему

## Связанные файлы

- `technical-domain.md` - Техническая реализация, на которую влияют эти решения
- `business-tech-bridge.md` - Как решения связывают бизнес и технологии
- `living-notes.md` - Текущие открытые вопросы, которые могут стать решениями
