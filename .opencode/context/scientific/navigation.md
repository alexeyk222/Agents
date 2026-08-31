<!-- Context: scientific/navigation | Priority: high | Version: 1.0 | Updated: 2026-08-26 -->

# Навигация по научному профилю

**Назначение**: маршрутизация научных задач к `ScientificAgent` и одному из 87
разрешённых Scientific Agent Skills. Полный профиль и закреплённый upstream
хранятся в `.opencode/config/scientific-skills.json`; сами skills vendored в
`.opencode/skills/<skill-name>/`.

## Структура

```text
scientific/
├── navigation.md
├── databases/navigation.md
├── cheminformatics/navigation.md
├── machine-learning/navigation.md
├── engineering-simulation/navigation.md
├── data-analysis/navigation.md
├── communication/navigation.md
├── document-processing/navigation.md
├── research-methodology/navigation.md
└── analysis-methodology/navigation.md
```

## Быстрые маршруты

| Задача | Путь | Skills |
|---|---|---:|
| Научные базы и актуальные данные | `databases/navigation.md` | 9 |
| Молекулы и drug discovery | `cheminformatics/navigation.md` | 9 |
| ML, бейзлайны и quantum workflows | `machine-learning/navigation.md` | 18 |
| Симуляции и инженерные расчёты | `engineering-simulation/navigation.md` | 6 |
| Табличный анализ и визуализация | `data-analysis/navigation.md` | 9 |
| Публикации, citations и posters | `communication/navigation.md` | 11 |
| PDF, Office и Markdown | `document-processing/navigation.md` | 7 |
| Поиск работ, grants и review | `research-methodology/navigation.md` | 6 |
| Дизайн исследования и статистика | `analysis-methodology/navigation.md` | 12 |

## Стратегия загрузки

1. `ContextScout` возвращает только релевантный navigation-файл.
2. `OpenCoder` делегирует научный scope `ScientificAgent`.
3. `ScientificAgent` выбирает один основной и не более двух вспомогательных skills.
4. Полный `SKILL.md` загружается через native OpenCode skill tool.

Не загружать все 87 `SKILL.md` одновременно и не копировать их содержимое в
OAC context.
