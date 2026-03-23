# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![CI](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Algorithms](https://img.shields.io/badge/algorithms-{{ total_algorithms }}-blue.svg)](#-统计--statistics)
[![Categories](https://img.shields.io/badge/categories-{{ total_categories }}-green.svg)](#-统计--statistics)

> 🧬 生物信息学算法概要汇总 | A curated list of bioinformatics algorithms

本项目收集和整理生物信息学领域常用的算法，提供算法的简要介绍、复杂度分析和相关资源链接，帮助开发者快速了解和选择合适的算法。

This project collects and organizes commonly used algorithms in bioinformatics, providing brief introductions, complexity analysis, and related resource links to help developers quickly understand and choose appropriate algorithms.

The bundled Python commands are intended for repository maintenance workflows and should be run from a repository checkout with the local `data/` and `templates/` directories available.

## 🚀 快速开始 | Quick Start

> 在仓库根目录执行以下命令。 Run the following commands from the repository root.


```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"

# 生成 README | Generate README
python -m scripts generate

# 验证数据 | Validate data
python -m scripts validate

# 查看统计 | Show statistics
python -m scripts stats
```


## 📊 统计 | Statistics

- 📊 算法总数 (Total Algorithms): **{{ total_algorithms }}**
- 📁 分类数量 (Categories): **{{ total_categories }}**
- 🏷️ 标签数量 (Tags): **{{ total_tags }}**

## 📑 目录 | Table of Contents

{{ toc }}

---

{{ content }}

## 🤝 贡献 | Contributing

欢迎贡献！我们接受以下类型的贡献：

We welcome contributions! We accept the following types of contributions:

- 🆕 添加新算法 | Add new algorithms
- 📝 改进现有描述 | Improve existing descriptions
- 🔗 添加参考链接 | Add reference links
- 🐛 修复错误 | Fix errors

请阅读 [贡献指南](CONTRIBUTING.md) 了解详情。

Please read the [Contributing Guide](CONTRIBUTING.md) for details.

## 📚 相关资源 | Related Resources

- [Rosalind](http://rosalind.info/) - 生物信息学算法学习平台
- [NCBI](https://www.ncbi.nlm.nih.gov/) - 美国国家生物技术信息中心
- [EBI](https://www.ebi.ac.uk/) - 欧洲生物信息学研究所
- [Bioconductor](https://www.bioconductor.org/) - R 语言生物信息学工具包
- [Galaxy](https://usegalaxy.org/) - 开放的生物信息学分析平台
- [BioStars](https://www.biostars.org/) - 生物信息学问答社区
- [SEQanswers](http://seqanswers.com/) - 高通量测序社区
- [scverse](https://scverse.org/) - 单细胞分析 Python 生态

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

本项目采用 [CC0 1.0 通用](https://creativecommons.org/publicdomain/zero/1.0/deed.zh) 许可协议，您可以自由地复制、修改、分发和使用本项目。

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). You are free to copy, modify, distribute and use this project.
