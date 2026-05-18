<template>
  <div class="algo-table-wrapper">
    <table class="algo-table">
      <thead>
        <tr>
          <th v-for="col in columns" :key="col.key" :style="col.width ? `width:${col.width}` : ''">
            {{ col.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id || row.name">
          <td v-for="col in columns" :key="col.key">
            <template v-if="col.key === 'complexity'">
              <ComplexityBadge v-if="row[col.key]" :value="row[col.key]" />
              <span v-else class="na">—</span>
            </template>
            <template v-else-if="col.key === 'name'">
              <a v-if="row.link" :href="row.link" class="algo-link">{{ row[col.key] }}</a>
              <span v-else>{{ row[col.key] }}</span>
            </template>
            <template v-else>{{ row[col.key] || '—' }}</template>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import ComplexityBadge from './ComplexityBadge.vue'

defineProps({
  columns: {
    type: Array,
    default: () => [
      { key: 'name', label: 'Algorithm' },
      { key: 'year', label: 'Year', width: '4rem' },
      { key: 'complexity', label: 'Time Complexity' },
      { key: 'purpose', label: 'Purpose' },
    ],
  },
  rows: {
    type: Array,
    default: () => [],
  },
})
</script>

<style scoped>
.algo-table-wrapper {
  overflow-x: auto;
  margin: 1.5rem 0;
  border-radius: var(--aba-radius-md, 0.75rem);
  border: 1px solid var(--vp-c-border);
  box-shadow: var(--aba-shadow-sm, 0 1px 3px rgba(0,0,0,0.06));
}

.algo-table {
  width: 100%;
  border-collapse: collapse;
}

.algo-table th {
  background: var(--vp-c-bg-soft);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-2);
  padding: 0.65rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--vp-c-border);
  white-space: nowrap;
}

.algo-table td {
  padding: 0.65rem 1rem;
  border-bottom: 1px solid var(--vp-c-divider);
  font-size: 0.88rem;
  color: var(--vp-c-text-2);
  line-height: 1.5;
}

.algo-table tr:last-child td { border-bottom: none; }

.algo-table tr:hover td { background: var(--vp-c-bg-soft); }

.algo-link {
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 550;
}

.algo-link:hover { text-decoration: underline; }

.na { color: var(--vp-c-text-3); }
</style>
