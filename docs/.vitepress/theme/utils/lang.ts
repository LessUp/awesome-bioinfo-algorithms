<script setup lang="ts">
import { useRouter } from 'vitepress'

const LANG_KEY = 'preferred-language'

/**
 * 切换语言并存储偏好
 * @param lang 'zh' | 'en'
 */
export function switchLanguage(lang: 'zh' | 'en') {
  const router = useRouter()

  // 存储语言偏好
  localStorage.setItem(LANG_KEY, lang)

  // 跳转到对应语言版本
  router.go(lang === 'zh' ? '/zh/' : '/en/')
}

/**
 * 获取当前语言偏好
 */
export function getStoredLanguage(): 'zh' | 'en' | null {
  if (typeof localStorage === 'undefined') return null
  const stored = localStorage.getItem(LANG_KEY)
  if (stored === 'zh' || stored === 'en') return stored
  return null
}

/**
 * 根据浏览器语言检测并返回建议语言
 */
export function detectBrowserLanguage(): 'zh' | 'en' {
  if (typeof navigator === 'undefined') return 'en'
  const browserLang = navigator.language || navigator.userLanguage || 'en'
  return browserLang.toLowerCase().startsWith('zh') ? 'zh' : 'en'
}
</script>
