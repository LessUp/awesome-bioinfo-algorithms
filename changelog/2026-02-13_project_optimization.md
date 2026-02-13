# 项目优化 | Project Optimization

**日期**: 2026-02-13
**类型**: 优化 / Optimization

---

## 变更摘要 | Summary

在远程最新代码基础上进行补充优化，包括 Bug 修复、代码质量改进和项目规范化。

## 详细变更 | Changes

### Bug 修复

1. **`scripts/validate.py`** - 修复 `validate_algorithms_file` 和 `validate_categories_file` 中重复读取 YAML 文件的问题，`validate_yaml_file` 现在返回 `(ValidationResult, data)` 元组，避免二次 I/O

### 代码质量改进

2. **`scripts/schema.py`** - 移除 `AlgorithmEntry` 中冗余的 `__eq__` 方法（dataclass 自动生成等价实现），添加 `__hash__` 方法使其可用于集合和字典键
3. **`scripts/data_io.py`** - 将 `format` 参数重命名为 `fmt`，避免遮蔽 Python 内置函数 `format()`
4. **`tests/test_data_io.py`** - 同步更新 `format=` 参数调用为 `fmt=`

### 项目规范化

5. **移除所有测试文件中的 `sys.path` hack** - 涉及 7 个测试文件，通过 `pyproject.toml` + `pip install -e .` 实现正确的包导入
6. **新增 `tests/conftest.py`** - 添加共享 pytest fixtures（`project_root`, `data_dir`, `sample_category`, `sample_algorithm`, `loaded_registry`, `loaded_category_manager`）
7. **`requirements.txt`** - 启用开发依赖（black, flake8, mypy），去掉注释

## 测试结果 | Test Results

全部 28 个测试通过 ✅

```
28 passed in 35.68s
```

## 受影响文件 | Affected Files

- `scripts/validate.py`
- `scripts/schema.py`
- `scripts/data_io.py`
- `tests/test_validate.py`
- `tests/test_schema.py`
- `tests/test_algorithm_registry.py`
- `tests/test_category_manager.py`
- `tests/test_readme_generator.py`
- `tests/test_data_io.py`
- `tests/test_data_completeness.py`
- `tests/conftest.py` (新增)
- `requirements.txt`
