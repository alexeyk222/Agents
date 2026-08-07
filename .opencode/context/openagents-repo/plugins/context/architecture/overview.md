<!-- Context: openagents-repo/overview | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Обзор плагинов OpenCode

Плагины OpenCode — это модули JavaScript или TypeScript, которые подключаются к **25+ событиям** всего жизненного цикла OpenCode: от ввода prompt до выполнения инструментов и завершения сессий.

## Ключевые концепции

- **Zero-Config**: сборка или компиляция не нужны. Достаточно положить `.ts` или `.js` файлы в папку плагинов.
- **Паттерн middleware**: плагины подписываются на события и выполняют логику, как middleware в Express.js.
- **Доступ**: плагины получают объект `context` с:
  - `project`: метаданные текущего проекта.
  - `client`: клиент OpenCode SDK для программного управления.
  - `$`: shell API Bun для запуска команд.
  - `directory`: текущая рабочая директория.
  - `worktree`: путь к Git worktree.

## Регистрация плагинов

OpenCode ищет плагины в:
1. **Уровень проекта**: `.opencode/plugin/` (корень проекта)
2. **Глобально**: `~/.config/opencode/plugin/` (домашняя директория)

## Базовая структура

```typescript
export const MyPlugin = async (context) => {
  const { project, client, $, directory, worktree } = context;

  return {
    event: async ({ event }) => {
      // Handle events here
    }
  };
};
```

Каждая экспортированная функция становится отдельным экземпляром плагина. Имя экспорта используется как имя плагина.

## Сборка и разработка

Плагины OpenCode обычно пишут на TypeScript и собирают в один JavaScript-файл для выполнения.

### Команда сборки
Используйте Bun, чтобы собрать плагин в директорию `dist`:

```bash
bun build src/index.ts --outdir dist --target bun --format esm
```

На выходе будет один файл (например, `./index.js`) со всеми зависимостями.

### Процесс разработки
1. **Исходный код**: пишите плагин в `src/index.ts`.
2. **Сборка**: запустите команду сборки, чтобы создать `dist/index.js`.
3. **Загрузка**: укажите OpenCode на собранный файл или директорию с манифестом.
4. **Режим наблюдения**: для быстрой разработки используйте флаг `--watch` с Bun build:
   ```bash
   bun build src/index.ts --outdir dist --target bun --format esm --watch
   ```
