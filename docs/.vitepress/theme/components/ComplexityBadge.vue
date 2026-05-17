<template>
  <span class="complexity-badge" :class="colorClass">
    <span v-if="label" class="complexity-label">{{ label }}:</span>
    <span class="complexity-value">{{ value }}</span>
  </span>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  value: { type: String, required: true },
  label: { type: String, default: 'T' },
})

const colorClass = computed(() => {
  const v = props.value.toLowerCase().trim()
  // Green: O(1), O(log n), O(√n)
  if (v.includes('o(1)') || v.includes('o(log') || v.includes('o(sqrt') || v.includes('o(√')) {
    return 'green'
  }
  // Yellow: O(n), O(n log n) — wait, spec says O(n) yellow, O(n log n)/O(n²) orange/red
  if (v.includes('o(n)') && !v.includes('log') && !v.includes('²') && !v.includes('^2') && !v.includes('n^2')) {
    return 'yellow'
  }
  // Orange: O(n log n), O(n^1.something)
  if (v.includes('o(n log') || v.includes('o(nlog') || (v.includes('o(n') && v.includes('^') && !v.includes('^2'))) {
    return 'orange'
  }
  // Red: O(n²), O(n^3), exponential, factorial
  if (v.includes('²') || v.includes('^2') || v.includes('n^2') || v.includes('o(2^') || v.includes('o(n!)') || v.includes('exp')) {
    return 'red'
  }
  // Default to yellow for O(n) variants
  if (v.includes('o(n')) {
    return 'yellow'
  }
  return 'yellow'
})
</script>

<style scoped>
.complexity-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-family: var(--vp-font-family-mono);
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.2rem 0.5rem;
  border-radius: 0.375rem;
  border: 1px solid var(--vp-c-border);
}

.complexity-label {
  opacity: 0.7;
  font-weight: 400;
}

.complexity-badge.green {
  background: oklch(0.90 0.05 145);
  color: oklch(0.25 0.06 145);
  border-color: oklch(0.75 0.08 145);
}

.dark .complexity-badge.green {
  background: oklch(0.25 0.05 145);
  color: oklch(0.85 0.06 145);
  border-color: oklch(0.40 0.06 145);
}

.complexity-badge.yellow {
  background: oklch(0.94 0.06 95);
  color: oklch(0.30 0.06 85);
  border-color: oklch(0.80 0.08 85);
}

.dark .complexity-badge.yellow {
  background: oklch(0.28 0.04 85);
  color: oklch(0.90 0.06 85);
  border-color: oklch(0.45 0.05 85);
}

.complexity-badge.orange {
  background: oklch(0.92 0.06 65);
  color: oklch(0.30 0.08 50);
  border-color: oklch(0.75 0.10 55);
}

.dark .complexity-badge.orange {
  background: oklch(0.28 0.04 55);
  color: oklch(0.88 0.08 55);
  border-color: oklch(0.45 0.06 55);
}

.complexity-badge.red {
  background: oklch(0.88 0.08 25);
  color: oklch(0.30 0.10 25);
  border-color: oklch(0.70 0.12 25);
}

.dark .complexity-badge.red {
  background: oklch(0.25 0.05 25);
  color: oklch(0.85 0.08 25);
  border-color: oklch(0.42 0.08 25);
}
</style>
