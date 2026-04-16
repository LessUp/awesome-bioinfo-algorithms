# 2026-02-13 项目优化

**日期**: 2026-02-13  
**类型**: 优化 / Optimization

---

## 变更摘要

代码质量改进和项目规范化。

## 详细变更

### Bug 修复

| 文件 | 问题 | 修复 |
|------|------|------|
| `scripts/validate.py` | 重复读取 YAML 文件 | 返回 `(ValidationResult, data)` 元组避免二次 I/O |

### 代码质量改进

| 文件 | 问题 | 修复 |
|------|------|------|
| `scripts/schema.py` | 冗余 `__eq__` 方法 | 移除（dataclass 自动生成） |
| `scripts/schema.py` | 不可哈希 | 添加 `__hash__` 方法 |
| `scripts/data_io.py` | 遮蔽内置函数 `format()` | 参数重命名为 `fmt` |
| `tests/test_data_io.py` | 参数名不匹配 | 同步更新为 `fmt=` |

### 项目规范化

| 变更项 | 说明 |
|--------|------|
| 移除 `sys.path` hack | 7 个测试文件，改用 `pip install -e .` |
| 新增 `conftest.py` | 添加共享 pytest fixtures |
| 更新 `requirements.txt` | 启用开发依赖 |

### 新增 Fixtures

```python
# tests/conftest.py
- project_root
- data_dir
- sample_category
- sample_algorithm
- loaded_registry
- loaded_category_manager
```

## 测试结果

```
28 passed in 35.68s
```

## 影响范围

- `scripts/validate.py`
- `scripts/schema.py`
- `scripts/data_io.py`
- `tests/` (8 个文件)
- `requirements.txt`
