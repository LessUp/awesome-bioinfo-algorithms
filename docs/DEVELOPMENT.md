---
title: 开发指南
layout: default
nav_order: 3
description: "项目结构、环境设置与核心组件"
---

# 开发指南 | Development Guide

[English](#english) | [中文](#中文)

---

## 中文

### 项目结构

```
awesome-bioinfo-algorithms/
├── README.md                    # 自动生成的主文档
├── CONTRIBUTING.md              # 贡献指南
├── CODE_OF_CONDUCT.md           # 行为准则
├── SECURITY.md                  # 安全政策
├── CHANGELOG.md                 # 版本变更记录
├── LICENSE                      # 许可证
├── pyproject.toml               # 项目配置（主要）
├── .pre-commit-config.yaml      # 代码质量钩子
├── requirements.txt             # 依赖安装快捷入口（指向 pyproject 配置）
├── data/
│   ├── categories.yaml          # 分类定义
│   └── algorithms/              # 算法数据文件
│       ├── sequence-alignment.yaml
│       ├── assembly.yaml
│       └── ...
├── docs/
│   ├── DEVELOPMENT.md           # 开发指南
│   ├── API.md                   # API 文档
│   └── FAQ.md                   # 常见问题
├── scripts/
│   ├── __main__.py              # CLI 入口（generate/validate/stats）
│   ├── schema.py                # 数据模型定义
│   ├── validate.py              # 数据验证器
│   ├── category_manager.py      # 分类管理器
│   ├── algorithm_registry.py    # 算法注册表
│   ├── readme_generator.py      # README 生成器
│   ├── data_io.py               # 数据导入导出
│   └── generate_readme.py       # 兼容旧用法的包装脚本
├── templates/
│   ├── readme_template.md       # README 模板
│   └── algorithm_template.yaml  # 算法条目模板
├── tests/                       # 测试文件
│   ├── test_schema.py
│   ├── test_validate.py
│   ├── test_category_manager.py
│   ├── test_algorithm_registry.py
│   ├── test_readme_generator.py
│   └── test_data_io.py
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
        └── ci.yml               # CI 工作流
```

### 环境设置

> 本项目的 Python 命令行入口主要服务于仓库维护流程，默认依赖当前仓库中的 `data/` 和 `templates/` 目录；请在仓库根目录运行相关命令。


```bash
# 克隆仓库
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 安装依赖（开发模式，推荐）
pip install -e ".[dev]"

# 或使用 requirements 快捷入口
# pip install -r requirements.txt
```

### 核心组件

#### 1. 数据模型 (schema.py)

定义了两个核心数据类：

- `Category`: 算法分类，支持嵌套子分类
- `AlgorithmEntry`: 算法条目，包含必填和可选字段

#### 2. 验证器 (validate.py)

提供数据验证功能：

- 必填字段检查
- 描述长度验证 (50-500字)
- 分类 ID 验证
- 子分类与父分类关系验证
- 跨文件重复算法 ID 检查
- YAML 格式验证

#### 3. 分类管理器 (category_manager.py)

管理算法分类：

- 从 YAML 加载分类
- 支持子分类层级
- 提供分类查询接口

#### 4. 算法注册表 (algorithm_registry.py)

管理所有算法条目：

- 加载算法数据
- 按分类/标签筛选
- 搜索功能
- 统计信息

#### 5. README 生成器 (readme_generator.py)

生成 README 文档：

- 目录生成
- 分类内容格式化
- 统计信息

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_validate.py -v

# 运行带覆盖率的测试
python -m pytest tests/ --cov=scripts --cov-report=html
```

### 生成 README

```bash
python -m awesome_bioinfo generate
```

### 数据导入导出

```python
from scripts.data_io import DataIO
from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager

# 导出数据
registry = AlgorithmRegistry('data/algorithms')
registry.load_all()
category_manager = CategoryManager()
category_manager.load_categories('data/categories.yaml')

data_io = DataIO(registry, category_manager)
data_io.export_data('backup.yaml', fmt='yaml')
data_io.export_data('backup.json', fmt='json')

# 导入数据
categories, algorithms = data_io.import_data('backup.yaml')
```

---

## English

### Project Structure

```
awesome-bioinfo-algorithms/
├── README.md                    # Auto-generated main document
├── CONTRIBUTING.md              # Contributing guide
├── CODE_OF_CONDUCT.md           # Code of conduct
├── SECURITY.md                  # Security policy
├── CHANGELOG.md                 # Changelog
├── LICENSE                      # License
├── pyproject.toml               # Project config (primary)
├── .pre-commit-config.yaml      # Pre-commit hooks
├── requirements.txt             # Convenience install entrypoint backed by pyproject
├── data/
│   ├── categories.yaml          # Category definitions
│   └── algorithms/              # Algorithm data files
├── docs/                        # Documentation
├── scripts/                     # Core scripts
├── templates/                   # Templates
├── tests/                       # Test files
└── .github/                     # GitHub configurations
```

### Setup

```bash
# Clone repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS

# Install dependencies (dev mode)
pip install -e ".[dev]"
```

### Core Components

1. **schema.py** - Data models (Category, AlgorithmEntry)
2. **validate.py** - Data validation
3. **category_manager.py** - Category management
4. **algorithm_registry.py** - Algorithm registry
5. **readme_generator.py** - README generation
6. **data_io.py** - Data import/export

### Running Tests

```bash
python -m pytest tests/ -v
```

### Generating README

```bash
python -m awesome_bioinfo generate
```
