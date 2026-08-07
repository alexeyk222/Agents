<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: валидация profiles

**Цель**: убедиться, что installation profiles включают все нужные компоненты  
**Приоритет**: HIGH — проверяйте это при добавлении новых агентов или обновлении registry

---

## Что такое profiles?

Profiles — это заранее настроенные bundles компонентов в `registry.json`, которые устанавливают пользователи:
- **essential** — минимальная установка (openagent + core subagents)
- **developer** — полное dev-окружение (все dev agents + tools)
- **business** — фокус на content/product (content agents + tools)
- **full** — всё (все agents, subagents, tools)
- **advanced** — full + meta-level (system-builder, repo-manager)

---

## Проблема

**Проблема**: новые агенты добавлены в `components.agents[]`, но НЕ добавлены в profiles

**Результат**: пользователи устанавливают profile, но не получают новых агентов

**Пример** (bug v0.5.0):
```json
// ✅ Agent exists in components
{
  "id": "devops-specialist",
  "path": ".opencode/agent/subagents/development/devops-specialist.md"
}

// ❌ But NOT in developer profile
"developer": {
  "components": [
    "agent:openagent",
    "agent:opencoder"
    // Missing: "agent:devops-specialist"
  ]
}
```

---

## Чеклист валидации

При добавлении нового агента **ВСЕГДА** проверяйте:

### 1. Агент добавлен в components
```bash
# Check agent exists in registry
cat registry.json | jq '.components.agents[] | select(.id == "your-agent")'
```

### 2. Агент добавлен в подходящие profiles

**Development-агенты** → добавить в:
- ✅ `developer` profile
- ✅ `full` profile
- ✅ `advanced` profile

**Content-агенты** → добавить в:
- ✅ `business` profile
- ✅ `full` profile
- ✅ `advanced` profile

**Data-агенты** → добавить в:
- ✅ `business` profile (если business-focused)
- ✅ `full` profile
- ✅ `advanced` profile

**Meta-агенты** → добавить в:
- ✅ только `advanced` profile

**Core-агенты** → добавить в:
- ✅ `essential` profile
- ✅ все остальные profiles

### 3. Проверьте, что profile включает агента

```bash
# Check if agent is in developer profile
cat registry.json | jq '.profiles.developer.components[] | select(. == "agent:your-agent")'

# Check if agent is in business profile
cat registry.json | jq '.profiles.business.components[] | select(. == "agent:your-agent")'

# Check if agent is in full profile
cat registry.json | jq '.profiles.full.components[] | select(. == "agent:your-agent")'
```

---

## Правила назначения profiles

