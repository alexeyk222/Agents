<!-- Context: core/standards | Priority: critical | Version: 1.0 | Updated: 2026-02-16 -->

# Универсальные стандарты TypeScript

**Назначение**: Универсальные паттерны TypeScript для любого TypeScript-проекта  
**Область**: Паттерны уровня языка, не специфичные для фреймворков  
**Последнее обновление**: 2026-02-16

---

## Содержание

1. [Паттерны функций](#1-function-patterns)
2. [Type Safety](#2-type-safety)
3. [Операции с массивами](#3-array-operations)
4. [Async-паттерны](#4-async-patterns)
5. [Control Flow](#5-control-flow)
6. [Организация кода](#6-code-organization)
7. [Принципы тестирования](#7-testing-principles)
8. [Именование переменных](#8-variable-naming)

---

<a id="1-function-patterns"></a>

## 1. Паттерны функций

### 1.1 Соглашение об именовании

**Правило: Предпочитайте имена функций из одного слова**

```typescript
// ✅ GOOD - Single-word names
export function create() {...}
export function fork() {...}
export function touch() {...}
export function get() {...}
export async function stream(input: StreamInput) {...}

// ✅ ACCEPTABLE - Multi-word only when necessary
export function isDefaultTitle(title: string) {...}      // Boolean predicate
export function assertNotBusy(sessionID: string) {...}   // Assertion pattern
export async function createNext(input) {...}            // Version disambiguation
export async function resolvePromptParts(template) {...} // Complex operation needs clarity

// ❌ AVOID - Unnecessary multi-word names
function prepareJournal(dir: string) {}  // Use: journal()
function getUserData(id: string) {}      // Use: user()
function processFileContent(path) {}     // Use: process()
```

### 1.2 Чистые функции

**Правило: По возможности предпочитайте чистые функции**

```typescript
// ✅ GOOD - Pure function
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0)
}

// ❌ AVOID - Side effects
let total = 0
function addToTotal(item: Item) {
  total += item.price  // Mutates external state
}
```

### 1.3 Композиция функций

```typescript
// ✅ GOOD - Functional composition with pipes
const filtered = agents
  .filter((a) => a.mode !== "primary")
  .filter((a) => hasPermission(a, caller))
  .map((a) => a.name)

// ✅ GOOD - Higher-order functions
export function withRetry<T>(fn: () => Promise<T>, maxRetries: number): Promise<T> {
  return fn().catch((error) => {
    if (maxRetries > 0) {
      return withRetry(fn, maxRetries - 1)
    }
    throw error
  })
}
```

---

<a id="2-type-safety"></a>

## 2. Type Safety

### 2.1 TypeScript-типы

**Правило: Используйте систему типов TypeScript, избегайте `any`**

```typescript
// ✅ GOOD - Explicit types
interface User {
  id: string
  name: string
  email: string
}

function getUser(id: string): User {
  // Implementation
}

// ❌ AVOID - any type
function getUser(id: any): any {
  // Loses all type safety
}
```

### 2.2 Вывод типов

**Правило: Позволяйте TypeScript выводить тип, когда он очевиден**

```typescript
// ✅ GOOD - Inference works
const count = 42  // TypeScript knows this is number
const users = await fetchUsers()  // Type inferred from return type

// ❌ AVOID - Redundant annotations
const count: number = 42
const users: User[] = await fetchUsers()
```

### 2.3 Type guards

**Правило: Используйте type guards для runtime-проверки типов**

```typescript
// ✅ GOOD - Type guard
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  )
}

// Usage
if (isUser(data)) {
  console.log(data.name)  // TypeScript knows data is User
}
```

### 2.4 Избегайте Any

**Правило: Используйте `unknown` вместо `any`, когда тип действительно неизвестен**

```typescript
// ✅ GOOD - unknown requires type checking
function processData(data: unknown) {
  if (typeof data === "string") {
    return data.toUpperCase()
  }
  throw new Error("Invalid data")
}

// ❌ AVOID - any bypasses type checking
function processData(data: any) {
  return data.toUpperCase()  // No compile-time safety
}
```

---

<a id="3-array-operations"></a>

## 3. Операции с массивами

### 3.1 Функциональные методы (предпочтительно)

**Правило: Предпочитайте map/filter/reduce вместо for-loops**

```typescript
// ✅ GOOD - Functional chain with type inference
const files = messages
  .flatMap((x) => x.parts)
  .filter((x): x is Patch => x.type === "patch")
  .flatMap((x) => x.files)
  .map((x) => path.relative(worktree, x))

// ✅ GOOD - Parallel async operations
const results = await Promise.all(
  toolCalls.map(async (call) => {
    return executeCall(call)
  }),
)

// ✅ GOOD - Reduce for aggregation
const totalAdditions = diffs.reduce((sum, x) => sum + x.additions, 0)

// ✅ GOOD - Unique values
const uniqueNames = Array.from(new Set(items.map((x) => x.name)))

// ✅ GOOD - Sorting
const sorted = items.toSorted((a, b) => a.timestamp - b.timestamp)
```

### 3.2 For-loops (когда нужно)

**Правило: Используйте for-loops только для:**
1. Сложных алгоритмов (DP, graph traversal)
2. Требований early exit
3. Последовательных side effects
4. Performance-critical iteration

```typescript
// ✅ GOOD - Early exit
const patches = []
for (const msg of all) {
  if (msg.info.id === targetID) break
  for (const part of msg.parts) {
    if (part.type === "patch") {
      patches.push(part)
    }
  }
}

// ✅ GOOD - Sequential mutations
for (const key of Object.keys(tools)) {
  if (disabled.has(key)) {
    delete tools[key]
  }
}
```

### 3.3 Type guards в filter

**Правило: Используйте type guards, чтобы сохранить дальнейший вывод типов**

```typescript
// ✅ GOOD - Type guard preserves type information
const patches = messages
  .flatMap((msg) => msg.parts)
  .filter((part): part is PatchPart => part.type === "patch")
// patches is now PatchPart[], not Part[]

// ❌ BAD - Loses type information
const patches = messages
  .flatMap((msg) => msg.parts)
  .filter((part) => part.type === "patch")
// patches is still Part[], requires casting later
```

---

<a id="4-async-patterns"></a>

## 4. Async-паттерны

### 4.1 Параллельное выполнение (default pattern)

**Правило: Используйте `Promise.all` для независимых операций**

```typescript
// ✅ GOOD - Parallel independent operations
const [language, cfg, provider, auth] = await Promise.all([
  getLanguage(model),
  getConfig(),
  getProvider(model.providerID),
  getAuth(model.providerID),
])

// ✅ GOOD - Parallel array processing
const results = await Promise.all(
  items.map(async (item) => {
    return processItem(item)
  }),
)

// ❌ BAD - Sequential when independent
const language = await getLanguage(model)
const cfg = await getConfig()  // Could run in parallel!
const provider = await getProvider(model.providerID)
```

### 4.2 Последовательные операции

**Правило: Стройте цепочку, когда операции зависят от предыдущих результатов**

```typescript
// ✅ GOOD - Sequential dependency chain
const session = await createSession({ title: "New" })
const message = await addMessage(session.id, { content: "Hello" })
const response = await processMessage(message.id)

// ✅ GOOD - Promise chain for clarity
const result = await createSession({ title: "New" })
  .then((session) => addMessage(session.id, { content: "Hello" }))
  .then((message) => processMessage(message.id))
```

### 4.3 Обработка ошибок в async

**Правило: По возможности предпочитайте `.catch()` вместо try/catch**

```typescript
// ✅ GOOD - Catch at call site
const result = await operation().catch((error) => {
  console.error("Operation failed", error)
  return defaultValue
})

// ✅ GOOD - Promise.all with error handling
const results = await Promise.all(
  items.map(async (item) => {
    return processItem(item).catch((error) => {
      console.error("Item failed", { item, error })
      return null
    })
  }),
)

// ✅ ACCEPTABLE - try/catch for multiple operations
try {
  const session = await createSession(input)
  await addMessage(session.id, message)
  await publishEvent({ session })
  return session
} catch (error) {
  console.error("Session creation failed", error)
  throw error
}

// ❌ AVOID - try/catch for single operation
try {
  const result = await operation()
  return result
} catch (error) {
  console.error(error)
  throw error
}
// Better:
const result = await operation().catch((error) => {
  console.error(error)
  throw error
})
```

---

<a id="5-control-flow"></a>

## 5. Control Flow

### 5.1 Early returns

**Правило: Избегайте `else`, используйте early returns**

```typescript
// ✅ GOOD - Early returns
function getStatus(session: Session) {
  if (!session) return "not_found"
  if (session.busy) return "busy"
  if (session.error) return "error"
  return "ready"
}

async function process(id: string) {
  const session = await getSession(id)
  if (!session) return { error: "Not found" }

  const result = await execute(session)
  if (!result.success) return { error: result.message }

  return { data: result.data }
}

// ❌ BAD - Else statements
function getStatus(session: Session) {
  if (!session) {
    return "not_found"
  } else {
    if (session.busy) {
      return "busy"
    } else {
      if (session.error) {
        return "error"
      } else {
        return "ready"
      }
    }
  }
}
```

### 5.2 Guard clauses

```typescript
// ✅ GOOD - Guard clauses at function start
async function updateSession(id: string, data: UpdateData) {
  if (!id) throw new Error("ID required")
  if (!data) throw new Error("Data required")
  if (data.title && data.title.length > 100) throw new Error("Title too long")

  // Main logic here
  const session = await getSession(id)
  await update(id, data)
  return session
}
```

### 5.3 Switch statements

**Правило: Используйте exhaustive switch с default case**

```typescript
// ✅ GOOD - Exhaustive switch
function handleEvent(event: Event) {
  switch (event.type) {
    case "start":
      return handleStart(event)
    
    case "update":
      return handleUpdate(event)
    
    case "complete":
      return handleComplete(event)
    
    default:
      const _exhaustive: never = event
      throw new Error(`Unhandled event type: ${(event as any).type}`)
  }
}
```

---

<a id="6-code-organization"></a>

## 6. Организация кода

### 6.1 Порядок импортов

**Правило: Организуйте импорты по источнику**

```typescript
// ✅ GOOD - Organized imports
// 1. Node built-ins
import path from "path"
import fs from "fs/promises"

// 2. External packages
import { z } from "zod"
import express from "express"

// 3. Internal modules
import { User } from "./types"
import { getConfig } from "./config"
```

### 6.2 Соглашения об именовании

```typescript
// ✅ GOOD - Clear naming
const session = await getSession(id)
const user = await getCurrentUser()
const messages = await getMessages({ sessionID })

// ❌ BAD - Unnecessary verbosity
const currentSession = await getSession(id)
const currentlyAuthenticatedUser = await getCurrentUser()
const sessionMessagesList = await getMessages({ sessionID })

// ✅ GOOD - Multi-word when single word is ambiguous
const sessionID = params.id
const userAgent = req.headers["user-agent"]
const maxRetries = config.retries
```

### 6.3 Структура файла

**Правило: Один основной export на файл**

```typescript
// user.ts
export interface User {
  id: string
  name: string
}

export async function getUser(id: string): Promise<User> {
  // Implementation
}

export async function createUser(data: CreateUserInput): Promise<User> {
  // Implementation
}
```

---

<a id="7-testing-principles"></a>

## 7. Принципы тестирования

### 7.1 Структура теста

**Правило: Следуйте паттерну Arrange-Act-Assert**

```typescript
// ✅ GOOD - AAA pattern
test("creates user with valid data", async () => {
  // Arrange
  const userData = { name: "Alice", email: "alice@example.com" }
  
  // Act
  const user = await createUser(userData)
  
  // Assert
  expect(user.name).toBe("Alice")
  expect(user.email).toBe("alice@example.com")
})
```

### 7.2 Цели покрытия

**Правило: Тестируйте и успешные, и ошибочные сценарии**

```typescript
// ✅ GOOD - Both positive and negative tests
describe("createUser", () => {
  test("creates user with valid data", async () => {
    const user = await createUser({ name: "Alice", email: "alice@example.com" })
    expect(user).toBeDefined()
  })
  
  test("throws error with invalid email", async () => {
    await expect(
      createUser({ name: "Alice", email: "invalid" })
    ).rejects.toThrow("Invalid email")
  })
})
```

### 7.3 Мокайте внешние зависимости

**Правило: Мокайте все внешние зависимости**

```typescript
// ✅ GOOD - Mocked dependencies
test("fetches user data", async () => {
  const mockFetch = vi.fn().mockResolvedValue({
    json: () => Promise.resolve({ id: "1", name: "Alice" })
  })
  
  global.fetch = mockFetch
  
  const user = await fetchUser("1")
  expect(user.name).toBe("Alice")
})
```

---

<a id="8-variable-naming"></a>

## 8. Именование переменных

### 8.1 Объявление переменных

**Правило: Предпочитайте `const` вместо `let`**

```typescript
// ✅ GOOD - Immutable with ternary
const foo = condition ? 1 : 2
const result = await (isValid ? processValid() : processInvalid())

// ❌ BAD - Reassignment
let foo
if (condition) {
  foo = 1
} else {
  foo = 2
}

// ✅ GOOD - Early return instead of reassignment
function getValue(condition: boolean) {
  if (condition) return 1
  return 2
}

// ✅ ACCEPTABLE - let when mutation is necessary
let accumulator = 0
for (const item of items) {
  accumulator += item.value
}
```

### 8.2 Destructuring

**Правило: Избегайте лишнего destructuring, сохраняйте контекст через dot notation**

```typescript
// ✅ GOOD - Preserve context
function process(session: Session) {
  console.log("processing", { id: session.id, title: session.title })
  return {
    id: session.id,
    status: session.status,
    owner: session.owner
  }
}

// ❌ BAD - Loses context, harder to read
function process(session: Session) {
  const { id, title, status, owner } = session
  console.log("processing", { id, title })
  return { id, status, owner }
}

// ✅ ACCEPTABLE - Destructuring when improving readability
function renderUser({ name, email, avatar }: User) {
  return `<div>${name} (${email})</div>`
}

// ✅ ACCEPTABLE - Destructuring array returns
const [language, cfg, provider] = await Promise.all([...])
```

---

## Связанные стандарты

- **OpenCode TypeScript**: `.opencode/context/openagents-repo/standards/opencode-typescript.md` (паттерны конкретного фреймворка)
- **Качество кода**: `.opencode/context/core/standards/code-quality.md` (общие стандарты качества)
- **Покрытие тестами**: `.opencode/context/core/standards/test-coverage.md` (стандарты тестирования)

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-16  
**Maintainer**: OpenAgents Control Team
