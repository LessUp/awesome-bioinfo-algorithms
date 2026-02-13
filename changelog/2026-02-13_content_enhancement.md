# 内容扩充与修复 | Content Enhancement & Fixes

**日期**: 2026-02-13
**类型**: 内容扩充 + Bug 修复 / Content Enhancement + Bug Fix

---

## 变更摘要 | Summary

修复残留问题，补充缺失的子分类算法，扩充算法数据库至 24 个算法。

## 详细变更 | Changes

### Bug 修复

1. **`templates/readme_template.md`** - 修复残留的 git merge conflict 标记（`<<<<<<< HEAD` / `=======` / `>>>>>>>` ）
2. **`templates/readme_template.md`** + **`README.md`** - 修复 `YOUR_GITHUB_USERNAME` 占位符，替换为 `LessUp/awesome-bioinfo-algorithms`
3. **`scripts/generate_readme.py`** - 移除残留的 `sys.path.insert` hack
4. **`tests/test_data_completeness.py`** - 修复 `test_property_2_category_coverage` Hypothesis deadline 超时

### 新增算法（7 个）

5. **Clustal Omega** (`sequence-alignment/multiple`) - 大规模多序列比对工具
6. **MUSCLE** (`sequence-alignment/multiple`) - 高精度迭代多序列比对算法
7. **Minimap2** (`sequence-alignment/pairwise`) - 长读段和短读段通用快速比对
8. **Reference-Guided Assembly** (`assembly/reference-guided`) - 基于参考序列的组装方法
9. **Delly** (`variant-calling/structural`) - 结构变异检测（缺失、重复、倒位、易位）
10. **Manta** (`variant-calling/structural`) - 高性能结构变异和大型 Indel 检测
11. **STAR** (`expression-analysis`) - RNA-seq 剪接感知比对工具

### 子分类覆盖完善

- `sequence-alignment/multiple` — 从 0 → 2 个算法（Clustal Omega, MUSCLE）
- `assembly/reference-guided` — 从 0 → 1 个算法（Reference-Guided Assembly）
- `variant-calling/structural` — 从 0 → 2 个算法（Delly, Manta）

## 统计变化 | Statistics

| 指标 | 之前 | 之后 |
|------|------|------|
| 算法总数 | 17 | 24 |
| 标签数量 | 51 | 68 |

## 测试结果 | Test Results

全部 28 个测试通过 ✅

```
28 passed in 39.09s
```

## 受影响文件 | Affected Files

- `templates/readme_template.md`
- `README.md`（重新生成）
- `scripts/generate_readme.py`
- `data/algorithms/sequence-alignment.yaml`（+3 算法）
- `data/algorithms/assembly.yaml`（+1 算法）
- `data/algorithms/variant-calling.yaml`（+2 算法）
- `data/algorithms/expression-analysis.yaml`（+1 算法）
- `tests/test_data_completeness.py`
