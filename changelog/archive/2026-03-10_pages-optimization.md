# 2026-03-10 GitHub Pages 优化

**日期**: 2026-03-10  
**类型**: 文档部署优化 / Documentation Deployment

---

## 变更摘要

优化 GitHub Pages 构建流程和文档 SEO。

## 详细变更

### Pages 构建优化

| 变更项 | 文件 | 说明 |
|--------|------|------|
| 稀疏检出 | `pages.yml` | 仅检出 `docs/` 目录，加速 CI 构建 |
| SEO 增强 | `_config.yml` | 添加 `lang: zh-CN`，改善搜索引擎识别 |
| 语法高亮 | `_config.yml` | 配置 kramdown + rouge |
| 排除规则 | `_config.yml` | 排除非文档文件（`*.py`, `*.toml` 等） |

### 文档内容优化

| 变更项 | 文件 | 说明 |
|--------|------|------|
| 着陆页增强 | `docs/index.md` | 添加开发指南按钮、资源表格、更新年份 |
| 徽章修复 | `README.zh-CN.md` | `validate.yml` → `ci.yml` |
| 徽章添加 | `README.md` | 添加 Pages workflow 徽章 |

### 代码质量

| 变更项 | 文件 | 说明 |
|--------|------|------|
| 版本更新 | `.pre-commit-config.yaml` | ruff v0.8.6 → v0.9.0 |
| 缓存忽略 | `.gitignore` | 添加 `.ruff_cache/` |

## 影响范围

- `.github/workflows/pages.yml`
- `docs/_config.yml`
- `docs/index.md`
- `README.md`
- `README.zh-CN.md`
- `.pre-commit-config.yaml`
- `.gitignore`
