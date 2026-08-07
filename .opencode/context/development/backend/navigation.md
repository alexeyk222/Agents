<!-- Context: development/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по backend-разработке

**Назначение**: Паттерны серверной разработки

**Статус**: 🚧 Заготовка — контент скоро появится

---

## Планируемая структура

```
backend/
├── navigation.md
│
├── api-patterns/              # По подходу
│   ├── rest-design.md
│   ├── graphql-design.md
│   ├── grpc-patterns.md
│   └── trpc-patterns.md
│
├── nodejs/                    # По технологии
│   ├── express-patterns.md
│   ├── fastify-patterns.md
│   └── nextjs-api-routes.md
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

## Пока

Используйте специализированную навигацию: `../backend-navigation.md`

Также см.: `../principles/api-design.md`

---

## Связанный контекст

- **Навигация по backend** → `../backend-navigation.md`
- **Принципы проектирования API** → `../principles/api-design.md`
- **Базовые стандарты** → `../../core/standards/code-quality.md`
