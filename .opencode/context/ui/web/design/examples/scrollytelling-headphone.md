<!-- Context: ui/scrollytelling-headphone | Priority: high | Version: 1.0 | Updated: 2026-02-15 -->

---
description: "Полная Next.js-реализация scroll-linked-анимации последовательности изображений"
---

# Example: Scrollytelling-анимация наушников

**Purpose**: Полная Next.js-реализация scroll-linked-анимации последовательности изображений

**Last Updated**: 2026-01-07

---

## Обзор

Полный рабочий пример scrollytelling-страницы для наушников "Zenith X" на Next.js 14, Framer Motion и Canvas.

**Стек**: Next.js 14 (App Router) + Framer Motion + Canvas + Tailwind CSS

---

## Структура файлов

```
app/
├── page.tsx
├── components/
│   └── HeadphoneScroll.tsx
└── globals.css
public/
└── frames/
    └── frame_0001.webp through frame_0120.webp
```

---

## 1. globals.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-[#050505] text-white antialiased;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  }
}
```

---

## 2. app/page.tsx

```tsx
import HeadphoneScroll from './components/HeadphoneScroll'

export default function Home() {
  return (
    <main className="bg-[#050505]">
      <HeadphoneScroll />
    </main>
  )
}
```

---

## 3. components/HeadphoneScroll.tsx

```tsx
'use client'

import { useEffect, useRef, useState } from 'react'
import { motion, useScroll, useTransform } from 'framer-motion'

const FRAME_COUNT = 120

export default function HeadphoneScroll() {
  const containerRef = useRef<HTMLDivElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [images, setImages] = useState<HTMLImageElement[]>([])
  const [loading, setLoading] = useState(true)

  // Track scroll progress (0 to 1)
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end end']
  })

  // Map scroll progress to frame index
  const frameIndex = useTransform(scrollYProgress, [0, 1], [0, FRAME_COUNT - 1])
  const [currentFrame, setCurrentFrame] = useState(0)

  // Update current frame
  useEffect(() => {
    return frameIndex.on('change', (latest) => {
      setCurrentFrame(Math.round(latest))
    })
  }, [frameIndex])

  // Preload all images
  useEffect(() => {
    const loadImages = async () => {
      const promises = Array.from({ length: FRAME_COUNT }, (_, i) => {
        return new Promise<HTMLImageElement>((resolve) => {
          const img = new Image()
          const frameNum = String(i + 1).padStart(4, '0')
          img.src = `/frames/frame_${frameNum}.webp`
          img.onload = () => resolve(img)
        })
      })

      const loaded = await Promise.all(promises)
      setImages(loaded)
      setLoading(false)
    }

    loadImages()
  }, [])

  // Render current frame to canvas
  useEffect(() => {
    if (!canvasRef.current || !images.length) return

    const canvas = canvasRef.current
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    const img = images[currentFrame]

    // Set canvas size
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight

    // Clear and draw centered
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    
    const scale = Math.min(
      canvas.width / img.width,
      canvas.height / img.height
    )
    
    const x = (canvas.width - img.width * scale) / 2
    const y = (canvas.height - img.height * scale) / 2
    
    ctx.drawImage(img, x, y, img.width * scale, img.height * scale)
  }, [currentFrame, images])

  // Text overlay opacity transforms
  const title = useTransform(scrollYProgress, [0, 0.1, 0.2], [1, 1, 0])
  const text1 = useTransform(scrollYProgress, [0.25, 0.3, 0.4], [0, 1, 0])
  const text2 = useTransform(scrollYProgress, [0.55, 0.6, 0.7], [0, 1, 0])
  const cta = useTransform(scrollYProgress, [0.85, 0.9, 1], [0, 1, 1])

  if (loading) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-[#050505]">
        <div className="h-12 w-12 animate-spin rounded-full border-4 border-white/20 border-t-white" />
      </div>
    )
  }

  return (
    <div ref={containerRef} className="relative h-[400vh]">
      {/* Sticky Canvas */}
      <canvas
        ref={canvasRef}
        className="sticky top-0 h-screen w-full"
        style={{ willChange: 'transform' }}
      />

      {/* Text Overlays */}
      <motion.div
        style={{ opacity: title }}
        className="pointer-events-none fixed inset-0 flex items-center justify-center"
      >
        <div className="text-center">
          <h1 className="text-7xl font-bold tracking-tight text-white/90">
            Zenith X
          </h1>
          <p className="mt-4 text-xl text-white/60">Pure Sound.</p>
        </div>
      </motion.div>

      <motion.div
        style={{ opacity: text1 }}
        className="pointer-events-none fixed inset-y-0 left-20 flex items-center"
      >
        <p className="text-4xl font-bold tracking-tight text-white/90">
          Precision Engineering.
        </p>
      </motion.div>

      <motion.div
        style={{ opacity: text2 }}
        className="pointer-events-none fixed inset-y-0 right-20 flex items-center"
      >
        <p className="text-4xl font-bold tracking-tight text-white/90">
          Titanium Drivers.
        </p>
      </motion.div>

      <motion.div
        style={{ opacity: cta }}
        className="pointer-events-none fixed inset-0 flex items-center justify-center"
      >
        <div className="text-center">
          <h2 className="text-6xl font-bold tracking-tight text-white/90">
            Hear Everything.
          </h2>
          <button className="pointer-events-auto mt-8 rounded-full bg-white px-8 py-3 text-lg font-semibold text-black transition hover:bg-white/90">
            Pre-Order Now
          </button>
        </div>
      </motion.div>
    </div>
  )
}
```

---

## Ключевые детали реализации

**Строки 15-18**: `useScroll` отслеживает scroll progress от начала до конца контейнера
**Строка 21**: `useTransform` мапит scroll 0-1 на frame index 0-119
**Строки 32-46**: preload всех 120 кадров через Promise.all
**Строки 49-70**: отрисовка текущего кадра в canvas с масштабированием и центровкой
**Строки 73-76**: opacity transforms для fade in/out текста в заданных scroll positions

---

## Использование

1. Установите зависимости: `npm install framer-motion`
2. Поместите 120 WebP-кадров в `/public/frames/`
3. Скопируйте код в соответствующие файлы
4. Запустите: `npm run dev`

---

## Кастомизация

**Изменить frame count**: обновите константу `FRAME_COUNT` (строка 7)
**Настроить scroll length**: замените `h-[400vh]` на `h-[300vh]` или `h-[500vh]` (строка 120)
**Изменить text timing**: обновите диапазоны transform в строках 73-76
**Изменить цвета**: обновите `bg-[#050505]`, чтобы совпадал с фоном изображения

---

## Связано

- concepts/scroll-linked-animations.md - понять технику
- guides/scrollytelling-setup.md - быстрый старт
- lookup/scroll-animation-prompts.md - генерация последовательностей изображений

---

## Ссылки

- [Framer Motion Docs](https://www.framer.com/motion/)
- [Next.js App Router](https://nextjs.org/docs/app)
