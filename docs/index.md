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

[算法列表](https://github.com/LessUp/awesome-bioinfo-algorithms#%E5%BA%8F%E5%88%97%E6%AF%94%E5%AF%B9-sequence-alignment){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[API 文档]({% link API.md %}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 统计

| 指标 | 数值 |
|:--|:--|
| 📊 算法总数 | **54** |
| 📁 分类数量 | **12** |
| 🏷️ 标签数量 | **139** |

---

## 算法分类

| 分类 | 说明 |
|:--|:--|
| **序列比对** | Smith-Waterman、Needleman-Wunsch、BLAST、BWA、Minimap2 等 |
| **序列组装** | De Bruijn Graph、SPAdes、Hifiasm、OLC 等 |
| **变异检测** | GATK HaplotypeCaller、Delly、Manta、FreeBayes 等 |
| **基因表达分析** | DESeq2、STAR、Kallisto 等 |
| **蛋白质结构预测** | AlphaFold、Rosetta、ESMFold 等 |
| **系统发育分析** | Neighbor-Joining、Maximum Likelihood、BEAST 等 |
| **功能注释** | BLAST-based、HMMER、InterProScan 等 |
| **数据压缩** | GZIP for FASTQ、CRAM 等 |
| **单细胞基因组学** | Cell Ranger、Seurat、Scanpy、scVI 等 |
| **宏基因组学** | Kraken2、MetaPhlAn、HUMAnN 等 |
| **表观基因组学** | MACS2、Bismark、ChromHMM 等 |
| **基因预测** | AUGUSTUS、Prodigal、BRAKER 等 |

---

## 快速开始

```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"

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

## 许可证

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) © LessUp
