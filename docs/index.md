---
layout: home
hero:
  name: Awesome Bioinformatics Algorithms
  text: Technical Whitepaper Hub
  tagline: 生物信息学算法技术白皮书与架构学院
  actions:
    - theme: brand
      text: 简体中文
      link: /zh/
    - theme: alt
      text: English
      link: /en/
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
