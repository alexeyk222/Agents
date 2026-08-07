<!-- Context: development/navigation | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по full-stack-разработке

**Область**: Сквозная разработка приложений

---

## Распространённые стеки

### MERN (MongoDB, Express, React, Node)
```
Frontend: development/frontend/react/ [future]
Backend:  development/backend/nodejs/express-patterns.md [future]
Data:     development/data/nosql-patterns/mongodb.md [future]
API:      development/backend/api-patterns/rest-design.md [future]
```

### T3 Stack (Next.js, tRPC, Prisma, Tailwind)
```
Frontend: development/frontend/react/ + ui/web/ui-styling-standards.md [future]
Backend:  development/backend/nodejs/ + api-patterns/trpc-patterns.md [future]
Data:     development/data/orm-patterns/prisma.md [future]
```

### Full-stack на Python (FastAPI + React)
```
Frontend: development/frontend/react/ [future]
Backend:  development/backend/python/fastapi-patterns.md [future]
Data:     development/data/sql-patterns/ or nosql-patterns/ [future]
API:      development/backend/api-patterns/rest-design.md [future]
```

---

## Быстрые маршруты

| Слой | Куда идти |
|-------|-------------|
| **Frontend** | `ui-navigation.md` |
| **Backend** | `backend-navigation.md` |
| **Данные** | `data/navigation.md` [future] |
| **Интеграция** | `integration/navigation.md` [future] |
| **Инфраструктура** | `infrastructure/navigation.md` [future] |

---

## Типовые рабочие процессы

**Новый endpoint API**:
1. `principles/api-design.md` (принципы)
2. `backend/api-patterns/rest-design.md` (подход) [future]
3. `backend/nodejs/express-patterns.md` (реализация) [future]

**Новая возможность React**:
1. `frontend/react/component-architecture.md` (структура) [future]
2. `frontend/react/hooks-patterns.md` (логика) [future]
3. `ui/web/ui-styling-standards.md` (стилизация)

**Интеграция базы данных**:
1. `data/sql-patterns/` или `data/nosql-patterns/` (подход) [future]
2. `data/orm-patterns/` (если используется ORM) [future]
3. `backend/nodejs/` или `backend/python/` (реализация) [future]

**Сторонний сервис**:
1. `integration/third-party-services/` (паттерны) [future]
2. `integration/api-integration/` (использование API) [future]

---

## Связанный контекст

- **Чистый код** → `principles/clean-code.md`
- **Проектирование API** → `principles/api-design.md`
- **Базовые стандарты** → `../core/standards/navigation.md`
