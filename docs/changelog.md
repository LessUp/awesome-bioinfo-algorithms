---
title: 变更日志
layout: default
nav_order: 6
description: "版本发布历史"
---

# 变更日志
{: .no_toc }

本页记录每个版本的主要变更。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

---

## v1.0.1 — 2026-02-13
{: .d-inline-block }

Latest
{: .label .label-green }

### 修复

- 修复 `requirements.txt` 与 `pyproject.toml` 一致性（用 `ruff` 替换 `black`/`flake8`）
- 修复 `docs/API.md` 中 API 签名错误
- 修复 `docs/FAQ.md` 中分类列表不完整（4→8）
- 修复 `CHANGELOG.md` 章节顺序及不完整的分类/算法列表
- 修复 `pyproject.toml` 开发状态标识
- 更新 `.pre-commit-config.yaml` 钩子版本

### 新增

- 添加 `SECURITY.md` 安全政策
- 添加 Pull Request 模板与 Bug Report Issue 模板
- 添加 `changelog/` 变更日志目录

---

## v1.0.0 — 2026-01-07

### 新增

- 初始版本，包含核心功能
- 算法注册表、分类管理器、验证系统
- README 自动生成（从 YAML 数据）
- Hypothesis 属性测试
- GitHub Actions CI/CD
- 代码质量工具（ruff、mypy）
- Pre-commit 钩子
- 12 个算法分类、54 个算法条目

---

完整变更日志请参阅 [CHANGELOG.md](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/CHANGELOG.md)。
