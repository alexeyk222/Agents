<!-- Context: workflows/design-iteration-plan-iterations | Priority: high | Version: 1.0 | Updated: 2025-12-09 -->
# Обработка правок файла плана и итераций

## Пользователь редактирует файл плана напрямую

**Сценарий**: пользователь открывает `.tmp/design-plans/{name}.md` и вносит изменения

**Процесс**:
1. Пользователь редактирует файл плана (меняет требования, добавляет ограничения, корректирует цели)
2. Пользователь сообщает агенту: "I've updated the plan file"
3. Агент читает обновленный файл плана
4. Агент определяет, что изменилось
5. Агент предлагает, как учесть изменения
6. Агент обновляет затронутые этапы

**Пример**:
```
User: "I've updated the plan file - changed the color scheme to dark mode"

Agent: 
✅ Read updated plan: .tmp/design-plans/saas-landing-page.md

Changes detected:
- Color scheme: Light → Dark mode
- Primary color: Blue → Purple

This affects:
- Stage 2 (Theme) - needs regeneration
- Stage 4 (Implementation) - needs CSS update

Would you like me to:
1. Regenerate theme with dark mode
2. Update implementation with new theme
```

---

## Итерация внутри этапа

**Сценарий**: пользователь просит изменения во время этапа

**Процесс**:
1. Агент показывает результат этапа (например, layout wireframe)
2. Пользователь просит изменения: "Make the hero section taller"
3. Агент обновляет файл плана обратной связью
4. Агент вносит изменения
5. Агент обновляет файл плана новой итерацией
6. Агент показывает обновленный результат

**Пример**:
```
Stage 1 - Layout Design

Agent: [presents wireframe]

User: "Make the hero section taller and move CTA above the fold"

Agent:
✅ Updated plan file with feedback
✅ Revised layout wireframe
✅ Updated plan file with Iteration 2

[presents updated wireframe]
```

---

## Отслеживание итераций в файле плана

**Формат**:
```markdown
## Design Evolution

### Iteration 1 - Initial Layout
- Date: 2026-01-30T10:00:00Z
- Stage: Layout
- Changes: Initial wireframe created
- User feedback: "Hero section too short, CTA below fold"

### Iteration 2 - Revised Layout
- Date: 2026-01-30T10:15:00Z
- Stage: Layout
- Changes: Increased hero height from 400px to 600px, moved CTA above fold
- User feedback: "Perfect! Approved."
- Status: ✅ Approved

### Iteration 3 - Theme Adjustment
- Date: 2026-01-30T10:30:00Z
- Stage: Theme
- Changes: Changed from light to dark mode, primary color blue → purple
- User feedback: "Love the dark mode!"
- Status: ✅ Approved
```

---

## Сохранение контекста subagent

**Проблема**: subagents теряют контекст между вызовами

**Решение**: всегда передавайте путь к файлу плана

**Паттерн**:
```javascript
// When delegating to subagent
task(
  subagent_type="OpenFrontendSpecialist",
  description="Implement Stage 4",
  prompt="Load design plan from .tmp/design-plans/saas-landing-page.md
  
  Read the plan file for:
  - All approved decisions from Stages 1-3
  - User requirements and constraints
  - Design evolution and iterations
  
  Implement Stage 4 (Implementation) following all approved decisions.
  
  Update the plan file with:
  - Output file paths
  - Implementation status
  - Any issues encountered"
)
```

---

## Файл плана как единый источник правды

### Преимущества

- ✅ Все дизайн-решения в одном месте
- ✅ Пользователь может просматривать и редактировать в любое время
- ✅ У subagents есть полный контекст
- ✅ История дизайна сохранена
- ✅ Легко выполнять итерации и уточнения
- ✅ Нет потери контекста между этапами

### Лучшие практики

- Всегда читайте файл плана в начале каждого этапа
- Обновляйте файл плана после каждого взаимодействия с пользователем
- Отслеживайте все итерации с timestamps
- Документируйте обратную связь пользователя дословно
- Ясно отмечайте утвержденные решения
- Передавайте путь к файлу плана всем subagents

---

## Связанные файлы

- [Обзор](./design-iteration-overview.md)
- [Файл плана дизайна](./design-iteration-plan-file.md)
- [Лучшие практики](./design-iteration-best-practices.md)
