---
title: 贡献指南
layout: default
nav_order: 5
description: "如何添加新算法、分支规范与提交流程"
---

# 贡献指南 | Contributing
{: .no_toc }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

欢迎贡献！我们接受以下类型的贡献：

- 🆕 添加新算法
- 📝 改进现有描述
- 🔗 添加参考链接
- 🐛 修复错误

## 添加新算法

1. Fork 本仓库
2. 在 `data/algorithms/` 中找到对应分类的 YAML 文件
3. 按模板格式添加新算法条目
4. 提交 Pull Request

**算法条目格式**：

```yaml
algorithms:
  - id: algorithm-id          # 唯一标识（小写、数字、连字符）
    name: Algorithm Name      # 算法名称
    description: |            # 描述（50-500 字符）
      详细描述，包括原理、特点和应用场景。
    purpose: 主要用途          # 算法主要用途
    time_complexity: O(n)     # 时间复杂度
    space_complexity: O(n)    # 空间复杂度（可选）
    category: category-id     # 分类 ID
    paper_url: https://...    # 原始论文链接（可选）
    implementation_url: https://...  # 参考实现链接（可选）
    related_tools:            # 相关工具（可选）
      - Tool1
    tags:                     # 标签（可选）
      - tag1
```

## 可用分类

| 分类 ID | 中文名 | 英文名 |
|:--|:--|:--|
| sequence-alignment | 序列比对 | Sequence Alignment |
| assembly | 序列组装 | Sequence Assembly |
| variant-calling | 变异检测 | Variant Calling |
| expression-analysis | 基因表达分析 | Gene Expression Analysis |
| protein-structure | 蛋白质结构预测 | Protein Structure Prediction |
| phylogenetics | 系统发育分析 | Phylogenetics |
| functional-annotation | 功能注释 | Functional Annotation |
| data-compression | 数据压缩 | Data Compression |
| single-cell | 单细胞基因组学 | Single-Cell Genomics |
| metagenomics | 宏基因组学 | Metagenomics |
| epigenomics | 表观基因组学 | Epigenomics |
| gene-prediction | 基因预测 | Gene Prediction |
| population-genetics | 群体遗传学 | Population Genetics |
| spatial-omics | 空间组学 | Spatial Omics |
| graph-genomics | 图基因组学 | Graph Genomics |
| protein-language-model | 蛋白质语言模型 | Protein Language Model |

## 质量要求

- ✅ 描述长度在 50-500 字之间
- ✅ 必须包含所有必填字段
- ✅ 分类 ID 和子分类 ID 必须有效
- ✅ `subcategory` 必须属于所选 `category`
- ✅ 算法 ID 在整个仓库范围内必须唯一
- ✅ YAML 格式正确
- ✅ 链接有效且可访问
- ✅ `difficulty` 如填写，必须为 `beginner` / `intermediate` / `advanced`
- ✅ `references[*].type` 如填写，必须为 `tutorial` / `blog` / `video` / `book` / `documentation` / `slides`

## 本地验证

```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
python -m scripts validate
python -m scripts mkdocs
python -m scripts generate
```

## 提交规范

推荐使用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
feat: add new algorithm entry for XXX
fix: correct complexity of YYY
docs: update API reference
```

---

完整贡献指南请参阅 [CONTRIBUTING.md](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/CONTRIBUTING.md)。
