<!-- Context: ui/building-scrollytelling-pages | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

---
description: "Пошаговая реализация scroll-linked-анимаций последовательности изображений"
---

# Руководство: создание scrollytelling-страниц

**Purpose**: Пошаговая реализация scroll-linked-анимаций последовательности изображений

**Last Updated**: 2026-01-07

---

## Требования

- Проект Next.js 14+ с App Router
- Установленный Framer Motion (`npm i framer-motion`)
- Настроенный Tailwind CSS
- Готовая последовательность изображений (60-240 WebP frames)

---

## Шаг 1: Генерация последовательностей изображений

Используйте nano banana или AI-инструменты для изображений, чтобы создать стартовые/финальные кадры, затем сгенерируйте interpolation:

**Промпт start frame**:
```
Ultra-premium product photography of [product] on matte black surface,
minimalistic studio shoot, deep black background with subtle gradient,
soft rim lighting, cinematic, high contrast, luxury aesthetic, sharp focus,
no clutter, DSLR 85mm f/1.8, photorealistic
```

**Промпт end frame**:
```
Exploded technical diagram of same [product], every component separated
and floating in alignment, against deep black studio background, visible
internal structure, hyper-realistic, studio rim lighting, cinematic,
high contrast, no labels, photorealistic
```

**Сгенерируйте видео**: используйте AI video tools (Runway, Pika), чтобы интерполировать между кадрами.

**Экспортируйте кадры**: используйте ffmpeg или ezgif, чтобы разделить видео на 120+ WebP-изображений.

```bash
ffmpeg -i animation.mp4 -vf fps=30 frame_%04d.webp
```

---

## Шаг 2: Структура проекта

```
app/
├── page.tsx                    # Main landing page
├── components/
│   └── HeadphoneScroll.tsx    # Scroll animation component
└── globals.css                 # Dark theme, Inter font
public/
└── frames/
    ├── frame_0001.webp        # 120+ frames
    ├── frame_0002.webp
    └── ...
```

---

## Шаг 3: Настройка globals.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-[#050505] text-white antialiased;
    font-family: 'Inter', -apple-system, sans-serif;
  }
}
```

---

## Шаг 4: Создание scroll-компонента

**Ключевые паттерны**:
- Container с `h-[400vh]` для длинного scroll
- Canvas с `sticky top-0` остается fixed
- `useScroll` отслеживает scroll progress (0-1)
- `useTransform` мапит progress на frame index
- `useEffect` предварительно загружает все изображения

**Основная логика**:
```tsx
const { scrollYProgress } = useScroll({ target: containerRef })
const frameIndex = useTransform(scrollYProgress, [0, 1], [0, 119])
```

---

## Шаг 5: Реализация preloader

Всегда предварительно загружайте изображения перед стартом анимации:

```tsx
useEffect(() => {
  const loadImages = async () => {
    const promises = Array.from({ length: 120 }, (_, i) => {
      return new Promise((resolve) => {
        const img = new Image()
        img.src = `/frames/frame_${String(i + 1).padStart(4, '0')}.webp`
        img.onload = () => resolve(img)
      })
    })
    
    const loaded = await Promise.all(promises)
    setImages(loaded)
    setLoading(false)
  }
  
  loadImages()
}, [])
```

---

## Шаг 6: Canvas rendering

Рисуйте текущий кадр в canvas при каждом обновлении scroll:

```tsx
useEffect(() => {
  if (!canvasRef.current || !images.length) return
  
  const canvas = canvasRef.current
  const ctx = canvas.getContext('2d')
  const img = images[Math.round(currentFrame)]
  
  // Scale canvas to window
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  
  // Draw centered
  ctx.drawImage(img, 
    (canvas.width - img.width) / 2, 
    (canvas.height - img.height) / 2
  )
}, [currentFrame, images])
```

---

## Шаг 7: Добавление текстовых overlays

Делайте fade in/out текста в конкретных scroll positions:

```tsx
<motion.div
  style={{
    opacity: useTransform(scrollYProgress, 
      [0.25, 0.30, 0.35], // Fade in 25-30%, out 35%
      [0, 1, 0]
    )
  }}
  className="absolute left-20 text-4xl font-bold"
>
  Precision Engineering.
</motion.div>
```

---

## Шаг 8: Совпадение backgrounds

**ВАЖНО**: фон страницы ДОЛЖЕН точно совпадать с фоном изображения.

1. Откройте первый кадр в графическом редакторе
2. Используйте пипетку на фоне (например, `#050505`)
3. Установите фон страницы в globals.css тем же цветом
4. Проверьте: края изображения должны быть невидимыми

---

## Шаг 9: Оптимизация производительности

```tsx
// Add GPU hint
<canvas 
  ref={canvasRef}
  className="sticky top-0 h-screen w-full"
  style={{ willChange: 'transform' }}
/>

// Throttle redraws on mobile
useEffect(() => {
  let rafId
  const render = () => {
    // Draw logic here
    rafId = requestAnimationFrame(render)
  }
  render()
  return () => cancelAnimationFrame(rafId)
}, [])
```

---

## Шаг 10: Добавление loading state

Показывайте spinner, пока загружаются кадры:

```tsx
{loading && (
  <div className="fixed inset-0 flex items-center justify-center bg-[#050505]">
    <div className="animate-spin h-12 w-12 border-4 border-white/20 border-t-white rounded-full" />
  </div>
)}
```

---

## Частые проблемы и исправления

### Изображения не загружаются
- Проверьте точное совпадение путей файлов (case-sensitive)
- Убедитесь, что все кадры есть в `/public/frames/`
- Откройте browser console и проверьте 404 errors

### Анимация дергается
- Убедитесь, что все изображения предварительно загружены перед стартом
- Используйте WebP (не PNG/JPEG)
- Проверьте, что размер canvas не слишком большой

### Видимые края изображения
- Цвета фона не совпадают точно
- Используйте пипетку, не подбирайте на глаз
- Проверьте gradients на фоне изображения

### Производительность на mobile
- Уменьшите frame count (используйте каждый 2-й frame)
- Делайте debounce через requestAnimationFrame
- Рассмотрите отключение на small screens

---

## Чеклист тестирования

- [ ] Все кадры загружаются без 404
- [ ] Анимация плавная на 0-100% scroll
- [ ] Текст делает fade in/out в корректных позициях
- [ ] Background бесшовно совпадает с изображениями
- [ ] Loading spinner показывается до анимации
- [ ] Работает на mobile (или gracefully disabled)
- [ ] Нет console errors

---

## Связано

- concepts/scroll-linked-animations.md - понять технику
- examples/headphone-scrollytelling.md - полный пример кода
- lookup/animation-image-prompts.md - промпты для генерации кадров

---

## Ссылки

- [Next.js Image Optimization](https://nextjs.org/docs/app/building-your-application/optimizing/images)
- [Framer Motion useScroll](https://www.framer.com/motion/use-scroll/)
