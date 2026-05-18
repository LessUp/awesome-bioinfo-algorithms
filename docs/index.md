---
layout: home
title: Awesome Bioinformatics Algorithms
hero:
  name: Awesome Bioinformatics
  text: Algorithm Whitepaper
  tagline: A curated, structured knowledge base of bioinformatics algorithms — 195+ entries · 16 categories · 392 tags
  image:
    src: /favicon.svg
    alt: Awesome Bioinformatics Algorithms
  actions:
    - theme: brand
      text: 简体中文 →
      link: /zh/
    - theme: alt
      text: English →
      link: /en/

features:
  - icon: 🧬
    title: 195+ Algorithms
    details: Curated entries spanning sequence alignment, assembly, variant calling, protein structure prediction, single-cell analysis, and more — all with complexity annotations and literature references.
  - icon: 📐
    title: Data-Driven Generation
    details: Every page is generated from structured YAML sources. Single source of truth ensures zero documentation drift — add one YAML entry, get one fully-formatted page.
  - icon: 🔬
    title: Academic Citation Standard
    details: GB-T 7714 (Chinese) / IEEE (English) reference formats. Every complexity claim is traceable to peer-reviewed literature, with DOI links and official implementation URLs.
  - icon: 🏗
    title: Verifiable Engineering
    details: Three-layer validation (field rules + JSON Schema + build-time checks) with 89% test coverage. GitHub Actions CI/CD ensures every commit is validated before deployment.
  - icon: 🌐
    title: Bilingual Architecture
    details: Strict Chinese–English parity. Algorithm descriptions, category names, and documentation are provided in both languages with automatic fallback.
  - icon: 📊
    title: Complexity Atlas
    details: Time and space complexity annotated for every algorithm, enabling rapid performance evaluation and algorithm selection for real-world genomics workloads.
---

<script setup>
import { onMounted } from 'vue'
onMounted(() => {
  // Auto-redirect to preferred language after a short delay
  const lang = navigator.language || navigator.userLanguage || 'zh'
  const preferZh = lang.startsWith('zh')
  const base = import.meta.env.BASE_URL
  // Only redirect if user lands exactly on root
  if (window.location.pathname === base || window.location.pathname === base.slice(0, -1) + '/') {
    setTimeout(() => {
      window.location.replace(base + (preferZh ? 'zh/' : 'en/'))
    }, 2000)
  }
})
</script>
