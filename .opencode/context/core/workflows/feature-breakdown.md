<!-- Context: workflows/task-breakdown | Priority: high | Version: 2.0 | Updated: 2025-01-21 -->

# Руководство по декомпозиции задач

## Краткая справка

**Когда использовать**: 4+ файла, >60 мин работы, сложные зависимости, многошаговая координация

**Процесс**: область → фазы → малые задачи (1-2 ч) → зависимости → оценки

**Разделы шаблона**: обзор, предварительные условия, задачи (по фазам), стратегия тестирования, общая оценка, заметки

**Лучшие практики**: держите задачи маленькими (1-2 ч), явно указывайте зависимости, добавляйте проверку, реалистично оценивайте сроки

---

## Назначение
Фреймворк для разбиения сложных задач на управляемые последовательные подзадачи.

## Когда использовать
Обращайтесь к этому, когда:
- Задача затрагивает 4+ файла
- Оценка трудозатрат >60 минут
- Есть сложные зависимости
- Нужна многошаговая координация
- Пользователь просит декомпозицию задач

## Процесс декомпозиции

### 1. Понять полный объем
- Какое полное требование?
- Какие компоненты нужны?
- Какая конечная цель?
- Какие ограничения?

### 2. Определить основные фазы
- Какие логические группы?
- Что должно произойти первым?
- Что можно делать параллельно?
- Что от чего зависит?

### 3. Разбить на малые задачи
- Каждая задача — максимум 1-2 часа
- Ясные, выполнимые пункты
- Можно завершить независимо
- Легко проверить завершение

### 4. Определить зависимости
- Что нужно сделать первым?
- Что можно выполнять параллельно?
- Что что блокирует?
- Какой критический путь?

### 5. Оценить трудозатраты
- Реалистичные оценки времени
- Учитывать время на тестирование
- Учитывать неизвестные факторы
- Добавить буфер на сложность

## Шаблон декомпозиции

```markdown
# Task Breakdown: {Task Name}

## Обзор
{1-2 sentence description of what we're building}

## Prerequisites
- [ ] {Prerequisite 1}
- [ ] {Prerequisite 2}

## Tasks

### Phase 1: {Phase Name}
**Goal:** {What this phase accomplishes}

- [ ] **Task 1.1:** {Description}
  - **Files:** {files to create/modify}
  - **Estimate:** {time estimate}
  - **Dependencies:** {none / task X}
  - **Verification:** {how to verify it's done}

- [ ] **Task 1.2:** {Description}
  - **Files:** {files to create/modify}
  - **Estimate:** {time estimate}
  - **Dependencies:** {task 1.1}
  - **Verification:** {how to verify it's done}

### Phase 2: {Phase Name}
**Goal:** {What this phase accomplishes}

- [ ] **Task 2.1:** {Description}
  - **Files:** {files to create/modify}
  - **Estimate:** {time estimate}
  - **Dependencies:** {phase 1 complete}
  - **Verification:** {how to verify it's done}

## Стратегия тестирования
- [ ] Unit tests for {component}
- [ ] Integration tests for {flow}
- [ ] Manual testing: {scenarios}

## Total Estimate
**Time:** {X} hours
**Complexity:** {Low / Medium / High}

## Notes
{Any important context, decisions, or considerations}
```

## Пример декомпозиции

