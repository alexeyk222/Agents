<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Создание CLI в OpenAgents Control: краткое руководство

**Категория**: руководство  
**Цель**: быстро создавать, регистрировать и разворачивать CLI-инструменты для OpenAgents Control skills  
**Фреймворк**: FAB (Features, Advantages, Benefits)

---

## 🚀 Быстрый старт

**Не начинайте с нуля.** Используйте стандартный шаблон, чтобы собрать надежный CLI за минуты.

1.  **Создайте**: `mkdir -p .opencode/skills/{name}/scripts`
2.  **Реализуйте**: создайте `skill-cli.ts` (TypeScript) и `router.sh` (Bash)
3.  **Зарегистрируйте**: добавьте в `registry.json`
4.  **Запустите**: `bash .opencode/skills/{name}/router.sh help`

---

## 🏗️ Базовая архитектура

| Компонент | Файл | Назначение |
|-----------|------|---------|
| **Логика** | `scripts/skill-cli.ts` | Типобезопасная реализация через `ts-node`. Обрабатывает аргументы, логику и вывод. |
| **Router** | `router.sh` | Универсальная точка входа. Направляет команды в TS-скрипт. |
| **Документация** | `SKILL.md` | Руководство пользователя, примеры и детали интеграции. |
| **Конфиг** | `registry.json` | Делает skill доступным для поиска и установки через `install.sh`. |

---

## ⚡ Шаблоны реализации

### 1. Router (`router.sh`)
**Зачем**: дает единообразную точку входа без зависимостей для любых окружений.

```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

case "$1" in
    help|--help|-h)
        echo "Usage: bash router.sh <command>"
        ;;
    *)
        # Route to TypeScript implementation
        npx ts-node "$SCRIPT_DIR/scripts/skill-cli.ts" "$@"
        ;;
esac
```

### 2. CLI-логика (`skill-cli.ts`)
**Зачем**: типобезопасность, поддержка async/await и доступ к богатой экосистеме.

```typescript
#!/usr/bin/env ts-node

async function main() {
  const [command, ...args] = process.argv.slice(2);
  
  switch (command) {
    case 'action':
      await handleAction(args);
      break;
    default:
      console.log("Unknown command");
      process.exit(1);
  }
}

main().catch(console.error);
```

---

## ✅ Чеклист качества

Перед публикацией убедитесь, что CLI приносит пользу:

- [ ] **Команда help**: дает ли `router.sh help` понятную и практичную справку?
- [ ] **Обработка ошибок**: возвращают ли неверные входные данные полезные ошибки, а не stack traces?
- [ ] **Производительность**: стартует ли CLI быстрее чем за 1 с? (избегайте тяжелых импортов на верхнем уровне)
- [ ] **Идемпотентность**: можно ли безопасно запускать команды несколько раз?
- [ ] **Registry**: добавлен ли CLI в `registry.json` с корректными путями?

---

## 🧠 Принципы copywriting для вывода CLI

Применяйте принципы `content-creation` к выводу CLI:

1.  **Ясность**: используйте **active voice**. "Created file" (хорошо) vs "File has been created" (плохо).
2.  **Конкретика**: "Processed 5 files" (хорошо) vs "Processing complete" (плохо).
3.  **Действие**: скажите пользователю, что делать дальше. "Run `npm test` to verify."

---

**Ссылка**: полное подробное руководство см. в `.opencode/context/openagents-repo/guides/adding-skill-basics.md`.
