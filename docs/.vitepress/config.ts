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
  description: 'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',

  // Clean URLs
  cleanUrls: true,
  
  // Last updated timestamp
  lastUpdated: true,

  locales: {
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'Awesome Bioinformatics Algorithms',
      description: '生物信息学算法技术白皮书与架构学院',
      themeConfig: {
        nav: [
          { text: '导读', link: '/zh/guides/project-overview', activeMatch: '/zh/guides/' },
          { text: '学院', link: '/zh/academy/', activeMatch: '/zh/academy/' },
          { text: '架构', link: '/zh/architecture/system-architecture', activeMatch: '/zh/architecture/' },
          { text: '研究', link: '/zh/research/references', activeMatch: '/zh/research/' },
          { text: '算法图谱', link: '/zh/algorithms/', activeMatch: '/zh/algorithms/' },
          { text: '参考', link: '/zh/reference/', activeMatch: '/zh/reference/' },
        ],
        sidebar: {
          '/zh/guides/': [
            {
              text: '导读',
              items: [
                { text: '项目导读', link: '/zh/guides/project-overview' },
              ],
            },
          ],
          '/zh/academy/': [
            {
              text: '算法法学院',
              items: [
                { text: '学院首页', link: '/zh/academy/' },
                { text: '学习路径', link: '/zh/academy/learning-path' },
              ],
            },
          ],
          '/zh/architecture/': [
            {
              text: '系统架构',
              items: [
                { text: '系统架构', link: '/zh/architecture/system-architecture' },
                { text: '数据与生成链路', link: '/zh/architecture/data-pipeline' },
                { text: '质量保障', link: '/zh/architecture/quality-assurance' },
              ],
            },
          ],
          '/zh/research/': [
            {
              text: '学术研究',
              items: [
                { text: '参考文献', link: '/zh/research/references' },
                { text: '相关项目', link: '/zh/research/related-projects' },
                { text: '演进思考', link: '/zh/research/evolution' },
              ],
            },
          ],
          '/zh/algorithms/': [
            {
              text: '算法图谱',
              items: [
                { text: '算法总览', link: '/zh/algorithms/' },
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
          '/zh/reference/': [
            {
              text: '参考手册',
              items: [
                { text: '参考手册首页', link: '/zh/reference/' },
                { text: 'CLI 工作流参考', link: '/zh/reference/cli-workflow' },
                { text: '贡献指南', link: '/zh/reference/contribution' },
                { text: '标签索引', link: '/zh/tags' },
              ],
            },
          ],
        },
        docFooter: {
          prev: '上一页',
          next: '下一页',
        },
        outline: {
          label: '页面导航',
        },
        lastUpdated: {
          text: '最后更新于',
          formatOptions: {
            dateStyle: 'short',
            timeStyle: 'short',
          },
        },
      },
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      title: 'Awesome Bioinformatics Algorithms',
      description: 'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',
      themeConfig: {
        nav: [
          { text: 'Overview', link: '/en/guides/project-overview', activeMatch: '/en/guides/' },
          { text: 'Academy', link: '/en/academy/', activeMatch: '/en/academy/' },
          { text: 'Architecture', link: '/en/architecture/system-architecture', activeMatch: '/en/architecture/' },
          { text: 'Research', link: '/en/research/references', activeMatch: '/en/research/' },
          { text: 'Algorithm Atlas', link: '/en/algorithms/', activeMatch: '/en/algorithms/' },
          { text: 'Reference', link: '/en/reference/', activeMatch: '/en/reference/' },
        ],
        sidebar: {
          '/en/guides/': [
            {
              text: 'Overview',
              items: [
                { text: 'Project Overview', link: '/en/guides/project-overview' },
              ],
            },
          ],
          '/en/academy/': [
            {
              text: 'Algorithm Academy',
              items: [
                { text: 'Academy Home', link: '/en/academy/' },
                { text: 'Learning Path', link: '/en/academy/learning-path' },
              ],
            },
          ],
          '/en/architecture/': [
            {
              text: 'System Architecture',
              items: [
                { text: 'System Architecture', link: '/en/architecture/system-architecture' },
                { text: 'Data and Generation Pipeline', link: '/en/architecture/data-pipeline' },
                { text: 'Quality Assurance', link: '/en/architecture/quality-assurance' },
              ],
            },
          ],
          '/en/research/': [
            {
              text: 'Research',
              items: [
                { text: 'References', link: '/en/research/references' },
                { text: 'Related Projects', link: '/en/research/related-projects' },
                { text: 'Evolution Notes', link: '/en/research/evolution' },
              ],
            },
          ],
          '/en/algorithms/': [
            {
              text: 'Algorithm Atlas',
              items: [
                { text: 'All Algorithms', link: '/en/algorithms/' },
              ],
            },
          ],
          '/en/categories/': [
            {
              text: 'Categories',
              items: [
                { text: 'All Categories', link: '/en/categories/' },
              ],
            },
          ],
          '/en/reference/': [
            {
              text: 'Reference Manual',
              items: [
                { text: 'Reference Home', link: '/en/reference/' },
                { text: 'CLI Workflow Reference', link: '/en/reference/cli-workflow' },
                { text: 'Contributing Guide', link: '/en/reference/contribution' },
                { text: 'Tags Index', link: '/en/tags' },
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
    editLink: {
      pattern: 'https://github.com/LessUp/awesome-bioinfo-algorithms/edit/master/docs/:path',
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lessup/awesome-bioinfo-algorithms' },
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024-present Awesome Bioinfo Contributors',
    },
  },

  head: [
    ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#10b981' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:title', content: 'Awesome Bioinformatics Algorithms' }],
    ['meta', { name: 'og:site_name', content: 'Awesome Bioinfo Algorithms' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
  ],

  vite: {
    plugins: [llmstxt()],
  },
}))
