<!-- Context: openagents-repo/lifecycle | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Жизненный цикл и упаковка плагина

## Структура файлов для сложных плагинов

Для крупных плагинов используйте такую структуру:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Manifest (required for packaging)
├── commands/                # Custom slash commands
├── agents/                  # Custom agents
├── hooks/                   # Event handlers
└── README.md               # Documentation
```

## Манифест (`plugin.json`)

```json
{
  "name": "my-plugin",
  "description": "A custom plugin",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

`name` становится префиксом пространства имен для команд: `/my-plugin:command`.

## Доступ к SDK

Плагины имеют полный доступ к OpenCode SDK через `context.client`. Это позволяет:
- Отправлять prompt-сообщения программно: `client.session.prompt()`
- Управлять сессиями: `client.session.list()`, `client.session.get()`
- Показывать элементы UI: `client.tui.showToast()`
- Добавлять текст в prompt: `client.tui.appendPrompt()`
