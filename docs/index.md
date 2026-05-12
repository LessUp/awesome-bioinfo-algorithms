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

const LANG_KEY = 'preferred-language'

onMounted(() => {
  // 获取 VitePress base 路径
  const base = window.__VP_SITE_DATA__?.base || '/'

  // 检查是否有存储的语言偏好
  const storedLang = localStorage.getItem(LANG_KEY)

  if (storedLang) {
    // 用户已有偏好，直接跳转（使用完整页面跳转，更可靠）
    window.location.href = base + (storedLang === 'zh' ? 'zh/' : 'en/')
    return
  }

  // 首次访问：根据浏览器语言自动检测
  const browserLang = navigator.language || navigator.userLanguage || 'en'
  const isZh = browserLang.toLowerCase().startsWith('zh')
  const targetLang = isZh ? 'zh' : 'en'

  // 存储偏好
  localStorage.setItem(LANG_KEY, targetLang)

  // 跳转到对应语言版本（使用完整页面跳转，更可靠）
  window.location.href = base + (isZh ? 'zh/' : 'en/')
})
</script>
