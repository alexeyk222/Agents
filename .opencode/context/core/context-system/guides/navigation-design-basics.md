<!-- Context: core/navigation-design-basics | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: проектирование файлов навигации

**Назначение**: как создавать токен-эффективные, быстро просматриваемые файлы навигации

---

## Предварительные условия

- Понимать принцип MVI (`context-system/standards/mvi.md`)
- Знать организационный паттерн вашей категории
- Иметь уже созданные файлы контента

**Оценка времени**: 15–20 мин на файл навигации

---

## Основные принципы

### 1. Токен-эффективность
**Цель**: 200–300 токенов на файл навигации

**Как**:
- Используйте ASCII-деревья (не подробные описания)
- Используйте таблицы (не абзацы)
- Будьте краткими (не исчерпывающими)

### 2. Сканируемая структура
**Цель**: AI может найти нужное за <5 секунд

**Формат**:
1. **Structure** (ASCII-дерево) - увидеть, что существует
2. **Quick Routes** (таблица) - перейти к частым задачам
3. **By Concern/Type** (разделы) - просматривать по категории

### 3. Самодостаточность
**Включать**: ✅ пути | ✅ краткие описания (3-5 слов) | ✅ когда использовать
**Исключать**: ❌ содержимое файлов | ❌ подробные объяснения | ❌ дубликаты

---

## Шаги

### 1. Определить тип навигации

| Тип | Путь | Назначение |
|------|------|---------|
| Уровень категории | `{category}/navigation.md` | Обзор категории |
| Уровень подкатегории | `{category}/{sub}/navigation.md` | Файлы в подкатегории |
| Специализированная | `{category}/{domain}-navigation.md` | Сквозная навигация (например, ui-navigation.md) |

### 2. Создать раздел Structure

```markdown
## Structure

```
openagents-repo/
├── navigation.md
├── quick-start.md
├── concepts/
│   └── subagent-testing-modes.md
├── guides/
│   ├── adding-agent.md
│   └── testing-agent.md
└── lookup/
    └── commands.md
```
```

**Количество токенов**: ~50–100 токенов

### 3. Создать таблицу Quick Routes

```markdown
## Быстрые маршруты

| Task | Path |
|------|------|
| **Add agent** | `guides/adding-agent.md` |
| **Test agent** | `guides/testing-agent.md` |
| **Find files** | `lookup/file-locations.md` |
```

**Рекомендации**: используйте **жирный шрифт** для задач | относительные пути | 5–10 частых задач

### 4. Создать разделы By Concern/Type

```markdown
## By Type

**Concepts** → Core ideas and principles
**Guides** → Step-by-step workflows
**Lookup** → Quick reference tables
**Errors** → Troubleshooting
```

### 5. Добавить Related Context (опционально)

```markdown
## Related Context

- **Core Standards** → `../core/standards/navigation.md`
```

### 6. Проверить количество токенов

**Цель**: 200–300 токенов

```bash
wc -w navigation.md  # Multiply by 1.3 for token estimate
```

---

## Чеклист проверки

- [ ] Количество токенов 200–300?
- [ ] ASCII-дерево включено?
- [ ] Таблица быстрых маршрутов?
- [ ] Раздел по задаче/типу?
- [ ] Относительные пути?
- [ ] Описания 3-5 слов?
- [ ] Нет дублирующей информации?

---

## Связанные материалы

- `navigation-templates.md` - готовые шаблоны
- `../standards/mvi.md` - принцип MVI
- `../examples/navigation-examples.md` - больше примеров
