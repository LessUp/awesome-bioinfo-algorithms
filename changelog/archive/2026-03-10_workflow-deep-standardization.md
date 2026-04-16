# 2026-03-10 工作流深度标准化

**日期**: 2026-03-10  
**类型**: CI/CD 优化 / Workflow Optimization

---

## 变更摘要

GitHub Actions 工作流深度标准化：统一命名、权限、并发、路径过滤与缓存策略。

## 详细变更

### CI 工作流 (`ci.yml`)

| 变更项 | 说明 |
|--------|------|
| 文件重命名 | `validate.yml` → `ci.yml` |
| 权限配置 | 统一 `permissions: contents: read` |
| 并发控制 | 添加 `concurrency` 配置，避免重复运行 |

### Pages 工作流 (`pages.yml`)

| 变更项 | 说明 |
|--------|------|
| 配置步骤 | 补充 `actions/configure-pages@v5` |
| 路径过滤 | 添加 `paths` 触发过滤，减少无效构建 |

## 影响范围

- `.github/workflows/ci.yml`
- `.github/workflows/pages.yml`
