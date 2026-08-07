<!-- Context: core/navigation | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Навигация по базовым стандартам

**Назначение**: Универсальные стандарты для всей разработки

---

## Файлы

| Файл | Тема | Приоритет | Когда загружать |
|------|-------|----------|-----------|
| `code-quality.md` | Правила качества кода | ⭐⭐⭐⭐⭐ | Написание/ревью кода |
| `test-coverage.md` | Стандарты тестирования | ⭐⭐⭐⭐⭐ | Написание тестов |
| `documentation.md` | Правила документации | ⭐⭐⭐⭐ | Написание документации |
| `security-patterns.md` | Лучшие практики безопасности | ⭐⭐⭐⭐ | Ревью безопасности, паттерны |
| `project-intelligence.md` | Что и зачем | ⭐⭐⭐⭐ | Онбординг, понимание проектов |
| `project-intelligence-management.md` | Как управлять | ⭐⭐⭐ | Управление intelligence-файлами |
| `code-analysis.md` | Подходы к анализу | ⭐⭐⭐ | Анализ кода, отладка |
| `typescript.md` | Универсальные паттерны TypeScript | ⭐⭐⭐⭐ | Написание/ревью TypeScript-кода |
| `csharp.md` | Универсальные паттерны C# / .NET | ⭐⭐⭐⭐ | Написание/ревью C#-кода |
| `csharp-project-structure.md` | Структура проекта ASP.NET Core (Minimal APIs, CQRS, EF Core + PostgreSQL) | ⭐⭐⭐⭐ | Старт или структурирование C# API-проекта |

---

## Стратегия загрузки

**Для реализации кода**:
1. Загрузить `code-quality.md` (critical)
2. Загрузить `security-patterns.md` (high)

**Для TypeScript-кода**:
1. Загрузить `typescript.md` (critical)
2. Загрузить `code-quality.md` (high)

**Для C# / .NET-кода**:
1. Загрузить `csharp.md` (critical)
2. Загрузить `code-quality.md` (high)

**Для структуры C# API-проекта**:
1. Загрузить `csharp-project-structure.md` (critical)
2. Загрузить `csharp.md` (high)

**Для тестирования**:
1. Загрузить `test-coverage.md` (critical)
2. Зависит от: `code-quality.md`

**Для документации**:
1. Загрузить `documentation.md` (critical)

**Для ревью кода**:
1. Загрузить `code-quality.md` (critical)
2. Загрузить `security-patterns.md` (high)
3. Загрузить `test-coverage.md` (high)

**Для онбординга/понимания проекта**:
1. Загрузить `project-intelligence.md` (high)
2. Затем загрузить папку `../../project-intelligence/` для полного контекста проекта

---

## Связанное

- **Процессы** → `../workflows/navigation.md`
- **Принципы разработки** → `../../development/principles/`
- **Project Intelligence** → `../../project-intelligence/navigation.md` (полный контекст проекта)
