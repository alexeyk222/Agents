<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: устранение сбоев wildcard в installer

**Цель**: зафиксировать причину, исправление и выводы из сбоев установки wildcard context.

**Последнее обновление**: 2026-01-12

---

## Предварительные условия
- Изменения installer ограничены `install.sh`
- Записи registry проверены (`./scripts/registry/validate-registry.sh`)

**Оценка времени**: 10 мин

## Шаги

### 1. Определите режим сбоя
**Симптом**:
```
curl: (3) URL rejected: Malformed input to a URL function
```
**Причина**: wildcard expansion вернул context IDs, не согласованные с paths (например, `standards-code` сопоставлен с `.opencode/context/core/standards/code-quality.md`). Installer обработал IDs как paths.

### 2. Разверните wildcards в path-based IDs
**Цель**: сделать так, чтобы wildcard expansion выводил IDs вида `core/...`, которые напрямую map to path.

**Обновление**:
- Разворачивайте `context:core/*` в IDs формата `core/standards/code-quality`

### 3. Разрешайте context paths детерминированно
**Цель**: избегать неоднозначных совпадений и гарантировать использование одной registry entry.

**Обновление**:
- Добавьте `resolve_component_path`, чтобы map context IDs to registry path
- Используйте `first(...)` в jq queries для детерминированного выбора

### 4. Проверьте установку
```bash
bash scripts/tests/test-e2e-install.sh
```
**Ожидается**: все E2E-тесты проходят на macOS и Ubuntu.

## Проверка
```bash
REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
```

## Диагностика
| Проблема | Решение |
|-------|----------|
| `Malformed input to a URL function` | Убедитесь, что wildcard expansion возвращает IDs вида `core/...` и использует `resolve_component_path` |
| Несколько context entries для одного path | Используйте `first(...)` в jq lookups |

## Связанное
- guides/debugging.md
- guides/updating-registry.md
- core-concepts/registry.md
