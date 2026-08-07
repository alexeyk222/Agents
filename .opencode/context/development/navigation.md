<!-- Context: development/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по разработке

**Назначение**: Разработка ПО для всех стеков

---

## Структура

```
development/
├── navigation.md
├── ui-navigation.md           # Специализированная
├── backend-navigation.md      # Специализированная
├── fullstack-navigation.md    # Специализированная
│
├── principles/                # Универсальные (не зависят от языка)
│   ├── navigation.md
│   ├── clean-code.md
│   └── api-design.md
│
├── frameworks/                # Full-stack-фреймворки
│   ├── navigation.md
│   └── tanstack-start/
│
├── ai/                        # AI и агенты
│   ├── navigation.md
│   └── mastra-ai/
│
├── frontend/                  # Клиентская часть
│   ├── navigation.md
│   ├── when-to-delegate.md    # Когда использовать frontend-specialist
│   └── react/
│       ├── navigation.md
│       └── react-patterns.md
│
├── backend/                   # Серверная часть (будущее)
│   ├── navigation.md
│   ├── api-patterns/
│   ├── nodejs/
│   ├── python/
│   └── authentication/
│
├── data/                      # Слой данных (будущее)
│   ├── navigation.md
│   ├── sql-patterns/
│   ├── nosql-patterns/
│   └── orm-patterns/
│
├── integration/               # Связь систем (будущее)
│   ├── navigation.md
│   ├── package-management/
│   ├── api-integration/
│   └── third-party-services/
│
└── infrastructure/            # DevOps (будущее)
    ├── navigation.md
    ├── docker/
    └── ci-cd/
```

---

## Быстрые маршруты

| Задача | Путь |
|------|------|
| **UI/Frontend** | `ui-navigation.md` |
| **Когда делегировать frontend** | `frontend/when-to-delegate.md` |
| **Backend/API** | `backend-navigation.md` |
| **Full-stack** | `fullstack-navigation.md` |
| **Чистый код** | `principles/clean-code.md` |
| **Проектирование API** | `principles/api-design.md` |

---

## По области

**Принципы** → Универсальные практики разработки
**Фреймворки** → Full-stack-фреймворки (Tanstack Start, Next.js)
**AI** → AI-фреймворки и среды выполнения агентов (MAStra AI)
**Frontend** → Паттерны React и проектирование компонентов
**Backend** → API, Node.js, Python, аутентификация (будущее)
**Данные** → SQL, NoSQL, ORM (будущее)
**Интеграция** → Пакеты, API, сервисы (будущее)
**Инфраструктура** → Docker, CI/CD (будущее)

---

## Связанный контекст

- **Базовые стандарты** → `../core/standards/navigation.md`
- **Паттерны UI** → `../ui/navigation.md`
