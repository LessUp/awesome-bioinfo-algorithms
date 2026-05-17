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

  locales: {
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'Awesome Bioinformatics Algorithms',
      description: '生物信息学算法知识库',
      themeConfig: {
        nav: [
          { text: '导读', link: '/zh/guides/project-overview', activeMatch: '/zh/guides/' },
          { text: '学院', link: '/zh/academy/learning-path', activeMatch: '/zh/academy/' },
          { text: '架构', link: '/zh/architecture/system-architecture', activeMatch: '/zh/architecture/' },
          { text: '研究', link: '/zh/research/references', activeMatch: '/zh/research/' },
          { text: '算法图谱', link: '/zh/algorithms/', activeMatch: '/zh/algorithms/' },
          { text: '参考', link: '/zh/reference/cli-workflow', activeMatch: '/zh/reference/' },
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
              text: '学院',
              items: [
                { text: '学习路径', link: '/zh/academy/learning-path' },
              ],
            },
          ],
          '/zh/architecture/': [
            {
              text: '架构',
              items: [
                { text: '系统架构', link: '/zh/architecture/system-architecture' },
                { text: '数据与生成链路', link: '/zh/architecture/data-pipeline' },
                { text: '质量保障', link: '/zh/architecture/quality-assurance' },
              ],
            },
          ],
          '/zh/research/': [
            {
              text: '研究',
              items: [
                { text: '参考文献与相关项目', link: '/zh/research/references' },
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
              text: '分类',
              items: [
                { text: '全部分类', link: '/zh/categories/' },
              ],
            },
          ],
          '/zh/reference/': [
            {
              text: '参考',
              items: [
                { text: 'CLI 工作流参考', link: '/zh/reference/cli-workflow' },
                { text: '标签索引', link: '/zh/tags' },
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
          { text: 'Overview', link: '/en/guides/project-overview', activeMatch: '/en/guides/' },
          { text: 'Academy', link: '/en/academy/learning-path', activeMatch: '/en/academy/' },
          { text: 'Architecture', link: '/en/architecture/system-architecture', activeMatch: '/en/architecture/' },
          { text: 'Research', link: '/en/research/references', activeMatch: '/en/research/' },
          { text: 'Algorithm Atlas', link: '/en/algorithms/', activeMatch: '/en/algorithms/' },
          { text: 'Reference', link: '/en/reference/cli-workflow', activeMatch: '/en/reference/' },
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
              text: 'Academy',
              items: [
                { text: 'Learning Path', link: '/en/academy/learning-path' },
              ],
            },
          ],
          '/en/architecture/': [
            {
              text: 'Architecture',
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
                { text: 'References and Related Projects', link: '/en/research/references' },
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
              text: 'Reference',
              items: [
                { text: 'CLI Workflow Reference', link: '/en/reference/cli-workflow' },
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
  },

  vite: {
    plugins: [llmstxt()],
  },
}))
