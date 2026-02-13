# Changelog / 变更日志

All notable changes to this project will be documented in this file.

本文件记录项目的所有重要变更。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] / 未发布

### Planned / 计划中

- Interactive web interface / 交互式 Web 界面
- Algorithm comparison tools / 算法比较工具

---

## [1.0.1] - 2026-02-13

### Fixed / 修复

- Fixed `requirements.txt` to align with `pyproject.toml` (replaced `black`/`flake8` with `ruff`) / 修复 `requirements.txt` 与 `pyproject.toml` 一致性（用 `ruff` 替换 `black`/`flake8`）
- Fixed incorrect API signatures in `docs/API.md` for `DataIO.export_data` and `ReadmeGenerator` constructor / 修复 `docs/API.md` 中 `DataIO.export_data` 和 `ReadmeGenerator` 构造函数签名错误
- Fixed incomplete category list in `docs/FAQ.md` (4→8 categories) / 修复 `docs/FAQ.md` 中分类列表不完整（4→8）
- Fixed `CHANGELOG.md` section order and incomplete category/algorithm lists / 修复 `CHANGELOG.md` 章节顺序及不完整的分类/算法列表
- Removed irrelevant `YOUR_GITHUB_USERNAME` placeholder from `docs/DEVELOPMENT.md` and `docs/FAQ.md` / 清除文档中无关的占位符
- Fixed `pyproject.toml` Development Status from Beta to Production/Stable / 修复开发状态标识
- Updated `.pre-commit-config.yaml` hook versions / 更新 pre-commit 钩子版本

### Added / 新增

- Added `SECURITY.md` contact email / 添加安全政策联系邮箱
- Added Pull Request template / 添加 PR 模板
- Added Bug Report issue template / 添加 Bug 报告 issue 模板
- Added `changelog/` directory for tracking modifications / 添加变更日志目录

### Removed / 移除

- Removed unnecessary `.gitkeep` files from `data/algorithms/` and `templates/` / 移除不必要的 `.gitkeep` 文件

---

## [1.0.0] - 2026-01-07

### Added / 新增

- Initial release with core functionality / 初始版本，包含核心功能
- Algorithm registry for managing algorithm entries / 算法注册表，用于管理算法条目
- Category manager for organizing algorithms / 分类管理器，用于组织算法
- Validation system for data integrity / 数据完整性验证系统
- README auto-generation from YAML data / 从 YAML 数据自动生成 README
- Property-based testing with Hypothesis / 使用 Hypothesis 进行属性测试
- GitHub Actions CI/CD pipeline / GitHub Actions CI/CD 流水线
- Multi-Python version testing (3.9, 3.10, 3.11, 3.12) / 多 Python 版本测试
- Code quality tools (ruff, mypy) / 代码质量工具
- Pre-commit hooks configuration / Pre-commit 钩子配置
- Community templates (PR, Issues) / 社区模板
- Code of Conduct / 行为准则
- Security Policy / 安全政策
- API documentation / API 文档
- FAQ documentation / FAQ 文档

### Algorithm Categories / 算法分类

- Sequence Alignment / 序列比对
- Sequence Assembly / 序列组装
- Variant Calling / 变异检测
- Gene Expression Analysis / 基因表达分析
- Protein Structure Prediction / 蛋白质结构预测
- Phylogenetics / 系统发育分析
- Functional Annotation / 功能注释
- Data Compression / 数据压缩

### Algorithms / 算法 (24)

- Smith-Waterman, Needleman-Wunsch, Clustal Omega, MUSCLE, Minimap2, BWT Alignment
- De Bruijn Graph Assembly, Reference-Guided Assembly, Overlap-Layout-Consensus (OLC)
- GATK HaplotypeCaller, Delly, Manta, FreeBayes
- DESeq2, STAR, Kallisto
- AlphaFold, Rosetta
- Neighbor-Joining, Maximum Likelihood Phylogeny
- BLAST-based Annotation, HMMER
- GZIP for FASTQ, CRAM
