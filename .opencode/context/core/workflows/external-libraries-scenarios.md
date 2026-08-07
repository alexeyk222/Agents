<!-- Context: workflows/external-libraries-scenarios | Priority: medium | Version: 1.0 | Updated: 2026-02-05 -->
# Внешние библиотеки: распространенные сценарии

**Назначение**: практические примеры использования ExternalScout

---

## Сценарий 1: новая сборка с внешними пакетами

**Пример**: приложение Next.js с Drizzle + Better Auth

**Процесс:**
1. Проверить install scripts: `ls scripts/install/`
2. Определить пакеты: Next.js, Drizzle ORM, Better Auth
3. Вызвать ExternalScout для каждого пакета
4. Проверить требования: PostgreSQL? Env vars?
5. Проверить совместимость версий
6. Реализовать по актуальной документации
7. Протестировать точки интеграции

**Вызовы ExternalScout:**
```javascript
// Drizzle ORM
task(
  subagent_type="ExternalScout",
  description="Fetch Drizzle PostgreSQL setup",
  prompt="Fetch Drizzle ORM docs: PostgreSQL setup w/ modular schemas
  Focus on: Installation | DB connection | Schema patterns | Migrations
  Context: Next.js commerce site w/ PostgreSQL"
)

// Next.js App Router
task(
  subagent_type="ExternalScout",
  description="Fetch Next.js App Router docs",
  prompt="Fetch Next.js docs: App Router w/ Server Actions
  Focus on: Installation | Directory structure | Server Actions
  Context: Commerce site w/ order processing"
)
```

---

## Сценарий 2: ошибка пакета во время сборки

**Пример**: `Error: Cannot find module 'drizzle-orm/pg-core'`

**Процесс:**
1. Определить пакет: Drizzle ORM
2. ExternalScout: "Fetch Drizzle docs: PostgreSQL imports"
3. Проверить текущие паттерны import
4. Убедиться, что в `package.json` правильные зависимости
5. Предложить исправление по актуальной документации
6. Запросить одобрение → применить исправление

---

## Сценарий 3: первая настройка пакета

**Пример**: настройка TanStack Query в Next.js

**Процесс:**
1. Проверить install scripts
2. ExternalScout: "Fetch TanStack Query docs: Next.js App Router setup"
3. Получить: шаги установки | peer deps | config | patterns
4. Если install script есть: review → run
5. Если скрипта нет: следовать документации для ручной настройки
6. Реализовать → протестировать

---

## Сценарий 4: обновление версии

**Пример**: Next.js 14 → 15

**Процесс:**
1. ExternalScout: "Fetch Next.js 15 docs: Breaking changes and migration"
2. Проверить breaking changes
3. Определить затронутый код
4. Спланировать шаги миграции
5. Запросить одобрение → реализовать → протестировать

---

## Практический пример: реализация Auth

**Задача**: "Add authentication with Better Auth to Next.js commerce"

```javascript
// 1. ContextScout: Project standards
task(
  subagent_type="ContextScout",
  description="Find auth standards",
  prompt="Find context files: Auth patterns | Security standards"
)
// Returns: security-patterns.md, code-quality.md

// 2. ExternalScout: Better Auth docs (MANDATORY)
task(
  subagent_type="ExternalScout",
  description="Fetch Better Auth + Next.js docs",
  prompt="Fetch Better Auth docs: Next.js App Router integration
  Focus on: Installation | App Router setup | Drizzle adapter | Session mgmt
  Context: Adding auth to Next.js commerce w/ Drizzle ORM"
)
// Returns: Installation | Integration patterns | Working examples

// 3. Combine and implement
// - Better Auth patterns (from ExternalScout)
// - Security standards (from ContextScout)
// = Secure, well-structured auth ✅
```

---

## Паттерны обработки ошибок

| Тип ошибки | Процесс |
|------------|---------|
| **Установка пакета** | ExternalScout: документация по установке → проверить имя/версию пакета → проверить peer deps |
| **Import/Module** | ExternalScout: паттерны import → проверить текущие API-exports |
| **API/конфигурация** | ExternalScout: API-документация → проверить текущие сигнатуры |
| **Ошибки сборки** | Определить пакет → ExternalScout: релевантная документация → проверить known issues |

---

## Связанные материалы

- `external-libraries-workflow.md` - основной workflow
- `external-libraries-faq.md` - FAQ по устранению неполадок
