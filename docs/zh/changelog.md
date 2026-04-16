---
title: 变更日志
layout: default
nav_order: 6
description: "版本发布历史和变更记录"
---

# 变更日志
{: .no_toc }

本文档记录 Awesome Bioinformatics Algorithms 项目的所有重要变更。遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 格式。
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 当前版本

### v1.0.2 — 2026-04-16

**变更内容：**

- 修复 Python 3.9 兼容性，将联合类型语法替换为 `Optional[X]`
- 修复搜索不一致问题，添加 `purpose` 字段到搜索逻辑
- 合并 4 个文件中重复的 `difficulty_labels` 映射
- 修复 MkDocs 生成测试的错误期望
- 使用 `HealthCheck.too_slow` 抑制修复不稳定的 hypothesis 测试
- 修复 PyYAML 的 mypy 类型存根问题

[查看详细变更日志 →](../../changelog/zh/2026-04-16_code-review.md)

---

## 版本历史

### v1.0.1 — 2026-02-13

**变更内容：**

- 修复 `requirements.txt` 与 `pyproject.toml` 一致性（用 `ruff` 替换 `black`/`flake8`）
- 修复 `docs/API.md` 中的 API 签名错误
- 修复 `docs/FAQ.md` 中不完整的分类列表（4→8 个）
- 修复 `CHANGELOG.md` 章节顺序和不完整列表
- 修复 `pyproject.toml` 开发状态标识（从 Beta 改为 Production/Stable）
- 更新 `.pre-commit-config.yaml` 钩子版本
- 添加 `SECURITY.md` 安全政策
- 添加 Pull Request 和 Bug Report 模板
- 添加 `changelog/` 目录用于详细变更跟踪

[查看详细变更日志 →](../../changelog/2026-02-13_content_enhancement.md)

### v1.0.0 — 2026-01-07

**初始版本：**

- 算法注册表用于管理算法条目
- 分类管理器用于组织算法
- 数据完整性验证系统
- 从 YAML 数据自动生成 README
- 基于 Hypothesis 的属性测试
- GitHub Actions CI/CD 流水线
- 多 Python 版本测试（3.9、3.10、3.11、3.12）
- 代码质量工具（ruff、mypy）
- Pre-commit 钩子配置
- 社区模板（PR、Issues）
- 行为准则
- 安全政策
- API 文档
- FAQ 文档

**初始统计：**

- 16 个算法分类
- 201 个算法
- 399 个唯一标签

---

## 详细变更日志

每个版本的详细信息请参阅 `changelog/` 目录：

| 日期 | 文件 | 说明 |
|:-----|:-----|:------------|
| 2026-04-16 | [code-review](../../changelog/zh/2026-04-16_code-review.md) | 代码审查和 Bug 修复 |
| 2026-03-10 | [pages-optimization](../../changelog/2026-03-10_pages-optimization.md) | GitHub Pages 优化 |
| 2026-03-10 | [workflow-deep-standardization](../../changelog/2026-03-10_workflow-deep-standardization.md) | CI/CD 工作流标准化 |
| 2026-02-13 | [content-enhancement](../../changelog/2026-02-13_content_enhancement.md) | 内容扩充和 Bug 修复 |
| 2026-02-13 | [project-optimization](../../changelog/2026-02-13_project_optimization.md) | 项目优化 |
| 2026-01-08 | [maintenance](../../changelog/2026-01-08-maintenance.md) | 项目维护 |

---

## 版本控制

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **MAJOR** 版本 — 不兼容的 API 变更
- **MINOR** 版本 — 添加功能（向后兼容）
- **PATCH** 版本 — Bug 修复（向后兼容）

---

## 即将到来的

### v2.0.0 计划

- [ ] 交互式 Web 界面
- [ ] 算法比较工具
- [ ] 增强的过滤搜索
- [ ] 算法性能基准
- [ ] RESTful API

---

另见：[完整 CHANGELOG.md](../../CHANGELOG.md) | [历史详情](../../changelog/)
