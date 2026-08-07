<!-- Context: openagents-repo/guides | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

# Руководство: создание релиза

**Цель**: пошаговый процесс создания нового релиза

---

## Быстрые шаги

```bash
# 1. Update version
echo "0.X.Y" > VERSION
jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json

# 2. Update CHANGELOG
# (Edit CHANGELOG.md manually)

# 3. Commit and tag
git add VERSION package.json CHANGELOG.md
git commit -m "chore: bump version to 0.X.Y"
git tag -a v0.X.Y -m "Release v0.X.Y"

# 4. Push
git push origin main
git push origin v0.X.Y
```

---

## Шаг 1: определите версию

### Семантическое версионирование

```
MAJOR.MINOR.PATCH

- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes
```

### Примеры

- `0.5.0` → `0.5.1` (bug fix)
- `0.5.0` → `0.6.0` (новая feature)
- `0.5.0` → `1.0.0` (breaking change)

---

## Шаг 2: обновите файлы версии

### Файл VERSION

```bash
echo "0.X.Y" > VERSION
```

### package.json

```bash
jq '.version = "0.X.Y"' package.json > tmp && mv tmp package.json
```

### Проверьте согласованность

```bash
cat VERSION
cat package.json | jq '.version'
# Both should show same version
```

---

## Шаг 3: обновите CHANGELOG

### Формат

```markdown
# Changelog

## [0.X.Y] - 2025-12-10

### Added
- New feature 1
- New feature 2

### Changed
- Updated feature 1
- Improved feature 2

### Fixed
- Bug fix 1
- Bug fix 2

### Removed
- Deprecated feature 1

## [Previous Version] - Date
...
```

### Советы

✅ **Группируйте по типу** — Added, Changed, Fixed, Removed  
✅ **Фокус на пользователе** — описывайте влияние, а не реализацию  
✅ **Ссылайтесь на PR** — указывайте номера PR  
✅ **Breaking changes** — явно отмечайте breaking changes  

---

## Шаг 4: зафиксируйте изменения

```bash
# Stage files
git add VERSION package.json CHANGELOG.md

# Commit
git commit -m "chore: bump version to 0.X.Y"
```

---

## Шаг 5: создайте Git tag

```bash
# Create annotated tag
git tag -a v0.X.Y -m "Release v0.X.Y"

# Verify tag
git tag -l "v0.X.Y"
git show v0.X.Y
```

---

## Шаг 6: отправьте в GitHub

```bash
# Push commit
git push origin main

# Push tag
git push origin v0.X.Y
```

---

## Шаг 7: создайте GitHub Release

### Через GitHub UI

1. Перейдите в repository на GitHub
2. Нажмите "Releases"
3. Нажмите "Create a new release"
4. Выберите tag: `v0.X.Y`
5. Title: `v0.X.Y`
6. Description: скопируйте из CHANGELOG
7. Нажмите "Publish release"

### Через GitHub CLI

```bash
gh release create v0.X.Y \
  --title "v0.X.Y" \
  --notes "$(cat CHANGELOG.md | sed -n '/## \[0.X.Y\]/,/## \[/p' | head -n -1)"
```

---

## Шаг 8: проверьте релиз

### Проверьте GitHub

- ✅ Release отображается на GitHub
- ✅ Tag корректный
- ✅ CHANGELOG включен
- ✅ Assets прикреплены (если есть)

### Проверьте установку

```bash
# Test install from GitHub
./install.sh --list

# Verify version
cat VERSION
```

---

## Полный пример

```bash
# Releasing v0.6.0

# 1. Update version
echo "0.6.0" > VERSION
jq '.version = "0.6.0"' package.json > tmp && mv tmp package.json

# 2. Update CHANGELOG
cat >> CHANGELOG.md << 'EOF'
## [0.6.0] - 2025-12-10

### Added
- New API specialist agent
- GraphQL support in backend specialist

### Changed
- Improved eval framework performance
- Updated registry schema to 2.0.0

### Fixed
- Fixed path resolution for subagents
- Fixed registry validation edge cases
EOF

# 3. Commit
git add VERSION package.json CHANGELOG.md
git commit -m "chore: bump version to 0.6.0"

# 4. Tag
git tag -a v0.6.0 -m "Release v0.6.0"

# 5. Push
git push origin main
git push origin v0.6.0

# 6. Create GitHub release
gh release create v0.6.0 \
  --title "v0.6.0" \
  --notes "See CHANGELOG.md for details"
```

---

## Чеклист

Перед релизом:

- [ ] Все тесты проходят
- [ ] Registry валиден
- [ ] VERSION обновлен
- [ ] package.json обновлен
- [ ] CHANGELOG обновлен
- [ ] Изменения закоммичены
- [ ] Tag создан
- [ ] Отправлено в GitHub
- [ ] GitHub release создан
- [ ] Установка протестирована

---

## Частые проблемы

### Несовпадение версий

**Проблема**: VERSION и package.json не совпадают  
**Решение**: обновите оба до одной версии

### Tag уже существует

**Проблема**: tag уже существует  
**Решение**: удалите tag и создайте заново
```bash
git tag -d v0.X.Y
git push origin :refs/tags/v0.X.Y
```

### Push отклонен

**Проблема**: push отклонен (ветка не актуальна)  
**Решение**: сначала подтяните последние изменения
```bash
git pull origin main
git push origin main
git push origin v0.X.Y
```

---

## Связанные файлы

- **Управление версиями**: `scripts/versioning/bump-version.sh`
- **CHANGELOG**: `CHANGELOG.md`
- **VERSION**: `VERSION`

---

**Последнее обновление**: 2025-12-10  
**Версия**: 0.5.0
