<!-- Context: openagents-repo/events | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# События плагинов OpenCode

OpenCode генерирует более 25 событий, к которым можно подключаться хуками. Категории ниже:

## События команд
- `command.executed`: срабатывает, когда пользователь или плагин запускает команду.

## События файлов
- `file.edited`: срабатывает при изменении файла через инструменты OpenCode.
- `file.watcher.updated`: срабатывает, когда наблюдатель файлов обнаруживает изменения.

## События сообщений (только чтение)
- `message.updated`: срабатывает при обновлении сообщения в сессии.
- `message.part.updated`: срабатывает при обновлении отдельных частей сообщения.
- `message.part.removed`: срабатывает при удалении части сообщения.
- `message.removed`: срабатывает при удалении всего сообщения.

## События сессии
- `session.created`: запущена новая сессия.
- `session.updated`: состояние сессии изменилось.
- `session.idle`: сессия завершена (новой активности не ожидается).
- `session.status`: статус сессии изменился.
- `session.error`: в сессии произошла ошибка.
- `session.compacted`: сессия была сжата (контекст суммирован).

## События инструментов (перехват)
- `tool.execute.before`: срабатывает до запуска инструмента. **Может заблокировать выполнение**, выбросив ошибку.
- `tool.execute.after`: срабатывает после завершения инструмента с результатом.

## События TUI
- `tui.prompt.append`: текст добавлен во ввод prompt.
- `tui.command.execute`: команда выполнена из TUI.
- `tui.toast.show`: показано toast-уведомление.

## Сопоставление с хуками Claude Code

| Хук Claude | Событие OpenCode |
|---|---|
| PreToolUse | tool.execute.before |
| PostToolUse | tool.execute.after |
| UserPromptSubmit | события message.* |
| SessionEnd | session.idle |
