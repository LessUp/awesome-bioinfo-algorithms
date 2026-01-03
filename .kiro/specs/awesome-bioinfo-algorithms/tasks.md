# Implementation Plan: Awesome Bioinformatics Algorithms

## Overview

本实现计划将设计文档转化为可执行的编码任务。项目使用 Python 实现，采用 YAML 存储数据，自动生成 awesome-list 风格的 README 文档。

## Tasks

- [x] 1. 项目初始化和数据模型定义
  - [x] 1.1 创建项目目录结构和基础配置文件
    - 创建 `data/`, `scripts/`, `templates/` 目录
    - 创建 `pyproject.toml` 或 `requirements.txt`
    - 添加 PyYAML, Hypothesis 依赖
    - _Requirements: 6.1_

  - [x] 1.2 实现数据模型类 (schema.py)
    - 实现 `Category` 和 `AlgorithmEntry` dataclass
    - 定义必填和可选字段
    - _Requirements: 1.3, 2.1, 2.2_

  - [x] 1.3 编写数据模型属性测试
    - **Property 4: Optional Fields Storage**
    - **Validates: Requirements 2.2, 2.4**

- [x] 2. 数据验证器实现
  - [x] 2.1 实现 Validator 类 (validate.py)
    - 实现 `validate_algorithm()` 方法
    - 实现 `validate_category()` 方法
    - 实现必填字段检查
    - 实现描述长度验证 (50-200字)
    - _Requirements: 2.1, 4.2, 6.2_

  - [x] 2.2 编写验证器属性测试 - 必填字段
    - **Property 3: Required Fields Validation**
    - **Validates: Requirements 1.4, 2.1, 4.2**

  - [x] 2.3 编写验证器属性测试 - 错误信息
    - **Property 7: Validation Error Specificity**
    - **Validates: Requirements 4.4, 6.3**

  - [x] 2.4 编写验证器属性测试 - 数据格式
    - **Property 10: Data Format Validation**
    - **Validates: Requirements 6.2**

- [x] 3. Checkpoint - 验证数据模型和验证器
  - 确保所有测试通过，如有问题请询问用户

- [x] 4. 分类管理器实现
  - [x] 4.1 实现 CategoryManager 类
    - 实现 `load_categories()` 从 YAML 加载分类
    - 实现 `get_category()` 获取单个分类
    - 实现 `list_all_categories()` 列出所有分类
    - _Requirements: 1.1, 1.3_

  - [x] 4.2 编写分类管理器属性测试
    - **Property 2: Subcategory Hierarchy Preservation**
    - **Validates: Requirements 1.3**

- [x] 5. 算法注册表实现
  - [x] 5.1 实现 AlgorithmRegistry 类
    - 实现 `load_all()` 加载所有算法
    - 实现 `get_by_category()` 按分类获取
    - 实现 `get_by_tag()` 按标签获取
    - 实现 `search()` 搜索功能
    - 实现 `get_statistics()` 统计信息
    - _Requirements: 1.2, 5.1, 5.2, 5.3_

  - [x] 5.2 编写注册表属性测试 - 分类计数
    - **Property 1: Category Algorithm Count Accuracy**
    - **Validates: Requirements 1.2, 3.4**

  - [x] 5.3 编写注册表属性测试 - 搜索功能
    - **Property 8: Search Result Correctness**
    - **Validates: Requirements 5.1, 5.2, 5.3**

- [x] 6. Checkpoint - 验证核心功能
  - 确保所有测试通过，如有问题请询问用户

- [x] 7. README 生成器实现
  - [x] 7.1 创建 README 模板文件
    - 创建 `templates/readme_template.md`
    - 包含统计信息、目录、内容占位符
    - _Requirements: 3.3, 3.4_

  - [x] 7.2 实现 ReadmeGenerator 类
    - 实现 `generate()` 主生成方法
    - 实现 `generate_toc()` 目录生成
    - 实现 `generate_category_section()` 分类内容
    - 实现 `generate_algorithm_entry()` 算法条目格式化
    - 实现 `generate_statistics()` 统计信息
    - _Requirements: 3.1, 3.2, 3.4, 5.4_

  - [x] 7.3 编写生成器属性测试 - 目录完整性
    - **Property 6: Table of Contents Completeness**
    - **Validates: Requirements 3.1**

  - [x] 7.4 编写生成器属性测试 - Markdown 格式
    - **Property 5: Markdown Output Consistency**
    - **Validates: Requirements 2.3**

  - [x] 7.5 编写生成器属性测试 - 锚点链接
    - **Property 9: Anchor Link Format Validity**
    - **Validates: Requirements 5.4**

- [x] 8. 数据导入导出功能
  - [x] 8.1 实现数据导入导出方法
    - 实现 `export_data()` 导出到 YAML/JSON
    - 实现 `import_data()` 从 YAML/JSON 导入
    - _Requirements: 6.4_

  - [x] 8.2 编写导入导出属性测试
    - **Property 11: Data Import/Export Round-Trip**
    - **Validates: Requirements 6.4**

- [x] 9. Checkpoint - 验证生成器和导入导出
  - 确保所有测试通过，如有问题请询问用户

- [x] 10. 示例数据和模板创建
  - [x] 10.1 创建分类定义文件
    - 创建 `data/categories.yaml`
    - 包含所有主要分类和子分类
    - _Requirements: 1.1_

  - [x] 10.2 创建示例算法数据
    - 创建 `data/algorithms/sequence-alignment.yaml`
    - 添加 2-3 个示例算法条目
    - _Requirements: 2.1, 2.2_

  - [x] 10.3 创建算法提交模板
    - 创建 `templates/algorithm_template.yaml`
    - _Requirements: 4.1_

- [x] 11. 贡献指南和 CI 配置
  - [x] 11.1 创建贡献指南文档
    - 创建 `CONTRIBUTING.md`
    - 说明如何提交新算法
    - _Requirements: 4.3_

  - [x] 11.2 创建 GitHub Issue 模板
    - 创建 `.github/ISSUE_TEMPLATE/new_algorithm.md`
    - _Requirements: 4.1_

  - [x] 11.3 创建 CI 验证工作流
    - 创建 `.github/workflows/validate.yml`
    - 配置自动验证和 README 生成
    - _Requirements: 3.2_

- [x] 12. 主脚本和集成
  - [x] 12.1 创建主生成脚本
    - 创建 `scripts/generate_readme.py`
    - 整合所有组件生成 README
    - _Requirements: 3.1, 3.2_

  - [x] 12.2 生成初始 README.md
    - 运行生成脚本创建 README
    - _Requirements: 3.1, 3.3, 3.4_

- [x] 13. Final Checkpoint - 完整功能验证
  - 确保所有测试通过
  - 验证 README 生成正确
  - 如有问题请询问用户

## Notes

- 所有任务都是必需的，包括完整的属性测试覆盖
- 每个任务都引用了具体的需求以便追溯
- Checkpoint 任务用于阶段性验证
- 属性测试使用 Hypothesis 库，每个测试至少运行 100 次迭代
