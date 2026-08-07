<!-- Context: development/api-design | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# Паттерны проектирования API

**Категория**: development  
**Назначение**: Принципы проектирования REST API, паттерны GraphQL и стратегии версионирования API  
**Используют**: opencoder

---

## Обзор

Это руководство описывает лучшие практики проектирования надёжных, масштабируемых и поддерживаемых API, включая REST, GraphQL и стратегии версионирования.

## Проектирование REST API

### 1. URL на основе ресурсов

**Используйте существительные, а не глаголы**:
```
# Bad
GET  /getUsers
POST /createUser
POST /updateUser/123

# Good
GET    /users
POST   /users
PUT    /users/123
PATCH  /users/123
DELETE /users/123
```

### 2. HTTP-методы

**Используйте подходящие HTTP-методы**:
- `GET` - получение ресурсов (идемпотентный, безопасный)
- `POST` - создание новых ресурсов
- `PUT` - полная замена ресурса (идемпотентный)
- `PATCH` - частичное обновление (идемпотентный)
- `DELETE` - удаление ресурса (идемпотентный)

### 3. Коды статуса

**Используйте стандартные коды статуса HTTP**:
```
2xx Success
  200 OK - Successful GET, PUT, PATCH
  201 Created - Successful POST
  204 No Content - Successful DELETE

4xx Client Errors
  400 Bad Request - Invalid input
  401 Unauthorized - Missing/invalid auth
  403 Forbidden - Authenticated but not authorized
  404 Not Found - Resource doesn't exist
  409 Conflict - Resource conflict (e.g., duplicate)
  422 Unprocessable Entity - Validation errors

5xx Server Errors
  500 Internal Server Error - Unexpected error
  503 Service Unavailable - Temporary unavailability
```

### 4. Единый формат ответа

**Стандартизируйте структуру ответа**:
```json
// Success response
{
  "data": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z"
  }
}

// Error response
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z",
    "requestId": "abc-123"
  }
}

// Collection response
{
  "data": [...],
  "meta": {
    "total": 100,
    "page": 1,
    "pageSize": 20,
    "totalPages": 5
  },
  "links": {
    "self": "/users?page=1",
    "next": "/users?page=2",
    "prev": null,
    "first": "/users?page=1",
    "last": "/users?page=5"
  }
}
```

### 5. Фильтрация, сортировка, пагинация

**Поддерживайте типовые query-операции**:
```
# Filtering
GET /users?status=active&role=admin

# Sorting
GET /users?sort=createdAt:desc,name:asc

# Pagination
GET /users?page=2&pageSize=20

# Field selection
GET /users?fields=id,name,email

# Search
GET /users?q=john
```

### 6. Вложенные ресурсы

**Обрабатывайте связи корректно**:
```
# Good - Shallow nesting
GET /users/123/posts
GET /posts?userId=123

# Avoid - Deep nesting
GET /users/123/posts/456/comments/789
# Better
GET /comments/789
```

## Паттерны GraphQL

### 1. Проектирование схемы

**Проектируйте понятные, интуитивные схемы**:
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
  publishedAt: DateTime
}

type Query {
  user(id: ID!): User
  users(filter: UserFilter, page: Int, pageSize: Int): UserConnection!
  post(id: ID!): Post
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}

input CreateUserInput {
  name: String!
  email: String!
}

input UserFilter {
  status: UserStatus
  role: UserRole
  search: String
}
```

### 2. Паттерны resolver-ов

**Реализуйте эффективные resolvers**:
```javascript
const resolvers = {
  Query: {
    user: async (_, { id }, { dataSources }) => {
      return dataSources.userAPI.getUser(id);
    },
    users: async (_, { filter, page, pageSize }, { dataSources }) => {
      return dataSources.userAPI.getUsers({ filter, page, pageSize });
    }
  },
  
  User: {
    posts: async (user, _, { dataSources }) => {
      // Use DataLoader to batch requests
      return dataSources.postAPI.getPostsByUserId(user.id);
    }
  },
  
  Mutation: {
    createUser: async (_, { input }, { dataSources, user }) => {
      // Check authorization
      if (!user) throw new AuthenticationError('Not authenticated');
      
      // Validate input
      const validatedInput = validateUserInput(input);
      
      // Create user
      return dataSources.userAPI.createUser(validatedInput);
    }
  }
};
```

### 3. DataLoader для предотвращения N+1

**Батчите и кэшируйте запросы к базе данных**:
```javascript
import DataLoader from 'dataloader';

