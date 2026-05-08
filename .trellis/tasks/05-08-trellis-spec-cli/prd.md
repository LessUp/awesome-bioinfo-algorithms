# 重新设计 Trellis Spec 目录结构以适配数据管理 CLI 项目

## Goal

将 `.trellis/spec/` 目录从"后端 Web 项目"模板重新设计为适配本项目（**算法数据管理 + CLI 工具**）的结构，使 AI 助手在开发前能获取到真正相关的编码规范和模式。

## What I already know

**项目性质**：
- 纯 Python 数据管理库，非前后端 Web 项目
- 核心功能：YAML 数据管理、CLI 工具、文档生成
- 无数据库、无 API 服务、无 Web 框架

**当前 spec 目录问题**：
- `.trellis/spec/backend/` 使用 "backend" 命名，暗示 Web 后端
- 包含不适用的指南：`database-guidelines.md`、`logging-guidelines.md`
- 指南文件状态均为 "To fill"，尚未填充内容

**已有价值内容**：
- `.trellis/spec/guides/` 的思维指南（code-reuse、cross-layer）可保留
- `awesome_bioinfo/CLAUDE.md` 已记录包边界、模块职责、关键不变量

**项目实际模块**：
- `schema.py` — 数据类定义
- `algorithm_registry.py` — 数据加载与索引
- `category_manager.py` — 分类层级管理
- `validate.py` — YAML 验证规则
- `data_io.py` — 数据导入导出
- `readme_generator.py` / `generate_mkdocs.py` — 文档生成
- `__main__.py` + 各命令模块 — CLI 入口

## Assumptions (temporary)

- 保留 `guides/` 目录，不需要修改
- 新的 spec 目录应该按**功能领域**划分，而非技术层（backend/frontend）
- 应该填充实际约定而非空白模板

## Decisions

1. **目录命名**：~~采用 `data-management/`~~ → **不再需要**
2. **指南范围**：~~4 个 guideline 文件~~ → **不再需要**
3. **迁移策略**：~~删除 `backend/` 目录，创建新的 `data-management/` 目录~~ → **删除整个 `.trellis/spec/` 目录**
4. **Spec 系统统一**：**只保留 OpenSpec**（`openspec/specs/`），删除 Trellis Spec（`.trellis/spec/`）
5. **思维指南处理**：**删除** — 连同 `.trellis/spec/` 一起删除，依赖 OpenSpec 和 CLAUDE.md

### 决策依据

| 系统 | 格式 | 目的 | 内容 | 状态 |
|------|------|------|------|------|
| OpenSpec | Gherkin (Given/When/Then) | 需求契约、测试可执行 | WHAT（功能需求） | **已完整填充** |
| Trellis Spec | 自由 Markdown | 开发指南、模式约定 | HOW（编码规范） | **空白模板** |

OpenSpec 已覆盖：
- `algorithm-schema/spec.md` — 数据模型规则
- `cli-interface/spec.md` — CLI 命令契约
- `testing-strategy/spec.md` — 测试要求
- `core-architecture/spec.md` — 架构设计
- `product-vision/spec.md` — 产品愿景

## Open Questions

（所有问题已解决）

## Requirements

- 删除 `.trellis/spec/` 整个目录（包括 `backend/` 和 `guides/`）
- 更新 `get_context.py` 以读取 `openspec/specs/` 而非 `.trellis/spec/`
- 更新 `/trellis-before-dev` skill 以读取 OpenSpec 而非 Trellis Spec

## Acceptance Criteria

- [ ] `.trellis/spec/` 目录已删除
- [ ] `get_context.py` 更新为读取 `openspec/specs/`
- [ ] `/trellis-before-dev` skill 更新为读取 OpenSpec

## Definition of Done

- 新 spec 目录结构创建完成
- guideline 文件填充实际内容
- 更新相关配置（如 `get_context.py`）以适配新结构
- 提交变更并通过 CI

## Out of Scope (explicit)

- 修改 `.trellis/spec/guides/` 思维指南
- 创建 OpenSpec 规范（`openspec/specs/` 是独立系统）

## Technical Approach

1. **删除目录**：`rm -rf .trellis/spec/`
2. **更新 `get_context.py`**：修改 `--mode packages` 输出，指向 `openspec/specs/`
3. **更新 `/trellis-before-dev` skill**：修改 skill 脚本，读取 OpenSpec 目录

## Implementation Plan

1. **检查依赖**：确认哪些脚本引用 `.trellis/spec/`
2. **删除目录**：删除 `.trellis/spec/`
3. **更新脚本**：更新 `get_context.py` 和相关 skill
4. **验证**：运行 `/trellis-before-dev` 确认读取 OpenSpec 正常
