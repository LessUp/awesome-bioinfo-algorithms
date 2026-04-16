---
title: 常见问题
layout: default
nav_order: 4
description: "常见问题解答和故障排除指南"
---

# 常见问题
{: .no_toc }

查找关于使用和贡献 Awesome Bioinformatics Algorithms 项目的常见问题的答案。
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 一般问题

### 这个项目是什么？

Awesome Bioinformatics Algorithms 是一个精心策划的生物信息学算法开源集合。它提供：

- 📊 以 YAML 格式存储的结构化算法数据
- 🔍 搜索和比较功能
- 📖 自动生成的文档
- 🌐 双语支持（英文和中文）

所有算法包括时间/空间复杂度、相关论文、实现链接和标签。

### 谁维护这个项目？

该项目由 LessUp 组织下的社区维护。欢迎生物信息学社区的任何人贡献。

### 项目多久更新一次？

更新频率因社区贡献而异。我们通常会在几天内审核和合并 pull request。

---

## 快速开始

### 如何设置开发环境？

```bash
# 克隆仓库
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

# 安装依赖
pip install -e ".[dev]"

# 验证设置
python -m scripts validate
```

### 需要什么 Python 版本？

需要 Python 3.9 或更高版本。我们在 Python 3.9、3.10、3.11 和 3.12 上进行测试。

### 贡献需要生物信息学专业知识吗？

不需要！虽然添加算法需要生物信息学知识，但您可以通过多种方式贡献：

- 改进文档
- 修正拼写和格式
- 添加测试用例
- 改进 Python 工具

---

## 添加算法

### 新算法需要什么信息？

**必填字段：**

| 字段 | 说明 | 示例 |
|:-----|:------------|:--------|
| `id` | 唯一标识符（小写、连字符） | `smith-waterman` |
| `name` | 算法名称 | `Smith-Waterman` |
| `description` | 描述（50-500 字符） | 算法描述 |
| `purpose` | 算法用途 | `局部序列比对` |
| `time_complexity` | 大 O 表示法 | `O(mn)` |
| `category` | 必须是有效的分类 ID | `sequence-alignment` |

**可选但推荐的字段：**
- `space_complexity` — 空间复杂度
- `year` — 发表年份
- `paper_url` — 原始论文链接
- `implementation_url` — 参考实现链接
- `tags` — 用于分类的相关标签

### 如何选择正确的分类？

查看 [`data/categories.yaml`](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/data/categories.yaml) 获取完整的分类和子分类列表。如果不确定，您可以：

1. 使用 `python -m scripts search "keyword"` 搜索类似算法
2. 查看它们属于哪个分类
3. 为您的算法使用相同分类

### 为什么我的描述被拒绝？

描述必须为 **50-500 字符**（修剪后）。这确保：

- 足够详细以理解算法功能
- 在列表中简洁易读

**良好描述示例：**
```yaml
description: |
  Smith-Waterman 算法执行局部序列比对，
  识别两个序列之间最相似的子序列。
  它使用动态规划保证最优局部比对。
```

### 可以添加新分类吗？

可以，但请先开启 issue 讨论。新分类应该：

- 代表一个独特的生物信息学领域
- 具有广泛的适用性
- 能够包含多个算法

### 如何选择难度级别？

使用 `difficulty` 字段，可选值：

- `beginner` — 基础算法，易于理解和实现
- `intermediate` — 中等复杂度，需要一些背景知识
- `advanced` — 复杂算法，研究级实现

---

## 使用 CLI

### 如何搜索算法？

```bash
# 基本搜索
python -m scripts search "alignment"

# 在特定分类中搜索
python -m scripts search "fast" --category sequence-alignment

# 不区分大小写搜索
python -m scripts search "BLAST"
```

### 如何比较两个算法？

```bash
python -m scripts compare smith-waterman needleman-wunsch
```

这将并排显示：
- 时间/空间复杂度
- 使用场景
- 相关工具

### 如何导出数据？

```bash
# 导出为 JSON
python -m scripts export --format json > algorithms.json

# 导出为 YAML
python -m scripts export --format yaml > algorithms.yaml
```

