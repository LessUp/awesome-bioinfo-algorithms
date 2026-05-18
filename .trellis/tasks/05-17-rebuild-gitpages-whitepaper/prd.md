# 颠覆式重构 GitHub Pages 为技术白皮书架构学院

## Goal

将项目的 GitHub Pages 从"算法知识库"升级为"高级技术白皮书 / 架构展示站 / 生物信息学算法学院"，具备"降维打击"优势，面向严苛面试官和高级开发者，展现专业度、学术感和极客美学。

## What I already know

**当前项目状态：**
- VitePress 1.6.4，已配置双语支持（zh/en）
- 195 个算法条目，16 个分类，392 个标签
- 已有 vitepress-plugin-mermaid 和 vitepress-plugin-llms 插件
- 已有 OKLCH 颜色系统，深浅色模式基础支持
- 导航配置指向不存在的页面（guides/academy/architecture 等）

**kimi-cli 参考架构：**
- VitePress 1.5.0 + 自定义 style.css（658 行）
- 客户端 JS 语言检测跳转
- Mermaid 图表实际使用
- 清晰的导航结构（Guides/Customization/Configuration/Reference）

**用户需求：**
- 激进策略：不考虑向后兼容
- 视觉升级：精美、极客感、深浅色完美适配
- 内容重构：白皮书 / 学院 / 学术引用机制
- 图示优化：架构图、流程图达到商业级水准

## Assumptions (temporary)

- 用户接受"生物信息学绿"（Emerald）配色方案
- 需要创建全新的内容模块（白皮书、学院、研究、参考）
- 需要添加自定义 Vue 组件（AlgorithmCard、ComplexityChart 等）
- 需要绘制 Mermaid 架构图

## Open Questions

~~1. **配色方案确认**：使用 Emerald（生物信息学绿）还是保持现有配色？~~
~~2. **首页设计**：完全重设计 Hero 还是保留现有结构并优化？~~
~~3. **学术引用**：是否需要从算法数据自动生成引用列表？~~
~~4. **Mermaid 图表**：是否在算法页面添加复杂度可视化图表？~~

## 用户确认 (2026-05-19)

- **视觉风格**：更加学术（academic）
- **配色方案**：保持 Indigo/Cyan 双色调，增加学术感
- **首页设计**：重新设计为"白皮书学院门户"
- **学术引用**：实现规范引用格式
- **Mermaid 图表**：在关键页面添加架构图和流程图

## Requirements (evolving)

### 必须完成（P0）

- [ ] 修复导航配置与实际内容不匹配的问题
- [ ] 创建缺失的内容模块（白皮书、学院、研究、参考）
- [ ] 完善 SVG 深浅色适配（解决图标看不清的问题）
- [ ] 添加 public/ 目录和静态资源（favicon、logo）
- [ ] 重写 style.css，提升视觉质量
- [ ] 创建首页 Hero 重设计

### 应该完成（P1）

- [ ] 添加自定义 Vue 组件
- [ ] 绘制 Mermaid 架构图和流程图
- [ ] 实现学术引用模块
- [ ] 创建算法复杂度可视化
- [ ] 添加时间线组件

### 可以完成（P2）

- [ ] 自动从算法数据生成引用列表
- [ ] 添加页面访问统计
- [ ] 优化语言跳转逻辑

## Acceptance Criteria (evolving)

- [ ] 所有导航链接可用，无 404 页面
- [ ] 深浅色模式下所有 SVG/图标清晰可见
- [ ] 首页设计现代、高级感强
- [ ] 白皮书/学院/研究模块内容完整
- [ ] 本地构建成功，CI 通过
- [ ] GitHub Pages 部署成功

## Definition of Done (team quality bar)

- VitePress 构建成功（npm run build）
- 本地预览测试通过（npm run preview）
- 深浅色模式切换测试通过
- 所有页面导航测试通过
- 代码提交并推送到远程仓库

## Out of Scope (explicit)

- ~~不修改 Python 数据生成脚本~~ — **已移除限制**，需要修改生成器以持久化学术风格改进
- 不添加新的算法数据
- 不实现搜索增强（如 Algolia）
- 不添加评论系统

## Technical Notes

**关键技术决策：**

1. **框架保持 VitePress**：已经是最先进的选择
2. **样式系统**：基于 OKLCH 颜色变量，扩展 CSS 变量体系
3. **组件开发**：Vue 3 Composition API
4. **图表绘制**：Mermaid + 自定义 SVG
5. **部署**：GitHub Pages + GitHub Actions

**文件影响范围：**

```
docs/
├── .vitepress/
│   ├── config.ts          # 重构导航和侧边栏
│   └── theme/
│       ├── index.ts       # 扩展主题
│       └── style.css      # 重写样式
├── public/                # 新增
├── zh/
│   ├── index.md           # 重设计首页
│   ├── whitepaper/        # 新增
│   ├── academy/           # 新增
│   ├── research/          # 新增
│   └── reference/         # 新增
└── en/                    # 镜像结构
```

**参考项目：**

- kimi-cli: `/home/shane/dev/kimi-cli/docs/`
