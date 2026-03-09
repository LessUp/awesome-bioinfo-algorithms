# GitHub Pages 优化 (2026-03-10)

## Pages 构建优化

1. **pages.yml — sparse-checkout**：仅检出 `docs/` 目录，跳过 Python 脚本、测试、数据文件、模板等，加速 CI 构建
2. **_config.yml — SEO 增强**：添加 `lang: zh-CN`，改善搜索引擎和浏览器语言识别
3. **_config.yml — kramdown 配置**：显式配置 rouge 语法高亮
4. **_config.yml — exclude 扩展**：排除 `*.py`、`*.toml`、`*.txt`、`*.yaml`、`*.yml`、Makefile、LICENSE、SECURITY.md、CODE_OF_CONDUCT.md 等非文档文件

## 文档内容优化

5. **docs/index.md — 着陆页增强**：添加"开发指南"按钮、相关资源表格、更新版权年份
6. **README.zh-CN.md — 修复失效徽章**：`validate.yml`（不存在）→ `ci.yml`

## README 更新

7. **README.md + README.zh-CN.md**：添加 Pages workflow 徽章

## 代码质量

8. **.pre-commit-config.yaml**：ruff v0.8.6 → v0.9.0
9. **.gitignore**：添加 `.ruff_cache/`
