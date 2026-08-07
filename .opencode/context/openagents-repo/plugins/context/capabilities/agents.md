<!-- Context: openagents-repo/agents | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Пользовательские агенты в OpenCode

Плагины могут регистрировать пользовательских AI-агентов с заданными ролями, инструкциями и наборами инструментов.

## Определение агента

Пользовательские агенты настраиваются в функции `config` плагина.

```typescript
export const registerCustomAgents = (config) => {
  return {
    ...config,
    agents: [
      {
        name: "my-helper",
        description: "A friendly assistant for this project",
        instructions: "You are a helpful assistant. Use your tools to help the user.",
        model: "claude-3-5-sonnet-latest", // Specify the model
        tools: ["say_hello", "read", "write"] // Reference built-in or custom tools
      }
    ]
  };
};
```

## Интеграция в плагин

Метод `config` в возвращаемом объекте плагина используется для регистрации агентов.

```typescript
export const MyPlugin: Plugin = async (context) => {
  return {
    config: async (currentConfig) => {
      return registerCustomAgents(currentConfig);
    },
    // ... other properties
  };
};
```

## Возможности агента
- **Выбор модели**: можно выбирать разные модели для разных агентов.
- **Ограниченные инструменты**: ограничивайте инструменты агента для безопасности или фокуса.
- **Системные инструкции**: задавайте «личность» и правила агента.
