# 贡献指南 | Contributing Guide

[English](#english) | [中文](#中文)

---

## 中文

感谢您对 Awesome Bioinformatics Algorithms 项目的关注！我们欢迎各种形式的贡献。

### 贡献方式

#### 1. 添加新算法

**步骤：**

1. Fork 本仓库
2. 在 `data/algorithms/` 目录下找到对应分类的 YAML 文件
3. 按照模板格式添加新算法条目
4. 提交 Pull Request

**算法条目格式：**

```yaml
algorithms:
  - id: algorithm-id          # 唯一标识符（小写字母、数字、连字符）
    name: Algorithm Name      # 算法名称
    description: |            # 算法描述（50-200字）
      算法的详细描述，包括基本原理、特点和适用场景。
    purpose: 主要用途          # 算法的主要用途
    time_complexity: O(n)     # 时间复杂度
    space_complexity: O(n)    # 空间复杂度（可选）
    category: category-id     # 分类ID
    subcategory: sub-id       # 子分类ID（可选）
    paper_url: https://...    # 原始论文链接（可选）
    implementation_url: https://...  # 参考实现链接（可选）
    related_tools:            # 相关工具（可选）
      - Tool1
      - Tool2
    tags:                     # 标签（可选）
      - tag1
      - tag2
```

#### 2. 可用分类

| 分类 ID | 中文名称 | English Name | 子分类 |
|---------|----------|--------------|--------|
| sequence-alignment | 序列比对 | Sequence Alignment | pairwise, multiple |
| assembly | 序列组装 | Sequence Assembly | de-novo, reference-guided |
| variant-calling | 变异检测 | Variant Calling | snv, structural |
| expression-analysis | 基因表达分析 | Gene Expression Analysis | - |
| protein-structure | 蛋白质结构预测 | Protein Structure Prediction | - |
| phylogenetics | 系统发育分析 | Phylogenetics | - |
| functional-annotation | 功能注释 | Functional Annotation | - |
| data-compression | 数据压缩 | Data Compression | - |

#### 3. 质量要求

- ✅ 描述长度在 50-200 字之间
- ✅ 必须包含所有必填字段
- ✅ 分类 ID 必须有效
- ✅ YAML 格式正确
- ✅ 链接有效且可访问

#### 4. 本地验证

在提交前，请在本地运行验证：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行测试
python -m pytest tests/ -v

# 生成 README 预览
python scripts/generate_readme.py
```

### 其他贡献方式

- 📝 改进现有算法描述
- 🔗 添加或更新参考链接
- 🐛 报告错误或问题
- 💡 提出新功能建议

### 行为准则

- 尊重所有贡献者
- 保持专业和友好的交流
- 接受建设性的批评

---

## English

Thank you for your interest in Awesome Bioinformatics Algorithms! We welcome all kinds of contributions.

### How to Contribute

#### 1. Adding New Algorithms

**Steps:**

1. Fork this repository
2. Find the corresponding category YAML file in `data/algorithms/`
3. Add a new algorithm entry following the template format
4. Submit a Pull Request

**Algorithm Entry Format:**

```yaml
algorithms:
  - id: algorithm-id          # Unique identifier (lowercase, numbers, hyphens)
    name: Algorithm Name      # Algorithm name
    description: |            # Description (50-200 characters)
      Detailed description including principles, features, and use cases.
    purpose: Main purpose     # Main purpose of the algorithm
    time_complexity: O(n)     # Time complexity
    space_complexity: O(n)    # Space complexity (optional)
    category: category-id     # Category ID
    subcategory: sub-id       # Subcategory ID (optional)
    paper_url: https://...    # Original paper URL (optional)
    implementation_url: https://...  # Reference implementation URL (optional)
    related_tools:            # Related tools (optional)
      - Tool1
      - Tool2
    tags:                     # Tags (optional)
      - tag1
      - tag2
```

#### 2. Available Categories

| Category ID | Chinese Name | English Name | Subcategories |
|-------------|--------------|--------------|---------------|
| sequence-alignment | 序列比对 | Sequence Alignment | pairwise, multiple |
| assembly | 序列组装 | Sequence Assembly | de-novo, reference-guided |
| variant-calling | 变异检测 | Variant Calling | snv, structural |
| expression-analysis | 基因表达分析 | Gene Expression Analysis | - |
| protein-structure | 蛋白质结构预测 | Protein Structure Prediction | - |
| phylogenetics | 系统发育分析 | Phylogenetics | - |
| functional-annotation | 功能注释 | Functional Annotation | - |
| data-compression | 数据压缩 | Data Compression | - |

#### 3. Quality Requirements

- ✅ Description length between 50-200 characters
- ✅ All required fields must be included
- ✅ Category ID must be valid
- ✅ Correct YAML format
- ✅ Links must be valid and accessible

#### 4. Local Validation

Before submitting, please run validation locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Generate README preview
python scripts/generate_readme.py
```

### Other Ways to Contribute

- 📝 Improve existing algorithm descriptions
- 🔗 Add or update reference links
- 🐛 Report bugs or issues
- 💡 Suggest new features

### Code of Conduct

- Respect all contributors
- Maintain professional and friendly communication
- Accept constructive criticism

---

## License

By contributing, you agree that your contributions will be licensed under CC0 1.0 Universal.