```markdown
# Task Breakdown: User Authentication System

## Обзор
Build authentication system with login, registration, and password reset.

## Prerequisites
- [ ] Database schema designed
- [ ] Email service configured

## Tasks

### Phase 1: Core Authentication
**Goal:** Basic login/logout functionality

- [ ] **Task 1.1:** Create user model and database schema
  - **Files:** `models/user.js`, `migrations/001_users.sql`
  - **Estimate:** 1 hour
  - **Dependencies:** none
  - **Verification:** Can create user in database

- [ ] **Task 1.2:** Implement password hashing
  - **Files:** `utils/password.js`
  - **Estimate:** 30 min
  - **Dependencies:** Task 1.1
  - **Verification:** Passwords are hashed, not plain text

- [ ] **Task 1.3:** Create login endpoint
  - **Files:** `routes/auth.js`, `controllers/auth.js`
  - **Estimate:** 1.5 hours
  - **Dependencies:** Task 1.1, 1.2
  - **Verification:** Can login with valid credentials

### Phase 2: Registration
**Goal:** New user registration

- [ ] **Task 2.1:** Create registration endpoint
  - **Files:** `routes/auth.js`, `controllers/auth.js`
  - **Estimate:** 1 hour
  - **Dependencies:** Phase 1 complete
  - **Verification:** Can create new user account

- [ ] **Task 2.2:** Add email validation
  - **Files:** `utils/validation.js`
  - **Estimate:** 30 min
  - **Dependencies:** Task 2.1
  - **Verification:** Invalid emails rejected

### Phase 3: Password Reset
**Goal:** Users can reset forgotten passwords

- [ ] **Task 3.1:** Generate reset tokens
  - **Files:** `utils/tokens.js`
  - **Estimate:** 1 hour
  - **Dependencies:** Phase 1 complete
  - **Verification:** Tokens generated and validated

- [ ] **Task 3.2:** Create reset endpoints
  - **Files:** `routes/auth.js`, `controllers/auth.js`
  - **Estimate:** 1.5 hours
  - **Dependencies:** Task 3.1
  - **Verification:** Can request and complete password reset

- [ ] **Task 3.3:** Send reset emails
  - **Files:** `services/email.js`
  - **Estimate:** 1 hour
  - **Dependencies:** Task 3.2
  - **Verification:** Reset emails sent successfully

## Стратегия тестирования
- [ ] Unit tests for password hashing
- [ ] Unit tests for token generation
- [ ] Integration tests for login flow
- [ ] Integration tests for registration flow
- [ ] Integration tests for password reset flow
- [ ] Manual testing: Complete user journey

## Total Estimate
**Time:** 8.5 hours
**Complexity:** Medium

## Notes
- Use bcrypt for password hashing (industry standard)
- Reset tokens expire after 1 hour
- Rate limit password reset requests
- Email service must be configured before Phase 3
```

## Лучшие практики

### Делайте задачи маленькими
- Максимум 1-2 часа на задачу
- Если больше — разбейте дальше
- Каждая задача должна завершаться за один подход

### Делайте зависимости явными
- Явно указывайте, что нужно сделать первым
- Находите возможности параллельной работы
- Отмечайте блокирующие зависимости

### Добавляйте проверку
- Как понять, что задача завершена?
- Что должно работать после завершения?
- Как это можно протестировать?

### Реалистично оценивайте сроки
- Учитывайте время на тестирование
- Учитывайте неизвестные факторы
- Добавляйте буфер на сложность
- Лучше переоценить, чем недооценить

### Группируйте связанную работу
- Организуйте по функции или компоненту
- Держите связанные задачи вместе
- Делайте фазы логичными и цельными

## Распространенные паттерны

### Паттерн Database-First
1. Спроектировать схему
2. Создать миграции
3. Собрать модели
4. Реализовать бизнес-логику
5. Добавить API-endpoints
6. Написать тесты

### Паттерн Feature-First
1. Определить требования
2. Спроектировать интерфейс
3. Реализовать основную логику
4. Добавить обработку ошибок
5. Написать тесты
6. Документировать использование

### Паттерн рефакторинга
1. Добавить тесты для текущего поведения
2. Отрефакторить небольшой участок
3. Проверить, что тесты все еще проходят
4. Повторить для следующего участка
5. Очистить и оптимизировать
6. Обновить документацию

## Краткая справка

**Хорошая декомпозиция:**
- Малые сфокусированные задачи (1-2 часа)
- Явные зависимости
- Реалистичные оценки
- Критерии проверки
- Логичные фазы

**Чеклист декомпозиции:**
- [ ] Все требования учтены
- [ ] Задачи маленькие и сфокусированные
- [ ] Зависимости определены
- [ ] Оценки реалистичны
- [ ] Тестирование включено
- [ ] Критерии проверки ясны
