<!-- Context: openagents-repo/context-bundle-template | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Шаблон context bundle

**Назначение**: шаблон для создания context bundles при делегировании задач субагентам

**Расположение**: `.tmp/context/{session-id}/bundle.md`

**Используется**: агентом repo-manager при делегировании субагентам

---

## Шаблон

```markdown
# Пакет контекста: {Task Name}

Session: {session-id}
Created: {ISO timestamp}
For: {subagent-name}
Status: in_progress

## Обзор задачи

{Brief description of what we're building/doing}

## User Request

{Original user request - what they asked for}

## Relevant Standards (Load These Before Starting)

**Core Standards**:
- `.opencode/context/core/standards/code.md` → Modular, functional code patterns
- `.opencode/context/core/standards/tests.md` → Testing requirements and TDD
- `.opencode/context/core/standards/docs.md` → Documentation standards
- (example: `.opencode/context/core/standards/patterns.md`) → Error handling, security patterns

**Core Workflows**:
- (example: `.opencode/context/core/workflows/delegation.md`) → Delegation process
- (example: `.opencode/context/core/workflows/task-breakdown.md`) → Task breakdown methodology
- (example: `.opencode/context/core/workflows/review.md`) → Code review guidelines

## Repository-Specific Context (Load These Before Starting)

**Quick Start** (ALWAYS load first):
- `.opencode/context/openagents-repo/quick-start.md` → Repo orientation and common commands

**Core Concepts** (Load based on task type):
- `.opencode/context/openagents-repo/core-concepts/agents.md` → How agents work
- `.opencode/context/openagents-repo/core-concepts/evals.md` → How testing works
- `.opencode/context/openagents-repo/core-concepts/registry.md` → How registry works
- `.opencode/context/openagents-repo/core-concepts/categories.md` → How organization works

**Guides** (Load for specific workflows):
- `.opencode/context/openagents-repo/guides/adding-agent-basics.md` → Step-by-step agent creation
- `.opencode/context/openagents-repo/guides/testing-agent.md` → Testing workflow
- `.opencode/context/openagents-repo/guides/updating-registry.md` → Registry workflow
- `.opencode/context/openagents-repo/guides/debugging.md` → Troubleshooting

**Lookup** (Quick reference):
- `.opencode/context/openagents-repo/lookup/file-locations.md` → Where everything is
- `.opencode/context/openagents-repo/lookup/commands.md` → Command reference

## Key Requirements

{Extract key requirements from loaded context}

**From Standards**:
- {requirement 1 from standards/code.md}
- {requirement 2 from standards/tests.md}
- {requirement 3 from standards/docs.md}

**From Repository Context**:
- {requirement 1 from repo context}
- {requirement 2 from repo context}
- {requirement 3 from repo context}

**Naming Conventions**:
- {convention 1}
- {convention 2}

**File Structure**:
- {structure requirement 1}
- {structure requirement 2}

## Technical Constraints

{List technical constraints and limitations}

- {constraint 1 - e.g., "Must use TypeScript"}
- {constraint 2 - e.g., "Must follow category-based organization"}
- {constraint 3 - e.g., "Must include proper frontmatter metadata"}

## Files to Create/Modify

{List all files that need to be created or modified}

**Create**:
- `{file-path-1}` - {purpose and what it should contain}
- `{file-path-2}` - {purpose and what it should contain}

**Modify**:
- `{file-path-3}` - {what needs to be changed}
- `{file-path-4}` - {what needs to be changed}

## Success Criteria

{Define what "done" looks like - binary pass/fail conditions}

- [ ] {criteria 1 - e.g., "Agent file created with proper frontmatter"}
- [ ] {criteria 2 - e.g., "Eval tests pass"}
- [ ] {criteria 3 - e.g., "Registry validation passes"}
- [ ] {criteria 4 - e.g., "Documentation updated"}

## Validation Requirements

{How to validate the work}

**Scripts to Run**:
- `{validation-script-1}` - {what it validates}
- `{validation-script-2}` - {what it validates}

**Tests to Run**:
- `{test-command-1}` - {what it tests}
- `{test-command-2}` - {what it tests}

**Manual Checks**:
- {check 1}
- {check 2}

## Expected Output

{What the subagent should produce}

**Deliverables**:
- {deliverable 1}
- {deliverable 2}

**Format**:
- {format requirement 1}
- {format requirement 2}

## Progress Tracking

{Track progress through the task}

- [ ] Context loaded and understood
- [ ] {step 1}
- [ ] {step 2}
- [ ] {step 3}
- [ ] Validation passed
- [ ] Documentation updated

---

## Instructions for Subagent

{Specific, detailed instructions for the subagent}

**IMPORTANT**: 
1. Load ALL context files listed in "Relevant Standards" and "Repository-Specific Context" sections BEFORE starting work
2. Follow ALL requirements from the loaded context
3. Apply naming conventions and file structure requirements
4. Validate your work using the validation requirements
5. Update progress tracking as you complete steps

**Your Task**:
{Detailed description of what the subagent needs to do}

**Approach**:
{Suggested approach or methodology}

**Constraints**:
{Any additional constraints or notes}

**Questions/Clarifications**:
{Any questions the subagent should consider or clarifications needed}
```

---

## Инструкции по использованию

### Когда создавать context bundle

Создавайте context bundle, когда:
- Делегируете любому субагенту
- Задача требует координации нескольких компонентов
- Субагенту нужен контекст проекта
- У задачи сложные требования или ограничения

### Как создать context bundle

1. **Создайте директорию сессии**:
   ```bash
   mkdir -p .tmp/context/{session-id}
   ```

2. **Скопируйте шаблон**:
   ```bash
   cp .opencode/context/openagents-repo/templates/context-bundle-template.md \
      .tmp/context/{session-id}/bundle.md
   ```

3. **Заполните все секции**:
   - Замените все `{placeholders}` реальными значениями
   - Перечислите конкретные контекстные файлы для загрузки (с полными путями)
   - Извлеките ключевые требования из загруженного контекста
   - Определите четкие критерии успеха
   - Дайте конкретные инструкции

4. **Передайте субагенту**:
   ```javascript
   task(
     subagent_type="subagents/core/{subagent}",
     description="Brief description",
     prompt="Load context from .tmp/context/{session-id}/bundle.md before starting.
             
             {Specific task instructions}
             
             Follow all standards and requirements in the context bundle."
   )
   ```

### Лучшие практики

**Делайте**:
- ✅ Перечисляйте контекстные файлы с полными путями (не дублируйте содержимое)
- ✅ Извлекайте ключевые требования из загруженного контекста
- ✅ Задавайте бинарные критерии успеха (pass/fail)
- ✅ Указывайте конкретные требования к валидации
- ✅ Добавляйте ясные инструкции для субагента
- ✅ Отслеживайте прогресс по задаче

**Не делайте**:
- ❌ Не дублируйте полный текст контекстных файлов (достаточно ссылок на пути)
- ❌ Не используйте расплывчатые критерии успеха ("make it good")
- ❌ Не пропускайте требования к валидации
- ❌ Не забывайте перечислять технические ограничения
- ❌ Не опускайте пути файлов для создания/изменения

### Пример context bundle

Полный пример см. в `.opencode/context/openagents-repo/examples/context-bundle-example.md`.

---

**Последнее обновление**: 2025-01-21  
**Версия**: 1.0.0
