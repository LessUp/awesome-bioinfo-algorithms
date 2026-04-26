# Changelog / 变更日志

All notable changes to this project will be documented in this file.  
本文件记录项目的所有重要变更。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

---

## [1.0.1] - 2026-02-13

### Fixed / 修复

- Fixed `requirements.txt` to align with `pyproject.toml` (replaced `black`/`flake8` with `ruff`) / 修复 `requirements.txt` 与 `pyproject.toml` 一致性
- Fixed incorrect API signatures in documentation / 修复文档中的 API 签名错误
- Fixed incomplete category list in FAQ (4→8 categories) / 修复 FAQ 分类列表不完整
- Fixed `CHANGELOG.md` section order and incomplete lists / 修复变更日志章节顺序
- Removed irrelevant `YOUR_GITHUB_USERNAME` placeholder from docs / 清除文档占位符
- Fixed `pyproject.toml` Development Status from Beta to Production/Stable / 修复开发状态标识
- Updated `.pre-commit-config.yaml` hook versions / 更新 pre-commit 钩子版本

### Added / 新增

- Added `SECURITY.md` contact email / 添加安全政策联系邮箱
- Added Pull Request template / 添加 PR 模板
- Added Bug Report issue template / 添加 Bug 报告模板

### Removed / 移除

- Removed unnecessary `.gitkeep` files / 移除不必要的占位文件

---

## [1.0.0] - 2026-01-07

### Added / 新增

- Initial release with core functionality / 初始版本，包含核心功能
- Algorithm registry, category manager, validation system / 算法注册表、分类管理器、数据验证
- README auto-generation from YAML data / README 自动生成
- Property-based testing with Hypothesis / 属性测试
- GitHub Actions CI/CD pipeline / CI/CD 流水线
- Multi-Python version testing (3.9, 3.10, 3.11, 3.12) / 多版本测试
- Code quality tools (ruff, mypy), pre-commit hooks / 代码质量工具、Pre-commit 配置
- Community templates, Code of Conduct, Security Policy / 社区模板、行为准则、安全政策
- 195 algorithms across 16 categories / 16 个分类共 195 条算法
