<!-- Context: workflows/delegation-specialists | Priority: high | Version: 1.0 | Updated: 2026-02-05 -->
# Когда делегировать специалистам

**Назначение**: рекомендации, когда делегировать конкретным агентам-специалистам

---

## OpenFrontendSpecialist - UI/UX-дизайн

**✅ ДЕЛЕГИРУЙТЕ, когда:**
- Создаете новый UI/UX-дизайн (landing pages, dashboards)
- Собираете дизайн-системы (компоненты, темы, style guides)
- Нужны сложные макеты с адаптивным дизайном
- Требуется визуальная полировка (анимации, transitions, micro-interactions)
- Страницы сфокусированы на бренде (маркетинг, showcases продукта)
- UI критичен для доступности

**Паттерн делегирования:**
```javascript
task(
  subagent_type="OpenFrontendSpecialist",
  description="Design {feature} UI",
  prompt="Load context from .tmp/sessions/{session-id}/context.md
  
  Design {feature} following 4-stage workflow:
  1. Stage 0: Create design plan file (MANDATORY FIRST)
  2. Stage 1: Layout (ASCII wireframe)
  3. Stage 2: Theme (design system, colors)
  4. Stage 3: Animation (micro-interactions)
  5. Stage 4: Implementation (single HTML file)
  
  Request approval between stages."
)
```

**Почему?** Следует структурированному 4-этапному процессу с точками одобрения и выдает отполированный UI.

---

## TestEngineer - написание тестов

**✅ ДЕЛЕГИРУЙТЕ, когда:**
- Пишете комплексные наборы тестов
- Используете TDD-workflows (тесты до реализации)
- Нужны сложные тестовые сценарии (крайние случаи, обработка ошибок)
- Нужны интеграционные тесты для нескольких компонентов

**Паттерн делегирования:**
```javascript
task(
  subagent_type="TestEngineer",
  description="Write tests for {feature}",
  prompt="Load context from .tmp/sessions/{session-id}/context.md
  
  Write comprehensive tests for {feature}
  Files to test: {file list}
  Follow test coverage standards from context."
)
```

---

## CodeReviewer - контроль качества

**✅ ДЕЛЕГИРУЙТЕ, когда:**
- Проверяете сложные реализации
- Нужен security-critical code review
- Нужны pre-merge проверки качества
- Нужна валидация архитектуры

**Паттерн делегирования:**
```javascript
task(
  subagent_type="CodeReviewer",
  description="Review {feature}",
  prompt="Load context from .tmp/sessions/{session-id}/context.md
  
  Review {feature} against standards
  Files: {file list}
  Focus: security, performance, maintainability"
)
```

---

## CoderAgent - сфокусированная реализация

**✅ ДЕЛЕГИРУЙТЕ, когда:**
- Реализуете атомарные подзадачи от TaskManager
- Работа изолирована (один компонент/модуль)
- Нужно строго следовать спецификациям реализации

**Паттерн делегирования:**
```javascript
task(
  subagent_type="CoderAgent",
  description="Implement {subtask}",
  prompt="Load context from .tmp/sessions/{session-id}/context.md
  
  Implement subtask: {description}
  Follow implementation spec exactly.
  Mark subtask complete when done."
)
```

---

## Матрица решений

| Сценарий | Агент | Почему |
|----------|-------|-----|
| Новый landing page | OpenFrontendSpecialist | 4-этапный процесс дизайна |
| Набор тестов для auth | TestEngineer | Комплексное покрытие |
| Security review | CodeReviewer | Фокус на безопасности |
| Один API-endpoint | CoderAgent | Сфокусированная реализация |
| Сложная multi-file фича | TaskManager → CoderAgent | Сначала декомпозиция, затем реализация |

---

## Ключевой принцип

**TestEngineer и CodeReviewer должны ВСЕГДА получать путь к контексту сессии.** Это гарантирует проверку по тем же стандартам, которые использовались при реализации.

---

## Связанные материалы

- `task-delegation-basics.md` - основной workflow делегирования
- `task-delegation-caching.md` - кэширование контекста
- `design-iteration-overview.md` - workflow OpenFrontendSpecialist
