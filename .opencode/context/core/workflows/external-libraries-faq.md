<!-- Context: workflows/external-libraries-faq | Priority: medium | Version: 1.0 | Updated: 2026-02-05 -->
# Внешние библиотеки: FAQ

**Назначение**: устранение неполадок и частые вопросы об ExternalScout

---

## Когда именно использовать ExternalScout?

**ВСЕГДА при работе с внешними пакетами.**

**Триггеры:**
- Пользователь упоминает библиотеку
- Операторы `import`/`require`
- Зависимости в `package.json`
- Ошибки сборки
- Первая настройка
- Обновления версий

**Правило**: если этого нет в `.opencode/context/`, используйте ExternalScout.

---

## Что если я уже знаю библиотеку?

**НЕ полагайтесь на обучающие данные — они устарели.**

Пример: вы думаете «Я знаю Next.js, использую `pages/`»  
Реальность: Next.js 15 использует `app/`  
Результат: сломанный код ❌

**Всегда получайте актуальную документацию, даже если вы «знаете» библиотеку.**

---

## Как понять, что что-то внешнее?

**Внешнее:** пакеты npm/pip/gem/cargo | сторонние фреймворки | ORM | библиотеки auth | UI-библиотеки

**Не внешнее:** код вашего проекта | проектные утилиты | внутренние модули

**Проверка:** есть ли это в зависимостях `package.json`? → внешнее → используйте ExternalScout

---

## Можно ли использовать ContextScout и ExternalScout вместе?

**ДА! Для большинства функций используйте оба.**

```javascript
// 1. ContextScout: Project standards
task(subagent_type="ContextScout", ...)

// 2. ExternalScout: Library docs  
task(subagent_type="ExternalScout", ...)

// 3. Combine: Implement using both
```

---

## Что если у ExternalScout нет библиотеки?

У ExternalScout есть два источника:
1. **Context7 API** (основной): 50+ популярных библиотек
2. **Официальная документация** (fallback): любая библиотека с публичной документацией

Если библиотеки нет в Context7: автоматический fallback на официальную документацию через webfetch.

---

## Как написать хороший prompt для ExternalScout?

**Шаблон:**
```javascript
task(
  subagent_type="ExternalScout",
  description="Fetch [Library] docs for [specific topic]",
  prompt="Fetch current documentation for [Library]: [specific question]
  
  Focus on:
  - [What you need - be specific]
  - [Related features/APIs]
  
  Context: [What you're building]"
)
```

**Хорошо:** ✅ конкретно | ✅ сфокусировано (3-5 пунктов) | ✅ с контекстом
**Плохо:** ❌ расплывчато | ❌ слишком широко | ❌ без контекста

---

## Что если после ExternalScout появилась ошибка?

**Процесс:**
1. Внимательно прочитайте сообщение об ошибке
2. Снова вызовите ExternalScout с конкретной ошибкой:
```javascript
task(
  subagent_type="ExternalScout",
  description="Fetch docs for error resolution",
  prompt="Fetch [Library] docs: [error message]
  Error: [paste actual error]
  Focus on: Common causes | Solutions"
)
```
3. Проверьте install scripts (возможно, настройка неполная)
4. Проверьте версии (`package.json` vs документация)

---

## Нужно ли одобрение для использования ExternalScout?

**НЕТ — ExternalScout работает только на чтение, одобрение не требуется.**

**Требуется одобрение:** ❌ писать код | ❌ запускать команды | ❌ устанавливать пакеты
**Одобрение не нужно:** ✅ ContextScout | ✅ ExternalScout | ✅ читать файлы

---

## ContextScout и ExternalScout

| Аспект | ContextScout | ExternalScout |
|--------|--------------|---------------|
| **Ищет** | Внутренние файлы проекта | Внешнюю документацию |
| **Расположение** | `.opencode/context/` | Интернет (Context7, документация) |
| **Возвращает** | Стандарты проекта | API библиотек |
| **Использовать для** | "Как мы делаем это здесь" | "Как работает эта библиотека" |
| **Скорость** | Быстро (локально) | Медленнее (сеть) |

**Для лучшего результата используйте оба вместе.**

---

## Краткий чеклист

Перед реализацией с внешними библиотеками:

- [ ] Использовали ContextScout для стандартов проекта?
- [ ] Сначала проверили install scripts?
- [ ] Использовали ExternalScout для КАЖДОЙ внешней библиотеки?
- [ ] Запросили шаги установки?
- [ ] Запросили актуальные паттерны API?
- [ ] Прочитали возвращенную документацию перед кодингом?

**Все отмечено? → Вы все делаете правильно! ✅**

---

## Поддерживаемые библиотеки

**См.**: `.opencode/skills/context7/library-registry.md`

**Категории:** Database/ORM | Auth | Frontend | Infrastructure | UI | State | Validation | Testing

Нет в списке? ExternalScout все равно может получить данные из официальной документации.

---

## Связанные материалы

- `external-libraries-workflow.md` - основной рабочий процесс
- `external-libraries-scenarios.md` - распространенные сценарии
- `.opencode/agent/subagents/core/externalscout.md` - агент ExternalScout
