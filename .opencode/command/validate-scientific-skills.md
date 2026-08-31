---
description: Validate the vendored ScientificAgent profile, skill paths, permissions, navigation, and upstream provenance
agent: OpenCoder
---

# Validate ScientificAgent integration

Запусти из корня проекта:

```bash
python3 .opencode/scripts/validate-scientific-integration.py
```

Команда выполняет только локальные read-only проверки и не импортирует тяжёлые
научные зависимости. Сообщи итог, число skills и все найденные расхождения.
