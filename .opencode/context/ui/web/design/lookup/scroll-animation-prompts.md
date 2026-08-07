<!-- Context: ui/scroll-animation-prompts | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

---
description: "AI-промпты для генерации стартовых/финальных кадров и видеопоследовательностей для scrollytelling"
---

# Lookup: Промпты генерации изображений для scroll animation

**Purpose**: AI-промпты для генерации стартовых/финальных кадров и видеопоследовательностей для scrollytelling

**Last Updated**: 2026-01-07

---

## Обзор

Используйте эти промпты с nano banana, Runway, Pika или другими AI-инструментами, чтобы создавать последовательности изображений для scroll-анимаций.

**Workflow**: стартовый кадр → финальный кадр → video interpolation → извлечение кадров

---

## Промпты стартового кадра

### Hero shot продукта

```
Ultra-premium product photography of [PRODUCT NAME] placed on a matte black 
surface, minimalistic studio photoshoot. Deep black background (#050505) with 
subtle gradient falloff, soft rim lighting outlining edges, controlled 
reflections on smooth textures. Cinematic lighting, high contrast, luxury tech 
aesthetic, sharp focus, shallow depth of field. No clutter, no text, no logos 
emphasized. Shot with professional DSLR, 85mm lens, f/1.8, ultra-high 
resolution, photorealistic, Apple-level product shoot, dramatic mood, modern 
and elegant.
```

**Переменные**: замените [PRODUCT NAME] на ваш продукт
**Результат**: стартовая позиция, полностью собранный продукт, hero-ракурс

---

### Вариации по типу продукта

| Тип продукта | Дополнительные детали |
|--------------|-------------------|
| **Наушники** | "over-ear headphones with leather cushions and metal headband" |
| **Смартфон** | "smartphone with edge-to-edge OLED display, aluminum frame" |
| **Часы** | "luxury smartwatch with titanium case and sapphire crystal" |
| **Ноутбук** | "thin laptop with aluminum unibody, open at 45 degrees" |
| **Камера** | "mirrorless camera with prime lens attached, side profile" |

---

## Промпты финального кадра

### Разнесенный технический вид

```
Exploded technical diagram view of [PRODUCT NAME], every component precisely 
separated and floating in perfect alignment, suspended in mid-air against deep 
black studio background (#050505). Visible internal structure including 
[INTERNAL COMPONENTS], all parts evenly spaced showing assembly order. 
Hyper-realistic product visualization, ultra-sharp focus, studio rim lighting 
identical to hero shot, soft highlights tracing each component, controlled 
reflections on matte and metal surfaces. Cinematic lighting, high contrast, 
luxury engineering aesthetic, no labels, no annotations, no text. 
Photorealistic, ultra-high resolution, Apple-style industrial design render, 
dramatic and clean.
```

**Переменные**:
- [PRODUCT NAME]: ваш продукт
- [INTERNAL COMPONENTS]: конкретные детали для показа

---

### Внутренние компоненты по продуктам

| Продукт | Примеры внутренних компонентов |
|---------|------------------------------|
| **Наушники** | "copper wiring, titanium drivers, magnets, circuit boards, padding layers, metal frame" |
| **Смартфон** | "battery, logic board, cameras, OLED panel, antenna bands, frame" |
| **Часы** | "watch movement, gears, battery, sensors, display, crown mechanism" |
| **Ноутбук** | "keyboard assembly, trackpad, battery cells, logic board, cooling fans, display panel" |
| **Камера** | "sensor, shutter mechanism, lens elements, mirror assembly, circuit boards" |

---

## Промпты интерполяции видео

### Для Runway/Pika

```
Smoothly transition from fully assembled [PRODUCT] to exploded view. 
Components separate slowly and precisely, maintaining perfect alignment. 
Camera stays locked, product rotates slightly clockwise. Cinematic motion, 
professional product animation, 4-5 seconds duration, 30fps.
```

**Настройки**:
- Длительность: 4-5 секунд
- FPS: 30 (дает 120-150 кадров)
- Камера: static или slow orbit
- Движение: плавное контролируемое разделение

---

## Извлечение кадров

### Через ffmpeg

```bash
# Extract as WebP (best for web)
ffmpeg -i animation.mp4 -vf fps=30 frame_%04d.webp

# Extract as PNG (higher quality, larger)
ffmpeg -i animation.mp4 -vf fps=30 frame_%04d.png

# Extract with quality control
ffmpeg -i animation.mp4 -vf fps=30 -quality 90 frame_%04d.webp
```

### Через ezgif.com

1. Загрузите MP4-видео
2. Выберите "Video to GIF" → "Split to frames"
3. Выберите формат WebP
4. Скачайте все кадры как ZIP
5. Переименуйте: `frame_0001.webp`, `frame_0002.webp` и т. д.

---

## Совпадение цвета фона

**ВАЖНО**: фон страницы ДОЛЖЕН точно совпадать с фоном изображения

### Рекомендуемые темные фоны

| Код цвета | Использование |
|------------|-------|
| `#050505` | Почти черный с легким lift (рекомендуется) |
| `#0a0a0a` | Немного светлее, мягче |
| `#000000` | Настоящий черный (только если изображения реально черные) |
| `#1a1a1a` | Темно-серый (для более светлых render) |

**Совет**: используйте пипетку на фоне первого кадра и точный hex в CSS

---

## Альтернативные стили анимации

### Rotation (360° spin)

**Старт**: вид спереди
**Финиш**: вид спереди (после поворота на 360°)
**Промпт**: "Rotate product 360 degrees on turntable, maintain lighting"

### Zoom In (feature reveal)

**Старт**: полный вид продукта
**Финиш**: крупный план ключевой feature
**Промпт**: "Smooth camera push-in focusing on [FEATURE], maintain focus"

### Morph (смена цвета/стиля)

**Старт**: продукт в цвете A
**Финиш**: продукт в цвете B
**Промпт**: "Seamlessly morph product color from [A] to [B], maintain form"

---

## Настройки качества

### Для high-end результата

- **Разрешение**: минимум 1920x1080 (4K для high-DPI)
- **Формат**: WebP (compression) или PNG (quality)
- **Количество кадров**: 90-150 frames (3-5 секунд при 30fps)
- **Общий размер**: цель <50MB для всех кадров вместе

### Советы по оптимизации

1. Используйте формат WebP (на 70% меньше PNG)
2. Сжимайте с quality 85-90
3. Уменьшайте ширину изображений до max 2000px
4. Используйте одинаковый aspect ratio (16:9 или 1:1)

---

## Чеклист тестирования

- [ ] Цвет фона совпадает точно (без видимых краев)
- [ ] Все кадры одного размера
- [ ] Motion плавный (нет jumps между кадрами)
- [ ] Освещение консистентно по всей sequence
- [ ] Имена файлов последовательны (от `frame_0001` до `frame_0120`)
- [ ] Общий размер файлов разумный (<50MB)

---

## Связано

- concepts/scroll-linked-animations.md - понять технику
- examples/scrollytelling-headphone.md - полная реализация
- guides/scrollytelling-setup.md - инструкции по настройке

---

## Ссылки на инструменты

- [Runway ML](https://runwayml.com) - генерация AI-видео
- [Pika Labs](https://pika.art) - AI-интерполяция видео
- [ezgif](https://ezgif.com/split-video) - извлечение frames
- [FFmpeg](https://ffmpeg.org) - обработка video
