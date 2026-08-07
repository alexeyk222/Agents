<!-- Context: workflows/delegation-caching | Priority: medium | Version: 1.0 | Updated: 2026-02-05 -->
# Кэширование контекста для делегирования

**Назначение**: кэшировать найденный контекст, чтобы избежать повторного поиска в повторяющихся задачах

---

## Когда кэшировать

Кэшируйте контекст, когда:
- Один тип задачи встречается в сессии несколько раз
- Одни и те же файлы контекста нужны повторно
- Несколько подзадач используют одинаковые стандарты
- Параллельным задачам нужен один и тот же контекст

---

## Структура кэша

```
.tmp/sessions/{session-id}/
├── context.md (main session context)
├── .cache/
│   ├── test-coverage.md (cached from .opencode/context/)
│   ├── code-quality.md
│   └── code-review.md
└── .manifest.json (tracks cache status)
```

---

## Cache Manifest

```json
{
  "session_id": "2026-01-28-parallel-tests",
  "created_at": "2026-01-28T14:30:22Z",
  "cache": {
    "test-coverage.md": {
      "source": ".opencode/context/core/standards/test-coverage.md",
      "cached_at": "2026-01-28T14:30:25Z",
      "used_by": ["subtask_01", "subtask_02"],
      "status": "valid"
    }
  }
}
```

---

## Правила инвалидации

**Кэш НЕВАЛИДЕН, когда:**
- Исходный файл изменен (проверьте временную метку)
- Сессия старше 24 часов
- Версия файла контекста изменилась
- Пользователь явно запросил refresh

**Кэш ВАЛИДЕН, когда:**
- Временная метка исходника совпадает
- Сессии меньше 24 часов
- Нет изменений версии
- В одной сессии несколько задач

---

## Паттерн реализации

```javascript
// Before delegating to subagent
IF cache exists AND cache is valid:
  USE cached context file
  SKIP re-reading from .opencode/context/
ELSE:
  READ from .opencode/context/
  CACHE the file
```

---

## Пример: параллельные задачи

```javascript
session_id = "2026-01-28-parallel-tests"

// Task 1: Write component A (parallel)
task(
  subagent_type="CoderAgent",
  description="Write component A",
  prompt="Load context from .tmp/sessions/{session_id}/context.md
          Use cached context if available at .cache/"
)

// Task 2: Write component B (parallel)  
task(
  subagent_type="CoderAgent",
  description="Write component B",
  prompt="Load context from .tmp/sessions/{session_id}/context.md
          Use cached context if available at .cache/"
)

// Result: Task 1 caches context, Task 2 uses cache (faster)
```

---

## Эффективность кэша

Отслеживайте метрики:
```json
{
  "cache_stats": {
    "total_reads": 15,
    "cache_hits": 9,
    "cache_misses": 6,
    "hit_rate": "60%"
  }
}
```

---

## Лучшие практики

✅ **Делайте:**
- Кэшируйте контекст для повторяющихся типов задач
- Валидируйте кэш перед использованием
- Инвалидируйте при изменении исходника
- Отслеживайте hit rate
- Очищайте кэш вместе с сессией

❌ **Не делайте:**
- Не кэшируйте внешний контекст (всегда получайте свежий)
- Не кэшируйте для сессий с одной задачей (overhead не оправдан)
- Не игнорируйте правила инвалидации
- Не смешивайте кэшированный и свежий контекст в одной задаче

---

## Связанные материалы

- `task-delegation-basics.md` - основной workflow делегирования
- `task-delegation-specialists.md` - когда делегировать
