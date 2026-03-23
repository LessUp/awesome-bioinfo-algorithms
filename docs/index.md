---
title: 首页
layout: home
nav_order: 1
description: "Awesome Bioinformatics Algorithms — 生物信息学算法概要汇总"
---

# Awesome Bioinformatics Algorithms
{: .fs-9 }

🧬 生物信息学算法概要汇总 — 收集和整理常用的生物信息学算法，提供简要介绍、复杂度分析和相关资源链接。
{: .fs-6 .fw-300 }

完整统计、算法目录和最新 README 内容以仓库根目录自动生成的 `README.md` 为准；当前页面只保留导航入口，避免与自动生成内容长期漂移。
{: .fs-4 .text-grey-dk-100 }

[算法列表](https://github.com/LessUp/awesome-bioinfo-algorithms#%E5%BA%8F%E5%88%97%E6%AF%94%E5%AF%B9-sequence-alignment){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[API 文档]({% link API.md %}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[开发指南]({% link DEVELOPMENT.md %}){: .btn .btn-outline .fs-5 .mb-4 .mb-md-0 }

---

## 统计与算法目录

- 最新统计请查看仓库根目录的 [`README.md`](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/README.md)
- 最新分类与算法目录也以该 README 为准
- 若您要贡献或校验数据，请优先参考 [开发指南]({% link DEVELOPMENT.md %}) 与 [贡献指南]({% link contributing.md %})

---

## 快速开始

```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"

# 以下命令需在仓库根目录执行

# 生成 README
python -m scripts generate

# 验证数据
python -m scripts validate

# 查看统计
python -m scripts stats
```

---

## 文档

| 页面 | 内容 |
|:--|:--|
| [API 文档]({% link API.md %}) | 公共 API 接口说明 |
| [开发指南]({% link DEVELOPMENT.md %}) | 项目结构、环境设置与核心组件 |
| [常见问题]({% link FAQ.md %}) | 使用与贡献常见问题解答 |
| [贡献指南]({% link contributing.md %}) | 如何添加新算法、分支规范与提交流程 |
| [变更日志]({% link changelog.md %}) | 版本发布历史 |
| [安全策略]({% link security.md %}) | 漏洞报告与处理流程 |

---

## 相关资源

| 资源 | 说明 |
|:--|:--|
| [Rosalind](http://rosalind.info/) | 生物信息学算法学习平台 |
| [NCBI](https://www.ncbi.nlm.nih.gov/) | 美国国家生物技术信息中心 |
| [EBI](https://www.ebi.ac.uk/) | 欧洲生物信息学研究所 |
| [Bioconductor](https://www.bioconductor.org/) | R 生物信息学工具包 |
| [Galaxy](https://usegalaxy.org/) | 开放生物信息学分析平台 |
| [scverse](https://scverse.org/) | 单细胞 Python 生态系统 |

---

## 许可证

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) © 2025-2026 LessUp
