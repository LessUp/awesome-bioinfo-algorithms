import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import llmstxt from 'vitepress-plugin-llms'

const rawBase = process.env.VITEPRESS_BASE
const base = rawBase
  ? rawBase.startsWith('/')
    ? rawBase.endsWith('/') ? rawBase : `${rawBase}/`
    : `/${rawBase}/`
  : '/'

// JSON-LD structured data
const JSON_LD_WEBSITE = {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  name: 'Awesome Bioinformatics Algorithms',
  description:
    'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',
  url: 'https://lessup.github.io/awesome-bioinfo-algorithms',
  potentialAction: {
    '@type': 'SearchAction',
    target:
      'https://lessup.github.io/awesome-bioinfo-algorithms/?s={search_term_string}',
    'query-input': 'required name=search_term_string',
  },
}

export default withMermaid(
  defineConfig({
    base,
    title: 'Awesome Bioinformatics Algorithms',
    description:
      'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',

    cleanUrls: true,
    lastUpdated: true,

    // Mermaid: use 'neutral' base theme — all colors come from CSS variables via themeCSS
    // Actual light/dark adaptation is handled client-side by MermaidDark.vue
    mermaid: {
      theme: 'neutral',
      themeVariables: {
        // These are overridden per-render by MermaidDark.vue via CSS custom props
        fontFamily: "'Inter', 'JetBrains Mono', system-ui, sans-serif",
        fontSize: '14px',
      },
      // Inject CSS that reads VitePress CSS custom properties,
      // making every Mermaid diagram honour the active colour scheme
      themeCSS: `
        :root {
          --mermaid-bg: #f8f9fc;
          --mermaid-node-bg: #eef0f8;
          --mermaid-node-border: #c5cae9;
          --mermaid-text: #1a1f3a;
          --mermaid-text-secondary: #3d4466;
          --mermaid-line: #7986cb;
          --mermaid-cluster-bg: #e8eaf6;
          --mermaid-cluster-border: #c5cae9;
          --mermaid-edge-label-bg: #f0f2fc;
        }
        .dark {
          --mermaid-bg: #1a1d2e;
          --mermaid-node-bg: #252840;
          --mermaid-node-border: #4a5080;
          --mermaid-text: #e8eaf6;
          --mermaid-text-secondary: #b0bae8;
          --mermaid-line: #7986cb;
          --mermaid-cluster-bg: #1e2135;
          --mermaid-cluster-border: #383d60;
          --mermaid-edge-label-bg: #252840;
        }

        /* Flowchart nodes */
        .node rect,
        .node circle,
        .node ellipse,
        .node polygon,
        .node path {
          fill: var(--mermaid-node-bg) !important;
          stroke: var(--mermaid-node-border) !important;
        }
        /* Node labels */
        .node .label,
        .nodeLabel,
        .label {
          color: var(--mermaid-text) !important;
          fill: var(--mermaid-text) !important;
        }
        .label text,
        .nodeLabel text,
        text.actor,
        .actor-line + text,
        g.label text {
          fill: var(--mermaid-text) !important;
        }
        /* Cluster / subgraph */
        .cluster rect {
          fill: var(--mermaid-cluster-bg) !important;
          stroke: var(--mermaid-cluster-border) !important;
        }
        .cluster text {
          fill: var(--mermaid-text-secondary) !important;
        }
        /* Edges */
        .edgePath .path,
        .flowchart-link {
          stroke: var(--mermaid-line) !important;
        }
        .arrowheadPath {
          fill: var(--mermaid-line) !important;
          stroke: var(--mermaid-line) !important;
        }
        .edgeLabel rect {
          fill: var(--mermaid-edge-label-bg) !important;
          opacity: 0.9;
        }
        .edgeLabel span,
        .edgeLabel {
          color: var(--mermaid-text-secondary) !important;
          background: transparent !important;
        }
        /* Sequence diagram */
        .actor {
          fill: var(--mermaid-node-bg) !important;
          stroke: var(--mermaid-node-border) !important;
        }
        .actor > rect {
          fill: var(--mermaid-node-bg) !important;
          stroke: var(--mermaid-node-border) !important;
        }
        .messageText {
          fill: var(--mermaid-text) !important;
          stroke: none !important;
        }
        .messageLine0,
        .messageLine1 {
          stroke: var(--mermaid-line) !important;
        }
        .loopText,
        .loopLine {
          fill: var(--mermaid-text-secondary) !important;
          stroke: var(--mermaid-node-border) !important;
        }
        /* Title text */
        .titleText,
        .pieTitleText {
          fill: var(--mermaid-text) !important;
        }
        /* Legend */
        .legend text {
          fill: var(--mermaid-text-secondary) !important;
        }
        /* General SVG text override */
        svg text {
          fill: var(--mermaid-text) !important;
        }
        /* Background rect of entire diagram */
        svg > rect:first-child {
          fill: var(--mermaid-bg) !important;
        }
      `,
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
            { text: '白皮书', link: '/zh/guides/project-overview', activeMatch: '/zh/guides/' },
            { text: '算法图谱', link: '/zh/algorithms/', activeMatch: '/zh/algorithms/' },
            { text: '学院', link: '/zh/academy/', activeMatch: '/zh/academy/' },
            {
              text: '研究',
              items: [
                { text: '参考文献', link: '/zh/research/references' },
                { text: '相关项目', link: '/zh/research/related-projects' },
                { text: '演进思考', link: '/zh/research/evolution' },
              ],
            },
            { text: '参考', link: '/zh/reference/', activeMatch: '/zh/reference/' },
          ],
          sidebar: {
            '/zh/guides/': [
              {
                text: '白皮书导读',
                items: [
                  { text: '项目导读', link: '/zh/guides/project-overview' },
                ],
              },
            ],
            '/zh/academy/': [
              {
                text: '算法学院',
                items: [
                  { text: '学院首页', link: '/zh/academy/' },
                  { text: '学习路径', link: '/zh/academy/learning-path' },
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
            level: [2, 3],
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
        description:
          'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms',
        themeConfig: {
          nav: [
            { text: 'Whitepaper', link: '/en/guides/project-overview', activeMatch: '/en/guides/' },
            { text: 'Algorithm Atlas', link: '/en/algorithms/', activeMatch: '/en/algorithms/' },
            { text: 'Academy', link: '/en/academy/', activeMatch: '/en/academy/' },
            {
              text: 'Research',
              items: [
                { text: 'References', link: '/en/research/references' },
                { text: 'Related Projects', link: '/en/research/related-projects' },
                { text: 'Evolution Notes', link: '/en/research/evolution' },
              ],
            },
            { text: 'Reference', link: '/en/reference/', activeMatch: '/en/reference/' },
          ],
          sidebar: {
            '/en/guides/': [
              {
                text: 'Whitepaper',
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
      search: {
        provider: 'local',
        options: {
          detailedView: true,
        },
      },
      editLink: {
        pattern:
          'https://github.com/LessUp/awesome-bioinfo-algorithms/edit/master/docs/:path',
        text: 'Edit this page on GitHub',
      },
      socialLinks: [
        { icon: 'github', link: 'https://github.com/lessup/awesome-bioinfo-algorithms' },
      ],
      footer: {
        message: 'Released under the MIT License.',
        copyright: 'Copyright © 2024–present Awesome Bioinfo Contributors',
      },
    },

    head: [
      // Favicon
      ['link', { rel: 'icon', href: `${base}favicon.svg`, type: 'image/svg+xml' }],

      // Open Graph / Twitter
      ['meta', { name: 'og:type', content: 'website' }],
      ['meta', { name: 'og:title', content: 'Awesome Bioinformatics Algorithms' }],
      ['meta', { name: 'og:site_name', content: 'Awesome Bioinfo Algorithms' }],
      [
        'meta',
        {
          name: 'og:description',
          content:
            'Technical Whitepaper and Architecture Academy for Bioinformatics Algorithms — 195+ algorithms, 16 categories',
        },
      ],
      ['meta', { name: 'twitter:card', content: 'summary_large_image' }],

      // Google Fonts preconnect
      ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
      ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
      [
        'link',
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap',
        },
      ],

      // JSON-LD structured data
      ['script', { type: 'application/ld+json' }, JSON.stringify(JSON_LD_WEBSITE)],
    ],

    vite: {
      plugins: [llmstxt()],
    },
  }),
)
