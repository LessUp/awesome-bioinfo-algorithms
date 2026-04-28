# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![CI](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml)
[![Pages](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/pages.yml/badge.svg)](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/pages.yml)
[![Docs](https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github)](https://lessup.github.io/awesome-bioinfo-algorithms/)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

**[English](README.md)** | 简体中文

> 简体中文入口页。完整算法列表、最新统计和自动生成目录统一维护在 [README.md](README.md)。

## 说明

本仓库内置的 Python 脚本主要用于仓库维护工作，例如数据校验、README 生成和统计汇总；它们默认依赖当前仓库中的 `data/` 与 `templates/` 目录运行。

为了避免 `README.md` 与 `README.zh-CN.md` 长期重复维护导致内容漂移，中文 README 现在保留为轻量入口页：

- 完整算法目录与统计：见 [README.md](README.md)
- GitHub Pages 文档站：见 <https://lessup.github.io/awesome-bioinfo-algorithms/>
- 贡献指南：见 [CONTRIBUTING.md](CONTRIBUTING.md)

主 README 本身已经采用中英双语内容，后续新增算法、分类统计和目录结构会优先在那里自动更新。

## 常用命令

```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"

# 以下命令需要在仓库根目录执行

# 校验数据
python -m awesome_bioinfo validate

# 生成主 README
python -m awesome_bioinfo generate

# 查看统计
python -m awesome_bioinfo stats
```

## 文档入口

- 项目首页：<https://lessup.github.io/awesome-bioinfo-algorithms/>
- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
- 变更日志：[CHANGELOG.md](CHANGELOG.md)

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