const userLoader = new DataLoader(async (userIds) => {
  const users = await db.users.findMany({
    where: { id: { in: userIds } }
  });
  
  // Return in same order as input
  return userIds.map(id => users.find(u => u.id === id));
});

// Usage in resolver
const user = await userLoader.load(userId);
```

## Паттерны frontend-клиента API (TanStack Query)

**Используйте TanStack Query для оптимальной работы с API на клиенте**:

### Интеграция REST
```javascript
// Optimal REST client with TanStack Query v5
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const apiClient = {
  getUsers: (filters) => 
    fetch(`/api/v1/users?${new URLSearchParams(filters)}`).then(r => r.json())
};

function UsersList() {
  const { data, isPending, error } = useQuery({
    queryKey: ['users', filters],
    queryFn: () => apiClient.getUsers(filters),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  return (
    <div>
      {isPending && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data?.data.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
}


## Версионирование API

### 1. Версионирование в URL

**Указывайте версию в URL path**:
```
GET /v1/users
GET /v2/users
```

**Плюсы**: понятно, легко маршрутизировать  
**Минусы**: меняется URL, сложнее поддерживать несколько версий

### 2. Версионирование в заголовке (header)

**Указывайте версию в Accept header**:
```
GET /users
Accept: application/vnd.myapi.v2+json
```

**Плюсы**: чистые URL, гибко  
**Минусы**: менее заметно, сложнее тестировать

### 3. Стратегия вывода из эксплуатации (deprecation)

**Сообщайте о выводе из эксплуатации явно**:
```javascript
// Response headers
Deprecation: true
Sunset: Sat, 31 Dec 2024 23:59:59 GMT
Link: <https://api.example.com/v2/users>; rel="successor-version"

// Response body
{
  "data": {...},
  "meta": {
    "deprecated": true,
    "deprecationDate": "2024-12-31",
    "migrationGuide": "https://docs.example.com/migration/v1-to-v2"
  }
}
```

## Аутентификация и авторизация

### 1. JWT-токены

**Используйте JWT для stateless auth**:
```javascript
// Token structure
{
  "sub": "user-123",
  "email": "user@example.com",
  "role": "admin",
  "iat": 1516239022,
  "exp": 1516242622
}

// Middleware
function authenticateToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

### 2. Управление доступом на основе ролей (RBAC)

**Реализуйте RBAC**:
```javascript
function authorize(...roles) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Not authenticated' });
    }
    
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    
    next();
  };
}

// Usage
app.delete('/users/:id', 
  authenticateToken, 
  authorize('admin'), 
  deleteUser
);
```

## Лучшие практики

1. **Используйте HTTPS везде** - шифруйте весь API-трафик
2. **Добавляйте rate limiting** - предотвращайте злоупотребления и обеспечивайте справедливое использование
3. **Валидируйте все inputs** - никогда не доверяйте данным клиента
4. **Используйте корректную обработку ошибок** - возвращайте понятные сообщения
5. **Документируйте API** - используйте OpenAPI/Swagger или GraphQL introspection
6. **Версионируйте API** - планируйте breaking changes
7. **Настраивайте CORS корректно** - аккуратно задавайте allowed origins
8. **Логируйте запросы и ошибки** - включайте отладку и мониторинг
9. **Используйте caching** - реализуйте ETags и Cache-Control headers
10. **Тестируйте тщательно** - unit, integration и contract tests

## Антипаттерны

- ❌ **Раскрытие внутренних IDs** - используйте UUID или opaque identifiers
- ❌ **Слишком много данных в ответе** - поддерживайте field selection
- ❌ **Игнорирование idempotency** - PUT/PATCH/DELETE должны быть idempotent
- ❌ **Несогласованное именование** - последовательно используйте camelCase или snake_case
- ❌ **Нет pagination** - всегда пагинируйте коллекции
- ❌ **Нет rate limiting** - защищайтесь от злоупотреблений
- ❌ **Избыточные сообщения об ошибках** - не раскрывайте детали реализации
- ❌ **Синхронные долгие операции** - используйте async jobs для долгих задач

## Источники

- REST API Design Rulebook — Mark Masse
- GraphQL Best Practices (graphql.org)
- API Design Patterns — JJ Geewax
- OpenAPI Specification (swagger.io)
