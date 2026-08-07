<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство по публикации в NPM

**Цель**: быстрый справочник по публикации OpenAgents Control в npm

**Время чтения**: 3 минуты

---

## Ключевая концепция

OpenAgents Control публикуется как `@nextsystems/oac` в npm. Пользователи устанавливают его глобально и запускают `oac [profile]`, чтобы настроить проекты.

**Ключевые файлы**:
- `package.json` — конфигурация пакета
- `bin/oac.js` — точка входа CLI
- `.npmignore` — исключение dev-файлов
- `install.sh` — основной installer (запускается при выполнении `oac` пользователем)

---

## Процесс публикации

### 1. Подготовьте релиз

```bash
# Update version
npm version patch  # 0.7.0 -> 0.7.1
npm version minor  # 0.7.0 -> 0.8.0

# Update VERSION file
node -p "require('./package.json').version" > VERSION

# Update CHANGELOG.md with changes
```

### 2. Проверьте локально

```bash
# Create package
npm pack

# Install globally from tarball
npm install -g ./nextsystems-oac-0.7.1.tgz

# Test CLI
oac --version
oac --help

# Uninstall
npm uninstall -g @nextsystems/oac
```

### 3. Опубликуйте

```bash
# Login (one-time)
npm login

# Publish (scoped packages need --access public)
npm publish --access public
```

### 4. Проверьте

```bash
# Check it's live
npm view @nextsystems/oac

# Test installation
npm install -g @nextsystems/oac
oac --version
```

### 5. Создайте GitHub Release

```bash
git tag v0.7.1
git push --tags
# Create release on GitHub with changelog
```

---

## Установка пользователями

После публикации пользователи могут:

```bash
# Global install (recommended)
npm install -g @nextsystems/oac
oac developer

# Or use npx (no install)
npx @nextsystems/oac developer
```

---

## Частые проблемы

**"You do not have permission to publish"**
```bash
npm whoami  # Check you're logged in
npm publish --access public  # Scoped packages need public access
```

**"Version already exists"**
```bash
npm version patch  # Bump version first
```

**"You must verify your email"**
```bash
npm profile get  # Check email verification status
```

---

## Конфигурация пакета

**Что включено** (см. `package.json` → `files`):
- `.opencode/` — агенты, команды, context, profiles, skills, tools
- `scripts/` — installation scripts
- `bin/` — точка входа CLI
- `registry.json` — component registry
- `install.sh` — основной installer
- Документация (README, CHANGELOG, LICENSE)

**Что исключено** (см. `.npmignore`):
- `node_modules/`
- `evals/`
- `.tmp/`
- Dev-файлы

---

## Безопасность

- ✅ Включите 2FA: `npm profile enable-2fa auth-and-writes`
- ✅ Используйте надежный npm-пароль
- ✅ Scope `@nextsystems` защищен (публиковать можете только вы)

---

## Ссылки

- **Пакет**: https://www.npmjs.com/package/@nextsystems/oac
- **Статистика**: https://npm-stat.com/charts.html?package=@nextsystems/oac
- **Кодовая база**: `package.json`, `bin/oac.js`, `.npmignore`

---

**Последнее обновление**: 2026-01-30
