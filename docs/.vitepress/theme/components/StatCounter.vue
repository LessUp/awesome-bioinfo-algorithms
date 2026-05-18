<template>
  <div class="stat-counter" :class="{ 'is-visible': visible }">
    <div class="stat-number">{{ displayValue }}{{ suffix }}</div>
    <div class="stat-label">{{ label }}</div>
    <div v-if="sublabel" class="stat-sub">{{ sublabel }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const props = defineProps({
  target: { type: Number, required: true },
  suffix: { type: String, default: '' },
  label: { type: String, required: true },
  sublabel: { type: String, default: '' },
  duration: { type: Number, default: 1200 },
})

const displayValue = ref(0)
const visible = ref(false)

function easeOutQuart(t) {
  return 1 - Math.pow(1 - t, 4)
}

function animate() {
  const start = performance.now()
  const end = props.target

  function step(now) {
    const elapsed = now - start
    const progress = Math.min(elapsed / props.duration, 1)
    displayValue.value = Math.round(easeOutQuart(progress) * end)
    if (progress < 1) requestAnimationFrame(step)
    else displayValue.value = end
  }
  requestAnimationFrame(step)
}

onMounted(() => {
  // Use IntersectionObserver to trigger animation on scroll-into-view
  const el = document.querySelector('.stat-counter')
  const observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        visible.value = true
        animate()
        observer.disconnect()
      }
    },
    { threshold: 0.2 },
  )
  // Observe parent element (the closest DOM node we can reference)
  // Fall back to immediate animation if not available
  try {
    observer.observe(el)
  } catch {
    animate()
  }
})
</script>

<style scoped>
.stat-counter {
  text-align: center;
  padding: 1.25rem 1rem;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: var(--aba-radius-lg, 1rem);
  transition: border-color 0.2s, box-shadow 0.2s, opacity 0.4s, transform 0.4s;
  opacity: 0;
  transform: translateY(8px);
}

.stat-counter.is-visible {
  opacity: 1;
  transform: translateY(0);
}

.stat-counter:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: var(--aba-shadow-glow, 0 0 24px oklch(0.51 0.19 265 / 0.18));
}

.stat-number {
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 1;
  background: var(--vp-home-hero-name-background);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  margin-bottom: 0.4rem;
}

.stat-label {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin-bottom: 0.2rem;
}

.stat-sub {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  font-family: var(--vp-font-family-mono);
}
</style>
