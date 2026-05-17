<template>
  <div class="algo-card">
    <div class="algo-header">
      <span class="algo-name">{{ name }}</span>
      <span class="algo-year" v-if="year">{{ year }}</span>
    </div>
    <div class="algo-meta">
      <ComplexityBadge v-if="timeComplexity" :value="timeComplexity" />
      <ComplexityBadge v-if="spaceComplexity" :value="spaceComplexity" label="S" />
      <span class="algo-difficulty" :class="difficulty">{{ difficultyLabel || difficulty }}</span>
    </div>
    <div class="algo-body" v-if="$slots.default">
      <slot />
    </div>
  </div>
</template>

<script setup>
import ComplexityBadge from './ComplexityBadge.vue'

defineProps({
  name: { type: String, required: true },
  year: { type: [String, Number], default: null },
  timeComplexity: { type: String, default: null },
  spaceComplexity: { type: String, default: null },
  difficulty: { type: String, default: null },
  difficultyLabel: { type: String, default: null },
})
</script>

<style scoped>
.algo-card {
  border: 1px solid var(--vp-c-border);
  border-radius: 1rem;
  background: var(--vp-c-bg);
  padding: 1.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: var(--aba-shadow-sm);
}

.algo-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: var(--aba-shadow-glow), var(--aba-shadow-md);
  transform: translateY(-2px);
}

.algo-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 0.75rem;
  gap: 0.5rem;
}

.algo-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.algo-year {
  font-size: 0.8rem;
  font-family: var(--vp-font-family-mono);
  color: var(--vp-c-text-3);
  background: var(--vp-c-bg-soft);
  padding: 0.15rem 0.5rem;
  border-radius: 0.25rem;
  flex-shrink: 0;
}

.algo-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.algo-difficulty {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.15rem 0.5rem;
  border-radius: 0.25rem;
}

.algo-difficulty.beginner {
  background: oklch(0.85 0.08 145);
  color: oklch(0.30 0.06 145);
}

.dark .algo-difficulty.beginner {
  background: oklch(0.30 0.06 145);
  color: oklch(0.85 0.08 145);
}

.algo-difficulty.intermediate {
  background: oklch(0.85 0.08 85);
  color: oklch(0.30 0.06 85);
}

.dark .algo-difficulty.intermediate {
  background: oklch(0.30 0.06 85);
  color: oklch(0.85 0.08 85);
}

.algo-difficulty.advanced {
  background: oklch(0.80 0.10 25);
  color: oklch(0.30 0.06 25);
}

.dark .algo-difficulty.advanced {
  background: oklch(0.30 0.06 25);
  color: oklch(0.80 0.10 25);
}

.algo-body {
  margin-top: 0.75rem;
  font-size: 0.95rem;
  color: var(--vp-c-text-2);
  line-height: 1.6;
}
</style>