---

## 故障排除

### "ModuleNotFoundError: No module named 'scripts'"

**原因：** 未以开发模式安装包。

**解决方案：**
```bash
pip install -e ".[dev]"
```

### "ValidationError: description too short"

**原因：** 描述少于 50 字符。

**解决方案：** 将描述扩展到至少 50 字符。

### YAML 语法错误

**症状：** 运行 `validate` 时解析器错误

**解决方案：**
1. 使用空格而非制表符缩进
2. 对特殊字符的字符串加引号
3. 使用 YAML 验证器：[yaml-validator.com](https://yaml-validator.com)

### 测试因 Hypothesis 错误失败

**原因：** 属性测试在您的机器上可能太慢。

**解决方案：** 这通常自动处理，但您可以运行特定测试：

```bash
# 仅运行验证测试
python -m pytest tests/test_validate.py -v

# 运行特定测试
python -m pytest tests/test_validate.py::test_algorithm_valid -v
```

### CI 中 "git diff --exit-code" 失败

**原因：** 生成的文件已过期。

**解决方案：**
```bash
# 重新生成所有输出
python -m scripts generate
python -m scripts mkdocs

# 检查差异
git diff

# 提交更改
git add README.md mkdocs/docs/
git commit -m "chore: regenerate documentation"
```

---

## 贡献相关

### 如何贡献？

我们在以下领域欢迎贡献：

1. **添加新算法** — 遵循我们的算法模板
2. **改进描述** — 使现有内容更准确
3. **添加引用** — 链接论文和实现
4. **Bug 修复** — 修复数据或代码中的错误
5. **文档** — 改进指南和 API 文档

### 贡献工作流程是什么？

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 运行验证：`python -m scripts validate`
5. 运行测试：`python -m pytest tests/ -v`
6. 生成输出：`python -m scripts generate`
7. 提交 pull request

### 提交信息规范是什么？

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/)：

```
feat: 添加新的序列比对算法
fix: 修正 XYZ 算法的时间复杂度
docs: 更新搜索函数的 API 参考
refactor: 简化验证逻辑
test: 添加边界情况测试
```

### PR 多久会被审核？

我们目标是在 3-5 天内审核 PR。在繁忙时期，可能需要一周。

---

## 数据问题

### 数据是如何组织的？

算法数据存储在 `data/algorithms/` 下的 YAML 文件中，按分类组织：

```
data/algorithms/
├── sequence-alignment.yaml
├── assembly.yaml
├── variant-calling.yaml
└── ...
```

每个文件包含 `algorithms:` 键下的多个算法条目。

### 可以在自己的项目中使用这些数据吗？

可以！数据在 CC0 1.0（公共领域）下授权。您可以：

- 自由使用数据
- 修改它
- 重新分发它
- 用于商业目的

不需要署名，但受到欢迎。

### 如何报告算法数据中的错误？

在 GitHub 上开启 issue 描述：
- 算法 ID
- 什么信息有误
- 正确信息应该是什么

或提交修复该问题的 pull request。

---

## 技术问题

### 为什么文档使用 Jekyll？

Jekyll 与 GitHub Pages 无缝集成，提供：
- 免费托管
- 版本控制集成
- 简单的 Markdown 内容
- 内置主题

### 为什么使用 YAML 而非 JSON？

选择 YAML 是因为：
- 带注释的更好可读性
- 支持多行字符串
- 对生物信息学家更简洁的语法
- 更容易手动编辑

### 可以在自己的代码中使用 Python API 吗？

可以！安装包后：

```python
from scripts.algorithm_registry import AlgorithmRegistry

registry = AlgorithmRegistry()
registry.load_all()

# 在应用中使用
algorithms = registry.search("alignment")
```

---

## 还有其他问题？

- 📖 阅读 [贡献指南](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/CONTRIBUTING.md)
- 📚 查看 [API 文档]({% link zh/api.md %})
- 🔍 搜索现有的 [GitHub Issues](https://github.com/LessUp/awesome-bioinfo-algorithms/issues)
- 💬 开启新 issue 咨询您的问题
