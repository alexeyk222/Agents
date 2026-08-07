<!-- Context: ui/scroll-linked-animations | Priority: critical | Version: 1.0 | Updated: 2026-02-15 -->

# Concept: Scroll-linked-анимации

**Purpose**: Синхронизация последовательностей изображений с позицией scroll для кинематографичного показа продукта

**Last Updated**: 2026-01-07

---

## Основная идея

Свяжите позицию scroll с кадрами видео. Пока пользователь скроллит, последовательность изображений проигрывается как scrubbing timeline. Это создает иллюзию 3D-анимации, управляемой scroll.

**Формула**: `scrollProgress (0→1) → frameIndex (0→N) → canvas.drawImage()`

---

## Ключевые части

1. **Image sequence** - 60-150 WebP-кадров из видео/3D render
2. **Sticky canvas** - фиксированный HTML5 canvas, всегда видим при scroll
3. **Scroll tracker** - hook Framer Motion `useScroll`
4. **Preloader** - предварительно загружает все кадры (убирает flicker)
5. **Background match** - фон страницы = фон изображения (скрывает края)

---

## Минимальный пример

```tsx
const { scrollYProgress } = useScroll({ target: containerRef })
const frameIndex = useTransform(scrollYProgress, [0, 1], [0, 119])

useEffect(() => {
  ctx.drawImage(images[Math.round(frameIndex)], 0, 0)
}, [frameIndex])
```

**Почему canvas?** В 10 раз быстрее, чем менять `<img src>`. DOM updates медленные.

---

## Связано

- examples/scrollytelling-headphone.md - полный код
- guides/building-scrollytelling-pages.md - реализация
- lookup/scroll-animation-prompts.md - генерация последовательностей изображений

---

## Ссылка

[Apple AirPods Pro](https://www.apple.com/airpods-pro/) - production-пример
