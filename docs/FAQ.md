---
title: 常见问题
layout: default
nav_order: 4
description: "使用与贡献常见问题解答"
---

# Frequently Asked Questions / 常见问题

## General / 一般问题

### What is this project? / 这个项目是什么？

This is a curated list of bioinformatics algorithms, organized by category with detailed information about each algorithm including time/space complexity, related papers, and implementations.

这是一个精选的生物信息学算法列表，按类别组织，包含每个算法的详细信息，如时间/空间复杂度、相关论文和实现。

### How can I contribute? / 如何贡献？

Please read our [Contributing Guide](../CONTRIBUTING.md) for detailed instructions. In short:

1. Fork the repository
2. Add your algorithm to the appropriate YAML file in `data/algorithms/`
3. Run validation: `python -m scripts validate`
4. Submit a Pull Request

请阅读我们的[贡献指南](../CONTRIBUTING.md)获取详细说明。简而言之：

1. Fork 仓库
2. 将算法添加到 `data/algorithms/` 中的相应 YAML 文件
3. 运行验证：`python -m scripts validate`
4. 提交 Pull Request

---

## Adding Algorithms / 添加算法

### What information is required for a new algorithm? / 新算法需要哪些信息？

Required fields:
- `id`: Unique identifier (lowercase, hyphens allowed)
- `name`: Algorithm name
- `description`: Description (50-500 characters)
- `purpose`: What the algorithm is used for
- `time_complexity`: Big-O notation (e.g., "O(n^2)")
- `category`: Must match an existing category ID

Optional fields:
- `space_complexity`: Space complexity
- `paper_url`: Link to the original paper
- `implementation_url`: Link to an implementation
- `tags`: List of relevant tags
- `related_tools`: List of tools using this algorithm

### Why is my description being rejected? / 为什么我的描述被拒绝？

Descriptions must be between 50 and 500 characters. This ensures:
- Enough detail to understand the algorithm
- Concise enough for readability

### What categories are available? / 有哪些可用的分类？

The project includes multiple top-level categories such as sequence alignment, assembly,
variant calling, expression analysis, protein structure, phylogenetics, functional annotation,
data compression, single-cell genomics, metagenomics, epigenomics, and gene prediction.

Check `data/categories.yaml` for the current complete list, including subcategories.

---

## Development / 开发

### How do I set up the development environment? / 如何设置开发环境？

```bash
# Clone the repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/

# Run linting and type checks
ruff check scripts/ tests/
mypy scripts/ --ignore-missing-imports
```

### How do I run the tests? / 如何运行测试？

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=scripts

# Run specific test file
python -m pytest tests/test_validate.py
```

### How do I generate the README? / 如何生成 README？

```bash
python -m scripts generate
```

This will regenerate `README.md` from the data in the repository `data/` directory and should be run from a repository checkout.

---

## Troubleshooting / 故障排除

### Tests are failing with Hypothesis errors / 测试因 Hypothesis 错误而失败

If you see "HealthCheck" errors, the test generators might be too slow. This is usually handled automatically, but you can increase the deadline:

```python
@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
```

### YAML validation errors / YAML 验证错误

Common issues:
- Indentation must use spaces, not tabs
- Strings with special characters should be quoted
- Lists must be properly formatted

Use a YAML validator to check your files.

### Import errors / 导入错误

Make sure you're running the command from a repository checkout and have installed the local dependencies:

```bash
pip install -e ".[dev]"
```

---

## Contact / 联系

For questions not covered here, please:
- Open an issue on GitHub
- Check existing issues for similar questions

如果这里没有涵盖您的问题，请：
- 在 GitHub 上开一个 issue
- 查看现有 issue 是否有类似问题
