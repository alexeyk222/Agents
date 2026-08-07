<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: процесс GitHub Issues и доски проекта

**Предварительно**: базовое понимание GitHub issues и projects  
**Цель**: пошаговый процесс управления issues и project board

---

## Обзор

Это руководство описывает, как работать с GitHub issues и project board, чтобы отслеживать и обрабатывать разные запросы, features и улучшения.

**Доска проекта**: https://github.com/users/darrenhinde/projects/2/views/2

**Время**: зависит от задачи

---

## Быстрый справочник команд

```bash
# List issues
gh issue list --repo darrenhinde/OpenAgentsControl

# Create issue
gh issue create --repo darrenhinde/OpenAgentsControl --title "Title" --body "Body" --label "label1,label2"

# Add issue to project
gh project item-add 2 --owner darrenhinde --url https://github.com/darrenhinde/OpenAgentsControl/issues/NUMBER

# View issue
gh issue view NUMBER --repo darrenhinde/OpenAgentsControl

# Update issue
gh issue edit NUMBER --repo darrenhinde/OpenAgentsControl --add-label "new-label"

# Close issue
gh issue close NUMBER --repo darrenhinde/OpenAgentsControl
```

---

## Шаг 1: создание issues

### Типы issue

**Запрос функции**
- Метки: `feature`, `enhancement`
- Включите: цели, ключевые возможности, критерии успеха
- Шаблон: см. «Шаблон feature issue» ниже

**Баг-репорт**
- Метки: `bug`
- Включите: шаги воспроизведения, ожидаемое vs фактическое поведение
- Шаблон: см. «Шаблон bug issue» ниже

**Улучшение**
- Метки: `enhancement`, `framework`
- Включите: текущее состояние, предлагаемое улучшение, влияние

**Вопрос**
- Метки: `question`
- Включите: контекст, конкретный вопрос, сценарий использования

### Метки приоритета

- `priority-high` — критично, блокирует работу
- `priority-medium` — важно, но не блокирует
- `priority-low` — желательно

### Метки категорий

- `agents` — связано с agent system
- `framework` — изменения core framework
- `evals` — evaluation framework
- `idea` — high-level предложение

### Создание issue

```bash
# Basic issue
gh issue create \
  --repo darrenhinde/OpenAgentsControl \
  --title "Add new feature X" \
  --body "Description of feature" \
  --label "feature,priority-medium"

# Feature with detailed body
gh issue create \
  --repo darrenhinde/OpenAgentsControl \
  --title "Build plugin system" \
  --label "feature,framework,priority-high" \
  --body "$(cat <<'EOF'
## Overview
Brief description

## Goals
- Goal 1
- Goal 2

## Key Features
- Feature 1
- Feature 2

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
EOF
)"
```

---

## Шаг 2: добавление issues на доску проекта

### Добавить один issue

```bash
# Add issue to project
gh project item-add 2 \
  --owner darrenhinde \
  --url https://github.com/darrenhinde/OpenAgentsControl/issues/NUMBER
```

### Добавить несколько issues

```bash
# Add issues 137-142 to project
for i in {137..142}; do
  gh project item-add 2 \
    --owner darrenhinde \
    --url https://github.com/darrenhinde/OpenAgentsControl/issues/$i
done
```

### Проверить issues на board

```bash
# View project items
gh project item-list 2 --owner darrenhinde --format json | jq '.items[] | {title, status}'
```

---

## Шаг 3: обработка issues

### Состояния workflow

1. **Backlog** — новые issues, еще не приоритизированы
2. **Todo** — приоритизированы, готовы к работе
3. **In Progress** — сейчас в работе
4. **In Review** — PR отправлен, ожидает review
5. **Done** — завершено и merged

### Перемещение issues

```bash
# Update issue status (via project board UI or gh CLI)
# Note: Status updates are typically done via web UI
```

### Назначение issues

```bash
# Assign to yourself
gh issue edit NUMBER \
  --repo darrenhinde/OpenAgentsControl \
  --add-assignee @me

# Assign to someone else
gh issue edit NUMBER \
  --repo darrenhinde/OpenAgentsControl \
  --add-assignee username
```

---

## Шаг 4: работа над issues

### Начать работу

1. **Назначьте issue на себя**
   ```bash
   gh issue edit NUMBER --repo darrenhinde/OpenAgentsControl --add-assignee @me
   ```

2. **Переместите в "In Progress"** (через web UI)

3. **Создайте branch** (опционально)
   ```bash
   git checkout -b feature/issue-NUMBER-description
   ```

4. **Ссылайтесь на issue в commits**
   ```bash
   git commit -m "feat: implement X (#NUMBER)"
   ```

### Обновить прогресс

```bash
# Add comment to issue
gh issue comment NUMBER \
  --repo darrenhinde/OpenAgentsControl \
  --body "Progress update: Completed X, working on Y"
```

### Завершить работу

1. **Создайте PR**
   ```bash
   gh pr create \
     --repo darrenhinde/OpenAgentsControl \
     --title "Fix #NUMBER: Description" \
     --body "Closes #NUMBER\n\nChanges:\n- Change 1\n- Change 2"
   ```

2. **Переместите в "In Review"** (через web UI)

3. **После merge issue закроется автоматически** (если PR использует "Closes #NUMBER")

---

## Шаг 5: использование issues для обработки запросов

