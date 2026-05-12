import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import llmstxt from 'vitepress-plugin-llms'

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith('/')
    ? rawBase.endsWith('/') ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : '/'

export default withMermaid(defineConfig({
  base,
  title: 'Awesome Bioinformatics Algorithms',
  description: '生物信息学算法知识库',

  locales: {
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'Awesome Bioinformatics Algorithms',
      description: '生物信息学算法知识库',
      themeConfig: {
        nav: [
          { text: '算法', link: '/zh/algorithms/', activeMatch: '/zh/algorithms/' },
          { text: '分类', link: '/zh/categories/', activeMatch: '/zh/categories/' },
          { text: '标签', link: '/zh/tags' },
        ],
        sidebar: {
          '/zh/algorithms/': [
            {
              text: '算法列表',
              items: [
                { text: '概览', link: '/zh/algorithms/' },
              ],
            },
          ],
          '/zh/categories/': [
            {
              text: '分类导航',
              items: [
                { text: '全部分类', link: '/zh/categories/' },
              ],
            },
          ],
        },
      },
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      title: 'Awesome Bioinformatics Algorithms',
      description: 'Bioinformatics Algorithm Knowledge Base',
      themeConfig: {
        nav: [
          { text: 'Algorithms', link: '/en/algorithms/', activeMatch: '/en/algorithms/' },
          { text: 'Categories', link: '/en/categories/', activeMatch: '/en/categories/' },
          { text: 'Tags', link: '/en/tags' },
        ],
        sidebar: {
          '/en/algorithms/': [
            {
              text: 'Algorithm List',
              items: [
                { text: 'Overview', link: '/en/algorithms/' },
              ],
            },
          ],
          '/en/categories/': [
            {
              text: 'Category Navigation',
              items: [
                { text: 'All Categories', link: '/en/categories/' },
              ],
            },
          ],
        },
      },
    },
  },

  themeConfig: {
    outline: [2, 3],
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lessup/awesome-bioinfo-algorithms' },
    ],
  },

  vite: {
    plugins: [llmstxt()],
  },
}))