### Профиль Developer
**Включать**:
- Core-агенты (openagent, opencoder)
- Development-субагенты-специалисты (frontend, devops)
- Все code-субагенты (tester, reviewer, coder-agent, build-agent)
- Dev-команды (commit, test, validate-repo, analyze-patterns)
- Dev-контекст (standards/code, standards/tests, workflows/*)
- Utility-субагенты (image-specialist для изображений сайта)
- Инструменты (env, gemini для генерации изображений)

**Исключать**:
- Content-агенты (copywriter, technical-writer)
- Data-агенты (data-analyst)
- Meta-агенты (system-builder, repo-manager)

### Профиль Business
**Включать**:
- Core-агент (openagent)
- Content-специалисты (copywriter, technical-writer)
- Data-специалисты (data-analyst)
- Инструменты изображений (gemini, image-specialist)
- Инструменты уведомлений (notify)

**Исключать**:
- Development-специалисты
- Code-субагенты
- Meta-агенты

### Профиль Full
**Включать**:
- Всё из developer profile
- Всё из business profile
- Все agents, кроме meta agents

**Исключать**:
- Meta-агенты (system-builder, repo-manager)

### Профиль Advanced
**Включать**:
- Всё из full profile
- Meta-агенты (system-builder, repo-manager)
- Meta-субагенты (domain-analyzer, agent-generator и т. д.)
- Meta-команды (build-context-system)

---

## Автоматическая валидация

### Скрипт для проверки покрытия profiles

```bash
#!/bin/bash
# Check if all agents are in appropriate profiles

echo "Checking profile coverage..."

# Get all agent IDs
agents=$(cat registry.json | jq -r '.components.agents[].id')

for agent in $agents; do
  # Get agent category
  category=$(cat registry.json | jq -r ".components.agents[] | select(.id == \"$agent\") | .category")
  
  # Check which profiles include this agent
  in_developer=$(cat registry.json | jq ".profiles.developer.components[] | select(. == \"agent:$agent\")" 2>/dev/null)
  in_business=$(cat registry.json | jq ".profiles.business.components[] | select(. == \"agent:$agent\")" 2>/dev/null)
  in_full=$(cat registry.json | jq ".profiles.full.components[] | select(. == \"agent:$agent\")" 2>/dev/null)
  in_advanced=$(cat registry.json | jq ".profiles.advanced.components[] | select(. == \"agent:$agent\")" 2>/dev/null)
  
  # Validate based on category
  case $category in
    "development")
      if [[ -z "$in_developer" ]]; then
        echo "❌ $agent (development) missing from developer profile"
      fi
      if [[ -z "$in_full" ]]; then
        echo "❌ $agent (development) missing from full profile"
      fi
      if [[ -z "$in_advanced" ]]; then
        echo "❌ $agent (development) missing from advanced profile"
      fi
      ;;
    "content"|"data")
      if [[ -z "$in_business" ]]; then
        echo "❌ $agent ($category) missing from business profile"
      fi
      if [[ -z "$in_full" ]]; then
        echo "❌ $agent ($category) missing from full profile"
      fi
      if [[ -z "$in_advanced" ]]; then
        echo "❌ $agent ($category) missing from advanced profile"
      fi
      ;;
    "meta")
      if [[ -z "$in_advanced" ]]; then
        echo "❌ $agent (meta) missing from advanced profile"
      fi
      ;;
    "essential"|"standard")
      if [[ -z "$in_full" ]]; then
        echo "❌ $agent ($category) missing from full profile"
      fi
      if [[ -z "$in_advanced" ]]; then
        echo "❌ $agent ($category) missing from advanced profile"
      fi
      ;;
  esac
done

echo "✅ Profile coverage check complete"
```

Сохраните как: `scripts/registry/validate-profile-coverage.sh`

---

## Шаги ручной проверки

### После добавления нового агента

1. **Добавьте агента в components**:
   ```bash
   ./scripts/registry/auto-detect-components.sh --auto-add
   ```

2. **Вручную добавьте в profiles**:
   отредактируйте `registry.json` и добавьте `"agent:your-agent"` в подходящие profiles

3. **Проверьте registry**:
   ```bash
   ./scripts/registry/validate-registry.sh
   ```

4. **Проверьте локальную установку**:
   ```bash
   # Test developer profile
   REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list
   
   # Verify agent appears in profile
   REGISTRY_URL="file://$(pwd)/registry.json" ./install.sh --list | grep "your-agent"
   ```

5. **Проверьте фактическую установку**:
   ```bash
   # Install to temp directory
   mkdir -p /tmp/test-install
   cd /tmp/test-install
   REGISTRY_URL="file://$(pwd)/registry.json" bash <(curl -s https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh) developer
   
   # Check if agent was installed
   ls .opencode/agent/category/your-agent.md
   ```

---

## Частые ошибки

### ❌ Ошибка 1: добавление только в components
```json
// Added to components
"components": {
  "agents": [
    {"id": "new-agent", ...}
  ]
}

// But forgot to add to profiles
"profiles": {
  "developer": {
    "components": [
      // Missing: "agent:new-agent"
    ]
  }
}
```

### ❌ Ошибка 2: неверное назначение profile
```json
// Development agent added to business profile
"business": {
  "components": [
    "agent:devops-specialist"  // ❌ Should be in developer
  ]
}
```

### ❌ Ошибка 3: несогласованное покрытие profiles
```json
// Added to full but not advanced
"full": {
  "components": ["agent:new-agent"]
},
"advanced": {
  "components": [
    // ❌ Missing: "agent:new-agent"
  ]
}
```

---

## Лучшие практики

✅ **Используйте auto-detect** — автоматически добавляет в components  
✅ **Проверяйте все profiles** — убедитесь, что агент в правильных profiles  
✅ **Тестируйте локально** — установите и проверьте перед push  
✅ **Валидируйте** — запускайте скрипт валидации после изменений  
✅ **Документируйте** — обновляйте CHANGELOG с изменениями profiles  

---

## Интеграция CI/CD

Добавьте валидацию profiles в CI:

```yaml
# .github/workflows/validate-registry.yml
- name: Validate Registry
  run: ./scripts/registry/validate-registry.sh

- name: Validate Profile Coverage
  run: ./scripts/registry/validate-profile-coverage.sh
```

---

## Краткий справочник

| Категория агента | Essential | Developer | Business | Full | Advanced |
|---------------|-----------|-----------|----------|------|----------|
| core          | ✅        | ✅        | ✅       | ✅   | ✅       |
| development*  | ❌        | ✅        | ❌       | ✅   | ✅       |
| content       | ❌        | ❌        | ✅       | ✅   | ✅       |
| data          | ❌        | ❌        | ✅       | ✅   | ✅       |
| meta          | ❌        | ❌        | ❌       | ❌   | ✅       |

*Примечание: категория development включает agents (opencoder) и specialist subagents (frontend, devops)

---

## Изменения профиля Developer (v2.0.0)

**Что изменилось**:
- frontend-specialist: Agent → Subagent (specialized executor)
- devops-specialist: Agent → Subagent (specialized executor)
- backend-specialist: удален (функциональность покрыта opencoder)
- codebase-pattern-analyst: удален (заменен command analyze-patterns)
- analyze-patterns: новая command для pattern analysis

**Почему**:
- Основные агенты сокращены до 2 (openagent, opencoder)
- Субагенты-специалисты дают сфокусированную экспертизу при необходимости
- Снижена когнитивная нагрузка для новых пользователей
- Более четкое разделение между основными agents и specialized tools

**Влияние**:
- Профиль Developer теперь содержит 2 main agents + 8 subagents
- Профиль стал меньше и сфокусированнее
- Те же возможности, лучшая организация
- Нет breaking changes для существующих процессов

---

## Связанные файлы

- **Концепции registry**: `core-concepts/registry.md`
- **Обновление registry**: `guides/updating-registry.md`
- **Добавление агентов**: `guides/adding-agent.md`

---

**Последнее обновление**: 2025-01-28  
**Версия**: 0.5.2
