<template>
  <span class="theme-aware-svg" :style="{ color: color }">
    <slot />
  </span>
</template>

<script setup>
defineProps({
  color: {
    type: String,
    default: 'var(--vp-c-text-1)',
  },
})
</script>

<style scoped>
.theme-aware-svg {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--vp-c-text-1);
}

.theme-aware-svg :deep(svg) {
  color: inherit;
}

.theme-aware-svg :deep(svg path),
.theme-aware-svg :deep(svg rect),
.theme-aware-svg :deep(svg circle),
.theme-aware-svg :deep(svg line),
.theme-aware-svg :deep(svg polyline),
.theme-aware-svg :deep(svg polygon),
.theme-aware-svg :deep(svg ellipse) {
  fill: currentColor;
  stroke: currentColor;
}

.theme-aware-svg :deep(svg [stroke="none"]),
.theme-aware-svg :deep(svg [fill="none"]) {
  fill: none;
  stroke: none;
}
</style>
