# 2026-02-13 内容扩充与修复

**日期**: 2026-02-13  
**类型**: 内容扩充 + Bug 修复 / Content Enhancement + Bug Fix

---

## 变更摘要

修复残留问题，补充缺失的子分类算法，扩充算法数据库。

## 详细变更

### Bug 修复

| 文件 | 问题 | 修复 |
|------|------|------|
| `templates/readme_template.md` | Git merge conflict 残留标记 | 移除冲突标记 |
| `templates/readme_template.md` | `YOUR_GITHUB_USERNAME` 占位符 | 替换为实际仓库地址 |
| `scripts/generate_readme.py` | 残留 `sys.path.insert` hack | 移除 hack |
| `tests/test_data_completeness.py` | Hypothesis deadline 超时 | 修复超时问题 |

### 新增算法 (7 个)

| 算法 | 分类 | 说明 |
|------|------|------|
| Clustal Omega | 多序列比对 | 大规模多序列比对工具 |
| MUSCLE | 多序列比对 | 高精度迭代多序列比对 |
| Minimap2 | 双序列比对 | 长读段快速比对 |
| Reference-Guided Assembly | 参考引导组装 | 基于参考序列组装 |
| Delly | 结构变异检测 | SV 检测（缺失、重复、倒位、易位） |
| Manta | 结构变异检测 | 高性能 SV 和 Indel 检测 |
| STAR | 基因表达分析 | RNA-seq 剪接感知比对 |

### 子分类覆盖完善

| 子分类 | 变化 | 新增算法 |
|--------|------|----------|
| `sequence-alignment/multiple` | 0 → 2 | Clustal Omega, MUSCLE |
| `assembly/reference-guided` | 0 → 1 | Reference-Guided Assembly |
| `variant-calling/structural` | 0 → 2 | Delly, Manta |

## 统计变化

| 指标 | 之前 | 之后 |
|------|------|------|
| 算法总数 | 17 | 24 |
| 标签数量 | 51 | 68 |

## 测试结果

```
28 passed in 39.09s
```

## 影响范围

- `templates/readme_template.md`
- `README.md`
- `scripts/generate_readme.py`
- `data/algorithms/sequence-alignment.yaml`
- `data/algorithms/assembly.yaml`
- `data/algorithms/variant-calling.yaml`
- `data/algorithms/expression-analysis.yaml`
- `tests/test_data_completeness.py`
