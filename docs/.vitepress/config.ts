import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import llmstxt from 'vitepress-plugin-llms'

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith('/')
    ? rawBase.endsWith('/') ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : '/'

// Light mode theme color (indigo)
const THEME_COLOR_LIGHT = '#4f46e5'
// Dark mode theme color (cyan)
const THEME_COLOR_DARK = '#22d3ee'

// Mermaid theme variables mapped to CSS variable values (concrete OKLCH)
const MERMAID_THEME_VARIABLES = {
  primaryColor: 'oklch(0.96 0.004 264)',
  primaryTextColor: 'oklch(0.20 0.02 264)',
  primaryBorderColor: 'oklch(0.88 0.012 264)',
  lineColor: 'oklch(0.58 0.015 264)',
  secondaryColor: 'oklch(0.94 0.006 264)',
  tertiaryColor: 'oklch(0.97 0.005 264)',
  fontFamily: "'Inter', 'JetBrains Mono', system-ui, sans-serif",
  fontSize: '14px',
}

const MERMAID_THEME_CSS = `
  .node rect, .node circle, .node ellipse, .node polygon, .node path {
    fill: var(--vp-c-bg-soft, oklch(0.96 0.004 264)) !important;
    stroke: var(--vp-c-text-2, oklch(0.40 0.02 264)) !important;
  }
  .node .label, .nodeLabel, .edgeLabel {
    color: var(--vp-c-text-1, oklch(0.20 0.02 264)) !important;
    fill: var(--vp-c-text-1, oklch(0.20 0.02 264)) !important;
  }
  .cluster rect {
    fill: var(--vp-c-bg-alt, oklch(0.94 0.006 264)) !important;
    stroke: var(--vp-c-border, oklch(0.88 0.012 264)) !important;
  }
  .edgePath .path {
    stroke: var(--vp-c-text-3, oklch(0.58 0.015 264)) !important;
  }
  .arrowheadPath {
    fill: var(--vp-c-text-3, oklch(0.58 0.015 264)) !important;
  }
  .edgeLabel rect {
    fill: var(--vp-c-bg-soft, oklch(0.96 0.004 264)) !important;
  }
  .label text {
    fill: var(--vp-c-text-1, oklch(0.20 0.02 264)) !important;
  }
  .titleText {
    fill: var(--vp-c-text-1, oklch(0.20 0.02 264)) !important;
  }
  .pieTitleText {
    fill: var(--vp-c-text-1, oklch(0.20 0.02 264)) !important;
  }
  .slice {
    stroke: var(--vp-c-border, oklch(0.88 0.012 264)) !important;
  }
  .legend text {
    fill: var(--vp-c-text-2, oklch(0.40 0.02 264)) !important;
  }
`

// JSON-LD structured data
const JSON_LD_WEBSITE = {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  name: 'Awesome Bioinformatics Algorithms',
  description: 'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',
  url: 'https://lessup.github.io/awesome-bioinfo-algorithms',
  potentialAction: {
    '@type': 'SearchAction',
    target: 'https://lessup.github.io/awesome-bioinfo-algorithms/?s={search_term_string}',
    'query-input': 'required name=search_term_string',
  },
}

export default withMermaid(defineConfig({
  base,
  title: 'Awesome Bioinformatics Algorithms',
  description: 'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',

  // Clean URLs
  cleanUrls: true,

  // Last updated timestamp
  lastUpdated: true,

  // Mermaid configuration with CSS-variable-bound theme
  mermaid: {
    theme: 'base',
    themeVariables: MERMAID_THEME_VARIABLES,
    themeCSS: MERMAID_THEME_CSS,
    startOnLoad: false,
    securityLevel: 'loose',
  },

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
    // Favicon
    ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],

    // Theme color (adapts to light/dark via media query)
    ['meta', { name: 'theme-color', content: THEME_COLOR_LIGHT, media: '(prefers-color-scheme: light)' }],
    ['meta', { name: 'theme-color', content: THEME_COLOR_DARK, media: '(prefers-color-scheme: dark)' }],

    // Open Graph / Twitter
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:title', content: 'Awesome Bioinformatics Algorithms' }],
    ['meta', { name: 'og:site_name', content: 'Awesome Bioinfo Algorithms' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],

    // Google Fonts preconnect
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap' }],

    // JSON-LD structured data
    ['script', { type: 'application/ld+json' }, JSON.stringify(JSON_LD_WEBSITE)],
  ],

  vite: {
    plugins: [llmstxt()],
  },
}))
