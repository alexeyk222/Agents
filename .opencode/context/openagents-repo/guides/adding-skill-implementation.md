<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: реализация OpenCode Skill

**Предварительно**: сначала загрузите `adding-skill-basics.md`  
**Цель**: CLI-реализация, registry и тестирование OpenCode skills

---

## CLI-реализация

### Базовая структура

```typescript
#!/usr/bin/env ts-node
// CLI implementation for {skill-name} skill

interface Args {
  command: string
  [key: string]: any
}

async function main() {
  const args = parseArgs()
  
  switch (args.command) {
    case 'command1':
      await handleCommand1(args)
      break
    case 'command2':
      await handleCommand2(args)
      break
    case 'help':
    default:
      showHelp()
  }
}

function parseArgs(): Args {
  const args = process.argv.slice(2)
  return {
    command: args[0] || 'help',
    ...parseOptions(args.slice(1))
  }
}

async function handleCommand1(args: Args) {
  console.log('Running command1...')
}

function showHelp() {
  console.log(`
{Skill Name}

Usage: npx ts-node scripts/skill-cli.ts <command> [options]

Commands:
  command1    Description
  command2    Description
  help        Show this help
`)
}

main().catch(console.error)
```

---

## Регистрация в registry (опционально)

### Добавьте в components

```json
{
  "skills": [
    {
      "id": "{skill-name}",
      "name": "Skill Name",
      "type": "skill",
      "path": ".opencode/skills/{skill-name}/SKILL.md",
      "description": "Brief description",
      "tags": ["tag1", "tag2"],
      "dependencies": []
    }
  ]
}
```

### Добавьте в profiles

```json
{
  "profiles": {
    "essential": {
      "components": [
        "skill:{skill-name}"
      ]
    }
  }
}
```

---

## Тестирование

### Проверьте CLI-команды

```bash
# Test help
bash .opencode/skills/{skill-name}/router.sh help

# Test commands
bash .opencode/skills/{skill-name}/router.sh command1 --option value

# Test with npx
npx ts-node .opencode/skills/{skill-name}/scripts/skill-cli.ts help
```

### Проверьте интеграцию с OpenCode

1. Вызовите skill через OpenCode
2. Проверьте, что event hooks срабатывают корректно
3. Проверьте conversation history на наличие skill content
4. Убедитесь, что output enhancement работает

---

## Лучшие практики

### Держите skills сфокусированными
- ✅ Task management skill → отслеживает задачи
- ❌ Task management + code generation + testing → слишком широко

### Понятная документация
- Давайте примеры использования
- Документируйте все команды
- Включайте ожидаемый вывод

### Обработка ошибок
- Корректно обрабатывайте отсутствующие аргументы
- Давайте полезные сообщения об ошибках
- Валидируйте ввод перед обработкой

### Производительность
- Используйте эффективные алгоритмы
- Кэшируйте, где уместно
- Избегайте лишних операций с файлами

---

## Чеклист

- [ ] `.opencode/skills/{skill-name}/SKILL.md` создан
- [ ] `.opencode/skills/{skill-name}/router.sh` создан (если skill основан на CLI)
- [ ] Router-скрипт исполняемый (`chmod +x`)
- [ ] Registry обновлен (если нужно)
- [ ] Profile обновлен (если нужно)
- [ ] Все команды протестированы
- [ ] Документация завершена

---

## Связанное

- `adding-skill-basics.md` — настройка каталога и SKILL.md
- `adding-skill-example.md` — полный пример
- `creating-skills.md` — Claude Code Skills
- `plugins/context/capabilities/events_skills.md` — Skills Plugin
