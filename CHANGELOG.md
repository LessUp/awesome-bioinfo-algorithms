# Changelog / 变更日志

All notable changes to this project will be documented in this file.  
本文件记录项目的所有重要变更。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] / 未发布

### Planned / 计划中

- Interactive web interface / 交互式 Web 界面
- Algorithm comparison visualization / 算法比较可视化
- RESTful API / RESTful API

---

## [2.0.0] - TBD / 待定

### Major Changes / 重大变更

- **Documentation Refactor** — Complete bilingual documentation system / 完整的双语文档系统
  - Reorganized docs into `en/` and `zh/` directories / 将文档重组为 `en/` 和 `zh/` 目录
  - Added comprehensive API documentation / 添加全面的 API 文档
  - Added detailed development guides / 添加详细的开发指南
  - Standardized changelog format / 标准化变更日志格式

---

## [1.0.2] - 2026-04-16

### Fixed / 修复

- Fixed Python 3.9 compatibility by replacing `X | Y` union syntax with `Optional[X]` / 修复 Python 3.9 兼容性，替换联合类型语法
- Fixed search inconsistency by adding `purpose` field to `AlgorithmRegistry.search()` / 修复搜索不一致，添加 `purpose` 字段到搜索逻辑
- Fixed duplicated `difficulty_labels` mapping across 4 files by consolidating into `DIFFICULTY_LABELS` constant / 合并重复的难度标签映射
- Fixed incorrect `test_generate_mkdocs_creates_expected_pages` test expectations / 修复 MkDocs 测试断言错误
- Fixed flaky hypothesis test by adding `HealthCheck.too_slow` suppression / 修复不稳定的属性测试
- Fixed mypy type stub issue for PyYAML `**kwargs` / 修复 PyYAML 类型检查问题
- Removed unused variable `cat_name_en` in `generate_mkdocs.py` / 移除未使用变量

### Added / 新增

- Added `DIFFICULTY_LABELS` constant to `schema.py` for centralized label management / 添加统一的难度标签常量
- Added docstring note documenting `validate_categories_file()` state mutation / 添加验证器状态变更文档说明

### Changed / 变更

- Simplified `search_algorithms()` to use `registry.search()` method / 简化搜索函数实现

### Refactored / 重构

- Code review: consolidated constants, improved Python 3.9 compatibility, enhanced search consistency / 代码审查：合并常量，改进兼容性，增强搜索一致性

**See detailed changelog:** / **详细变更日志：**
- [zh/代码审查](changelog/zh/2026-04-16_code-review.md)
- [en/Code Review](changelog/en/2026-04-16_code-review.md)

---

## [1.0.1] - 2026-02-13

### Fixed / 修复

- Fixed `requirements.txt` to align with `pyproject.toml` (replaced `black`/`flake8` with `ruff`) / 修复 `requirements.txt` 与 `pyproject.toml` 一致性
- Fixed incorrect API signatures in `docs/API.md` / 修复 API 文档签名错误
- Fixed incomplete category list in `docs/FAQ.md` (4→8 categories) / 修复 FAQ 分类列表不完整
- Fixed `CHANGELOG.md` section order and incomplete lists / 修复变更日志章节顺序
- Removed irrelevant `YOUR_GITHUB_USERNAME` placeholder from docs / 清除文档占位符
- Fixed `pyproject.toml` Development Status from Beta to Production/Stable / 修复开发状态标识
- Updated `.pre-commit-config.yaml` hook versions / 更新 pre-commit 钩子版本

### Added / 新增

- Added `SECURITY.md` contact email / 添加安全政策联系邮箱
- Added Pull Request template / 添加 PR 模板
- Added Bug Report issue template / 添加 Bug 报告模板
- Added `changelog/` directory for detailed change tracking / 添加变更日志目录

### Removed / 移除

- Removed unnecessary `.gitkeep` files / 移除不必要的占位文件

---

## [1.0.0] - 2026-01-07

### Added / 新增

- Initial release with core functionality / 初始版本，包含核心功能
- Algorithm registry for managing algorithm entries / 算法注册表
- Category manager for organizing algorithms / 分类管理器
- Validation system for data integrity / 数据验证系统
- README auto-generation from YAML data / README 自动生成
- Property-based testing with Hypothesis / 属性测试
- GitHub Actions CI/CD pipeline / CI/CD 流水线
- Multi-Python version testing (3.9, 3.10, 3.11, 3.12) / 多版本测试
- Code quality tools (ruff, mypy) / 代码质量工具
- Pre-commit hooks configuration / Pre-commit 配置
- Community templates (PR, Issues) / 社区模板
- Code of Conduct / 行为准则
- Security Policy / 安全政策
- API documentation / API 文档
- FAQ documentation / FAQ 文档

### Algorithm Categories / 算法分类 (16)

| Category | 中文名 | Algorithms |
|:---------|:-------|:----------:|
| Sequence Alignment | 序列比对 | 19 |
| Sequence Assembly | 序列组装 | 14 |
| Variant Calling | 变异检测 | 14 |
| Gene Expression Analysis | 基因表达分析 | 12 |
| Protein Structure Prediction | 蛋白质结构预测 | 14 |
| Phylogenetics | 系统发育分析 | 12 |
| Functional Annotation | 功能注释 | 12 |
| Data Compression | 数据压缩 | 10 |
| Single-Cell Genomics | 单细胞基因组学 | 15 |
| Metagenomics | 宏基因组学 | 14 |
| Epigenomics | 表观基因组学 | 12 |
| Gene Prediction | 基因预测 | 12 |
| Population Genetics | 群体遗传学 | 12 |
| Spatial Omics | 空间组学 | 10 |
| Graph Genomics | 图基因组学 | 9 |
| Protein Language Model | 蛋白质语言模型 | 10 |

### Statistics / 统计

- **Total Algorithms**: 195 / 算法总数：195
- **Total Categories**: 16 / 分类数：16
- **Total Tags**: 392 / 标签数：392

---

## Historical Changes / 历史变更

Detailed changelogs are available in the `changelog/` directory:  
详细变更日志可在 `changelog/` 目录中找到：

| Date | File | Description |
|:-----|:-----|:------------|
| 2026-03-10 | [/workflow-deep-standardization](changelog/archive/2026-03-10_workflow-deep-standardization.md) | CI/CD 工作流标准化 |
| 2026-03-10 | [/pages-optimization](changelog/archive/2026-03-10_pages-optimization.md) | GitHub Pages 优化 |
| 2026-02-13 | [/content-enhancement](changelog/archive/2026-02-13_content_enhancement.md) | 内容扩充与修复 |
| 2026-02-13 | [/project-optimization](changelog/archive/2026-02-13_project_optimization.md) | 项目优化 |
| 2026-01-08 | [/maintenance](changelog/archive/2026-01-08-maintenance.md) | 项目检查与修复 |

---

## Version History / 版本历史

```
2.0.0 - TBD          - Documentation Refactor / 文档重构
1.0.2 - 2026-04-16   - Code review and bug fixes / 代码审查和 Bug 修复
1.0.1 - 2026-02-13   - Documentation fixes and project standardization / 文档修复和项目标准化
1.0.0 - 2026-01-07   - Initial release / 初始版本
```
