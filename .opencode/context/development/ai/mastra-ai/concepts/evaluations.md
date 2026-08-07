<!-- Context: development/evaluations | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Концепция: Mastra Evaluations

**Назначение**: Контроль качества и оценивание выводов LLM.

**Обновлено**: 2026-01-09

---

## Основная идея
Evaluations в Mastra используют Scorers для оценки качества, точности и безопасности контента, сгенерированного LLM. Они дают количественный способ измерять качество и находить проблемы вроде галлюцинаций или фактических ошибок.

## Ключевые пункты
- **Scorers**: специализированные функции, которые принимают вывод LLM (и при необходимости эталонные данные) и возвращают балл (0-1).
- **Интеграция**: регистрируются в экземпляре Mastra и могут запускаться автоматически во время выполнения workflow.
- **Метрики**: типовые метрики включают обнаружение галлюцинаций, проверку фактов и оценку релевантности.
- **Аудит**: результаты Scorer сохраняются в таблице `mastra_scorers` для долгосрочного анализа и отчётности.

## Быстрый пример
```typescript
// Scorer definition
export const hallucinationDetector = new Scorer({
  id: 'hallucination-detector',
  description: 'Detects hallucinations in LLM output',
  execute: async ({ output, context }) => {
    // Logic to detect hallucinations
    return { score: 0.95, rationale: 'No hallucinations found' };
  },
});

// Registration
export const mastra = new Mastra({
  scorers: { hallucinationDetector },
});
```

**Источник**: `src/mastra/scorers/`, `src/mastra/evaluation/`
**Связано**:
- concepts/core.md
- concepts/workflows.md