### Типы запросов

**Пользовательский запрос функции**
1. Создайте issue с label `feature`
2. Добавьте в project board
3. Приоритизируйте по влиянию
4. Разбейте на subtasks при необходимости
5. Назначьте подходящему человеку/команде

**Баг-репорт**
1. Создайте issue с label `bug`
2. Добавьте reproduction steps
3. Приоритизируйте по severity
4. Назначьте для investigation
5. Свяжите с related issues, если применимо

**Предложение улучшения**
1. Создайте issue с label `enhancement`
2. Обсудите approach в comments
3. Получите consensus перед реализацией
4. Создайте implementation plan
5. Выполните и отслеживайте прогресс

### Разбиение больших issues

Для сложных features создавайте parent issue и subtasks:

```bash
# Parent issue
gh issue create \
  --repo darrenhinde/OpenAgentsControl \
  --title "[EPIC] Plugin System" \
  --label "feature,framework,priority-high" \
  --body "Parent issue for plugin system work"

# Subtask issues
gh issue create \
  --repo darrenhinde/OpenAgentsControl \
  --title "Plugin manifest system" \
  --label "feature" \
  --body "Part of #PARENT_NUMBER\n\nImplement plugin.json manifest"
```

---

## Шаг 6: шаблоны issue

### Шаблон feature issue

```markdown
## Overview
Brief description of the feature

## Goals
- Goal 1
- Goal 2
- Goal 3

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Related Issues
- #123 (related issue)

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
```

### Шаблон bug issue

```markdown
## Description
Brief description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: macOS/Linux/Windows
- Version: 0.5.2
- Node: v20.x

## Additional Context
Any other relevant information
```

### Шаблон issue для улучшения

```markdown
## Current State
Description of current implementation

## Proposed Improvement
What should be improved and why

## Impact
- Performance improvement
- Developer experience
- User experience

## Implementation Approach
High-level approach to implementation

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## Шаг 7: автоматизация и интеграция

### Автозакрытие issues

Используйте keywords в описаниях PR:
- `Closes #123`
- `Fixes #123`
- `Resolves #123`

### Связать issues с PR

```bash
# In PR description
gh pr create \
  --title "Add feature X" \
  --body "Implements #123\n\nChanges:\n- Change 1"
```

### Ссылки на issue в commits

```bash
# Reference issue in commit
git commit -m "feat: add plugin system (#137)"

# Close issue in commit
git commit -m "fix: resolve permission error (closes #140)"
```

---

## Лучшие практики

### Создание issues

✅ **Понятные заголовки** — описательные и конкретные  
✅ **Подробные описания** — включайте context и goals  
✅ **Правильные labels** — используйте единый labeling  
✅ **Критерии успеха** — определите, что значит "done"  
✅ **Связанные issues** — показывайте dependencies  

### Управление issues

✅ **Регулярный triage** — просматривайте и приоритизируйте еженедельно  
✅ **Держите актуальными** — добавляйте комментарии о прогрессе  
✅ **Закрывайте устаревшие issues** — очищайте старые/неактуальные issues  
✅ **Используйте milestones** — группируйте связанные issues  
✅ **Назначайте owners** — ясная ответственность  

### Доска проекта

✅ **Обновляйте status** — держите board актуальной  
✅ **Ограничивайте WIP** — не перегружайте "In Progress"  
✅ **Регулярно review** — еженедельный review board  
✅ **Архивируйте завершенное** — держите board чистой  

---

## Частые процессы

### Обработка пользовательского запроса

1. **Получите запрос** (через issue, email, chat)
2. **Создайте issue** с подходящими labels
3. **Добавьте в project board**
4. **Проведите triage и приоритизируйте**
5. **Назначьте участника команды**
6. **Отслеживайте прогресс** через обновления статуса
7. **Проверьте и merge** PR
8. **Закройте issue** и уведомите requester

### Планирование новой feature

1. **Создайте epic issue** для всей feature
2. **Разбейте на subtasks**
3. **Добавьте всё в project board**
4. **Приоритизируйте subtasks**
5. **Назначьте участников команды**
6. **Отслеживайте прогресс** по subtasks
7. **Завершите и закройте**, когда все subtasks готовы

### Triage багов

1. **Создайте bug issue** с шагами воспроизведения
2. **Добавьте label severity** (critical, high, medium, low)
3. **Добавьте в project board**
4. **Назначьте расследование**
5. **Воспроизведите и диагностируйте**
6. **Исправьте и протестируйте**
7. **Создайте PR** с fix
8. **Закройте issue** после merge

---

## Чеклист

Перед закрытием issue:

- [ ] Все критерии успеха выполнены
- [ ] Тесты проходят
- [ ] Документация обновлена
- [ ] PR merged (если применимо)
- [ ] Связанные issues обновлены
- [ ] Stakeholders уведомлены

---

## Связанные файлы

- **Руководство по registry**: `guides/updating-registry.md`
- **Руководство по релизу**: `guides/creating-release.md`
- **Руководство по тестированию**: `guides/testing-agent.md`
- **Диагностика**: `guides/debugging.md`

---

## Внешние ресурсы

- [Документация GitHub Issues](https://docs.github.com/en/issues)
- [Документация GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [Документация GitHub CLI](https://cli.github.com/manual/)

---

**Последнее обновление**: 2026-01-30  
**Версия**: 0.5.2
