---
layout: home
hero:
  name: Awesome Bioinformatics Algorithms
  text: ' '
  tagline: 生物信息学算法知识库
  actions:
    - theme: brand
      text: 简体中文
      link: /zh/
    - theme: alt
      text: English
      link: /en/
features:
  - icon: 🧬
    title: 195+ 算法
    details: 涵盖序列比对、基因组组装、变异检测等核心领域
  - icon: 📊
    title: 16 个分类
    details: 系统化分类体系，快速定位所需算法
  - icon: 🔍
    title: 智能搜索
    details: 本地全文搜索，即时查找算法详情
---

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vitepress'

onMounted(() => {
  const router = useRouter()
  const lang = navigator.language || navigator.userLanguage
  if (lang.startsWith('zh')) {
    router.go('/zh/')
  } else {
    router.go('/en/')
  }
})
</script>
