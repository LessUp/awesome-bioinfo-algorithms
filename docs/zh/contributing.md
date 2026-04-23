---
title: 贡献指南
layout: default
nav_order: 5
description: "如何添加算法、分支规范和贡献流程"
---

# 贡献指南
{: .no_toc }

感谢您对 Awesome Bioinformatics Algorithms 项目的贡献兴趣！本指南将帮助您开始。
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 贡献方式

我们在以下领域欢迎贡献：

| 类型 | 说明 |
|:-----|:------------|
| 🆕 **新算法** | 向现有分类添加算法 |
| 📝 **改进** | 增强现有描述 |
| 🔗 **引用** | 添加论文链接或实现 |
| 🐛 **Bug 修复** | 修复数据或代码中的错误 |
| 📚 **文档** | 改进指南和 API 文档 |
| 🧪 **测试** | 添加或改进测试覆盖 |

---

## 快速开始

### 1. Fork 和克隆

```bash
# 在 GitHub 上 Fork 仓库，然后：
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
```

### 2. 设置环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS

# 安装依赖
pip install -e ".[dev]"
```

### 3. 创建分支

```bash
git checkout -b feat/add-my-algorithm
```

**分支命名规范：**
- `feat/` — 新功能或算法
- `fix/` — Bug 修复
- `docs/` — 文档更新
- `refactor/` — 代码重构

### 4. 进行修改

按需编辑文件。添加算法请参见下方 [添加算法](#添加算法)。

### 5. 验证

```bash
# 验证数据
python -m awesome_bioinfo validate

# 运行测试
python -m pytest tests/ -v

# 检查代码质量
ruff check scripts/ tests/
mypy scripts/
```

### 6. 生成输出

```bash
# 重新生成 README
python -m awesome_bioinfo generate

# 重新生成文档
python -m awesome_bioinfo mkdocs
```

### 7. 提交和推送

```bash
git add .
git commit -m "feat: add algorithm for sequence alignment"
git push origin feat/add-my-algorithm
```

### 8. 创建 Pull Request

在 GitHub 上打开 pull request，包含：
- 清晰的标题和描述
- 相关问题引用（如有）
- 变更摘要

---

## 添加算法

### 算法数据格式

将您的算法添加到 `data/algorithms/` 中的相应 YAML 文件：

```yaml
algorithms:
  - id: your-algorithm-id      # 唯一，小写，连字符
    name: 算法名称
    description: |
      详细描述（50-500 字符），解释算法功能、
      主要特点和典型使用场景。
    purpose: 算法用途
    time_complexity: O(n)      # 大 O 表示法
    space_complexity: O(n)     # 可选
    category: category-id      # 见下方分类
    subcategory: sub-id        # 可选
    year: 2024                 # 发表年份（可选）
    paper_url: https://...     # 论文 DOI/URL（可选）
    implementation_url: https://...  # GitHub/代码链接（可选）
    related_tools:             # 相关工具列表（可选）
      - Tool1
      - Tool2
    tags:                      # 相关标签（可选）
      - tag1
      - tag2
    difficulty: intermediate   # beginner/intermediate/advanced（可选）
    language: Python           # 实现语言（可选）
```

### 可用分类

| 分类 ID | 名称 |
|:------------|:-----|
| `sequence-alignment` | 序列比对 |
| `assembly` | 序列组装 |
| `variant-calling` | 变异检测 |
| `expression-analysis` | 基因表达分析 |
| `protein-structure` | 蛋白质结构预测 |
| `phylogenetics` | 系统发育分析 |
| `functional-annotation` | 功能注释 |
| `data-compression` | 数据压缩 |
| `single-cell` | 单细胞基因组学 |
| `metagenomics` | 宏基因组学 |
| `epigenomics` | 表观基因组学 |
| `gene-prediction` | 基因预测 |
| `population-genetics` | 群体遗传学 |
| `spatial-omics` | 空间组学 |
| `graph-genomics` | 图基因组学 |
| `protein-language-model` | 蛋白质语言模型 |

子分类参见 `data/categories.yaml`。

### 质量要求

提交前确保您的算法条目：

- ✅ ID 唯一（小写，连字符）
- ✅ 描述 50-500 字符
- ✅ 所有必填字段存在
- ✅ 分类 ID 有效
- ✅ 子分类属于所选分类
- ✅ YAML 语法有效
- ✅ 链接可访问（如提供）
- ✅ 难度为：`beginner`、`intermediate`、`advanced` 之一

### 示例：添加新算法

```bash
# 1. 编辑相应分类文件
vim data/algorithms/sequence-alignment.yaml

# 2. 按上述格式添加算法条目

# 3. 验证
python -m awesome_bioinfo validate

# 4. 检查是否正确显示
python -m awesome_bioinfo info your-algorithm-id

# 5. 生成更新后的 README
python -m awesome_bioinfo generate
```

---

## 代码风格

### Python 代码

我们使用 `ruff` 进行代码检查和格式化：

```bash
# 检查格式
ruff format --check scripts/ tests/

# 修复格式
ruff format scripts/ tests/

# 检查代码规范
ruff check scripts/ tests/

# 自动修复代码规范问题
ruff check --fix scripts/ tests/
```

### YAML 数据

- 使用 2 空格缩进
- 对多行描述使用块标量 (`|`)
- 对特殊字符的字符串加引号
- 尽可能保持行宽在 100 字符以内

### 提交信息

遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/)：

```
<type>(<scope>): <描述>

[可选正文]

[可选脚注]
```

**类型：**
- `feat` — 新功能或算法
- `fix` — Bug 修复
- `docs` — 文档更改
- `style` — 代码风格（格式化、缺失分号等）
- `refactor` — 代码重构
- `test` — 添加或更新测试
- `chore` — 维护任务

**示例：**
```
feat: add Smith-Waterman algorithm entry

fix: correct time complexity for Dijkstra's algorithm

docs: update API documentation for search function

refactor: simplify validation logic in validate.py
```

---

## 测试

### 运行测试

```bash
# 所有测试
python -m pytest tests/ -v

# 特定测试文件
python -m pytest tests/test_validate.py -v

# 特定测试
python -m pytest tests/test_validate.py::test_algorithm_valid -v

# 带覆盖率
python -m pytest tests/ --cov=scripts --cov-report=html
```

### 编写测试

添加新功能时请包含测试：

```python
# tests/test_new_feature.py
def test_new_feature():
    """测试描述."""
    result = new_feature_function()
    assert result is True
```

---

## Pull Request 流程

### 提交前

1. ✅ 所有测试通过
2. ✅ 数据验证通过
3. ✅ 代码风格检查通过
4. ✅ README 已重新生成（如数据有变更）
5. ✅ 文档已更新（如需要）

### PR 描述模板

```markdown
## 描述
变更简述

## 变更类型
- [ ] Bug 修复
- [ ] 新算法
- [ ] 文档更新
- [ ] 重构

## 检查清单
- [ ] 测试通过
- [ ] 验证通过
- [ ] README 已重新生成（如数据有变更）
- [ ] 遵循贡献指南

## 相关问题
修复 #123
```

### 审核流程

1. 自动化测试在您的 PR 上运行
2. 维护者在 3-5 天内审核
3. 处理任何要求的更改
4. 批准后，您的 PR 将被合并

---

## 获取帮助

- 💬 开启 issue 咨询问题
- 📖 阅读 [常见问题]({% link zh/faq.md %})
- 🔍 查看现有 issue

---

## 许可证

通过贡献，您同意将您的贡献在 CC0 1.0 Universal（公共领域）下授权。

感谢您的贡献！🎉
