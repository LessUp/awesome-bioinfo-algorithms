---
title: 开发指南
layout: default
nav_order: 3
description: "项目结构、环境设置和核心架构"
---

# 开发指南
{: .no_toc }

本指南涵盖 Awesome Bioinformatics Algorithms 项目的架构、开发工作流程和贡献流程的所有内容。
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 项目概述

### 项目使命

为全球研究人员、学生和从业者创建最全面、组织良好且易于访问的生物信息学算法集合。

### 设计原则

1. **数据驱动**: 所有内容都存储为结构化 YAML 数据
2. **自动生成**: README 和文档从数据自动生成
3. **双语优先**: 完整支持英文和中文
4. **社区驱动**: 开放贡献流程并设有质量门槛

---

## 项目结构

```
awesome-bioinfo-algorithms/
├── README.md                    # 从模板+数据自动生成
├── CONTRIBUTING.md              # 贡献指南
├── CODE_OF_CONDUCT.md           # 社区行为准则
├── SECURITY.md                  # 安全政策
├── CHANGELOG.md                 # 版本变更日志
├── LICENSE                      # CC0 1.0 Universal
├── pyproject.toml               # Python 项目配置
├── .pre-commit-config.yaml      # Pre-commit 钩子
├── requirements.txt             # 依赖快捷入口
│
├── data/                        # 数据源 - 所有算法数据
│   ├── categories.yaml          # 分类体系
│   └── algorithms/              # 按分类的算法条目
│       ├── sequence-alignment.yaml
│       ├── assembly.yaml
│       └── ...
│
├── docs/                        # 文档 (Jekyll/GitHub Pages)
│   ├── index.md                 # 门户页面
│   ├── 404.md                   # 404 错误页面
│   ├── _config.yml              # Jekyll 配置
│   ├── en/                      # 英文文档
│   └── zh/                      # 中文文档
│
├── scripts/                     # 核心 Python 模块
│   ├── __main__.py              # CLI 入口点
│   ├── schema.py                # 数据模型 (Category, AlgorithmEntry)
│   ├── validate.py              # 数据验证
│   ├── category_manager.py      # 分类管理
│   ├── algorithm_registry.py    # 算法注册表
│   ├── readme_generator.py      # README 生成
│   ├── data_io.py               # 导入/导出功能
│   ├── search.py                # 搜索命令
│   ├── info_cmd.py              # 信息命令
│   ├── stats.py                 # 统计命令
│   ├── compare.py               # 算法比较
│   ├── export_cmd.py            # 导出命令
│   └── generate_mkdocs.py       # MkDocs 生成
│
├── templates/                   # Jinja2 模板
│   ├── readme_template.md       # README 生成模板
│   └── algorithm_template.yaml  # 算法条目模板
│
├── tests/                       # 测试套件 (pytest)
│   ├── conftest.py              # 共享 fixtures
│   ├── test_schema.py
│   ├── test_validate.py
│   ├── test_category_manager.py
│   ├── test_algorithm_registry.py
│   └── ...
│
├── changelog/                   # 详细变更日志
│   ├── archive/                 # 归档条目
│   ├── en/                      # 英文变更日志
│   └── zh/                      # 中文变更日志
│
└── mkdocs/                      # MkDocs 配置
    ├── mkdocs.yml
    └── docs/
```

---

## 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        数据层 (YAML)                        │
│  ┌─────────────┐  ┌─────────────────────────────────────┐  │
│  │ categories  │  │           algorithms/               │  │
│  │   .yaml     │  │  (sequence-alignment.yaml, ...)    │  │
│  └──────┬──────┘  └─────────────────┬───────────────────┘  │
└─────────┼──────────────────────────┼────────────────────────┘
          │                          │
          ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│                      核心 Python 模块                       │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │   schema    │  │   validate   │  │ category_manager │   │
│  │  (models)   │  │  (validate)  │  │ (category mgmt)  │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  algorithm_ │  │   readme_    │  │     data_io      │   │
│  │  registry   │  │   generator  │  │  (import/export) │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
          │                          │
          ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│                       输出生成                              │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  README.md  │  │  docs/ (web) │  │  MkDocs site     │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 环境设置

### 前置要求

- Python 3.9 或更高版本
- Git
- (可选) virtualenv 或 conda 用于隔离环境

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 以开发模式安装
pip install -e ".[dev]"
# 或使用: pip install -r requirements.txt

# 验证安装
python -m scripts --help
```

---

## 核心组件

### 1. 数据模型 (`schema.py`)

```python
@dataclass
class AlgorithmEntry:
    id: str                    # 唯一标识符
    name: str                  # 算法名称
    description: str           # 描述 (50-500 字符)
    purpose: str               # 用途
    time_complexity: str       # 大 O 表示法
    category: str              # 分类 ID
    space_complexity: str = "" # 可选
    year: int = 0              # 发表年份
    paper_url: str = ""        # 论文 URL
    implementation_url: str = ""  # 实现链接
    related_tools: list[str] = []
    tags: list[str] = []
    subcategory: str = ""
    difficulty: str = ""       # beginner/intermediate/advanced
    language: str = ""         # 实现语言
```

### 2. 分类管理器 (`category_manager.py`)

管理层次化分类，支持子分类：

```python
from scripts.category_manager import CategoryManager

cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')

# 按 ID 获取分类
category = cm.get_category('sequence-alignment')

# 列出所有子分类
subcats = cm.get_subcategories('sequence-alignment')

# 验证分类存在性
exists = cm.category_exists('variant-calling')
```

### 3. 算法注册表 (`algorithm_registry.py`)

带搜索功能的中央算法注册表：

```python
from scripts.algorithm_registry import AlgorithmRegistry

registry = AlgorithmRegistry('data/algorithms')
registry.load_all()

# 搜索算法
results = registry.search('dynamic programming')

# 按分类获取
alignment_algos = registry.get_by_category('sequence-alignment')

# 按标签获取
gpu_algos = registry.get_by_tag(' gpu-accelerated')

# 获取统计
stats = registry.get_statistics()
```

### 4. 验证器 (`validate.py`)

全面的数据完整性验证：

```python
from scripts.validate import Validator

validator = Validator()

# 验证单个算法
result = validator.validate_algorithm(algo_dict)

# 验证所有数据
result = validator.validate_all('data')

# 检查验证结果
if not result.is_valid:
    print("错误:", result.errors)
    print("警告:", result.warnings)
```

---

## CLI 命令

### 核心命令

```bash
# 验证所有数据文件
python -m scripts validate

# 生成 README.md
python -m scripts generate

# 生成 MkDocs 页面
python -m scripts mkdocs

# 显示统计
python -m scripts stats

# 搜索算法
python -m scripts search "smith"
python -m scripts search --category sequence-alignment

# 获取算法详情
python -m scripts info smith-waterman

# 比较两个算法
python -m scripts compare smith-waterman needleman-wunsch

# 导出数据
python -m scripts export --format json > algorithms.json
python -m scripts export --format yaml > algorithms.yaml
```

---

## 测试

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_validate.py -v

# 带覆盖率运行
python -m pytest tests/ --cov=scripts --cov-report=html

# 运行特定测试
python -m pytest tests/test_validate.py::test_algorithm_missing_required_field -v
```

### 测试结构

- `test_schema.py` — 数据模型测试
- `test_validate.py` — 验证逻辑测试（包括 Hypothesis 属性测试）
- `test_category_manager.py` — 分类管理测试
- `test_algorithm_registry.py` — 注册表功能测试
- `test_data_io.py` — 导入/导出测试
- `test_cli.py` — CLI 集成测试
- `conftest.py` — 共享 fixtures

---

## 代码质量

### 代码格式和检查

```bash
# 检查格式
ruff format --check scripts/ tests/

# 应用格式
ruff format scripts/ tests/

# 检查代码规范
ruff check scripts/ tests/

# 修复代码规范问题
ruff check --fix scripts/ tests/

# 类型检查
mypy scripts/ --ignore-missing-imports
```

### Pre-commit 钩子

```bash
# 安装钩子
pre-commit install

# 运行所有钩子
pre-commit run --all-files
```

---

## 贡献工作流程

### 1. 设置开发环境

参见上文 [环境设置](#环境设置)。

### 2. 进行修改

- 在 `data/` 中编辑数据文件
- 或在 `scripts/` 中编辑 Python 代码
- 或在 `docs/` 中编辑文档

### 3. 验证更改

```bash
# 验证数据
python -m scripts validate

# 运行测试
python -m pytest tests/ -v

# 检查代码质量
ruff check scripts/ tests/
mypy scripts/
```

### 4. 生成输出

```bash
# 如果编辑了数据或模板
python -m scripts generate      # 更新 README
python -m scripts mkdocs        # 更新文档

# 验证生成的输出是否正确
git diff --exit-code -- README.md mkdocs/docs/
```

### 5. 提交 Pull Request

- 遵循 [Conventional Commits](https://www.conventionalcommits.org/)
- 确保所有检查通过
- 包含清晰的 PR 描述

---

## 发布流程

### 版本号规则

我们遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- `MAJOR.MINOR.PATCH`
- 破坏性变更 → MAJOR
- 新功能 → MINOR
- Bug 修复 → PATCH

### 发布步骤

```bash
# 1. 更新变更日志
# 2. 创建发布标签
git tag -a v1.2.0 -m "Release v1.2.0"

# 3. 推送标签
git push origin v1.2.0

# 4. 创建 GitHub Release（通过 gh CLI 或网页界面）
gh release create v1.2.0 --generate-notes
```

---

## 故障排除

### 常见问题

| 问题 | 解决方案 |
|-----|----------|
| `ModuleNotFoundError` | 运行 `pip install -e ".[dev]"` |
| YAML 语法错误 | 使用在线 YAML 验证器 |
| 测试超时 | 使用 `-k` 指定特定测试 |
| 生成的 README 不同 | 确保运行了 `python -m scripts generate` |

### 获取帮助

- 查看 [常见问题]({% link zh/faq.md %})
- 在 GitHub 上开启 issue
- 加入讨论

---

## 资源链接

- [Python 文档](https://docs.python.org/zh-cn/3/)
- [Pytest 文档](https://docs.pytest.org/)
- [Jekyll 文档](https://jekyllrb.com/docs/)
- [MkDocs 文档](https://www.mkdocs.org/)
