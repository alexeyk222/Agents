<!-- Context: workflows/design-iteration-plan-file | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Файл плана дизайна (ОБЯЗАТЕЛЬНО)

**КРИТИЧНО**: перед любой работой над дизайном создайте постоянный файл плана.

**Расположение**: `.tmp/design-plans/{project-name}-{feature-name}.md`

**Назначение**: 
- Сохранять дизайн-решения между этапами
- Дать пользователю возможность просматривать и редактировать план
- Сохранять контекст для вызовов subagent
- Отслеживать развитие дизайна и итерации

**Когда создавать**: 
- ДО этапа 1 (дизайн макета)
- После понимания требований пользователя
- До начала любой работы над дизайном

## Шаблон

```markdown
---
project: {project-name}
feature: {feature-name}
created: {ISO timestamp}
updated: {ISO timestamp}
status: in_progress
current_stage: layout
---

# Design Plan: {Feature Name}

## User Requirements
{What the user asked for - verbatim or close paraphrase}

## Design Goals
- {goal 1}
- {goal 2}
- {goal 3}

## Target Audience
{Who will use this UI}

## Technical Constraints
- Framework: {Next.js, React, etc.}
- Responsive: {Yes/No}
- Accessibility: {WCAG level}
- Browser support: {Modern, IE11+, etc.}

---

## Stage 1: Layout Design

### Status
- [ ] Layout planned
- [ ] ASCII wireframe created
- [ ] User approved

### Layout Structure
{ASCII wireframe will be added here}

### Component Breakdown
{Component list will be added here}

### User Feedback
{User comments and requested changes}

---

## Stage 2: Theme Design

### Status
- [ ] Design system selected
- [ ] Color palette chosen
- [ ] Typography defined
- [ ] User approved

### Theme Details
{Theme specifications will be added here}

### User Feedback
{User comments and requested changes}

---

## Stage 3: Animation Design

### Status
- [ ] Micro-interactions defined
- [ ] Animation timing set
- [ ] User approved

### Animation Details
{Animation specifications will be added here}

### User Feedback
{User comments and requested changes}

---

## Stage 4: Implementation

### Status
- [ ] HTML structure complete
- [ ] CSS applied
- [ ] Animations implemented
- [ ] User approved

### Output Files
- HTML: {file path}
- CSS: {file path}
- Assets: {file paths}

### User Feedback
{Final comments and requested changes}

---

## Design Evolution

### Iteration 1
- Date: {timestamp}
- Changes: {what changed}
- Reason: {why it changed}

### Iteration 2
- Date: {timestamp}
- Changes: {what changed}
- Reason: {why it changed}
```

## Интеграция с рабочим процессом

1. **Создать файл плана** → записать в `.tmp/design-plans/{name}.md`
2. **Каждый этап** → обновлять план решениями и обратной связью пользователя
3. **Одобрение пользователя** → записать в план утвержденные решения
4. **Пользователь просит изменения** → записать обратную связь и выполнить итерацию
5. **Вызовы subagent** → передавать путь к плану для сохранения контекста
6. **Завершение** → план содержит полную историю дизайна

## Преимущества

- ✅ Контекст сохраняется между вызовами subagent
- ✅ Пользователь может просматривать и редактировать план напрямую
- ✅ Дизайн-решения задокументированы
- ✅ Легко выполнять итерации и уточнения
- ✅ Полная история дизайна отслеживается

---

## Этап 0: создать план дизайна (ОБЯЗАТЕЛЬНЫЙ ПЕРВЫЙ ШАГ)

**Назначение**: создать постоянный файл плана до любой работы над дизайном

**Процесс**:
1. Понять требования пользователя
2. Определить цели дизайна и ограничения
3. Создать файл плана в `.tmp/design-plans/{project-name}-{feature-name}.md`
4. Заполнить требованиями пользователя и целями
5. Показать пользователю расположение файла плана
6. Перейти к этапу 1

**Результат**: файл плана дизайна создан и инициализирован

**Пример**:
```
✅ Design plan created: .tmp/design-plans/saas-landing-page.md

You can review and edit this file at any time. All design decisions will be tracked here.

Ready to proceed to Stage 1 (Layout Design)?
```

**Точка одобрения**: "Файл плана создан. Готовы начать дизайн макета?"

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Этап 1: Макет](./design-iteration-stage-layout.md)
- [Итерации плана](./design-iteration-plan-iterations.md)
