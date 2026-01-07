# Design Document: Project Enhancement

## Overview

本设计文档描述如何将 Awesome Bioinformatics Algorithms 项目完善为一个优秀的开源项目。主要改进包括：修复测试问题、配置代码质量工具、完善文档、增强 CI/CD、建设社区资产、现代化项目配置。

## Architecture

项目结构将扩展为：

```
awesome-bioinfo-algorithms/
├── README.md                    # 主文档（更新徽章和占位符）
├── CONTRIBUTING.md              # 贡献指南（已有）
├── CODE_OF_CONDUCT.md           # 行为准则（新增）
├── SECURITY.md                  # 安全政策（新增）
├── CHANGELOG.md                 # 版本变更记录（新增）
├── LICENSE                      # 许可证（已有）
├── pyproject.toml               # 项目配置（新增，替代 requirements.txt）
├── .pre-commit-config.yaml      # pre-commit 配置（新增）
├── data/                        # 数据目录（已有）
├── docs/
│   ├── DEVELOPMENT.md           # 开发指南（已有）
│   ├── API.md                   # API 文档（新增）
│   └── FAQ.md                   # 常见问题（新增）
├── scripts/
│   ├── __init__.py              # 包初始化（已有）
│   ├── py.typed                 # 类型标记（新增）
│   └── ...                      # 其他脚本（已有）
├── tests/                       # 测试目录（已有，需修复）
├── templates/                   # 模板目录（已有）
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── new_algorithm.md     # 新算法模板（已有）
    │   ├── bug_report.md        # Bug 报告模板（新增）
    │   └── feature_request.md   # 功能请求模板（新增）
    ├── PULL_REQUEST_TEMPLATE.md # PR 模板（新增）
    └── workflows/
        └── validate.yml         # CI 工作流（更新）
```

## Components and Interfaces

### 1. 测试修复

修复 `test_property_1_category_algorithm_count_accuracy` 测试中的 Hypothesis 健康检查问题。

```python
# 优化策略：简化生成器，添加健康检查抑制
from hypothesis import settings, HealthCheck

@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.too_slow]
)
@given(algorithms=algorithms_list_strategy())
def test_property_1_category_algorithm_count_accuracy(algorithms):
    ...
```

### 2. pyproject.toml 配置

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "awesome-bioinfo-algorithms"
version = "1.0.0"
description = "A curated list of bioinformatics algorithms"
readme = "README.md"
license = {text = "CC0-1.0"}
requires-python = ">=3.9"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["bioinformatics", "algorithms", "awesome-list"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

dependencies = [
    "PyYAML>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "hypothesis>=6.0",
    "ruff>=0.1.0",
    "mypy>=1.0",
    "pre-commit>=3.0",
]

[project.urls]
Homepage = "https://github.com/YOUR_USERNAME/awesome-bioinformatics-algorithms"
Repository = "https://github.com/YOUR_USERNAME/awesome-bioinformatics-algorithms"
Issues = "https://github.com/YOUR_USERNAME/awesome-bioinformatics-algorithms/issues"

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "D", "UP", "B", "C4"]
ignore = ["D100", "D104"]

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"

[tool.coverage.run]
source = ["scripts"]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if __name__ == .__main__.:",
]
```

### 3. pre-commit 配置

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-PyYAML]
```

### 4. CI/CD 增强

更新 `.github/workflows/validate.yml` 以支持：
- 多 Python 版本测试矩阵
- 代码质量检查（ruff、mypy）
- 覆盖率报告上传到 Codecov

### 5. 社区模板

#### Pull Request 模板
```markdown
## 描述 / Description
简要描述此 PR 的更改内容。

## 更改类型 / Type of Change
- [ ] 新算法 / New algorithm
- [ ] Bug 修复 / Bug fix
- [ ] 文档更新 / Documentation update
- [ ] 其他 / Other

## 检查清单 / Checklist
- [ ] 我已阅读贡献指南
- [ ] 代码通过本地测试
- [ ] 已更新相关文档
```

#### Bug Report 模板
```markdown
---
name: Bug 报告 / Bug Report
about: 报告一个问题 / Report an issue
labels: 'bug'
---

## 问题描述 / Bug Description

## 复现步骤 / Steps to Reproduce

## 预期行为 / Expected Behavior

## 实际行为 / Actual Behavior

## 环境信息 / Environment
- Python 版本:
- 操作系统:
```

## Data Models

无新增数据模型，使用现有的 `Category` 和 `AlgorithmEntry` 数据类。

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

由于本次改进主要是配置和文档任务，大部分验收标准适合用示例测试验证。只有数据相关的需求适合用属性测试：

### Property 1: Algorithm Data Completeness

*For any* algorithm entry in the registry, the entry SHALL pass all validation rules including required fields, description length (50-200 characters), and valid category reference.

**Validates: Requirements 7.2, 7.3**

### Property 2: Category Coverage

*For any* main category defined in categories.yaml, the category SHALL contain at least 2 algorithms in the registry.

**Validates: Requirements 7.1**

注：现有的属性测试已经覆盖了大部分数据验证需求（Property 3-11 在原设计文档中）。本次改进主要是配置和文档任务，不需要新增大量属性测试。

## Error Handling

### 配置错误

| Error Type | Condition | Response |
|------------|-----------|----------|
| InvalidConfig | pyproject.toml 格式错误 | 提示检查 TOML 语法 |
| MissingDependency | 缺少必要依赖 | 提示运行 pip install -e ".[dev]" |
| LintError | 代码不符合规范 | 显示具体违规位置和修复建议 |
| TypeCheckError | 类型检查失败 | 显示类型错误详情 |

### CI 错误

| Error Type | Condition | Response |
|------------|-----------|----------|
| TestFailure | 测试失败 | 显示失败测试和错误信息 |
| CoverageBelow | 覆盖率低于阈值 | 提示增加测试覆盖 |
| ValidationFailure | 数据验证失败 | 显示验证错误详情 |

## Testing Strategy

### 单元测试

现有测试套件已覆盖核心功能，本次改进需要：

1. **修复失败测试**
   - 修复 `test_property_1_category_algorithm_count_accuracy` 的 Hypothesis 健康检查问题
   - 优化测试生成策略或添加健康检查抑制

2. **验证配置**
   - 验证 pyproject.toml 配置正确
   - 验证 pre-commit 配置可用
   - 验证 CI 工作流语法正确

### 属性测试

使用 Hypothesis 进行属性测试：

- 每个属性测试运行至少 100 次迭代
- 测试标注格式: **Feature: project-enhancement, Property {number}: {property_text}**

### 集成测试

1. 验证完整的 CI 流程
2. 验证代码质量工具链
3. 验证文档生成流程

