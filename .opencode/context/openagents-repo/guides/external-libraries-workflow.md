<!-- Context: openagents-repo/guides/external-libraries-workflow | Priority: high | Version: 1.0 | Updated: 2026-01-29 -->
# Руководство: процесс для внешних библиотек

**Цель**: получать актуальную документацию по внешним пакетам при добавлении агентов или skills

**Когда использовать**: каждый раз, когда вы работаете с внешними библиотеками (Drizzle, Better Auth, Next.js и т. д.)

**Время чтения**: 5 минут

---

## Быстрый старт

**Золотое правило**: НИКОГДА не полагайтесь на training data для внешних библиотек → ВСЕГДА получайте актуальную документацию

**Процесс**:
1. Определите внешний пакет в задаче
2. Проверьте install-скрипты (если это первая настройка)
3. Используйте **ExternalScout**, чтобы получить актуальную документацию
4. Реализуйте с учетом свежих, version-specific знаний

---

## Когда использовать ExternalScout (ОБЯЗАТЕЛЬНО)

✅ **Используйте ExternalScout, когда**:
- Добавляете новых агентов, зависящих от внешних пакетов
- Добавляете новые skills, интегрирующиеся с внешними библиотеками
- Впервые настраиваете пакет в реализации
- Возникают ошибки пакетов/зависимостей
- Нужны обновления версий
- Выполняется ЛЮБАЯ работа с внешней библиотекой

❌ **Не полагайтесь на**:
- Training data (устаревшие, часто неверные)
- Старую документацию (API меняются)
- Предположения о поведении пакета

---

## Почему это важно

**Пример**: эволюция Next.js
```
Training data (2023): Next.js 13 uses pages/ directory
Current (2025): Next.js 15 uses app/ directory (App Router)

Training data = broken code ❌
ExternalScout = working code ✅
```

**Реальное влияние**:
- API меняются (новые методы, deprecated features)
- Шаблоны конфигурации развиваются
- Breaking changes происходят часто
- Version-specific возможности различаются

---

## Шаги процесса

### Шаг 1: определите внешний пакет

**Триггеры**:
- Пользователь упоминает имя библиотеки
- Вы видите imports в коде
- В package.json появились новые dependencies
- Ошибки сборки ссылаются на внешние пакеты

**Действие**: определите, какие внешние пакеты задействованы

**Пример**:
```
User: "Add authentication with Better Auth"
→ External package detected: Better Auth
→ Proceed to Step 2
```

---

### Шаг 2: проверьте install-скрипты (только при первой настройке)

**Для первой настройки пакета** проверьте наличие install-скриптов:

```bash
# Look for install scripts
ls scripts/install/ scripts/setup/ bin/install* setup.sh install.sh

# Check package-specific requirements
grep -r "postinstall\|preinstall" package.json
```

**Если скрипты есть**:
- Прочитайте их, чтобы понять порядок настройки
- Проверьте нужные environment variables
- Определите prerequisites (database, services)
- Следуйте их указаниям перед реализацией

**Почему**: скрипты могут настраивать базы данных, генерировать файлы или конфигурировать services в определенном порядке

---

### Шаг 3: получите актуальную документацию (ОБЯЗАТЕЛЬНО)

**Используйте ExternalScout**, чтобы получить live, version-specific документацию:

```bash
# Invoke ExternalScout via task tool
task(
  subagent_type="ExternalScout",
  description="Fetch Drizzle ORM documentation",
  prompt="Fetch current documentation for Drizzle ORM focusing on:
          - Modular schema patterns
          - Next.js integration
          - Database setup
          - Migration strategies"
)
```

**Что возвращает ExternalScout**:
- Live-документация из официальных источников
- Version-specific возможности
- Integration patterns
- Setup requirements
- Code examples

**Поддерживаемые библиотеки** (18+):
- Drizzle ORM
- Better Auth
- Next.js
- TanStack Query/Router/Start
- Cloudflare Workers
- AWS Lambda
- Vercel
- Shadcn/ui
- Radix UI
- Tailwind CSS
- Zustand
- Jotai
- Zod
- React Hook Form
- Vitest
- Playwright
- И другие...

---

### Шаг 4: реализуйте со свежими знаниями

**Теперь реализуйте** с использованием документации от ExternalScout:
- Следуйте текущим best practices
- Используйте version-specific APIs
- Применяйте рекомендуемые patterns
- Ссылайтесь на полученные docs в коде

---

## Интеграция с созданием агентов/skills

### При добавлении агента

1. Прочитайте: `guides/adding-agent.md`
2. **Если агент использует внешние пакеты**:
   - Используйте ExternalScout, чтобы получить docs
   - Документируйте dependencies в metadata агента
   - Добавьте в registry с корректными версиями
3. Протестируйте: `guides/testing-agent.md`

### При добавлении skill

1. Прочитайте: `guides/adding-skill.md`
2. **Если skill использует внешние пакеты**:
   - Используйте ExternalScout, чтобы получить docs
   - Документируйте dependencies в metadata skill
   - Добавьте в registry с корректными версиями
3. Протестируйте: `guides/testing-subagents.md`

---

## Частые пакеты в OpenAgents

| Пакет | Назначение | Приоритет |
|---------|----------|----------|
| **Drizzle ORM** | Database schemas и queries | ⭐⭐⭐⭐⭐ |
| **Better Auth** | Authentication и authorization | ⭐⭐⭐⭐⭐ |
| **Next.js** | Full-stack web framework | ⭐⭐⭐⭐⭐ |
| **TanStack Query** | Управление server state | ⭐⭐⭐⭐ |
| **Zod** | Schema validation | ⭐⭐⭐⭐ |
| **Tailwind CSS** | Styling | ⭐⭐⭐⭐ |
| **Shadcn/ui** | UI components | ⭐⭐⭐ |
| **Vitest** | Testing framework | ⭐⭐⭐ |

---

## Чеклист

Перед реализацией с внешними библиотеками:

- [ ] Определены все задействованные внешние пакеты
- [ ] Проверены install-скрипты (если первая настройка)
- [ ] ExternalScout использован для получения актуальных docs
- [ ] Version-specific возможности просмотрены
- [ ] Dependencies задокументированы в metadata
- [ ] Добавлено в registry с корректными версиями
- [ ] Реализация тщательно протестирована
- [ ] Docs от ExternalScout упомянуты в комментариях к коду

---

## Связанные руководства

- `guides/adding-agent.md` — создание новых агентов
- `guides/adding-skill.md` — создание новых skills
- `guides/debugging.md` — диагностика проблем (включая dependency issues)
- `guides/updating-registry.md` — управление registry

---

## Ключевой принцип

> **Внешние библиотеки постоянно меняются. Ваши training data устарели. Всегда получайте актуальную документацию перед реализацией.**

Это не опционально — это разница между рабочим и сломанным кодом.
