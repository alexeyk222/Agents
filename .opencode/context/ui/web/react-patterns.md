<!-- Context: ui/react-patterns | Priority: low | Version: 1.0 | Updated: 2026-02-15 -->

# React-паттерны и лучшие практики

**Category**: development  
**Purpose**: Современные React-паттерны, использование hooks и принципы дизайна компонентов  
**Used by**: frontend-specialist

---

## Обзор

Гайд описывает современные React-паттерны с функциональными компонентами, hooks и лучшими практиками для масштабируемых React-приложений.

## Паттерны компонентов

### 1. Функциональные компоненты с hooks

**Всегда используйте функциональные компоненты**:
```jsx
// Good
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]);
  
  return <div>{user?.name}</div>;
}
```

### 2. Custom hooks для переиспользуемой логики

**Выносите общую логику в custom hooks**:
```jsx
// Custom hook
function useUser(userId) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    setLoading(true);
    fetchUser(userId)
      .then(setUser)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [userId]);
  
  return { user, loading, error };
}

// Usage
function UserProfile({ userId }) {
  const { user, loading, error } = useUser(userId);
  
  if (loading) return <Spinner />;
  if (error) return <Error message={error.message} />;
  return <div>{user.name}</div>;
}
```

### 3. Composition вместо props drilling

**Используйте composition, чтобы избежать props drilling**:
```jsx
// Bad - Props drilling
function App() {
  const [theme, setTheme] = useState('light');
  return <Layout theme={theme} setTheme={setTheme} />;
}

// Good - Composition with Context
const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Layout />
    </ThemeContext.Provider>
  );
}

function Layout() {
  const { theme } = useContext(ThemeContext);
  return <div className={theme}>...</div>;
}
```

### 4. Compound components

**Для сложных связанных компонентов**:
```jsx
function Tabs({ children }) {
  const [activeTab, setActiveTab] = useState(0);
  
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
}

Tabs.List = function TabsList({ children }) {
  return <div className="tabs-list">{children}</div>;
};

Tabs.Tab = function Tab({ index, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  return (
    <button 
      className={activeTab === index ? 'active' : ''}
      onClick={() => setActiveTab(index)}
    >
      {children}
    </button>
  );
};

Tabs.Panel = function TabPanel({ index, children }) {
  const { activeTab } = useContext(TabsContext);
  return activeTab === index ? <div>{children}</div> : null;
};

// Usage
<Tabs>
  <Tabs.List>
    <Tabs.Tab index={0}>Tab 1</Tabs.Tab>
    <Tabs.Tab index={1}>Tab 2</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panel index={0}>Content 1</Tabs.Panel>
  <Tabs.Panel index={1}>Content 2</Tabs.Panel>
</Tabs>
```

## Лучшие практики hooks

### 1. Зависимости useEffect

**Всегда указывайте зависимости корректно**:
```jsx
// Bad - Missing dependencies
useEffect(() => {
  fetchData(userId);
}, []);

// Good - Correct dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]);

// Good - Stable function reference
const fetchData = useCallback((id) => {
  api.getUser(id).then(setUser);
}, []);

useEffect(() => {
  fetchData(userId);
}, [userId, fetchData]);
```

### 2. useMemo для дорогих вычислений

**Мемоизируйте дорогие вычисления**:
```jsx
function DataTable({ data, filters }) {
  const filteredData = useMemo(() => {
    return data.filter(item => 
      filters.every(filter => filter(item))
    );
  }, [data, filters]);
  
  return <Table data={filteredData} />;
}
```

### 3. useCallback для стабильных ссылок

**Предотвращайте лишние re-render**:
```jsx
function Parent() {
  const [count, setCount] = useState(0);
  
  // Bad - New function on every render
  const handleClick = () => setCount(c => c + 1);
  
  // Good - Stable function reference
  const handleClick = useCallback(() => {
    setCount(c => c + 1);
  }, []);
  
  return <Child onClick={handleClick} />;
}

const Child = memo(function Child({ onClick }) {
  return <button onClick={onClick}>Click</button>;
});
```

## Паттерны управления состоянием

### 1. Сначала local state

**Начинайте с local state и поднимайте состояние только при необходимости**:
```jsx
// Local state
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}

// Lifted state when shared
function App() {
  const [count, setCount] = useState(0);
  return (
    <>
      <Counter count={count} setCount={setCount} />
      <Display count={count} />
    </>
  );
}
```

### 2. useReducer для сложного состояния

**Используйте reducer для связанных обновлений состояния**:
```jsx
const initialState = { count: 0, step: 1 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'setStep':
      return { ...state, step: action.payload };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return (
    <>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <span>{state.count}</span>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
    </>
  );
}
```

## Оптимизация производительности

### 1. Code splitting

**Lazy-load маршруты и тяжелые компоненты**:
```jsx
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./Dashboard'));
const Settings = lazy(() => import('./Settings'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

### 2. Виртуализация длинных списков

**Используйте виртуализацию для больших наборов данных**:
```jsx
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );
  
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

## Лучшие практики

1. **Держите компоненты маленькими и сфокусированными** - принцип single responsibility
2. **Используйте TypeScript** - type safety предотвращает баги и улучшает DX
3. **Colocate связанный код** - держите компоненты, стили и тесты рядом
4. **Используйте понятные имена props** - ясные описательные имена улучшают читаемость
5. **Избегайте inline functions в JSX** - выносите в именованные функции или useCallback
6. **Используйте fragments** - избегайте лишних wrapper div
7. **Обрабатывайте loading и error states** - всегда показывайте пользователям feedback
8. **Тестируйте компоненты** - используйте React Testing Library для user-centric тестов

## Антипаттерны

- ❌ **Prop drilling** - вместо этого используйте context или composition
- ❌ **Огромные компоненты** - разбивайте на маленькие сфокусированные компоненты
- ❌ **Прямая мутация state** - всегда используйте setState или dispatch
- ❌ **Index как key** - используйте стабильные уникальные идентификаторы
- ❌ **Лишний useEffect** - по возможности выводите state из данных
- ❌ **Игнорирование ESLint warnings** - правила React hooks предотвращают баги
- ❌ **Нет memoization для context values** - вызывает лишние re-render

## Ссылки

- React Documentation (react.dev)
- React Patterns by Kent C. Dodds
- Epic React by Kent C. Dodds
