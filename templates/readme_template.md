<h1 align="center">Awesome Bioinformatics Algorithms</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml"><img src="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/"><img src="https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github" alt="Documentation"></a>
  <a href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Algorithms-{{ total_algorithms }}-blue.svg" alt="Algorithms">
  <img src="https://img.shields.io/badge/Categories-{{ total_categories }}-green.svg" alt="Categories">
  <img src="https://img.shields.io/badge/Tags-{{ total_tags }}-orange.svg" alt="Tags">
</p>

<p align="center">
  <b>🧬 生物信息学算法概要汇总</b><br>
  <b>A curated collection of bioinformatics algorithms</b>
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> | 
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/">Documentation Site</a> | 
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

## 📖 About | 关于

> **Mission**: To create the most comprehensive, well-organized, and accessible collection of bioinformatics algorithms for researchers, students, and practitioners worldwide.

**中文**: 本项目收集和整理生物信息学领域常用的算法，提供算法的简要介绍、时间/空间复杂度分析、相关论文和实现链接，帮助研究人员和开发者快速了解和选择合适的算法。

**English**: This project collects and organizes commonly used algorithms in bioinformatics, providing brief introductions, time/space complexity analysis, and links to related papers and implementations. It helps researchers and developers quickly understand and choose appropriate algorithms.

---

## 🚀 Quick Start | 快速开始

> **Note**: Commands should be run from the repository root. | 以下命令需在仓库根目录执行。

```bash
# Clone repository | 克隆仓库
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Install dependencies | 安装依赖
pip install -e ".[dev]"

# Validate data | 验证数据
python -m scripts validate

# Generate README | 生成 README
python -m scripts generate

# Show statistics | 查看统计
python -m scripts stats
```

---

## 📊 Statistics | 统计数据

| Metric | Value | 指标 | 数值 |
|:-------|------:|:-----|-----:|
| Total Algorithms | **{{ total_algorithms }}** | 算法总数 | **{{ total_algorithms }}** |
| Categories | **{{ total_categories }}** | 分类数 | **{{ total_categories }}** |
| Unique Tags | **{{ total_tags }}** | 唯一标签数 | **{{ total_tags }}** |

---

## 📑 Table of Contents | 目录

{{ toc }}

---

## 🔬 Algorithm Categories | 算法分类

{{ content }}

---

## 💡 Key Features | 主要特性

- 📚 **Comprehensive Coverage** — 201 algorithms across 16 categories / 16个分类201个算法
- 📖 **Bilingual Documentation** — Chinese and English support / 中英文双语支持
- 🔍 **Powerful Search** — CLI and programmatic search capabilities / 强大的搜索功能
- ✅ **Data Validation** — Automated validation for data integrity / 自动化数据验证
- 🔄 **Auto-Generated** — README and docs generated from structured data / 从结构化数据自动生成
- 🧪 **Well Tested** — Comprehensive test suite with pytest / 全面的测试套件
- 🌍 **Open Source** — CC0 1.0 (Public Domain) license / CC0 1.0 开源许可

---

## 🛠️ CLI Commands | 命令行工具

```bash
# Search for algorithms | 搜索算法
python -m scripts search "alignment"

# Get algorithm details | 获取算法详情
python -m scripts info smith-waterman

# Compare two algorithms | 比较两个算法
python -m scripts compare smith-waterman needleman-wunsch

# Export data | 导出数据
python -m scripts export --format json > algorithms.json

# Generate MkDocs | 生成 MkDocs 文档
python -m scripts mkdocs
```

---

## 📚 Resources | 相关资源

### Learning Platforms | 学习平台
- [Rosalind](http://rosalind.info/) — Bioinformatics algorithm learning / 生物信息学算法学习
- [NCBI](https://www.ncbi.nlm.nih.gov/) — National Center for Biotechnology / 美国生物技术信息中心
- [EBI](https://www.ebi.ac.uk/) — European Bioinformatics Institute / 欧洲生物信息学研究所

### Tools & Communities | 工具和社区
- [Bioconductor](https://www.bioconductor.org/) — R bioinformatics toolkit / R 生物信息学工具包
- [Galaxy](https://usegalaxy.org/) — Open analysis platform / 开放分析平台
- [BioStars](https://www.biostars.org/) — Bioinformatics Q&A / 生物信息学问答
- [scverse](https://scverse.org/) — Single-cell Python ecosystem / 单细胞 Python 生态

---

## 🤝 Contributing | 贡献指南

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

我们欢迎各种形式的贡献！请阅读我们的 [贡献指南](CONTRIBUTING.md) 了解详情。

### Contribution Types | 贡献类型

- 🆕 **Add new algorithms** | 添加新算法
- 📝 **Improve descriptions** | 改进描述
- 🔗 **Add references** | 添加参考链接
- 🐛 **Report and fix bugs** | 报告和修复 Bug
- 📚 **Improve documentation** | 改进文档

---

## 📄 License | 许可证

<p align="center">
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" alt="CC0">
  </a>
</p>

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain).

本项目采用 [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)（公共领域）许可协议。

You are free to:
- ✅ Copy, modify, distribute
- ✅ Use for commercial purposes
- ✅ No attribution required

您可以自由：
- ✅ 复制、修改、分发
- ✅ 用于商业目的
- ✅ 无需署名

---

<p align="center">
  <b>Made with ❤️ by the community</b><br>
  © 2025-2026 <a href="https://github.com/LessUp">LessUp</a> Community
</p>
