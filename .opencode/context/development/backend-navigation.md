<!-- Context: development/navigation | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по backend-разработке

**Область**: Серверная часть, API, базы данных, аутентификация

---

## Структура

```
development/backend/           # [future]
├── navigation.md
│
├── api-patterns/              # По подходу
│   ├── rest-design.md
│   ├── graphql-design.md
│   ├── grpc-patterns.md
│   └── websocket-patterns.md
│
├── nodejs/                    # По технологии
│   ├── express-patterns.md
│   ├── fastify-patterns.md
│   └── error-handling.md
│
├── python/
│   ├── fastapi-patterns.md
│   └── django-patterns.md
│
├── authentication/            # Функциональная область
│   ├── jwt-patterns.md
│   ├── oauth-patterns.md
│   └── session-management.md
│
└── middleware/
    ├── logging.md
    ├── rate-limiting.md
    └── cors.md
```

---

## Быстрые маршруты

| Задача | Путь |
|------|------|
| **REST API** | `backend/api-patterns/rest-design.md` [future] |
| **GraphQL** | `backend/api-patterns/graphql-design.md` [future] |
| **Принципы проектирования API** | `principles/api-design.md` |
| **Node.js** | `backend/nodejs/express-patterns.md` [future] |
| **Python** | `backend/python/fastapi-patterns.md` [future] |
| **Аутентификация (JWT)** | `backend/authentication/jwt-patterns.md` [future] |

---

## По подходу

**REST** → `backend/api-patterns/rest-design.md` [future]
**GraphQL** → `backend/api-patterns/graphql-design.md` [future]
**gRPC** → `backend/api-patterns/grpc-patterns.md` [future]

## По языку

**Node.js** → `backend/nodejs/` [future]
**Python** → `backend/python/` [future]

## По области

**Аутентификация** → `backend/authentication/` [future]
**Middleware** → `backend/middleware/` [future]
**Слой данных** → `data/` [future]

---

## Связанный контекст

- **Принципы проектирования API** → `principles/api-design.md`
- **Базовые стандарты** → `../core/standards/code-quality.md`
- **Паттерны данных** → `data/navigation.md` [future]
