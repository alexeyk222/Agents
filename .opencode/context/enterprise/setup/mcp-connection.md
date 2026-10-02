<!-- Context: enterprise/guides | Priority: high | Version: 1.0 | Updated: 2026-10-02 -->

# Подключение Confluence, Jira и Impala к OpenCode

**Назначение**: как дать агентам доступ к корпоративным системам через MCP так,
чтобы права агентов в `agent/*.md` совпадали с именами инструментов.

---

## Соглашение об именах

OpenCode называет MCP-инструменты как `{имя_сервера}_{имя_инструмента}`.
Права агентов в этом репозитории рассчитаны на такие имена серверов:

| Сервер в `opencode.json` | Система | Пример инструмента |
|---|---|---|
| `atlassian` | Confluence + Jira | `atlassian_confluence_search`, `atlassian_jira_get_issue` |
| `impala` | Impala / Hive Metastore | `impala_*` (зависит от реализации сервера) |

Если сервер назван иначе, поправьте ключи `atlassian_*` / `impala_*` в блоках
`permission` у `ContextScout`, `OpenCoder` и `ScientificAgent`.

---

## Confluence и Jira (Server / Data Center)

В `.opencode/opencode.json` уже есть отключённая заготовка сервера `atlassian`
на базе open-source пакета `mcp-atlassian`. Чтобы включить:

1. Установите пакет из внутреннего PyPI-зеркала (в закрытом контуре `uvx`
   не скачает пакет из интернета):
   ```bash
   pip install --index-url "$PIP_INDEX_URL" mcp-atlassian
   ```
2. Заполните переменные окружения (см. `.opencode/env.example`):
   `CONFLUENCE_URL`, `CONFLUENCE_PERSONAL_TOKEN`, `JIRA_URL`,
   `JIRA_PERSONAL_TOKEN`. Для внутреннего CA — `CONFLUENCE_SSL_VERIFY` /
   `JIRA_SSL_VERIFY` или корпоративный bundle в `REQUESTS_CA_BUNDLE`.
3. Поставьте `"enabled": true` у сервера `atlassian`.
4. Оставьте `READ_ONLY_MODE=true` — сервер не будет регистрировать
   инструменты записи. Это второй рубеж защиты поверх прав агентов.
5. Сузьте поиск: `CONFLUENCE_SPACES_FILTER` (например, `DWH,DATA,ANALYTICS`)
   и `JIRA_PROJECTS_FILTER`.

Используйте **персональный токен (PAT) с минимальными правами**: агент видит
ровно то, что видит владелец токена.

---

## Impala

Единого стандартного MCP-сервера для Impala нет — выберите один вариант:

| Вариант | Когда | Как ограничить |
|---|---|---|
| **MCP-сервер `impala`** (внутренний или open-source на `impyla`) | Нужна разведка из `ContextScout` | Сервисная учётка только с `SELECT`/метаданными; права `impala_*` в агентах |
| **`impala-shell`** через bash | Разовая разведка из `OpenCoder` / `ScientificAgent` | Правило `"impala-shell *": "ask"` — каждый запрос подтверждается |
| **`impyla` в ноутбуке** | EDA, профилирование, графики | skill `jupyter-notebook`, параметры подключения из env |

Переменные: `IMPALA_HOST`, `IMPALA_PORT` (21050), `IMPALA_AUTH_MECHANISM`
(`GSSAPI` для Kerberos, `LDAP`), `IMPALA_USE_SSL`, при LDAP — `IMPALA_USER` /
`IMPALA_PASSWORD`. Для Kerberos билет получают заранее (`kinit`), keytab в
репозиторий не кладут.

---

## Проверка подключения

```text
opencode mcp list            # сервер в статусе connected
```

Тестовый запрос агенту:

```text
Используй ContextScout: найди в Confluence определение «дата операции»
и задачи Jira, где менялась логика её расчёта. Только ссылки и краткое резюме.
```

---

## Связанное

- Правила работы с источниками → `../sources/`
- Права агентов → `.opencode/agent/subagents/core/contextscout.md`
