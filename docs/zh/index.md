---
title: 首页
layout: home
nav_order: 1
description: "Awesome Bioinformatics Algorithms — 生物信息学算法精选集"
permalink: /zh/
---

# Awesome Bioinformatics Algorithms
{: .fs-9 }

🧬 生物信息学算法精选集 — 提供算法简介、复杂度分析和相关资源链接
{: .fs-6 .fw-300 }

本项目收集和整理了生物信息学领域常用的算法，帮助研究人员和开发者快速了解并选择适合其需求的算法。所有内容由社区驱动并开源。
{: .fs-4 .text-grey-dk-100 }

[浏览算法列表](https://github.com/LessUp/awesome-bioinfo-algorithms#sequence-alignment){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[API 文档]({% link zh/api.md %}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[开发指南]({% link zh/development.md %}){: .btn .btn-outline .fs-5 .mb-4 .mb-md-0 }

---

## 📊 统计信息

我们目前维护了 **201 个算法**，涵盖 **16 个分类**，全面覆盖生物信息学各个领域。

| 指标 | 数量 |
|:-----|-----:|
| 算法总数 | **201** |
| 分类数 | **16** |
| 标签数 | **399** |

---

## 🚀 快速开始

### 环境要求

- Python 3.9+
- Git

### 安装步骤

```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"
```

### 核心命令

```bash
# 从数据生成 README
python -m awesome_bioinfo generate

# 验证数据完整性
python -m awesome_bioinfo validate

# 查看统计数据
python -m awesome_bioinfo stats

# 搜索算法
python -m awesome_bioinfo search "alignment"

# 获取算法详情
python -m awesome_bioinfo info smith-waterman
```

---

## 📚 文档导航

| 文档 | 内容说明 |
|:-----|:---------|
| [API 文档]({% link zh/api.md %}) | 公共 API 参考和代码示例 |
| [开发指南]({% link zh/development.md %}) | 项目结构、环境设置和架构设计 |
| [常见问题]({% link zh/faq.md %}) | 常见问题解答和故障排除 |
| [贡献指南]({% link zh/contributing.md %}) | 如何添加算法、分支规范和 PR 流程 |
| [变更日志]({% link zh/changelog.md %}) | 版本发布历史 |
| [安全策略]({% link zh/security.md %}) | 漏洞报告和处理流程 |

---

## 🌐 语言选择

- [English]({% link en/index.md %}) (英文)
- [中文]({% link zh/index.md %}) (当前)

---

## 🏷️ 算法分类

### 序列分析
- **序列比对** — 双序列和多序列比对算法
- **序列组装** — 从头组装和参考引导组装方法
- **变异检测** — SNV 检测和结构变异算法

### 表达与功能
- **基因表达分析** — 表达定量和差异表达分析
- **功能注释** — 基于同源性和结构域的方法

### 组学技术
- **单细胞基因组学** — 数据预处理和细胞聚类
- **宏基因组学** — 物种分类和功能分析
- **表观基因组学** — ChIP-seq 和甲基化分析
- **空间组学** — 空间转录组学和蛋白质组学

### 结构与进化
- **蛋白质结构预测** — 从头预测和基于模板建模
- **系统发育分析** — 距离法和特征法

### 进阶主题
- **群体遗传学** — GWAS、PCA 和选择信号检测
- **图基因组学** — 泛基因组和变异图
- **蛋白质语言模型** — 预训练和功能预测

---

## 🤝 贡献方式

我们欢迎以下类型的贡献：

- 🆕 添加新算法
- 📝 改进现有描述
- 🔗 添加参考链接
- 🐛 修复错误

请阅读我们的 [贡献指南]({% link zh/contributing.md %}) 获取详细说明。

---

## 📖 相关资源

| 资源 | 说明 |
|:-----|:-----|
| [Rosalind](http://rosalind.info/) | 生物信息学算法学习平台 |
| [NCBI](https://www.ncbi.nlm.nih.gov/) | 美国国家生物技术信息中心 |
| [EBI](https://www.ebi.ac.uk/) | 欧洲生物信息学研究所 |
| [Bioconductor](https://www.bioconductor.org/) | R 语言生物信息学工具包 |
| [Galaxy](https://usegalaxy.org/) | 开放的生物信息学分析平台 |
| [BioStars](https://www.biostars.org/) | 生物信息学问答社区 |
| [scverse](https://scverse.org/) | 单细胞分析 Python 生态系统 |

---

## 📄 许可证

本项目采用 [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.zh) 许可协议。
您可以自由地复制、修改、分发和使用本项目，用于任何目的。

---

© 2025-2026 LessUp Community
