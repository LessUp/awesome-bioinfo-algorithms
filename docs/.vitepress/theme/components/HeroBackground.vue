<template>
  <div class="hero-bg" :class="{ 'dark': isDark }">
    <slot />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const isDark = ref(false)

onMounted(() => {
  // Detect dark mode from VitePress
  const html = document.documentElement
  isDark.value = html.classList.contains('dark')

  // Watch for theme changes
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.attributeName === 'class') {
        isDark.value = html.classList.contains('dark')
      }
    })
  })

  observer.observe(html, { attributes: true })
})
</script>

<style scoped>
.hero-bg {
  position: relative;
  overflow: hidden;
}

.hero-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
  background:
    radial-gradient(circle at 25% 25%, oklch(0.55 0.18 264 / 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, oklch(0.65 0.15 195 / 0.1) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, oklch(0.50 0.12 180 / 0.08) 0%, transparent 60%);
  background-size: 200% 200%;
  animation: heroBgDrift 20s ease-in-out infinite;
  pointer-events: none;
}

.hero-bg.dark::before {
  background:
    radial-gradient(circle at 25% 25%, oklch(0.75 0.14 195 / 0.15) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, oklch(0.70 0.12 264 / 0.12) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, oklch(0.65 0.10 180 / 0.10) 0%, transparent 60%);
  background-size: 200% 200%;
  animation: heroBgDrift 20s ease-in-out infinite;
}

@keyframes heroBgDrift {
  0%, 100% {
    background-position: 0% 0%, 100% 100%, 50% 50%;
  }
  50% {
    background-position: 100% 100%, 0% 0%, 50% 50%;
  }
}

.hero-bg > :deep(*) {
  position: relative;
  z-index: 1;
}
</style>
