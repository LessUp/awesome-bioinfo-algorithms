<template>
  <div class="citation-block">
    <div class="citation-label">{{ label }}</div>
    <div class="citation-text">{{ formattedCitation }}</div>
    <div class="citation-actions">
      <button class="citation-copy-btn" @click="handleCopy" :aria-label="copyLabel">
        <svg v-if="!copied" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
        <span>{{ copied ? 'Copied!' : 'Copy' }}</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  format: { type: String, default: 'ieee' },
  authors: { type: String, default: '' },
  title: { type: String, default: '' },
  journal: { type: String, default: '' },
  year: { type: [String, Number], default: '' },
  doi: { type: String, default: '' },
})

const copied = ref(false)

const label = computed(() => {
  const map = {
    gb7714: 'GB/T 7714',
    ieee: 'IEEE',
    apa: 'APA',
  }
  return map[props.format] || props.format.toUpperCase()
})

const copyLabel = computed(() => `Copy ${label.value} citation`)

function formatAuthorsGB7714(authors) {
  if (!authors) return ''
  const parts = authors.split(/,\s*/).filter(Boolean)
  if (parts.length === 0) return ''
  if (parts.length === 1) return parts[0]
  if (parts.length === 2) return `${parts[0]}, ${parts[1]}`
  return `${parts[0]} 等`
}

function formatAuthorsIEEE(authors) {
  if (!authors) return ''
  const parts = authors.split(/,\s*/).filter(Boolean)
  if (parts.length === 0) return ''
  if (parts.length <= 3) return parts.join(', ')
  return `${parts[0]} et al.`
}

function formatAuthorsAPA(authors) {
  if (!authors) return ''
  const parts = authors.split(/,\s*/).filter(Boolean)
  if (parts.length === 0) return ''
  if (parts.length === 1) return parts[0]
  if (parts.length === 2) return `${parts[0]} & ${parts[1]}`
  return `${parts[0]} et al.`
}

const formattedCitation = computed(() => {
  switch (props.format) {
    case 'gb7714':
      return `${formatAuthorsGB7714(props.authors)}. ${props.title}[J]. ${props.journal}, ${props.year}.` + (props.doi ? ` DOI: ${props.doi}` : '')
    case 'ieee':
      return `${formatAuthorsIEEE(props.authors)}, "${props.title}," ${props.journal}, ${props.year}.` + (props.doi ? ` DOI: ${props.doi}` : '')
    case 'apa':
      return `${formatAuthorsAPA(props.authors)} (${props.year}). ${props.title}. ${props.journal}.` + (props.doi ? ` https://doi.org/${props.doi}` : '')
    default:
      return `${props.authors}. "${props.title}." ${props.journal}, ${props.year}.`
  }
})

async function handleCopy() {
  try {
    await navigator.clipboard.writeText(formattedCitation.value)
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  } catch (err) {
    // Fallback for older browsers
    const textarea = document.createElement('textarea')
    textarea.value = formattedCitation.value
    textarea.style.position = 'fixed'
    textarea.style.opacity = '0'
    document.body.appendChild(textarea)
    textarea.select()
    document.execCommand('copy')
    document.body.removeChild(textarea)
    copied.value = true
    setTimeout(() => { copied.value = false }, 2000)
  }
}
</script>

<style scoped>
.citation-block {
  border: 1px solid var(--vp-c-border);
  border-radius: 0.75rem;
  background: var(--vp-c-bg-soft);
  padding: 1rem 1.25rem;
  margin: 1.5rem 0;
}

.citation-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--vp-c-brand-1);
  margin-bottom: 0.5rem;
}

.citation-text {
  font-family: var(--vp-font-family-mono);
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  word-break: break-word;
}

.citation-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 0.75rem;
}

.citation-copy-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--vp-c-brand-1);
  background: transparent;
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 0.375rem;
  padding: 0.35rem 0.75rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.citation-copy-btn:hover {
  background: var(--vp-c-brand-1);
  color: var(--vp-c-bg);
}

.citation-copy-btn:active {
  transform: scale(0.97);
}
</style>
