<!-- Context: core/navigation-templates | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Шаблоны файлов навигации

**Назначение**: готовые шаблоны для файлов навигации

---

## Шаблон навигации категории

```markdown
# {Category} Navigation

**Purpose**: [1 sentence]

---

## Structure

```
{category}/
├── navigation.md
├── {subcategory}/
│   ├── navigation.md
│   └── {files}.md
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **{Task 1}** | `{path}` |
| **{Task 2}** | `{path}` |
| **{Task 3}** | `{path}` |

---

## By {Concern/Type}

**{Section 1}** → {description}
**{Section 2}** → {description}
**{Section 3}** → {description}

---

## Related Context

- **{Category}** → `../{category}/navigation.md`
```

**Количество токенов**: ~200–250 токенов

---

## Шаблон специализированной навигации

```markdown
# {Domain} Navigation

**Scope**: [What this covers]

---

## Structure

```
{Relevant directories across multiple categories}
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **{Task 1}** | `{path}` |
| **{Task 2}** | `{path}` |

---

## By {Framework/Approach}

**{Tech 1}** → `{path}`
**{Tech 2}** → `{path}`

---

## Common Workflows

**{Workflow 1}**:
1. `{file1}` ({purpose})
2. `{file2}` ({purpose})
```

**Количество токенов**: ~250–300 токенов

---

## Хороший пример (токен-эффективный)

```markdown
# Development Navigation

**Purpose**: Software development across all stacks

---

## Structure

```
development/
├── navigation.md
├── ui-navigation.md
├── principles/
├── frontend/
├── backend/
└── data/
```

---

## Быстрые маршруты

| Task | Path |
|------|------|
| **UI/Frontend** | `ui-navigation.md` |
| **Backend/API** | `backend-navigation.md` |
| **Clean code** | `principles/clean-code.md` |

---

## By Concern

**Principles** → Universal practices
**Frontend** → React, Vue, state
**Backend** → APIs, Node, auth
**Data** → SQL, NoSQL, ORMs
```

**Количество токенов**: ~180 токенов ✅

---

## Плохой пример (слишком многословный)

```markdown
# Development Navigation

**Purpose**: This navigation file helps you find software development 
patterns, standards, and best practices across all technology stacks 
including frontend, backend, databases, and infrastructure.

---

## Introduction

The development category contains comprehensive guides and patterns 
for building modern applications. Whether you're working on frontend 
user interfaces, backend APIs, database integrations...

[... continues for 500+ tokens]
```

**Количество токенов**: 500+ токенов ❌

---

## Устранение неполадок

| Проблема | Решение |
|-------|----------|
| Слишком много токенов | Уберите многословные описания, сократите записи |
| Трудно сканировать | Используйте таблицы вместо абзацев |
| Не хватает файлов | Добавьте в структуру и быстрые маршруты |
| Неясные пути | Используйте относительные пути, добавьте краткие описания |

---

## Связанные материалы

- `navigation-design-basics.md` - основные принципы и шаги
- `../standards/mvi.md` - принцип MVI
- `../examples/navigation-examples.md` - больше примеров
