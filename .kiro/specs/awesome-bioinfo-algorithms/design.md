# Design Document: Awesome Bioinformatics Algorithms

## Overview

本项目是一个 GitHub 开源项目，采用 awesome-list 风格汇总生物信息学算法概要。项目使用 YAML 文件存储算法数据，通过 Python 脚本自动生成 README.md 文档。

## Architecture

```
awesome-bioinfo-algorithms/
├── README.md                    # 自动生成的主文档
├── CHANGELOG.md                 # 版本变更记录
├── CONTRIBUTING.md              # 贡献指南
├── CODE_OF_CONDUCT.md           # 行为准则
├── SECURITY.md                  # 安全政策
├── pyproject.toml               # 项目配置
├── .pre-commit-config.yaml      # pre-commit 配置
├── data/
│   ├── categories.yaml          # 分类定义
│   └── algorithms/              # 按分类组织的算法文件
├── scripts/                     # Python 脚本包
├── tests/                       # 测试目录
├── templates/                   # 模板目录
├── changelog/                   # 详细变更日志
├── docs/                        # 文档目录
├── mkdocs/                      # MkDocs 配置和文档
└── .github/                     # GitHub 配置
    ├── ISSUE_TEMPLATE/          # Issue 模板
    ├── workflows/               # CI 工作流
    └── PULL_REQUEST_TEMPLATE.md # PR 模板
```

## Components

### Core Components

| Component | File | Description |
|-----------|------|-------------|
| Category Manager | `category_manager.py` | 管理算法分类体系 |
| Algorithm Registry | `algorithm_registry.py` | 算法注册表，管理所有条目 |
| README Generator | `readme_generator.py` | 生成 README 文档 |
| Validator | `validate.py` | 数据验证 |
| Data IO | `data_io.py` | 数据导入导出 |
| Schema | `schema.py` | 数据模型定义 |

### CLI Commands

| Command | Description |
|---------|-------------|
| `python -m scripts generate` | 生成 README.md |
| `python -m scripts validate` | 验证数据文件 |
| `python -m scripts stats` | 显示统计信息 |
| `python -m scripts search` | 搜索算法 |
| `python -m scripts info` | 显示算法详情 |
| `python -m scripts compare` | 比较两个算法 |
| `python -m scripts export` | 导出数据 |
| `python -m scripts mkdocs` | 生成 MkDocs 页面 |

## Data Models

### Category

```python
@dataclass
class Category:
    id: str                           # 分类ID
    name: str                         # 中文名称
    name_en: str                      # 英文名称
    description: str = ""             # 描述
    subcategories: list[Category]     # 子分类
    parent_id: Optional[str] = None   # 父分类ID
```

### AlgorithmEntry

```python
@dataclass
class AlgorithmEntry:
    # 必填字段
    id: str                  # 唯一标识符
    name: str                # 算法名称
    description: str         # 简要描述 (50-500字)
    purpose: str             # 主要用途
    time_complexity: str     # 时间复杂度
    category: str            # 主分类ID
    
    # 可选字段
    space_complexity: str    # 空间复杂度
    year: int                # 发表年份
    paper_url: str           # 原始论文链接
    implementation_url: str  # 参考实现链接
    related_tools: list[str] # 相关工具
    tags: list[str]          # 标签
    subcategory: str         # 子分类ID
    difficulty: str          # 难度 (beginner/intermediate/advanced)
    language: list[str]      # 实现语言
    references: list[Reference]  # 扩展资料
```

## Correctness Properties

| Property | Description |
|----------|-------------|
| Property 1 | Category Algorithm Count Accuracy |
| Property 2 | Subcategory Hierarchy Preservation |
| Property 3 | Required Fields Validation |
| Property 4 | Optional Fields Storage |
| Property 5 | Markdown Output Consistency |
| Property 6 | Table of Contents Completeness |
| Property 7 | Validation Error Specificity |
| Property 8 | Search Result Correctness |
| Property 9 | Anchor Link Format Validity |
| Property 10 | Data Format Validation |
| Property 11 | Data Import/Export Round-Trip |

## Testing Strategy

- **Unit Tests**: 覆盖所有核心功能
- **Property-Based Tests**: 使用 Hypothesis，每个测试至少 100 次迭代
- **Integration Tests**: 完整的 README 生成和 CI 验证流程

## Current Status

| Metric | Value |
|--------|-------|
| Total Algorithms | 201 |
| Categories | 16 |
| Tags | 399 |
| Python Versions | 3.9, 3.10, 3.11, 3.12 |
| Test Coverage | >85% |
