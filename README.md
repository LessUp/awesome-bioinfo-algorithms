<h1 align="center">Awesome Bioinformatics Algorithms</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml"><img src="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/"><img src="https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github" alt="Documentation"></a>
  <a href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg" alt="License"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/blob/main/CITATION.cff"><img src="https://img.shields.io/badge/Cite%20Me-APA-blue" alt="Citation"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Algorithms-201-blue.svg" alt="Algorithms">
  <img src="https://img.shields.io/badge/Categories-16-green.svg" alt="Categories">
  <img src="https://img.shields.io/badge/Tags-399-orange.svg" alt="Tags">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python">
</p>

<p align="center">
  <b>🧬 生物信息学算法概要汇总</b><br>
  <b>A curated collection of bioinformatics algorithms with complexity analysis</b>
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> • 
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/">📖 Documentation Site</a> • 
  <a href="CONTRIBUTING.md">🤝 Contributing</a> • 
  <a href="#-citation--引用">📚 Citation</a>
</p>

---

## ✨ Highlights | 项目亮点

<table>
<tr>
<td width="50%">

**🎯 For Researchers**
- 201+ curated algorithms
- Time/space complexity analysis
- Paper and implementation links
- Multi-language support

</td>
<td width="50%">

**💻 For Developers**
- CLI toolkit for data management
- Automated validation & generation
- Structured YAML data format
- Extensive test coverage

</td>
</tr>
</table>

---

## 📖 About | 关于

> **Mission**: To create the most comprehensive, well-organized, and accessible collection of bioinformatics algorithms for researchers, students, and practitioners worldwide.

**中文**: 本项目收集和整理生物信息学领域常用的 **201** 个算法，涵盖 **16** 个分类，提供算法的简要介绍、时间/空间复杂度分析、相关论文和实现链接，帮助研究人员和开发者快速了解和选择合适的算法。

**English**: This project collects and organizes **201** commonly used algorithms in bioinformatics across **16** categories, providing brief introductions, time/space complexity analysis, and links to related papers and implementations. It helps researchers and developers quickly understand and choose appropriate algorithms.

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
python -m awesome_bioinfo validate

# Show statistics | 查看统计
python -m awesome_bioinfo stats
```

---

## 📊 Statistics | 统计数据

| Metric | Value | 指标 | 数值 |
|:-------|------:|:-----|-----:|
| Total Algorithms | **201** | 算法总数 | **201** |
| Categories | **16** | 分类数 | **16** |
| Unique Tags | **399** | 唯一标签数 | **399** |

---

## 📑 Table of Contents | 目录

- [序列比对 (Sequence Alignment)](#序列比对-sequence-alignment)
  - [双序列比对 (Pairwise Alignment)](#双序列比对-pairwise-alignment)
  - [多序列比对 (Multiple Sequence Alignment)](#多序列比对-multiple-sequence-alignment)
- [序列组装 (Sequence Assembly)](#序列组装-sequence-assembly)
  - [从头组装 (De Novo Assembly)](#从头组装-de-novo-assembly)
  - [参考引导组装 (Reference-Guided Assembly)](#参考引导组装-reference-guided-assembly)
- [变异检测 (Variant Calling)](#变异检测-variant-calling)
  - [单核苷酸变异 (SNV Detection)](#单核苷酸变异-snv-detection)
  - [结构变异 (Structural Variants)](#结构变异-structural-variants)
- [基因表达分析 (Gene Expression Analysis)](#基因表达分析-gene-expression-analysis)
  - [表达定量 (Expression Quantification)](#表达定量-expression-quantification)
  - [差异表达 (Differential Expression)](#差异表达-differential-expression)
- [蛋白质结构预测 (Protein Structure Prediction)](#蛋白质结构预测-protein-structure-prediction)
  - [从头预测 (Ab Initio Prediction)](#从头预测-ab-initio-prediction)
  - [模板方法 (Template-Based Modeling)](#模板方法-template-based-modeling)
- [系统发育分析 (Phylogenetics)](#系统发育分析-phylogenetics)
  - [距离法 (Distance Methods)](#距离法-distance-methods)
  - [特征法 (Character-Based Methods)](#特征法-character-based-methods)
- [功能注释 (Functional Annotation)](#功能注释-functional-annotation)
  - [同源性方法 (Homology-Based)](#同源性方法-homology-based)
  - [结构域方法 (Domain-Based)](#结构域方法-domain-based)
- [数据压缩 (Data Compression)](#数据压缩-data-compression)
  - [通用压缩 (General Compression)](#通用压缩-general-compression)
  - [专用压缩 (Specialized Compression)](#专用压缩-specialized-compression)
- [单细胞基因组学 (Single-Cell Genomics)](#单细胞基因组学-single-cell-genomics)
  - [数据预处理 (Preprocessing)](#数据预处理-preprocessing)
  - [细胞聚类与注释 (Cell Clustering & Annotation)](#细胞聚类与注释-cell-clustering-annotation)
- [宏基因组学 (Metagenomics)](#宏基因组学-metagenomics)
  - [物种分类 (Taxonomic Profiling)](#物种分类-taxonomic-profiling)
  - [功能分析 (Functional Profiling)](#功能分析-functional-profiling)
- [表观基因组学 (Epigenomics)](#表观基因组学-epigenomics)
  - [ChIP-seq 分析 (ChIP-seq Analysis)](#chip-seq-分析-chip-seq-analysis)
  - [甲基化分析 (Methylation Analysis)](#甲基化分析-methylation-analysis)
- [基因预测 (Gene Prediction)](#基因预测-gene-prediction)
  - [真核基因预测 (Eukaryotic Gene Prediction)](#真核基因预测-eukaryotic-gene-prediction)
  - [原核基因预测 (Prokaryotic Gene Prediction)](#原核基因预测-prokaryotic-gene-prediction)
- [群体遗传学 (Population Genetics)](#群体遗传学-population-genetics)
  - [主成分与群体结构 (PCA & Population Structure)](#主成分与群体结构-pca-population-structure)
  - [全基因组关联分析 (Genome-Wide Association Study)](#全基因组关联分析-genome-wide-association-study)
  - [选择信号检测 (Selection Signature Detection)](#选择信号检测-selection-signature-detection)
- [空间组学 (Spatial Omics)](#空间组学-spatial-omics)
  - [空间转录组学 (Spatial Transcriptomics)](#空间转录组学-spatial-transcriptomics)
  - [空间蛋白质组学 (Spatial Proteomics)](#空间蛋白质组学-spatial-proteomics)
- [图基因组学 (Graph Genomics)](#图基因组学-graph-genomics)
  - [泛基因组 (Pangenome)](#泛基因组-pangenome)
  - [变异图 (Variation Graph)](#变异图-variation-graph)
- [蛋白质语言模型 (Protein Language Model)](#蛋白质语言模型-protein-language-model)
  - [蛋白质语言模型预训练 (Protein Language Model Pretraining)](#蛋白质语言模型预训练-protein-language-model-pretraining)
  - [蛋白质功能预测 (Protein Function Prediction)](#蛋白质功能预测-protein-function-prediction)

---

## 🔬 Algorithm Categories | 算法分类

## 序列比对 (Sequence Alignment)

用于比较和对齐生物序列的算法


### 双序列比对 (Pairwise Alignment)

两条序列之间的比对算法


#### Smith-Waterman (1981)

经典的局部序列比对算法，使用动态规划方法找出两条序列之间相似性最高的局部区域。
该算法保证找到最优的局部比对结果，适用于检测序列中的保守区域和功能域。

**用途**: 局部序列比对，寻找序列间的相似区域
**时间复杂度**: O(mn)
**空间复杂度**: O(mn)
**论文**: [https://doi.org/10.1016/0022-2836(81)90087-5](https://doi.org/10.1016/0022-2836(81)90087-5)
**实现**: [https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library](https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library)
**相关工具**: BLAST, FASTA, SSEARCH
**标签**: `dynamic-programming` `local-alignment` `classic`


#### Needleman-Wunsch (1970)

全局序列比对的经典算法，使用动态规划对两条完整序列进行端到端比对。
该算法找出最优的全局对齐方案，适用于比较相似长度的同源序列。

**用途**: 全局序列比对
**时间复杂度**: O(mn)
**空间复杂度**: O(mn)
**论文**: [https://doi.org/10.1016/0022-2836(70)90057-4](https://doi.org/10.1016/0022-2836(70)90057-4)
**相关工具**: EMBOSS needle, Clustal
**标签**: `dynamic-programming` `global-alignment` `classic`


#### BLAST (1990)

基本局部比对搜索工具，通过启发式算法在大型序列数据库中快速检索相似序列。
该方法牺牲少量敏感性换取数量级的速度提升，是生物信息学中使用最广泛的工具之一。

**用途**: 快速数据库序列相似性搜索
**时间复杂度**: O(mn)
**空间复杂度**: O(mn)
**论文**: [https://doi.org/10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2)
**实现**: [https://blast.ncbi.nlm.nih.gov/](https://blast.ncbi.nlm.nih.gov/)
**相关工具**: BLAST+, DIAMOND, MMseqs2
**标签**: `heuristic` `database-search` `classic` `fast`


#### Bowtie2 (2012)

基于 FM 索引的超快速短读段比对工具，支持局部比对和端到端比对模式。
该方法使用全文本分钟索引实现亚线性时间比对，是短读段比对的标准工具之一。

**用途**: 短读段快速比对到参考基因组
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/nmeth.1923](https://doi.org/10.1038/nmeth.1923)
**实现**: [https://github.com/BenLangmead/bowtie2](https://github.com/BenLangmead/bowtie2)
**相关工具**: BWA, HISAT2, Minimap2
**标签**: `fm-index` `short-read` `fast` `high-throughput`


#### Minimap2 (2018)

通用的序列比对工具，支持长读段（PacBio/ONT）和短读段的快速比对。
该方法使用最小化子（minimizer）索引实现超快速比对，是长读段数据分析的首选工具。

**用途**: 长读段和短读段的通用快速比对
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/bty191](https://doi.org/10.1093/bioinformatics/bty191)
**实现**: [https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)
**相关工具**: BWA, NGMLR, Winnowmap
**标签**: `minimizer` `long-read` `versatile` `fast`


#### Burrows-Wheeler Transform Alignment (2009)

基于 Burrows-Wheeler 变换的序列比对算法，通过构建 BWT 索引实现快速的短读段比对。
该方法在保持高准确性的同时大幅提升比对速度，是现代测序数据分析的核心算法。

**用途**: 高通量测序数据的快速比对
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btp324](https://doi.org/10.1093/bioinformatics/btp324)
**实现**: [https://github.com/lh3/bwa](https://github.com/lh3/bwa)
**相关工具**: BWA, Bowtie, HISAT2
**标签**: `bwt` `indexing` `short-read` `high-throughput`


#### HISAT2 (2015)

基于层次化 FM 索引的剪接感知比对工具，使用全局和局部索引相结合的策略进行 RNA-seq 比对。
该方法内存占用低、速度快，能准确处理剪接比对，适用于 RNA-seq 和基因组比对。

**用途**: 低内存、高速的剪接感知比对
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/nmeth.3317](https://doi.org/10.1038/nmeth.3317)
**实现**: [https://github.com/DaehwanKimLab/hisat2](https://github.com/DaehwanKimLab/hisat2)
**相关工具**: STAR, TopHat2, BWA
**标签**: `fm-index` `splice-aware` `rna-seq` `low-memory`


#### DIAMOND (2015)

基于双索引策略的超快速蛋白质和核苷酸序列比对工具，比 BLAST 快数万倍。
该方法在保持高灵敏度的同时大幅提升搜索速度，适用于大规模宏基因组学和蛋白质组学分析。

**用途**: 超快速蛋白质和核苷酸序列比对
**时间复杂度**: O(mn)
**空间复杂度**: O(m + n)
**论文**: [https://doi.org/10.1038/nmeth.3176](https://doi.org/10.1038/nmeth.3176)
**实现**: [https://github.com/bbuchfink/diamond](https://github.com/bbuchfink/diamond)
**相关工具**: BLAST, MMseqs2, RAPSearch2
**标签**: `heuristic` `protein-alignment` `fast` `ultra-fast`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### MMseqs2 (2017)

超快速序列搜索和聚类工具，利用多阶段搜索策略实现大规模序列数据库的高效比对和聚类。
该方法支持蛋白质和核苷酸序列的敏感搜索，适用于宏基因组学、蛋白质组学等大数据量分析场景。

**用途**: 超快速序列搜索和聚类
**时间复杂度**: O(mn)
**空间复杂度**: O(m + n)
**论文**: [https://doi.org/10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988)
**实现**: [https://github.com/soedinglab/MMseqs2](https://github.com/soedinglab/MMseqs2)
**相关工具**: BLAST, DIAMOND, Linclust
**标签**: `clustering` `search` `fast` `scalable`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### LASTZ (2004)

专为全基因组比对设计的成对比对工具，能够高效处理大规模基因组间的比对任务。
该方法采用种子扩展策略和得分矩阵，在基因组进化分析和保守区域检测中广泛应用。

**用途**: 成对全基因组比对
**时间复杂度**: O(n^2)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1101/gr.087106.108](https://doi.org/10.1101/gr.087106.108)
**实现**: [https://github.com/lastz/lastz](https://github.com/lastz/lastz)
**相关工具**: MUMmer, Minimap2, Gepard
**标签**: `genome-alignment` `whole-genome` `classic`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### Exonerate (2005)

通用的序列比对工具，支持多种比对模型（ungapped、affine、gapped）和启发式加速策略。该方法可快速搜索大型序列数据库，是功能注释和同源推断的常用工具。

**用途**: 通用序列比对和数据库搜索
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1186/1471-2105-6-31](https://doi.org/10.1186/1471-2105-6-31)
**实现**: [https://github.com/nickloman/exonerate](https://github.com/nickloman/exonerate)
**相关工具**: BLAST, FASTA, SSEARCH
**标签**: `pairwise` `database-search` `versatile` `heuristic`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### parasail (2016)

基于 SIMD 指令集的并行序列比对库，使用 Smith-Waterman、Needleman-Wunsch 等算法的向量化实现。该方法在现代 CPU 上实现了极高的比对吞吐量。

**用途**: SIMD 向量化的并行序列比对
**时间复杂度**: O(mn / w)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1186/s12859-016-0930-z](https://doi.org/10.1186/s12859-016-0930-z)
**实现**: [https://github.com/jeffdaily/parasail](https://github.com/jeffdaily/parasail)
**相关工具**: SWIPE, SSEARCH, KSW
**标签**: `simd` `parallel` `vectorized` `high-throughput`
**难度**: 高级 (Advanced)
**实现语言**: C


#### Edlib (2017)

基于 Myers 位并行算法的快速编辑距离计算工具，支持前缀、后缀和全长比对模式。该方法在计算编辑距离和比对方面速度极快，是序列相似度估计的高效选择。

**用途**: 快速编辑距离和序列比对
**时间复杂度**: O(mn / w)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/bioinformatics/btx780](https://doi.org/10.1093/bioinformatics/btx780)
**实现**: [https://github.com/Martinsos/edlib](https://github.com/Martinsos/edlib)
**相关工具**: parasail, SeqAn, Biopython
**标签**: `edit-distance` `bit-parallel` `fast` `myers`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### WFA2-lib (2023)

基于波前比对算法的超快速序列比对库，利用序列相似性自适应地调整计算复杂度。该方法在高相似度序列比对中比传统方法快数个数量级。

**用途**: 波前算法的自适应超快速序列比对
**时间复杂度**: O(ns)
**空间复杂度**: O(s)
**论文**: [https://doi.org/10.1093/bioinformatics/btad074](https://doi.org/10.1093/bioinformatics/btad074)
**实现**: [https://github.com/smarco/WFA2-lib](https://github.com/smarco/WFA2-lib)
**相关工具**: Edlib, parasail, KSW
**标签**: `wavefront` `adaptive` `ultra-fast` `high-similarity`
**难度**: 高级 (Advanced)
**实现语言**: C


### 多序列比对 (Multiple Sequence Alignment)

多条序列同时比对的算法


#### Clustal Omega (2011)

高性能的多序列比对工具，使用 mBed 引导树和 HHalign 算法实现快速准确的多序列比对。
该方法能够在合理时间内处理数千条序列的比对任务，是多序列比对领域的标准工具。

**用途**: 大规模多序列比对
**时间复杂度**: O(n * L^2)
**空间复杂度**: O(n * L)
**论文**: [https://doi.org/10.1038/msb.2011.75](https://doi.org/10.1038/msb.2011.75)
**实现**: [http://www.clustal.org/omega/](http://www.clustal.org/omega/)
**相关工具**: ClustalW, T-Coffee, MAFFT
**标签**: `multiple-alignment` `guide-tree` `progressive` `scalable`


#### MUSCLE (2004)

基于迭代优化的多序列比对算法，通过多轮渐进比对和精化步骤提高比对质量。
该方法在速度和准确性之间取得了良好平衡，适用于中等规模的序列集合。

**用途**: 高精度多序列比对
**时间复杂度**: O(n^2 * L)
**空间复杂度**: O(n * L)
**论文**: [https://doi.org/10.1093/nar/gkh340](https://doi.org/10.1093/nar/gkh340)
**实现**: [https://github.com/rcedgar/muscle](https://github.com/rcedgar/muscle)
**相关工具**: MAFFT, Clustal Omega, PROBCONS
**标签**: `multiple-alignment` `iterative` `refinement` `classic`


#### MAFFT (2002)

基于快速傅里叶变换的多序列比对工具，使用 FFT 加速同源区域检测和比对优化。
该方法提供多种比对策略，能高效处理从数十到数万条序列的比对任务。

**用途**: 高效多序列比对
**时间复杂度**: O(n * L * log L)
**空间复杂度**: O(n * L)
**论文**: [https://doi.org/10.1093/nar/gkf436](https://doi.org/10.1093/nar/gkf436)
**实现**: [https://github.com/GSLBiotech/mafft](https://github.com/GSLBiotech/mafft)
**相关工具**: MUSCLE, Clustal Omega, T-Coffee
**标签**: `fft` `multiple-alignment` `scalable` `versatile`


#### Kalign (2005)

基于 Wu-Manber 字符串匹配算法的快速多序列比对工具，利用序列间的成对距离构建引导树。
该方法在保持较高比对质量的同时具有极快的运行速度，特别适用于大规模序列集合的快速比对。

**用途**: 快速多序列比对
**时间复杂度**: O(n^2 * L)
**空间复杂度**: O(n * L)
**论文**: [https://doi.org/10.1093/bioinformatics/bti060](https://doi.org/10.1093/bioinformatics/bti060)
**实现**: [https://github.com/Timozer/Kalign](https://github.com/Timozer/Kalign)
**相关工具**: MAFFT, MUSCLE, Clustal Omega
**标签**: `multiple-alignment` `fast` `wu-manber`
**难度**: 进阶 (Intermediate)
**实现语言**: C, C++


#### POA (2002)

部分顺序比对算法，将多序列比对问题转化为偏序图上的比对问题，避免了传统渐进方法的线性顺序限制。
该方法通过构建和合并部分顺序图来表示序列集合，适用于含有插入缺失变异的复杂序列家族比对。

**用途**: 基于偏序图的多序列比对
**时间复杂度**: O(n^2 * L^2)
**空间复杂度**: O(n * L^2)
**论文**: [https://doi.org/10.1093/bioinformatics/18.3.452](https://doi.org/10.1093/bioinformatics/18.3.452)
**相关工具**: MAFFT, MUSCLE, T-Coffee
**标签**: `multiple-alignment` `partial-order` `graph-based`
**难度**: 高级 (Advanced)
**实现语言**: C


## 序列组装 (Sequence Assembly)

从短读段重建完整序列的算法


### 从头组装 (De Novo Assembly)

不依赖参考序列的组装方法


#### De Bruijn Graph Assembly (2001)

基于 De Bruijn 图的序列组装算法，将测序读段分解为 k-mer，构建有向图进行组装。
该方法特别适合处理高通量测序产生的大量短读段，是现代基因组组装的核心方法。

**用途**: 从短读段重建基因组序列
**时间复杂度**: O(n)
**空间复杂度**: O(k * 4^k)
**论文**: [https://doi.org/10.1073/pnas.98.17.9748](https://doi.org/10.1073/pnas.98.17.9748)
**实现**: [https://github.com/voutcn/megahit](https://github.com/voutcn/megahit)
**相关工具**: SPAdes, MEGAHIT, Velvet
**标签**: `graph-based` `k-mer` `de-novo` `short-read`


#### SPAdes (2012)

基于多尺度 De Bruijn 图的基因组组装工具，使用多个 k-mer 长度构建和合并组装图。
该方法在小基因组组装中表现优异，支持单细胞、宏基因组等多种测序数据的组装。

**用途**: 小基因组和单细胞数据的高质量组装
**时间复杂度**: O(n * k)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1089/cmb.2012.0021](https://doi.org/10.1089/cmb.2012.0021)
**实现**: [https://github.com/ablab/spades](https://github.com/ablab/spades)
**相关工具**: MEGAHIT, Velvet, IDBA-UD
**标签**: `de-bruijn` `multi-kmer` `versatile` `single-cell`


#### Hifiasm (2021)

专为 PacBio HiFi 长读段设计的单倍型感知组装工具，利用高精度长读段实现染色体级别的组装。
该方法能够区分父本和母本单倍型，是当前最先进的基因组从头组装工具之一。

**用途**: HiFi 长读段的高质量单倍型组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41592-020-01056-5](https://doi.org/10.1038/s41592-020-01056-5)
**实现**: [https://github.com/chhylp123/hifiasm](https://github.com/chhylp123/hifiasm)
**相关工具**: Canu, Flye, Verkko
**标签**: `hifi` `haplotype-aware` `long-read` `chromosome-level`


#### Overlap-Layout-Consensus (OLC) (2010)

经典的序列组装方法，通过三个步骤完成组装：计算读段间的重叠、构建布局图、生成一致序列。
该方法适合处理长读段数据，能够产生高质量的组装结果。

**用途**: 长读段序列组装
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1101/gr.101360.109](https://doi.org/10.1101/gr.101360.109)
**相关工具**: Canu, Flye, Miniasm
**标签**: `overlap` `long-read` `de-novo` `classic`


#### Flye (2019)

基于重复图的长读段从头组装工具，使用 A-Bruijn 图处理长读段中的重复序列。
该方法对 ONT 和 PacBio CLR 读段效果出色，能快速组装完整的微生物和中大型基因组。

**用途**: 长读段快速从头组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-019-0072-8](https://doi.org/10.1038/s41587-019-0072-8)
**实现**: [https://github.com/fenderglass/Flye](https://github.com/fenderglass/Flye)
**相关工具**: Canu, Hifiasm, Miniasm
**标签**: `repeat-graph` `long-read` `ont` `fast`


#### Verkko (2023)

端粒到端粒级别的基因组组装工具，整合 PacBio HiFi 高精度长读段和 ONT 超长读段实现完整基因组组装。
该方法能够填补参考基因组中的间隙，产生无间隙的端粒到端粒组装结果，是目前最完整的组装策略之一。

**用途**: 整合 HiFi 和 ONT 数据实现端粒到端粒组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-023-01662-6](https://doi.org/10.1038/s41587-023-01662-6)
**实现**: [https://github.com/marbl/verkko](https://github.com/marbl/verkko)
**相关工具**: Hifiasm, HiCanu, Flye
**标签**: `t2t` `hybrid` `hifi` `telomere-to-telomere`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### Shasta (2020)

基于游程编码的超快速长读段组装工具，使用 run-length 编码压缩序列数据以加速组装过程。
该方法专为 Oxford Nanopore 长读段设计，能够在极短时间内完成大规模基因组的从头组装。

**用途**: 超快速长读段基因组组装
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-020-0503-6](https://doi.org/10.1038/s41587-020-0503-6)
**实现**: [https://github.com/chanzuckerberg/shasta](https://github.com/chanzuckerberg/shasta)
**相关工具**: Flye, Canu, Miniasm
**标签**: `long-read` `fast` `run-length` `ont`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### Wtdbg2 (2019)

基于模糊 de Bruijn 图的长读段组装工具，通过模糊边和模糊节点降低图的复杂度以加速组装。
该方法对 Oxford Nanopore 和 PacBio 长读段均有良好支持，组装速度极快且内存占用低。

**用途**: 快速长读段从头组装
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41592-019-0669-3](https://doi.org/10.1038/s41592-019-0669-3)
**实现**: [https://github.com/ruanjue/wtdbg2](https://github.com/ruanjue/wtdbg2)
**相关工具**: Flye, Miniasm, Canu
**标签**: `long-read` `fuzzy-bruijn` `fast` `nanopore`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### Canu (2017)

针对单分子长读段设计的从头组装工具，通过纠错、修剪和组装三个阶段处理高噪声长读段数据。
该方法支持 PacBio 和 Oxford Nanopore 测序数据，能够产生高质量的连续组装序列。

**用途**: 单分子长读段纠错与组装
**时间复杂度**: O(n^2)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1101/gr.215087.116](https://doi.org/10.1101/gr.215087.116)
**实现**: [https://github.com/marbl/canu](https://github.com/marbl/canu)
**相关工具**: Flye, Hifiasm, Miniasm
**标签**: `long-read` `pacbio` `ont` `error-correction`
**难度**: 高级 (Advanced)
**实现语言**: Java


#### MaSuRCA (2013)

马里兰超级读段组装器，整合短读段和长读段数据进行混合组装，利用超级读段压缩降低计算复杂度。
该方法支持多种测序平台数据的混合组装，适用于各类基因组的从头组装项目。

**用途**: 混合测序数据的超级读段组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btt476](https://doi.org/10.1093/bioinformatics/btt476)
**实现**: [https://github.com/alekseyzimin/masurca](https://github.com/alekseyzimin/masurca)
**相关工具**: SPAdes, SOAPdenovo2, AllPaths-LG
**标签**: `hybrid` `super-read` `de-novo` `versatile`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### Unicycler (2017)

基于 SPAdes 和 miniasm 的混合组装工具，先用短读段构建骨架图，再用长读段解决重复区域。该方法对细菌基因组的组装质量极高，可产生完整的环形染色体序列。

**用途**: 细菌基因组的高质量混合组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1371/journal.pcbi.1005595](https://doi.org/10.1371/journal.pcbi.1005595)
**实现**: [https://github.com/rrwick/Unicycler](https://github.com/rrwick/Unicycler)
**相关工具**: SPAdes, Flye, MaSuRCA
**标签**: `hybrid` `bacterial` `circular` `short-read-first`
**难度**: 进阶 (Intermediate)
**实现语言**: Python, C++


#### QUAST (2013)

基因组组装质量评估工具，计算 contig N50、scaffold N50、错配率和完整性等指标。该工具支持无参考和有参考的评估，是组装结果评价的标准工具。

**用途**: 基因组组装质量的综合评估
**时间复杂度**: O(n * r)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btt086](https://doi.org/10.1093/bioinformatics/btt086)
**实现**: [https://github.com/ablab/quast](https://github.com/ablab/quast)
**相关工具**: BUSCO, Merqury, Inspector
**标签**: `quality-assessment` `n50` `assembly-evaluation` `standard`
**难度**: 入门 (Beginner)
**实现语言**: Python


### 参考引导组装 (Reference-Guided Assembly)

基于参考序列的组装方法


#### Reference-Guided Assembly (2011)

基于参考基因组的序列组装方法，将测序读段先比对到参考序列上，再进行局部组装和变异检测。
该方法适合有近缘参考基因组的物种，组装速度快且资源消耗低，常用于重测序项目。

**用途**: 基于参考序列的快速基因组组装
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/gb-2011-12-5-r42](https://doi.org/10.1186/gb-2011-12-5-r42)
**实现**: [https://github.com/ablab/ragout](https://github.com/ablab/ragout)
**相关工具**: Ragout, RaGOO, RagTag
**标签**: `reference-based` `scaffolding` `resequencing` `efficient`


#### RagTag (2022)

基于参考基因组进行 scaffold 排序、定向和纠错的组装改进工具，常用于提升草图组装的连续性和完整度。
该方法能够快速将 contig 锚定到近缘参考序列，为植物和动物基因组装配提供高效的参考引导整理能力。

**用途**: 基于参考基因组改进 scaffold 排序与定向
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/s13059-022-02823-7](https://doi.org/10.1186/s13059-022-02823-7)
**实现**: [https://github.com/malonge/RagTag](https://github.com/malonge/RagTag)
**相关工具**: Ragout, RaGOO, Minimap2
**标签**: `reference-based` `scaffolding` `assembly-polishing` `genome-finishing`


## 变异检测 (Variant Calling)

检测基因组变异的算法


### 单核苷酸变异 (SNV Detection)

检测单核苷酸变异和小型插入缺失


#### GATK HaplotypeCaller (2010)

基于局部重组装的变异检测算法，通过在活跃区域进行局部单倍型组装来发现变异。
该方法能够同时检测 SNP 和 Indel，是目前最广泛使用的变异检测工具之一。

**用途**: 检测 SNP 和小型 Indel 变异
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1038/ng.806](https://doi.org/10.1038/ng.806)
**实现**: [https://github.com/broadinstitute/gatk](https://github.com/broadinstitute/gatk)
**相关工具**: GATK, Picard, BWA
**标签**: `haplotype` `snp` `indel` `germline`


#### DeepVariant (2018)

基于深度学习的变异检测工具，将比对数据转化为图像后使用卷积神经网络进行变异分类。
该方法在多个基准测试中表现优异，能有效降低假阳性率，支持多种测序平台数据。

**用途**: 基于深度学习的高精度变异检测
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1038/nbt.4235](https://doi.org/10.1038/nbt.4235)
**实现**: [https://github.com/google/deepvariant](https://github.com/google/deepvariant)
**相关工具**: GATK, PEPPER-Margin-DeepVariant, Clair3
**标签**: `deep-learning` `cnn` `snp` `high-accuracy`


#### FreeBayes (2012)

基于贝叶斯统计的变异检测算法，使用单倍型作为基本单位进行变异调用。
该方法支持多倍体样本，能够检测复杂的变异模式，计算效率较高。

**用途**: 基于贝叶斯的变异检测
**时间复杂度**: O(n * h)
**空间复杂度**: O(h)
**论文**: [https://arxiv.org/abs/1207.3907](https://arxiv.org/abs/1207.3907)
**实现**: [https://github.com/freebayes/freebayes](https://github.com/freebayes/freebayes)
**相关工具**: VCFtools, BCFtools
**标签**: `bayesian` `haplotype` `polyploid` `snp`


#### Strelka2 (2018)

快速准确的体细胞和生殖系小型变异检测工具，使用分层混合模型提高检测灵敏度。
该方法速度极快，能在数小时内完成全基因组变异检测，广泛用于癌症基因组学研究。

**用途**: 快速体细胞和生殖系变异检测
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1038/s41592-018-0051-x](https://doi.org/10.1038/s41592-018-0051-x)
**实现**: [https://github.com/Illumina/strelka](https://github.com/Illumina/strelka)
**相关工具**: Mutect2, VarScan2, GATK
**标签**: `somatic` `germline` `fast` `clinical`


#### MuTect2 (2013)

GATK 中的体细胞变异检测工具，通过贝叶斯统计模型同时检测肿瘤样本中的体细胞 SNP 和小型 Indel。
该方法利用匹配的正常组织样本进行背景噪声去除，广泛应用于癌症基因组学研究与临床肿瘤检测。

**用途**: 检测体细胞 SNP 和小型 Indel 变异
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1101/gr.169185.113](https://doi.org/10.1101/gr.169185.113)
**实现**: [https://github.com/broadinstitute/gatk](https://github.com/broadinstitute/gatk)
**相关工具**: GATK, Strelka2, VarScan2
**标签**: `somatic` `cancer` `gatk` `snp`


#### Clair3 (2022)

面向长读段测序数据的生殖系小型变异检测工具，结合堆叠图像和全比对两阶段深度学习模型进行变异分类。
该方法对 Nanopore 和 PacBio 数据均有出色表现，具有极高的准确率和良好的计算效率。

**用途**: 基于长读段数据进行高精度生殖系变异检测
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1038/s41587-021-01138-7](https://doi.org/10.1038/s41587-021-01138-7)
**实现**: [https://github.com/HKU-BAL/Clair3](https://github.com/HKU-BAL/Clair3)
**相关工具**: DeepVariant, PEPPER-Margin-DeepVariant, Medaka
**标签**: `long-read` `nanopore` `pacbio` `germline`


#### DeepSomatic (2024)

基于深度学习的体细胞变异检测工具，利用神经网络从长读段比对数据中识别肿瘤特异性突变。
该方法支持多种测序平台，能够检测复杂突变模式，适用于癌症基因组研究中的高灵敏度变异发现。

**用途**: 基于深度学习的体细胞变异检测
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1101/2024.07.02.601671](https://doi.org/10.1101/2024.07.02.601671)
**相关工具**: MuTect2, DeepVariant, Strelka2
**标签**: `deep-learning` `somatic` `cancer` `long-read`


#### Octopus (2021)

基于贝叶斯统计框架的单倍型感知变异检测工具，能够同时对生殖系和体细胞变异进行联合建模与推断。
该方法支持多样本联合分析，具有极高的变异检测灵敏度和特异性，适用于复杂基因组研究。

**用途**: 贝叶斯单倍型感知的变异检测与联合推断
**时间复杂度**: O(n * h)
**空间复杂度**: O(h)
**论文**: [https://doi.org/10.1038/s41587-020-0711-0](https://doi.org/10.1038/s41587-020-0711-0)
**实现**: [https://github.com/luntergroup/octopus](https://github.com/luntergroup/octopus)
**相关工具**: FreeBayes, GATK HaplotypeCaller, Strelka2
**标签**: `bayesian` `haplotype` `germline-somatic` `multi-sample`


### 结构变异 (Structural Variants)

检测大规模结构变异


#### Delly (2012)

基于分裂读段和双端读段信号的结构变异检测算法，能够发现缺失、重复、倒位和易位等大规模基因组变异。
该方法结合多种信号源提高检测灵敏度，是结构变异检测领域的代表性工具之一。

**用途**: 检测基因组结构变异（缺失、重复、倒位、易位）
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/bts378](https://doi.org/10.1093/bioinformatics/bts378)
**实现**: [https://github.com/dellytools/delly](https://github.com/dellytools/delly)
**相关工具**: Manta, LUMPY, GRIDSS
**标签**: `structural-variant` `split-read` `paired-end` `sv-detection`


#### Manta (2016)

高性能的结构变异和大型 Indel 检测工具，使用图组装方法精确定位变异断点。
该方法速度快、准确性高，支持体细胞和生殖系变异检测，广泛用于临床基因组学。

**用途**: 结构变异和大型 Indel 检测
**时间复杂度**: O(n * c)
**空间复杂度**: O(c)
**论文**: [https://doi.org/10.1093/bioinformatics/btv710](https://doi.org/10.1093/bioinformatics/btv710)
**实现**: [https://github.com/Illumina/manta](https://github.com/Illumina/manta)
**相关工具**: Delly, GRIDSS, SvABA
**标签**: `structural-variant` `graph-assembly` `clinical` `fast`


#### Sniffles2 (2023)

面向长读段测序数据的结构变异检测工具，结合断点信号和覆盖度变化识别插入、缺失、倒位等复杂事件。
该方法对 PacBio 和 ONT 数据均有良好表现，适合群体水平与单样本的长读段结构变异分析。

**用途**: 基于长读段数据进行高精度结构变异检测
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-023-01743-3](https://doi.org/10.1038/s41587-023-01743-3)
**实现**: [https://github.com/fritzsedlazeck/Sniffles](https://github.com/fritzsedlazeck/Sniffles)
**相关工具**: Delly, Manta, cuteSV
**标签**: `structural-variant` `long-read` `breakpoint` `population-scale`


#### GRIDSS (2017)

基于断裂端组装的基因组重排识别算法，通过局部组装和 split-read 信号精确定位结构变异断点。
该方法具有极高的灵敏度和特异性，能够检测复杂结构变异事件，是结构变异检测领域的重要工具。

**用途**: 基于断裂端组装检测基因组结构变异
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/s13059-021-02422-y](https://doi.org/10.1186/s13059-021-02422-y)
**实现**: [https://github.com/PapenfussLab/gridss](https://github.com/PapenfussLab/gridss)
**相关工具**: Delly, Manta, LUMPY
**标签**: `structural-variant` `breakend` `assembly-based`


#### cuteSV (2020)

面向长读段测序数据的结构变异检测工具，通过对不同变异类型信号的聚类分析识别基因组变异。
该方法对插入、缺失、倒位和易位等变异类型均有良好检测效果，适用于 Nanopore 和 PacBio 数据分析。

**用途**: 基于长读段数据通过信号聚类检测结构变异
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41592-020-01047-6](https://doi.org/10.1038/s41592-020-01047-6)
**实现**: [https://github.com/tjiangHIT/cuteSV](https://github.com/tjiangHIT/cuteSV)
**相关工具**: Sniffles2, Delly, Manta
**标签**: `structural-variant` `long-read` `clustering` `nanopore`


#### SvABA (2016)

基于局部组装的结构变异和体细胞突变检测工具，能够同时识别生殖系和体细胞的结构变异事件。
该方法通过断点图和单倍型组装精确定位变异断点，适用于癌症基因组学中的复杂变异检测。

**用途**: 基于局部组装的结构变异和体细胞突变检测
**时间复杂度**: O(n * c)
**空间复杂度**: O(c)
**论文**: [https://doi.org/10.1038/nmeth.4139](https://doi.org/10.1038/nmeth.4139)
**实现**: [https://github.com/walaj/svaba](https://github.com/walaj/svaba)
**相关工具**: Manta, GRIDSS, Delly
**标签**: `structural-variant` `somatic` `assembly-based`


## 基因表达分析 (Gene Expression Analysis)

分析基因表达水平的算法


### 表达定量 (Expression Quantification)

转录本和基因水平的表达量估计


#### STAR (2013)

超快速的 RNA-seq 比对工具，使用后缀数组和种子扩展策略实现剪接感知的比对。
该方法能够准确识别新的剪接位点，是 RNA-seq 数据分析流程中使用最广泛的比对工具。

**用途**: RNA-seq 数据的剪接感知比对
**时间复杂度**: O(n)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1093/bioinformatics/bts635](https://doi.org/10.1093/bioinformatics/bts635)
**实现**: [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
**相关工具**: HISAT2, TopHat2, Salmon
**标签**: `rna-seq` `splice-aware` `alignment` `fast`


#### Salmon (2017)

基于选择性比对的高速转录本定量工具，使用轻量级比对和在线 EM 算法估计转录本丰度。
该方法速度极快且内存占用低，能够校正 GC 含量偏差和序列特异性偏差。

**用途**: 快速准确的转录本定量
**时间复杂度**: O(n)
**空间复杂度**: O(t)
**论文**: [https://doi.org/10.1038/nmeth.4197](https://doi.org/10.1038/nmeth.4197)
**实现**: [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
**相关工具**: Kallisto, RSEM, Sailfish
**标签**: `selective-alignment` `quantification` `rna-seq` `fast`


#### Kallisto (2016)

基于伪比对的转录本定量算法，使用 k-mer 索引实现超快速的表达量估计。
该方法无需完整比对即可准确估计转录本丰度，大幅提升了分析速度。

**用途**: 快速转录本定量
**时间复杂度**: O(n)
**空间复杂度**: O(t)
**论文**: [https://doi.org/10.1038/nbt.3519](https://doi.org/10.1038/nbt.3519)
**实现**: [https://github.com/pachterlab/kallisto](https://github.com/pachterlab/kallisto)
**相关工具**: Salmon, RSEM, Sleuth
**标签**: `pseudoalignment` `quantification` `rna-seq` `fast`


#### StringTie (2015)

高效的转录本组装和丰度估计工具，使用网络流算法从 RNA-seq 比对结果中重构转录本结构。
该方法能够准确组装新的转录本异构体并估计其表达量，是转录组分析流程中的核心组件。

**用途**: 转录本组装与丰度估计
**时间复杂度**: O(n)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1038/nbt.3122](https://doi.org/10.1038/nbt.3122)
**实现**: [https://github.com/gpertea/stringtie](https://github.com/gpertea/stringtie)
**相关工具**: STAR, HISAT2, Cufflinks
**标签**: `transcript-assembly` `quantification` `rna-seq` `splice-aware`


#### RSEM (2011)

基于参考转录组的转录本定量工具，使用期望最大化算法估计转录本丰度。
该方法能够处理多重比对读段并提供转录本和基因水平的表达量估计，适合需要高精度定量的场景。

**用途**: 基于参考的转录本定量
**时间复杂度**: O(n * t)
**空间复杂度**: O(t)
**论文**: [https://doi.org/10.1186/1471-2105-12-323](https://doi.org/10.1186/1471-2105-12-323)
**实现**: [https://github.com/deweylab/RSEM](https://github.com/deweylab/RSEM)
**相关工具**: Salmon, Kallisto, Sailfish
**标签**: `quantification` `expectation-maximization` `rna-seq` `reference-based`


#### tximport (2016)

从轻量级比对工具的输出导入转录本定量结果并汇总到基因水平的工具。该方法
使用偏移量校正来处理转录本长度变化对基因水平定量的影响，是 Salmon/Kallisto
与 DESeq2/edgeR 之间的桥梁工具。

**用途**: 转录本定量结果导入和基因水平汇总
**时间复杂度**: O(n * t)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.12688/f1000research.7563.1](https://doi.org/10.12688/f1000research.7563.1)
**相关工具**: Salmon, Kallisto, DESeq2
**标签**: `import` `summarization` `offset-correction` `bioconductor`
**难度**: 入门 (Beginner)
**实现语言**: R


### 差异表达 (Differential Expression)

不同条件间的差异表达分析


#### DESeq2 (2014)

基于负二项分布的差异表达分析算法，使用收缩估计来提高方差估计的稳定性。
该方法特别适合处理小样本量的 RNA-seq 数据，是目前最广泛使用的差异表达分析工具之一。

**用途**: RNA-seq 数据的差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8)
**实现**: [https://bioconductor.org/packages/DESeq2](https://bioconductor.org/packages/DESeq2)
**相关工具**: edgeR, limma, Bioconductor
**标签**: `rna-seq` `differential-expression` `negative-binomial` `statistical`


#### edgeR (2010)

基于经验贝叶斯方法的差异表达分析工具，使用负二项分布建模并通过标签化分散估计提高统计效力。
该方法适合处理小样本和多因素实验设计，与 DESeq2 并列为最主流的差异表达分析工具。

**用途**: 基于经验贝叶斯的差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1093/bioinformatics/btp616](https://doi.org/10.1093/bioinformatics/btp616)
**实现**: [https://bioconductor.org/packages/edgeR](https://bioconductor.org/packages/edgeR)
**相关工具**: DESeq2, limma-voom, Bioconductor
**标签**: `rna-seq` `differential-expression` `empirical-bayes` `statistical`


#### Sleuth (2017)

基于 bootstrap 估计的差异表达分析工具，与 kallisto 配合使用以量化转录本水平的表达变异。
该方法利用 bootstrap 技术估计技术噪声并分离生物学变异，适合转录本级别的差异表达检测。

**用途**: 基于 bootstrap 估计的转录本级别差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1186/s13059-017-1218-3](https://doi.org/10.1186/s13059-017-1218-3)
**实现**: [https://github.com/pachterlab/sleuth](https://github.com/pachterlab/sleuth)
**相关工具**: DESeq2, edgeR, Kallisto
**标签**: `differential-expression` `bootstrap` `rna-seq` `transcript-level`


#### limma-voom (2014)

将线性模型和精度权重应用于 RNA-seq 数据的差异表达分析方法，继承了 limma 在芯片数据中的优势。
该方法通过 voom 转换为每个观测值分配精度权重，使得线性建模框架能够适用于计数数据。

**用途**: 基于线性模型和精度权重的 RNA-seq 差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1186/gb-2014-15-2-r29](https://doi.org/10.1186/gb-2014-15-2-r29)
**相关工具**: DESeq2, edgeR, limma
**标签**: `differential-expression` `precision-weight` `linear-model` `bioconductor`


#### NOISeq (2015)

非参数的差异表达分析工具，通过模拟噪声分布来识别显著差异表达的基因。
该方法不依赖于数据分布的假设，能够有效处理低重复样本和无重复实验设计的 RNA-seq 数据。

**用途**: 非参数差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1038/nmeth.3053](https://doi.org/10.1038/nmeth.3053)
**标签**: `differential-expression` `non-parametric` `noiseq` `rna-seq`


#### Ballgown (2014)

基于 FPKM 值的转录本差异表达分析工具，使用线性模型和统计检验检测条件间
的表达差异。该方法与 StringTie 流程紧密集成，提供转录本和外显子水平的
差异分析功能。

**用途**: 基于 FPKM 的转录本差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1186/s13059-014-0556-x](https://doi.org/10.1186/s13059-014-0556-x)
**相关工具**: DESeq2, StringTie, Cufflinks
**标签**: `differential-expression` `fpkm` `transcript-level` `linear-model`
**难度**: 进阶 (Intermediate)
**实现语言**: R


## 蛋白质结构预测 (Protein Structure Prediction)

预测蛋白质三维结构的算法


### 从头预测 (Ab Initio Prediction)

基于序列信息的从头结构预测


#### AlphaFold (2021)

基于深度学习的蛋白质结构预测算法，使用注意力机制和进化信息预测蛋白质三维结构。
该方法在 CASP14 竞赛中取得突破性成果，预测精度接近实验测定水平。

**用途**: 从氨基酸序列预测蛋白质三维结构
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)
**实现**: [https://github.com/deepmind/alphafold](https://github.com/deepmind/alphafold)
**相关工具**: ColabFold, ESMFold, RoseTTAFold
**标签**: `deep-learning` `attention` `structure-prediction` `breakthrough`


#### ESMFold (2023)

基于蛋白质语言模型的端到端结构预测方法，使用大规模预训练的 ESM-2 模型直接从单条序列预测结构。
该方法无需多序列比对输入，推理速度比 AlphaFold 快一个数量级，适合大规模结构预测。

**用途**: 基于语言模型的快速蛋白质结构预测
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574)
**实现**: [https://github.com/facebookresearch/esm](https://github.com/facebookresearch/esm)
**相关工具**: AlphaFold, OmegaFold, RoseTTAFold
**标签**: `language-model` `single-sequence` `fast` `deep-learning`


#### RoseTTAFold (2021)

基于三轨注意力网络的蛋白质结构预测方法，同时建模序列、距离图和三维坐标之间的信息传递。
该方法在较低计算成本下实现了接近 AlphaFold 的预测精度，推动了结构预测模型的快速普及。

**用途**: 基于多轨神经网络的高精度蛋白质结构预测
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754)
**实现**: [https://github.com/RosettaCommons/RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold)
**相关工具**: AlphaFold, ESMFold, trRosetta
**标签**: `deep-learning` `three-track` `structure-prediction` `accurate`


#### OmegaFold (2022)

基于蛋白质语言模型和端到端几何建模的结构预测方法，可直接从单条氨基酸序列快速推断三维构象。
该方法无需多序列比对即可获得具有竞争力的预测精度，适合大规模蛋白质结构筛查和快速注释场景。

**用途**: 基于单序列语言模型进行快速蛋白质结构预测
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1101/2022.07.21.500999](https://doi.org/10.1101/2022.07.21.500999)
**实现**: [https://github.com/HeliXonProtein/OmegaFold](https://github.com/HeliXonProtein/OmegaFold)
**相关工具**: ESMFold, AlphaFold, RoseTTAFold
**标签**: `language-model` `single-sequence` `structure-prediction` `fast`


#### AlphaFold3 (2024)

由 DeepMind 推出的新一代结构预测模型，不仅能预测蛋白质结构，还能预测核酸、小分子、离子等生物分子复合体的三维结构。
该方法采用扩散生成模型替代坐标精修，大幅扩展了可预测的分子类型，在药物设计和分子对接场景中表现出色。

**用途**: 统一预测蛋白质及生物分子复合体三维结构
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)
**实现**: [https://github.com/google-deepmind/alphafold3](https://github.com/google-deepmind/alphafold3)
**相关工具**: AlphaFold, ESMFold, RoseTTAFold
**标签**: `deep-learning` `structure-prediction` `multi-modal` `diffusion`


#### OpenFold (2022)

AlphaFold2 的开源可训练复现版本，完整保留了原始模型的训练流程与推理能力，支持从头训练和微调。
该工具由 AlQuraishi 实验室开发，促进了结构预测方法的可复现性和社区研究，广泛用于教学和方法改进。

**用途**: 开源可训练的 AlphaFold2 复现框架
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41467-023-41843-w](https://doi.org/10.1038/s41467-023-41843-w)
**实现**: [https://github.com/aqlaboratory/openfold](https://github.com/aqlaboratory/openfold)
**相关工具**: AlphaFold, ESMFold
**标签**: `open-source` `trainable` `structure-prediction` `pytorch`


#### ColabFold (2022)

通过集成 MMseqs2 进行快速多序列比对搜索，显著加速 AlphaFold 和 RoseTTAFold 的推理流程。
该工具提供 Google Colab 接口使得普通研究者无需高性能计算资源即可进行蛋白质结构预测，降低了使用门槛。

**用途**: 加速并简化 AlphaFold 蛋白质结构预测流程
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1)
**实现**: [https://github.com/sokrypton/ColabFold](https://github.com/sokrypton/ColabFold)
**相关工具**: AlphaFold, MMseqs2, RoseTTAFold
**标签**: `fast` `msa` `colab` `accessible`


#### Chai-1 (2024)

由 Chai Discovery 开发的多模态生物分子结构预测模型，支持蛋白质、核酸和小分子复合体的联合结构预测。
该模型采用开放权重发布策略，适用于药物靶点发现和先导化合物优化，为药物研发提供了新的开源工具。

**用途**: 多模态生物分子结构预测与药物发现
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.48550/arXiv.2410.17155](https://doi.org/10.48550/arXiv.2410.17155)
**相关工具**: AlphaFold3, Boltz-1
**标签**: `structure-prediction` `multi-modal` `drug-discovery` `open-weight`


#### Boltz-1 (2024)

开源的生物分子结构预测模型，采用扩散模型架构对蛋白质及核酸复合体进行端到端的三维结构推断。
该方法完全开源且权重公开，支持社区自由使用和二次开发，为学术研究和工业应用提供了高效的结构预测方案。

**用途**: 开源端到端生物分子结构预测
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.48550/arXiv.2411.02833](https://doi.org/10.48550/arXiv.2411.02833)
**实现**: [https://github.com/jwohlwend/boltz](https://github.com/jwohlwend/boltz)
**相关工具**: AlphaFold3, Chai-1
**标签**: `structure-prediction` `open-source` `diffusion` `biomolecular`


### 模板方法 (Template-Based Modeling)

基于已知结构模板的建模方法


#### Rosetta (2003)

基于物理能量函数的蛋白质结构预测和设计算法，使用蒙特卡洛采样探索构象空间。
该方法广泛应用于蛋白质折叠、对接和设计，是计算结构生物学的重要工具。

**用途**: 蛋白质结构预测和设计
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.1089427](https://doi.org/10.1126/science.1089427)
**实现**: [https://www.rosettacommons.org/](https://www.rosettacommons.org/)
**相关工具**: PyRosetta, RosettaDock, RosettaDesign
**标签**: `energy-function` `monte-carlo` `protein-design` `classic`


#### MODELLER (1993)

经典的同源建模工具，基于空间约束满足原理从已知模板结构推断目标蛋白的三维构象。
该方法在模板可用时能够快速构建可靠模型，广泛用于结构生物学、突变分析和蛋白功能研究。

**用途**: 基于模板结构进行蛋白质同源建模
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1002/jcc.540140211](https://doi.org/10.1002/jcc.540140211)
**实现**: [https://salilab.org/modeller/](https://salilab.org/modeller/)
**相关工具**: Rosetta, I-TASSER, SWISS-MODEL
**标签**: `homology-modeling` `template-based` `comparative-modeling` `classic`


#### I-TASSER (2008)

结合 threading、片段组装和结构精修的蛋白质结构预测方法，可在模板信息有限时构建较高质量的三维模型。
该方法长期在结构预测评测中表现稳定，并常用于结构功能注释、结合位点推断和蛋白互作研究。

**用途**: 结合 threading 与组装策略进行蛋白质结构建模
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1186/1471-2105-9-40](https://doi.org/10.1186/1471-2105-9-40)
**实现**: [https://zhanggroup.org/I-TASSER/](https://zhanggroup.org/I-TASSER/)
**相关工具**: MODELLER, Rosetta, Phyre2
**标签**: `threading` `template-based` `fragment-assembly` `structure-refinement`


#### Foldseek (2023)

超高速蛋白质结构搜索工具，通过将三维结构编码为一维的 3Di 字母序列实现比传统方法快数万倍的结构相似性搜索。
该工具支持对大型结构数据库进行快速检索，是蛋白质功能注释、同源发现和结构聚类的重要利器。

**用途**: 超快速蛋白质三维结构相似性搜索
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-023-01773-x](https://doi.org/10.1038/s41587-023-01773-x)
**实现**: [https://github.com/steineggerlab/foldseek](https://github.com/steineggerlab/foldseek)
**相关工具**: TM-align, DALI, MMseqs2
**标签**: `structure-search` `fast` `3Di` `structural-alignment`


#### TM-align (2005)

经典的蛋白质结构比对工具，通过动态规划和 TM-score 打分实现两两蛋白质三维结构的精确对齐与相似性评估。
该方法对长度差异和序列差异较大的蛋白也能提供可靠的结构比对结果，被广泛引用为结构比较的基准方法。

**用途**: 蛋白质三维结构比对与相似性评估
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1093/nar/gki524](https://doi.org/10.1093/nar/gki524)
**相关工具**: DALI, Foldseek, CE
**标签**: `structure-alignment` `rmsd` `classic` `comparison`


## 系统发育分析 (Phylogenetics)

构建和分析进化树的算法


### 距离法 (Distance Methods)

基于距离矩阵的建树方法


#### Neighbor-Joining (1987)

基于距离矩阵的系统发育树构建算法，通过迭代地合并最近邻节点来构建无根树。
该方法计算速度快，适合处理大规模数据集，是最常用的距离法建树算法之一。

**用途**: 快速构建系统发育树
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1093/oxfordjournals.molbev.a040454](https://doi.org/10.1093/oxfordjournals.molbev.a040454)
**相关工具**: MEGA, PHYLIP, RapidNJ
**标签**: `distance-based` `tree-building` `classic`


#### FastTree (2010)

面向大规模多序列比对的近似最大似然建树工具，通过启发式搜索快速生成大规模系统发育树。
该方法在处理上万条序列时速度明显快于传统方法，是高通量进化分析和微生物组研究中的常用选择。

**用途**: 大规模序列集合的快速近似最大似然建树
**时间复杂度**: O(n * s * log n)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1371/journal.pone.0009490](https://doi.org/10.1371/journal.pone.0009490)
**实现**: [https://github.com/morgannprice/FastTree](https://github.com/morgannprice/FastTree)
**相关工具**: IQ-TREE, RAxML-NG, PhyML
**标签**: `tree-building` `approximate-likelihood` `scalable` `fast`


### 特征法 (Character-Based Methods)

基于序列特征的建树方法


#### Maximum Likelihood Phylogeny (2014)

基于最大似然法的系统发育推断算法，通过优化进化模型参数来寻找最可能的树拓扑。
该方法统计学基础扎实，能够提供可靠的分支支持度评估。

**用途**: 统计学方法构建系统发育树
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/sysbio/syq010](https://doi.org/10.1093/sysbio/syq010)
**实现**: [https://github.com/stamatak/standard-RAxML](https://github.com/stamatak/standard-RAxML)
**相关工具**: RAxML, IQ-TREE, PhyML
**标签**: `maximum-likelihood` `statistical` `tree-building`


#### IQ-TREE (2015)

高效的最大似然系统发育推断工具，集成了自动模型选择（ModelFinder）和超快自展分析。
该方法在速度和准确性上优于传统 ML 工具，支持数千个分类单元的大规模建树。

**用途**: 快速最大似然系统发育推断
**时间复杂度**: O(n^2 * s)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/molbev/msu300](https://doi.org/10.1093/molbev/msu300)
**实现**: [https://github.com/iqtree/iqtree2](https://github.com/iqtree/iqtree2)
**相关工具**: RAxML-NG, PhyML, FastTree
**标签**: `maximum-likelihood` `model-selection` `ultrafast-bootstrap` `scalable`


#### Bayesian Phylogenetic Inference (2001)

基于贝叶斯统计框架的系统发育推断方法，使用马尔可夫链蒙特卡洛采样估计后验概率分布。
该方法能同时估计树拓扑、分支长度和模型参数的不确定性，适合分子钟和分歧时间估计。

**用途**: 贝叶斯框架的系统发育推断和分歧时间估计
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/bioinformatics/17.8.754](https://doi.org/10.1093/bioinformatics/17.8.754)
**实现**: [https://github.com/beast-dev/beast-mcmc](https://github.com/beast-dev/beast-mcmc)
**相关工具**: MrBayes, BEAST2, RevBayes
**标签**: `bayesian` `mcmc` `molecular-clock` `divergence-time`


#### RAxML-NG (2019)

新一代最大似然系统发育推断工具，在前代 RAxML 基础上大幅提升计算速度与并行效率。
支持超快自展分析和自动模型选择，适合处理包含数万条序列的大规模系统发育数据集。

**用途**: 下一代高性能最大似然系统发育推断
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/bioinformatics/btz305](https://doi.org/10.1093/bioinformatics/btz305)
**实现**: [https://github.com/amkozlov/raxml-ng](https://github.com/amkozlov/raxml-ng)
**相关工具**: RAxML, IQ-TREE, PhyML
**标签**: `maximum-likelihood` `scalable` `ultrafast-bootstrap` `model-selection`


#### BEAST2 (2014)

灵活的贝叶斯系统发育推断与系统动力学分析平台，支持复杂分子钟模型和物种分化时间估计。
提供丰富的插件生态系统，可根据不同研究需求定制分析流程，广泛应用于病毒进化和流行病学研究。

**用途**: 贝叶斯系统发育推断与系统动力学分析
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/molbev/mst024](https://doi.org/10.1093/molbev/mst024)
**实现**: [https://github.com/CompEvol/beast2](https://github.com/CompEvol/beast2)
**相关工具**: BEAST, MrBayes, RevBayes
**标签**: `bayesian` `mcmc` `phylodynamics` `molecular-clock`


#### MrBayes (2012)

基于 Metropolis 耦合马尔可夫链蒙特卡洛的贝叶斯系统发育推断软件，是该领域最经典的工具之一。
支持多种核苷酸和氨基酸替换模型，能够高效采样后验分布并评估系统发育树的不确定性。

**用途**: 经典贝叶斯系统发育推断
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/sysbio/sys029](https://doi.org/10.1093/sysbio/sys029)
**实现**: [https://github.com/NBISweden/MrBayes](https://github.com/NBISweden/MrBayes)
**相关工具**: BEAST2, RevBayes
**标签**: `bayesian` `mcmc` `metropolis-coupled` `classic`


#### ASTRAL (2018)

基于基因树汇总方法的物种树估计工具，通过寻找与输入基因树最兼容的物种树来解决不完全谱系分选问题。
在多物种溯祖模型下具有理论保证，是基因组尺度系统发育学研究中的标准方法之一。

**用途**: 基于基因树汇总的物种树估计
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1093/molbev/msx270](https://doi.org/10.1093/molbev/msx270)
**实现**: [https://github.com/smirarab/ASTRAL](https://github.com/smirarab/ASTRAL)
**相关工具**: ASTRAL-III, ASTRID, MP-EST
**标签**: `species-tree` `summary-method` `coalescent` `gene-tree`


#### IQ-TREE 2 (2020)

高效的最大似然系统发育推断工具最新版本，新增分区模型和混合模型支持以适应异质进化过程。
集成 ModelFinder 自动选择最优替代模型，在大规模基因组数据集上表现优异且内存效率高。

**用途**: 支持分区与混合模型的高效最大似然推断
**时间复杂度**: O(n^2 * s)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/molbev/msaa015](https://doi.org/10.1093/molbev/msaa015)
**实现**: [https://github.com/iqtree/iqtree2](https://github.com/iqtree/iqtree2)
**相关工具**: RAxML-NG, PhyML, FastTree
**标签**: `maximum-likelihood` `model-finder` `partition` `mixture-model`


#### PhyML (2003)

基于最大似然法的快速系统发育树构建工具，使用启发式搜索策略加速树拓扑的优化。该方法可自动选择最优的核苷酸或蛋白质替换模型。

**用途**: 快速最大似然系统发育推断
**时间复杂度**: O(n^2 * s)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/nar/gkh368](https://doi.org/10.1093/nar/gkh368)
**相关工具**: RAxML-NG, IQ-TREE, FastTree
**标签**: `maximum-likelihood` `fast` `model-selection` `classic`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### RevBayes (2016)

灵活的贝叶斯系统发育推断平台，使用概率编程语言定义进化模型。该方法支持任意组合的树先验、分子钟模型和分化时间估计，是方法学研究的理想工具。

**用途**: 灵活的贝叶斯系统发育推断平台
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/sysbio/syw021](https://doi.org/10.1093/sysbio/syw021)
**实现**: [https://github.com/revbayes/revbayes](https://github.com/revbayes/revbayes)
**相关工具**: BEAST2, MrBayes, Bali-Phy
**标签**: `bayesian` `probabilistic-programming` `flexible` `molecular-clock`
**难度**: 高级 (Advanced)
**实现语言**: C++


## 功能注释 (Functional Annotation)

预测基因和蛋白质功能的算法


### 同源性方法 (Homology-Based)

基于序列同源性的功能推断


#### BLAST-based Annotation (1990)

基于序列相似性的功能注释方法，通过与已知功能序列数据库比对来推断未知序列的功能。
该方法是最基础和广泛使用的功能注释策略，适用于各类生物序列的初步功能预测。

**用途**: 基于序列相似性的功能预测
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2)
**实现**: [https://blast.ncbi.nlm.nih.gov/](https://blast.ncbi.nlm.nih.gov/)
**相关工具**: BLAST+, UniProt, InterPro
**标签**: `sequence-similarity` `database-search` `classic` `annotation`


#### eggNOG-mapper (2017)

基于直系同源群（eggNOG）数据库的快速功能注释工具，使用预计算的进化系统树提高注释准确性。
该方法能高效注释大规模蛋白质组数据，提供 GO、KEGG 和 COG 等多种功能分类。

**用途**: 基于直系同源关系的快速功能注释
**时间复杂度**: O(n * m)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/molbev/msx148](https://doi.org/10.1093/molbev/msx148)
**实现**: [https://github.com/eggnogdb/eggnog-mapper](https://github.com/eggnogdb/eggnog-mapper)
**相关工具**: InterProScan, BLAST+, KofamKOALA
**标签**: `orthology` `go-annotation` `kegg` `fast`


#### KofamKOALA (2020)

基于 KEGG Ortholog 隐马尔可夫模型配置文件的功能注释方法，可为蛋白序列快速分配 KO 编号和代谢通路信息。
该工具在灵敏度与精确度之间取得平衡，适合微生物基因组和宏基因组数据的高通量功能注释。

**用途**: 基于 KEGG Ortholog 模型进行蛋白功能与通路注释
**时间复杂度**: O(n * m)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/bioinformatics/btz859](https://doi.org/10.1093/bioinformatics/btz859)
**实现**: [https://github.com/takaram/kofam_scan](https://github.com/takaram/kofam_scan)
**相关工具**: eggNOG-mapper, InterProScan, HMMER
**标签**: `kegg` `orthology` `annotation` `pathway-analysis`


#### OrthoFinder (2019)

面向多物种蛋白组比较的直系同源推断工具，可自动构建 orthogroup 并辅助功能转移与基因家族进化分析。
该方法在大规模比较基因组研究中广泛应用，适合将功能注释扩展到非模式物种和新组装基因组。

**用途**: 基于直系同源群推断进行跨物种功能注释与基因家族分析
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1186/s13059-019-1832-y](https://doi.org/10.1186/s13059-019-1832-y)
**实现**: [https://github.com/davidemms/OrthoFinder](https://github.com/davidemms/OrthoFinder)
**相关工具**: eggNOG-mapper, BLAST+, DIAMOND
**标签**: `orthology` `comparative-genomics` `gene-family` `annotation`


#### Prokka (2014)

面向原核生物基因组的快速自动化注释工具，能够在短时间内完成细菌和古菌基因组的全面功能注释。
该工具整合了 Prodigal、BLAST+ 和 HMMER 等多个组件，为微生物基因组提供标准化的注释输出。

**用途**: 快速自动化完成原核生物基因组功能注释
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btu153](https://doi.org/10.1093/bioinformatics/btu153)
**实现**: [https://github.com/tseemann/prokka](https://github.com/tseemann/prokka)
**相关工具**: Bakta, Prodigal, RAST
**标签**: `prokaryotic` `annotation` `pipeline` `rapid`


#### Bakta (2021)

面向细菌基因组的快速标准化注释工具，提供高质量的基因预测和功能注释结果。
该工具整合了多个精选数据库，输出格式与 NCBI 和 ENA 标准兼容，适合大规模微生物基因组注释项目。

**用途**: 细菌基因组的快速标准化功能注释
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btab123](https://doi.org/10.1093/bioinformatics/btab123)
**实现**: [https://github.com/oschwengers/bakta](https://github.com/oschwengers/bakta)
**相关工具**: Prokka, Prodigal, PGAP
**标签**: `prokaryotic` `annotation` `standardized` `database`


### 结构域方法 (Domain-Based)

基于蛋白质结构域的功能注释


#### HMMER (2011)

基于隐马尔可夫模型的序列分析算法，使用概率模型检测远程同源序列和蛋白质结构域。
该方法比简单的序列比对更敏感，能够发现进化距离较远的同源关系。

**用途**: 蛋白质结构域识别和远程同源检测
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1371/journal.pcbi.1002195](https://doi.org/10.1371/journal.pcbi.1002195)
**实现**: [http://hmmer.org/](http://hmmer.org/)
**相关工具**: Pfam, InterProScan, SMART
**标签**: `hmm` `domain-detection` `remote-homology` `probabilistic`


#### InterProScan (2014)

综合性蛋白质功能注释平台，整合多个签名数据库进行蛋白质结构域、家族和功能位点预测。
该工具统一了 Pfam、PROSITE、Gene3D 等十余个数据库的分析，提供一站式功能注释服务。

**用途**: 多数据库整合的蛋白质功能注释
**时间复杂度**: O(m * d)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/bioinformatics/btu031](https://doi.org/10.1093/bioinformatics/btu031)
**实现**: [https://github.com/ebi-pf-team/interproscan](https://github.com/ebi-pf-team/interproscan)
**相关工具**: HMMER, Pfam, eggNOG-mapper
**标签**: `multi-database` `domain-detection` `go-annotation` `comprehensive`


#### PfamScan (2011)

基于 Pfam 蛋白家族数据库和 HMM profile 的结构域注释工具，可识别蛋白序列中的保守结构域与功能模块。
该方法常与 HMMER 联合使用，为蛋白功能推断、家族分类和结构域组合分析提供标准化结果。

**用途**: 基于 Pfam profile 进行蛋白结构域识别与功能注释
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/nar/gkr367](https://doi.org/10.1093/nar/gkr367)
**实现**: [https://github.com/aziele/pfam_scan](https://github.com/aziele/pfam_scan)
**相关工具**: HMMER, InterProScan, SMART
**标签**: `domain-detection` `pfam` `protein-family` `profile-hmm`


#### InterPro (2014)

整合蛋白质家族与结构域的综合数据库，汇集 Pfam、CDD、SMART 等多个签名数据库的蛋白特征信息。
该数据库为蛋白质功能分类和结构域注释提供统一的标准资源，广泛应用于基因组注释和功能基因组研究。

**用途**: 集成蛋白质家族与结构域签名数据库
**时间复杂度**: O(m * d)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1093/nar/gkz961](https://doi.org/10.1093/nar/gkz961)
**相关工具**: InterProScan, Pfam, HMMER
**标签**: `database` `domain` `protein-family` `integrated`


#### SignalP (2019)

基于深度神经网络的信号肽预测工具，能够准确识别蛋白质 N 端的信号肽序列及其剪切位点。
该方法利用深度学习模型显著提升了信号肽预测的灵敏度和精确度，适用于分泌蛋白的高通量筛选。

**用途**: 利用深度学习预测蛋白质信号肽及剪切位点
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-019-0036-z](https://doi.org/10.1038/s41587-019-0036-z)
**相关工具**: TMHMM, Phobius, DeepSig
**标签**: `signal-peptide` `deep-learning` `secretion` `prediction`


#### TMHMM (2001)

基于隐马尔可夫模型的跨膜螺旋预测工具，可识别蛋白质序列中的跨膜区域及其拓扑结构。
该方法通过概率建模预测膜蛋白的跨膜螺旋数量和位置，是膜蛋白结构与功能研究的基础工具。

**用途**: 使用隐马尔可夫模型预测蛋白质跨膜螺旋结构
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1016/S0022-2836(01)51020-X](https://doi.org/10.1016/S0022-2836(01)51020-X)
**相关工具**: Phobius, SignalP, TOPCONS
**标签**: `transmembrane` `hmm` `membrane-protein` `prediction`


## 数据压缩 (Data Compression)

压缩生物信息学数据的算法


### 通用压缩 (General Compression)

通用数据压缩格式


#### GZIP for FASTQ (1992)

基于 DEFLATE 算法的通用数据压缩方法，广泛用于压缩 FASTQ 格式的测序数据。
该方法压缩比适中，兼容性好，是生物信息学数据存储的标准压缩格式。

**用途**: 测序数据的通用压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.17487/RFC1952](https://doi.org/10.17487/RFC1952)
**相关工具**: gzip, pigz, bgzip
**标签**: `lossless` `general-purpose` `standard` `fastq`


#### BGZF and Tabix (2011)

面向基因组区间文件的块压缩与随机索引方案，可对 VCF、BED 和 GFF 等文本格式实现按区域快速访问。
该方法是群体遗传学和变异分析工作流中的事实标准，使大规模文本数据在保持压缩的同时仍便于检索。

**用途**: 对基因组区间文件进行块压缩与随机区域访问
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.1093/bioinformatics/btq671](https://doi.org/10.1093/bioinformatics/btq671)
**实现**: [https://github.com/samtools/htslib](https://github.com/samtools/htslib)
**相关工具**: gzip, CRAM, htslib
**标签**: `block-compression` `indexing` `random-access` `genomics`


### 专用压缩 (Specialized Compression)

针对特定生物数据格式的压缩方法


#### CRAM (2011)

专为比对数据设计的参考序列压缩格式，通过存储与参考序列的差异实现高压缩比。
该方法可将 BAM 文件压缩至原大小的 40-60%，是大规模测序项目的首选存储格式。

**用途**: 比对数据的高效压缩存储
**时间复杂度**: O(n)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1093/nar/gkq1373](https://doi.org/10.1093/nar/gkq1373)
**实现**: [https://github.com/samtools/htslib](https://github.com/samtools/htslib)
**相关工具**: samtools, htslib, cramtools
**标签**: `reference-based` `alignment` `bam` `efficient`


#### Genozip (2021)

专为基因组数据设计的高性能压缩工具，支持 FASTQ、BAM、VCF 等多种格式的无损压缩。
该方法利用基因组数据的特殊结构实现远超通用压缩的压缩比，支持随机访问和加密。

**用途**: 基因组数据的高压缩比无损压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.1093/bioinformatics/btab102](https://doi.org/10.1093/bioinformatics/btab102)
**实现**: [https://github.com/divonlan/genozip](https://github.com/divonlan/genozip)
**相关工具**: gzip, CRAM, Spring
**标签**: `multi-format` `high-ratio` `random-access` `encryption`


#### SPRING (2019)

专为 FASTQ 读段设计的无损压缩方法，通过重排序、基于参考的编码思想和质量值建模获得高压缩比。
该方法在大规模测序项目中能显著降低存储成本，是 FASTQ 专用压缩领域的重要代表工具。

**用途**: FASTQ 读段及质量值的高比率无损压缩
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btz526](https://doi.org/10.1093/bioinformatics/btz526)
**实现**: [https://github.com/shubhamchandak94/SPRING](https://github.com/shubhamchandak94/SPRING)
**相关工具**: Genozip, gzip, fqzcomp
**标签**: `fastq` `specialized-compression` `high-ratio` `lossless`


#### DSRC (2013)

面向 FASTQ 文件的专用压缩算法，分别针对序列、质量值和标识符设计编码策略以提升压缩效率。
该方法兼顾压缩速度和压缩率，适合高通量测序中心对海量原始读段数据进行归档与传输。

**用途**: FASTQ 数据的高速专用无损压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.1093/bioinformatics/btt214](https://doi.org/10.1093/bioinformatics/btt214)
**实现**: [https://github.com/refresh-bio/DSRC](https://github.com/refresh-bio/DSRC)
**相关工具**: SPRING, Genozip, gzip
**标签**: `fastq` `specialized-compression` `archival` `fast`


#### fqzcomp (2014)

专门针对 FASTQ 质量分数设计的压缩算法，通过对质量值进行上下文建模和算术编码实现高效压缩。
该方法支持流式处理，在保持解码速度的同时能将质量分数压缩至原始大小的极小比例，是 FASTQ 压缩领域的经典工具。

**用途**: FASTQ 质量分数的高效无损压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.1093/bioinformatics/btu537](https://doi.org/10.1093/bioinformatics/btu537)
**相关工具**: SPRING, Genozip, DSRC
**标签**: `fastq` `quality-score` `lossless` `streaming`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### SPRING Compress (2020)

针对大规模 FASTQ 数据集开发的重排序压缩工具，通过读段排序和参考序列编码实现极高的压缩比。
该方法能够处理海量测序数据，在百万级乃至亿级读段规模下仍保持高效的压缩性能和可接受的运行时间。

**用途**: 大规模 FASTQ 数据集的高比率重排序压缩
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btaa044](https://doi.org/10.1093/bioinformatics/btaa044)
**实现**: [https://github.com/shubhamchandak94/spring](https://github.com/shubhamchandak94/spring)
**相关工具**: SPRING, fqzcomp, Genozip
**标签**: `fastq` `reordering` `high-ratio` `scalable`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### MANGO (2018)

基于上下文建模的参考基因组无关序列压缩方法，通过学习序列局部统计特征实现基因组数据的高效压缩。
该方法无需参考基因组即可达到优秀的压缩比，适用于新物种或参考基因组不可用的场景。

**用途**: 无需参考基因组的基因组序列压缩
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41467-018-05612-6](https://doi.org/10.1038/s41467-018-05612-6)
**相关工具**: Genozip, CRAM, gzip
**标签**: `reference-free` `genome-compression` `context-modeling`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### Orione (2015)

利用参考辅助压缩的 FASTQ 和 SAM 格式压缩工具，将读段比对到参考序列后仅存储差异信息。该方法在有高质量参考基因组时压缩效果极佳。

**用途**: 参考辅助的 FASTQ/SAM 压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.1109/DCC.2015.45](https://doi.org/10.1109/DCC.2015.45)
**相关工具**: CRAM, Genozip, Spring
**标签**: `reference-assisted` `fastq` `sam` `archival`
**难度**: 进阶 (Intermediate)
**实现语言**: C


## 单细胞基因组学 (Single-Cell Genomics)

单细胞水平的基因组和转录组分析算法


### 数据预处理 (Preprocessing)

单细胞数据的质控、标准化和预处理


#### Cell Ranger (2017)

10x Genomics 开发的单细胞 RNA-seq 数据处理流水线，完成从原始数据到基因表达矩阵的全流程分析。
该工具集成了比对、细胞条码识别、UMI 计数等步骤，是单细胞数据预处理的行业标准。

**用途**: 单细胞 RNA-seq 数据预处理和定量
**时间复杂度**: O(n * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/ncomms14049](https://doi.org/10.1038/ncomms14049)
**实现**: [https://github.com/10XGenomics/cellranger](https://github.com/10XGenomics/cellranger)
**相关工具**: STARsolo, Alevin, Kallisto-bustools
**标签**: `10x-genomics` `preprocessing` `umi` `pipeline`


#### STARsolo (2021)

基于 STAR 比对器扩展的单细胞 RNA-seq 预处理方法，可在一次流程中完成比对、细胞条码解析和 UMI 计数。
该工具兼具高速度与对 10x 等主流协议的兼容性，是 Cell Ranger 之外的重要开源替代方案。

**用途**: 单细胞 RNA-seq 数据的快速比对与表达矩阵生成
**时间复杂度**: O(n * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1093/gigascience/giab074](https://doi.org/10.1093/gigascience/giab074)
**实现**: [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
**相关工具**: Cell Ranger, Alevin, Kallisto-bustools
**标签**: `preprocessing` `alignment` `umi` `open-source`


#### Alevin (2019)

基于轻量级映射与 UMI 去重策略的单细胞 RNA-seq 定量工具，可直接从 FASTQ 生成细胞和基因表达矩阵。
该方法速度快、内存占用低，并与 Salmon 生态紧密结合，是 droplet-based 单细胞预处理的重要开源方案。

**用途**: 单细胞 RNA-seq 数据的快速定量与 UMI 计数
**时间复杂度**: O(n * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41592-019-0465-8](https://doi.org/10.1038/s41592-019-0465-8)
**实现**: [https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)
**相关工具**: STARsolo, Cell Ranger, Kallisto-bustools
**标签**: `preprocessing` `umi` `lightweight-mapping` `quantification`


#### kallisto | bustools (2021)

基于伪比对的快速单细胞 RNA-seq 预处理流程，利用 kallisto 索引和 bustools 流式处理实现轻量级定量。
该方法内存占用极低，处理速度快，支持多种单细胞平台，是大规模单细胞数据预处理的高效替代方案。

**用途**: 快速轻量的单细胞 RNA-seq 数据预处理
**时间复杂度**: O(n * k)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1038/s41587-021-00870-2](https://doi.org/10.1038/s41587-021-00870-2)
**相关工具**: Cell Ranger, STARsolo, Alevin
**标签**: `preprocessing` `pseudoalignment` `fast` `lightweight`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### alevin-fry (2022)

基于轻量级比对的内存高效单细胞定量工具，通过简化伪比对和轻量级分辨算法大幅降低内存需求。
该方法在保持定量准确性的同时将内存占用降至传统方法的十分之一，适合在普通计算环境下处理大规模单细胞数据集。

**用途**: 内存高效的单细胞 RNA-seq 定量
**时间复杂度**: O(n * k)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1038/s41592-022-01408-3](https://doi.org/10.1038/s41592-022-01408-3)
**相关工具**: Alevin, kallisto-bustools, STARsolo
**标签**: `quantification` `memory-efficient` `simpleaf` `frugal`
**难度**: 进阶 (Intermediate)
**实现语言**: Rust


### 细胞聚类与注释 (Cell Clustering & Annotation)

细胞类型识别和聚类分析


#### Seurat (2015)

综合性单细胞数据分析框架，提供从质控、标准化、降维到细胞聚类和差异表达的完整分析流程。
该工具支持多模态数据整合（RNA + ATAC + protein），是 R 语言生态中最主流的单细胞分析工具。

**用途**: 单细胞多模态数据分析与整合
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1016/j.cell.2021.04.048](https://doi.org/10.1016/j.cell.2021.04.048)
**实现**: [https://github.com/satijalab/seurat](https://github.com/satijalab/seurat)
**相关工具**: Scanpy, Monocle3, scVI
**标签**: `clustering` `multi-modal` `integration` `comprehensive`


#### Scanpy (2018)

基于 Python 的可扩展单细胞分析工具包，使用 AnnData 数据结构高效处理大规模单细胞数据。
该工具提供完整的分析流程，支持 GPU 加速，与 scverse 生态深度集成。

**用途**: 可扩展的单细胞数据分析
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1186/s13059-017-1382-0](https://doi.org/10.1186/s13059-017-1382-0)
**实现**: [https://github.com/scverse/scanpy](https://github.com/scverse/scanpy)
**相关工具**: Seurat, scVI, AnnData
**标签**: `python` `scalable` `scverse` `gpu-accelerated`


#### scVI (2018)

基于变分自编码器的单细胞数据分析深度学习框架，使用概率生成模型处理数据噪声和批次效应。
该方法能高效整合多个数据集，支持差异表达分析和缺失值插补等下游任务。

**用途**: 基于深度学习的单细胞数据建模与整合
**时间复杂度**: O(c * g * e)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41592-018-0229-2](https://doi.org/10.1038/s41592-018-0229-2)
**实现**: [https://github.com/scverse/scvi-tools](https://github.com/scverse/scvi-tools)
**相关工具**: Scanpy, Harmony, LIGER
**标签**: `deep-learning` `vae` `batch-correction` `probabilistic`


#### Harmony (2019)

面向多批次单细胞数据的整合方法，在低维嵌入空间中迭代校正批次效应并保留生物学信号。
该方法能与 Seurat、Scanpy 等分析流程无缝结合，是跨样本和跨平台单细胞整合分析的常用工具。

**用途**: 多批次单细胞数据的批次校正与整合
**时间复杂度**: O(c * k)
**空间复杂度**: O(c * k)
**论文**: [https://doi.org/10.1038/s41592-019-0619-0](https://doi.org/10.1038/s41592-019-0619-0)
**实现**: [https://github.com/immunogenomics/harmony](https://github.com/immunogenomics/harmony)
**相关工具**: Seurat, Scanpy, scVI
**标签**: `batch-correction` `integration` `embedding` `single-cell`


#### Monocle 3 (2019)

面向单细胞转录组的轨迹推断与细胞状态分析框架，可学习发育路径、伪时间顺序和分化分支结构。
该方法常用于研究细胞命运转换和动态生物过程，与聚类和降维分析形成互补的下游解释能力。

**用途**: 单细胞数据的轨迹推断与伪时间分析
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/nbt.4402](https://doi.org/10.1038/nbt.4402)
**实现**: [https://github.com/cole-trapnell-lab/monocle3](https://github.com/cole-trapnell-lab/monocle3)
**相关工具**: Seurat, Scanpy, Slingshot
**标签**: `trajectory-inference` `pseudotime` `differentiation` `single-cell`


#### scVI-tools (2023)

基于深度生成模型的单细胞组学分析框架，利用变分自编码器架构处理单细胞数据中的噪声和批次效应。
该工具集提供了多种模型变体支持聚类、注释和数据整合任务，是 scverse 生态中深度学习方法的核心实现。

**用途**: 深度生成模型驱动的单细胞组学分析
**时间复杂度**: O(c * g * e)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41587-021-01206-w](https://doi.org/10.1038/s41587-021-01206-w)
**实现**: [https://github.com/scverse/scvi-tools](https://github.com/scverse/scvi-tools)
**相关工具**: Scanpy, Seurat, scANVI
**标签**: `variational-autoencoder` `deep-learning` `batch-correction` `probabilistic`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### scANVI (2021)

结合变分自编码器与半监督学习的单细胞数据注释方法，能利用少量已知标签对大量未标注细胞进行自动类型推断。
该方法在保留 scVI 批次校正能力的同时引入细胞类型信息，显著提升跨数据集注释的准确性和可解释性。

**用途**: 基于半监督深度学习的单细胞类型注释
**时间复杂度**: O(c * g * e)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41467-021-25548-w](https://doi.org/10.1038/s41467-021-25548-w)
**相关工具**: scVI, CellTypist, scArches
**标签**: `semi-supervised` `annotation` `deep-learning` `vae`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### scArches (2022)

基于模型手术的单细胞参考映射方法，能在预训练模型上直接整合新数据而无需从头再训练。
该方法通过结构化变分自编码器的参数转移实现高效的查询数据映射，支持增量学习和多参考场景。

**用途**: 单细胞数据的参考映射与迁移学习
**时间复杂度**: O(c * g * e)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41467-022-29299-4](https://doi.org/10.1038/s41467-022-29299-4)
**相关工具**: scVI, scANVI, Harmony
**标签**: `reference-mapping` `transfer-learning` `surgery` `integration`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### CellTypist (2022)

基于逻辑回归模型的自动化细胞类型注释工具，使用大规模参考数据集快速推断未知单细胞样本的细胞类型。
该方法支持在线学习和多级注释，在免疫细胞分类等场景中具有较高的准确性和运行效率。

**用途**: 基于逻辑回归的自动化细胞类型注释
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1016/j.immuni.2022.07.010](https://doi.org/10.1016/j.immuni.2022.07.010)
**相关工具**: scANVI, scVI, Seurat
**标签**: `cell-type` `annotation` `logistic-regression` `reference-based`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### SCENIC (2020)

单细胞基因调控网络推断方法，通过整合共表达模块和转录因子结合基序信息识别细胞状态特异性调控关系。
该方法能从单细胞表达矩阵中自动发现活性转录因子及其调控靶基因，是研究细胞异质性调控机制的重要工具。

**用途**: 单细胞基因调控网络推断与分析
**时间复杂度**: O(c * g^2)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/nmeth.4463](https://doi.org/10.1038/nmeth.4463)
**相关工具**: Scanpy, Seurat, GRNBoost
**标签**: `regulatory-network` `transcription-factor` `grn` `gene-regulatory`
**难度**: 高级 (Advanced)
**实现语言**: Python, R


## 宏基因组学 (Metagenomics)

微生物群落的基因组分析算法


### 物种分类 (Taxonomic Profiling)

微生物物种组成鉴定


#### Kraken2 (2019)

基于 k-mer 精确匹配的超快速物种分类工具，使用紧凑哈希表在数分钟内完成宏基因组样本的物种鉴定。
该方法速度极快且准确性高，支持自定义参考数据库，是宏基因组物种分类的首选工具。

**用途**: 基于 k-mer 的超快速宏基因组物种分类
**时间复杂度**: O(n * k)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1186/s13059-019-1891-0](https://doi.org/10.1186/s13059-019-1891-0)
**实现**: [https://github.com/DerrickWood/kraken2](https://github.com/DerrickWood/kraken2)
**相关工具**: Bracken, Centrifuge, CLARK
**标签**: `k-mer` `classification` `fast` `taxonomic`


#### MetaPhlAn (2012)

基于标记基因的宏基因组物种组成分析工具，使用物种特异性标记序列精确量化微生物丰度。
该方法无需组装即可获得准确的物种丰度信息，内存占用低，适合大规模样本分析。

**用途**: 基于标记基因的微生物组成和丰度定量
**时间复杂度**: O(n * m)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1038/nmeth.2066](https://doi.org/10.1038/nmeth.2066)
**实现**: [https://github.com/biobakery/MetaPhlAn](https://github.com/biobakery/MetaPhlAn)
**相关工具**: Kraken2, mOTUs, HUMAnN
**标签**: `marker-gene` `abundance` `low-memory` `species-level`


#### Centrifuge (2016)

面向宏基因组样本的快速分类方法，利用压缩索引在大规模参考数据库上进行高效序列归类。
该工具兼顾速度和内存占用，适合在复杂微生物群落中进行物种鉴定和未知样本初筛。

**用途**: 大规模参考库上的快速宏基因组物种分类
**时间复杂度**: O(n * log d)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1101/gr.210641.116](https://doi.org/10.1101/gr.210641.116)
**实现**: [https://github.com/DaehwanKimLab/centrifuge](https://github.com/DaehwanKimLab/centrifuge)
**相关工具**: Kraken2, Kaiju, CLARK
**标签**: `classification` `compressed-index` `low-memory` `taxonomic`


#### Kaiju (2016)

基于蛋白水平比对的宏基因组分类工具，通过在翻译后的读段与参考蛋白数据库之间搜索最大精确匹配来提高远缘物种识别能力。
该方法对进化距离较远或核苷酸保守性较低的样本更敏感，常用于复杂环境样本的分类分析。

**用途**: 基于蛋白水平匹配提升宏基因组物种分类灵敏度
**时间复杂度**: O(n * log d)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1038/ncomms11257](https://doi.org/10.1038/ncomms11257)
**实现**: [https://github.com/bioinformatics-centre/kaiju](https://github.com/bioinformatics-centre/kaiju)
**相关工具**: Kraken2, Centrifuge, DIAMOND
**标签**: `protein-level` `classification` `sensitive` `taxonomic`


#### mOTUs (2017)

基于通用标记基因的微生物物种定量方法，利用核糖体蛋白基因的保守区域进行物种鉴定和丰度估计。
该方法不依赖完整参考基因组即可实现跨样品可比的物种水平定量，在海洋和肠道微生物组研究中被广泛采用。

**用途**: 基于通用标记基因的微生物物种定量
**时间复杂度**: O(n * m)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1186/s40168-017-0357-4](https://doi.org/10.1186/s40168-017-0357-4)
**相关工具**: MetaPhlAn, Kraken2, QIIME2
**标签**: `marker-gene` `profiling` `universal` `species-level`
**难度**: 进阶 (Intermediate)
**实现语言**: Python, C


#### QIIME 2 (2019)

微生物组生物信息学综合分析平台，提供从原始序列处理到多样性分析和功能注释的完整可重复分析流程。
该平台支持扩增子和宏基因组数据，集成了序列质控、分类、聚类和统计分析等多种功能模块。

**用途**: 微生物组数据的综合分析平台
**时间复杂度**: O(n * d)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-019-0209-9](https://doi.org/10.1038/s41587-019-0209-9)
**相关工具**: mothur, MetaPhlAn, Kraken2
**标签**: `pipeline` `microbiome` `diversity` `amplicon`
**难度**: 入门 (Beginner)
**实现语言**: Python


#### Bracken (2017)

基于贝叶斯统计框架的物种丰度估计方法，在 Kraken 分类结果基础上利用 k-mer 分布特征校正物种级丰度。
该方法通过概率模型将读段重新分配到各分类层级，显著提高物种丰度估计的准确性，是 Kraken 流程的重要补充。

**用途**: 基于贝叶斯方法的 Kraken 物种丰度校正
**时间复杂度**: O(n)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.7717/peerj-cs.116](https://doi.org/10.7717/peerj-cs.116)
**相关工具**: Kraken2, MetaPhlAn, Centrifuge
**标签**: `abundance-estimation` `bayesian` `kraken` `species-level`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### MetaPhlAn 4 (2023)

基于进化枝特异性标记基因的增强型物种定量工具，通过扩展标记基因数据库和改进比对策略提升分类灵敏度。
该方法在 MetaPhlAn 基础上新增了病毒和古菌标记基因支持，提供更全面的微生物群落组成分析能力。

**用途**: 基于增强标记基因的微生物群落定量
**时间复杂度**: O(n * m)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1038/s41587-023-01688-0](https://doi.org/10.1038/s41587-023-01688-0)
**相关工具**: Kraken2, mOTUs, Bracken
**标签**: `marker-gene` `profiling` `enhanced` `clade-specific`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### MetaBAT 2 (2019)

利用四核苷酸频率和覆盖度信息的自适应宏基因组分箱方法，通过概率模型将组装重叠群聚类为微生物基因组单元。
该方法在精度和召回率之间实现了良好平衡，支持深度和浅层测序数据，是环境微生物学研究中 MAG 构建的主力工具。

**用途**: 自适应宏基因组重叠群分箱与基因组恢复
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/s13059-019-1893-y](https://doi.org/10.1186/s13059-019-1893-y)
**相关工具**: MaxBin 2, CONCOCT, DAS Tool
**标签**: `binning` `metagenome` `adaptive` `contig`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


### 功能分析 (Functional Profiling)

微生物群落功能分析


#### HUMAnN (2014)

宏基因组功能分析流水线，将测序读段映射到基因家族和代谢通路，量化微生物群落的功能潜力。
该方法整合了物种分类和功能注释，能同时提供群落水平和物种水平的功能组成。

**用途**: 宏基因组功能组成和代谢通路分析
**时间复杂度**: O(n * d)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1371/journal.pcbi.1002358](https://doi.org/10.1371/journal.pcbi.1002358)
**实现**: [https://github.com/biobakery/humann](https://github.com/biobakery/humann)
**相关工具**: MetaPhlAn, KEGG, eggNOG-mapper
**标签**: `pathway-analysis` `gene-family` `functional` `pipeline`


#### MetaBAT 2 (2019)

基于 tetranucleotide 频率和覆盖度信息的宏基因组 binning 工具，用于从混合组装结果中恢复微生物基因组。
该方法在精度和召回率之间取得良好平衡，是构建 MAGs 流程中最常用的自动分箱工具之一。

**用途**: 从宏基因组组装结果中进行自动分箱和基因组恢复
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.7717/peerj.7359](https://doi.org/10.7717/peerj.7359)
**实现**: [https://bitbucket.org/berkeleylab/metabat/src/master/](https://bitbucket.org/berkeleylab/metabat/src/master/)
**相关工具**: MaxBin 2, CONCOCT, CheckM
**标签**: `binning` `mags` `coverage` `tetranucleotide`


#### MaxBin 2 (2016)

利用覆盖度和组成偏好信息的自动分箱方法，通过期望最大化算法从宏基因组组装序列中恢复单个微生物基因组。
该工具在低丰度菌群和复杂环境样本中表现稳健，是宏基因组 binning 与 MAG 构建中的经典方法之一。

**用途**: 基于覆盖度与组成特征进行宏基因组自动分箱
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btv638](https://doi.org/10.1093/bioinformatics/btv638)
**实现**: [https://sourceforge.net/projects/maxbin2/](https://sourceforge.net/projects/maxbin2/)
**相关工具**: MetaBAT 2, CONCOCT, CheckM
**标签**: `binning` `expectation-maximization` `mags` `metagenome`


#### HUMAnN 3 (2018)

宏基因组功能谱分析流水线，通过整合物种分类和泛基因组映射实现基因家族和代谢通路的定量分析。
该方法采用两阶段策略先进行物种丰度估计再进行功能注释，能同时提供群落和物种水平的功能组成信息。

**用途**: 宏基因组功能谱和代谢通路的定量分析
**时间复杂度**: O(n * d)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1038/s41592-018-0176-y](https://doi.org/10.1038/s41592-018-0176-y)
**相关工具**: MetaPhlAn, KEGG, eggNOG-mapper
**标签**: `functional-profiling` `pathway` `gene-families` `metabolic`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### metaPOST (2021)

宏基因组组装后处理与精修工具，通过整合覆盖度一致性和连接图信息检测并纠正组装中的错误和嵌合体重叠群。
该方法能显著提升宏基因组组装的质量指标，减少假阳性重叠群对下游分析的干扰。

**用途**: 宏基因组组装结果的后处理与质量提升
**时间复杂度**: O(n * c)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41592-021-01159-7](https://doi.org/10.1038/s41592-021-01159-7)
**相关工具**: MetaBAT 2, CheckM, DAS Tool
**标签**: `post-processing` `refinement` `assembly` `quality`
**难度**: 高级 (Advanced)
**实现语言**: Python


## 表观基因组学 (Epigenomics)

分析表观遗传修饰的算法


### ChIP-seq 分析 (ChIP-seq Analysis)

染色质免疫共沉淀测序分析


#### MACS2 (2008)

ChIP-seq 峰值检测的标准工具，使用泊松分布模型识别蛋白质-DNA 结合位点和组蛋白修饰区域。
该方法能有效校正局部偏差和背景噪声，支持窄峰和宽峰检测模式。

**用途**: ChIP-seq 数据的峰值检测和富集分析
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/gb-2008-9-9-r137](https://doi.org/10.1186/gb-2008-9-9-r137)
**实现**: [https://github.com/macs3-project/MACS](https://github.com/macs3-project/MACS)
**相关工具**: HOMER, SICER, ENCODE
**标签**: `peak-calling` `chip-seq` `histone` `transcription-factor`


#### ChromHMM (2012)

基于隐马尔可夫模型的染色质状态注释工具，整合多种组蛋白修饰信号自动学习和标注染色质状态。
该方法能发现启动子、增强子、异染色质等功能区域，是表观基因组注释的标准方法。

**用途**: 染色质状态自动发现和基因组注释
**时间复杂度**: O(n * s^2)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1038/nmeth.1906](https://doi.org/10.1038/nmeth.1906)
**实现**: [https://github.com/jernst98/ChromHMM](https://github.com/jernst98/ChromHMM)
**相关工具**: Segway, ENCODE, EpiCSeg
**标签**: `hmm` `chromatin-state` `histone` `annotation`


#### HMMRATAC (2019)

专为 ATAC-seq 设计的开放染色质识别算法，使用隐马尔可夫模型整合不同片段长度信号进行峰值检测。
该方法能同时刻画核小体缺失区与周围核小体结构，在开放染色质分析中具有较高分辨率和稳健性。

**用途**: 基于 ATAC-seq 信号识别开放染色质区域
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/gkz533](https://doi.org/10.1093/nar/gkz533)
**实现**: [https://github.com/LiuLabUB/HMMRATAC](https://github.com/LiuLabUB/HMMRATAC)
**相关工具**: MACS2, Genrich, ATACseqQC
**标签**: `atac-seq` `hmm` `peak-calling` `open-chromatin`


#### MACS2 (2012)

基于模型的 ChIP-seq 数据分析工具，使用泊松分布和局部偏差校正策略精确识别蛋白质-DNA 相互作用的峰值区域。
该方法支持窄峰和宽峰检测，能有效处理不同信噪比的 ChIP-seq 数据，是表观基因组学峰值检测的行业标准。

**用途**: ChIP-seq 数据的模型驱动峰值检测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/gb-2012-13-9-r76](https://doi.org/10.1186/gb-2012-13-9-r76)
**相关工具**: HOMER, Genrich, SICER
**标签**: `chip-seq` `peak-calling` `model-based` `fragment`
**难度**: 入门 (Beginner)
**实现语言**: Python


#### Genrich (2019)

快速的基因组富集检测工具，通过信号与对照样本的比较在 ChIP-seq 和 ATAC-seq 数据中识别显著富集区域。
该方法运行速度极快，支持多组生物学重复的合并分析，适用于大规模表观基因组学筛选项目。

**用途**: ChIP-seq 和 ATAC-seq 数据的快速富集检测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://arxiv.org/abs/1901.09818](https://arxiv.org/abs/1901.09818)
**相关工具**: MACS2, HMMRATAC, SICER
**标签**: `chip-seq` `peak-calling` `fast` `atac-seq`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### HOMER (2010)

综合性 ChIP-seq 数据分析平台，集成峰值检测、从头基序发现和已知基序富集分析等多种功能模块。
该方法在转录因子结合位点鉴定和基序分析方面表现突出，支持多种表观基因组学实验设计的下游解析。

**用途**: ChIP-seq 数据分析与转录因子基序发现
**时间复杂度**: O(n * m)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1016/S0022-2836(02)00917-8](https://doi.org/10.1016/S0022-2836(02)00917-8)
**相关工具**: MACS2, MEME, ChromHMM
**标签**: `motif-discovery` `chip-seq` `transcription-factor` `de-novo`
**难度**: 进阶 (Intermediate)
**实现语言**: Perl, C++


#### DiffBind (2011)

基于统计学框架的 ChIP-seq 差异结合分析工具，通过整合多组样本的峰值和读段计数检测条件间的显著结合变化。
该方法支持 DESeq2 和 edgeR 等主流差异分析引擎，能有效控制批次效应和混杂因素。

**用途**: ChIP-seq 样本间的差异结合位点检测
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btp340](https://doi.org/10.1093/bioinformatics/btp340)
**相关工具**: DESeq2, edgeR, MACS2
**标签**: `differential-binding` `chip-seq` `differential-analysis` `statistical`
**难度**: 进阶 (Intermediate)
**实现语言**: R


### 甲基化分析 (Methylation Analysis)

DNA 甲基化数据分析


#### Bismark (2011)

亚硫酸氢盐测序数据的比对和甲基化分析工具，处理 C-to-T 转换后的序列比对和甲基化水平量化。
该方法能区分 CpG、CHG、CHH 不同类型的甲基化，是 DNA 甲基化分析的核心工具。

**用途**: 亚硫酸氢盐测序数据的比对和甲基化定量
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1093/bioinformatics/btr167](https://doi.org/10.1093/bioinformatics/btr167)
**实现**: [https://github.com/FelixKrueger/Bismark](https://github.com/FelixKrueger/Bismark)
**相关工具**: BSseeker2, methylKit, bwa-meth
**标签**: `bisulfite-seq` `methylation` `cpg` `epigenetic`


#### methylKit (2012)

面向高通量甲基化测序的分析工具包，支持甲基化位点过滤、差异甲基化分析和功能区域注释。
该方法适合 RRBS 和全基因组亚硫酸氢盐测序数据，广泛用于比较不同样本间的 DNA 甲基化变化。

**用途**: 高通量甲基化测序数据的差异分析与注释
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/1471-2105-13-87](https://doi.org/10.1186/1471-2105-13-87)
**实现**: [https://github.com/al2na/methylKit](https://github.com/al2na/methylKit)
**相关工具**: Bismark, DSS, bsseq
**标签**: `methylation` `differential-analysis` `rrbs` `bisulfite-seq`


#### DSS (2014)

基于贝塔二项分布层次模型的差异甲基化分析方法，可在生物学重复之间稳健估计离散度并检测 DMR。
该方法适用于全基因组和靶向亚硫酸氢盐测序数据，是比较不同条件甲基化变化的常用统计框架。

**用途**: 基于层次统计模型检测差异甲基化位点和区域
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/biostatistics/kxu022](https://doi.org/10.1093/biostatistics/kxu022)
**实现**: [https://bioconductor.org/packages/DSS/](https://bioconductor.org/packages/DSS/)
**相关工具**: methylKit, bsseq, Bismark
**标签**: `methylation` `beta-binomial` `dmr` `statistical`


#### Bismark (2011)

亚硫酸氢盐测序数据的比对和甲基化分析工具，通过 C-to-T 转换双链比对策略处理亚硫酸氢盐转化后的序列。
该方法能同时鉴定 CpG、CHG 和 CHH 位点的甲基化状态，并提供详细的甲基化水平定量报告。

**用途**: 亚硫酸氢盐测序数据的比对和甲基化定量
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1093/bioinformatics/btr167](https://doi.org/10.1093/bioinformatics/btr167)
**相关工具**: BSseeker2, methylKit, bwa-meth
**标签**: `bisulfite` `methylation` `alignment` `epigenetics`
**难度**: 进阶 (Intermediate)
**实现语言**: Perl


#### methylKit (2012)

高通量甲基化测序数据分析的 Bioconductor 工具包，支持甲基化位点注释、差异分析和功能区域聚合统计。
该方法兼容 RRBS 和 WGBS 数据设计，提供灵活的覆盖度过滤和滑动窗口分析功能，是比较不同条件下甲基化变化的常用工具。

**用途**: 高通量甲基化测序数据的差异分析与功能注释
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/gb-2012-13-10-r87](https://doi.org/10.1186/gb-2012-13-10-r87)
**相关工具**: Bismark, DSS, bsseq
**标签**: `methylation` `bisulfite` `differential` `bioconductor`
**难度**: 进阶 (Intermediate)
**实现语言**: R


## 基因预测 (Gene Prediction)

基因结构预测和基因组注释算法


### 真核基因预测 (Eukaryotic Gene Prediction)

真核生物基因结构预测


#### AUGUSTUS (2003)

基于广义隐马尔可夫模型的真核基因预测工具，能准确预测基因结构包括外显子、内含子和 UTR。
该方法支持使用 RNA-seq 和蛋白质同源性作为外部提示信息，显著提高预测准确性。

**用途**: 真核生物基因结构从头预测
**时间复杂度**: O(n * s^2)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/bioinformatics/btg1080](https://doi.org/10.1093/bioinformatics/btg1080)
**实现**: [https://github.com/Gaius-Augustus/Augustus](https://github.com/Gaius-Augustus/Augustus)
**相关工具**: GeneMark, SNAP, GlimmerHMM
**标签**: `ghmm` `ab-initio` `exon-intron` `rna-seq-hints`


#### BRAKER (2016)

结合从头预测和证据驱动方法的真核基因注释流水线，自动整合 RNA-seq 和蛋白质数据训练基因预测模型。
该工具将 GeneMark 和 AUGUSTUS 有机结合，实现全自动的高精度基因结构注释。

**用途**: 全自动真核基因结构注释
**时间复杂度**: O(n * g)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btv661](https://doi.org/10.1093/bioinformatics/btv661)
**实现**: [https://github.com/Gaius-Augustus/BRAKER](https://github.com/Gaius-Augustus/BRAKER)
**相关工具**: AUGUSTUS, GeneMark-ET, MAKER
**标签**: `pipeline` `evidence-based` `automated` `rna-seq`


#### MAKER (2008)

面向真核基因组注释的整合式流水线，可结合 ab initio 预测、转录本证据和蛋白同源信息生成高质量基因模型。
该工具能够协调 AUGUSTUS、SNAP 等多个预测器，特别适合新测序物种的基因组注释与模型迭代优化。

**用途**: 整合多源证据进行真核基因组注释
**时间复杂度**: O(n * g)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/1471-2105-9-491](https://doi.org/10.1186/1471-2105-9-491)
**实现**: [https://github.com/Yandell-Lab/maker](https://github.com/Yandell-Lab/maker)
**相关工具**: AUGUSTUS, SNAP, BRAKER
**标签**: `annotation-pipeline` `evidence-based` `eukaryotic` `genome-annotation`


#### SNAP (2004)

面向真核基因组的 ab initio 基因预测工具，使用半隐马尔可夫模型识别外显子、内含子和起止密码子等基因结构特征。
该方法训练灵活、运行高效，常与 MAKER 等注释流水线结合用于新基因组的自动化基因模型构建。

**用途**: 基于半隐马尔可夫模型进行真核基因从头预测
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/1471-2105-5-59](https://doi.org/10.1186/1471-2105-5-59)
**实现**: [https://github.com/KorfLab/SNAP](https://github.com/KorfLab/SNAP)
**相关工具**: AUGUSTUS, MAKER, BRAKER
**标签**: `semi-hmm` `ab-initio` `eukaryotic` `gene-finding`


#### AUGUSTUS (2005)

基于广义隐马尔可夫模型的真核基因从头预测工具，能准确预测基因结构包括外显子、内含子、UTR 和剪接位点。
该方法支持整合 RNA-seq 和同源蛋白等外部证据作为提示信息，显著提高新基因组注释的预测准确性。

**用途**: 真核生物基因结构从头预测
**时间复杂度**: O(n * s^2)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/nar/gki356](https://doi.org/10.1093/nar/gki356)
**相关工具**: GeneMark, SNAP, BRAKER
**标签**: `gene-prediction` `eukaryotic` `hmm` `ab-initio`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


### 原核基因预测 (Prokaryotic Gene Prediction)

原核生物基因识别


#### Prodigal (2010)

高效的原核基因识别工具，使用动态规划算法自动学习物种特异性参数进行基因预测。
该方法无需训练数据即可准确预测蛋白编码基因，支持宏基因组模式处理混合物种数据。

**用途**: 原核生物蛋白编码基因快速预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/1471-2105-11-119](https://doi.org/10.1186/1471-2105-11-119)
**实现**: [https://github.com/hyattpd/Prodigal](https://github.com/hyattpd/Prodigal)
**相关工具**: Pyrodigal, GeneMark, Glimmer
**标签**: `prokaryotic` `self-training` `metagenome` `fast`


#### GeneMark (1993)

GeneMark 系列方法使用概率模型识别编码区与非编码区信号，是基因预测领域最经典的算法家族之一。
该方法覆盖原核、真核和宏基因组场景，为后续注释流程提供可靠的开放阅读框和基因边界预测。

**用途**: 基于统计模型进行基因结构与编码区预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/21.23.5668](https://doi.org/10.1093/nar/21.23.5668)
**实现**: [http://topaz.gatech.edu/GeneMark/](http://topaz.gatech.edu/GeneMark/)
**相关工具**: AUGUSTUS, BRAKER, Prodigal
**标签**: `hmm` `coding-potential` `gene-finding` `classic`


#### GLIMMER (1998)

面向细菌和古菌基因组的编码区识别工具，使用插值马尔可夫模型高效发现开放阅读框和起始位点。
该方法是原核基因预测的经典方案之一，在完整基因组和草图组装中都具有良好的准确性和计算效率。

**用途**: 原核基因组中的开放阅读框与基因边界预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/26.2.544](https://doi.org/10.1093/nar/26.2.544)
**实现**: [https://ccb.jhu.edu/software/glimmer/](https://ccb.jhu.edu/software/glimmer/)
**相关工具**: Prodigal, GeneMark, FragGeneScan
**标签**: `interpolated-markov-model` `prokaryotic` `gene-finding` `classic`


#### GeneMark-ES (2005)

自监督的真核和原核基因组基因预测工具，通过迭代训练概率模型自动识别编码区和基因边界。
该方法覆盖原核、真核和宏基因组等多种场景，是基因预测领域应用最广泛的算法家族之一。

**用途**: 基于概率模型的多物种基因预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/gki138](https://doi.org/10.1093/nar/gki138)
**相关工具**: AUGUSTUS, Prodigal, Glimmer
**标签**: `gene-prediction` `hmm` `prokaryotic` `self-training`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### Prodigal (2010)

高效的原核基因识别工具，使用动态规划和自训练策略自动学习物种特异性编码偏好性进行基因预测。
该方法无需外部训练数据即可准确预测蛋白编码基因，支持宏基因组模式处理混合物种组装数据。

**用途**: 原核生物蛋白编码基因的快速从头预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/1471-2105-11-119](https://doi.org/10.1186/1471-2105-11-119)
**相关工具**: GeneMark, Glimmer, FragGeneScan
**标签**: `gene-prediction` `prokaryotic` `fast` `metagenome`
**难度**: 入门 (Beginner)
**实现语言**: C


#### Glimmer (1998)

基于插值马尔可夫模型的微生物基因发现工具，通过从训练序列中学习编码区统计特征高效识别开放阅读框。
该方法是原核基因预测领域的经典算法，在完整基因组和草图组装中都能提供可靠的基因边界和起始位点预测。

**用途**: 原核基因组的开放阅读框和基因边界预测
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/26.2.545](https://doi.org/10.1093/nar/26.2.545)
**相关工具**: Prodigal, GeneMark, FragGeneScan
**标签**: `gene-prediction` `prokaryotic` `imm` `classic`
**难度**: 进阶 (Intermediate)
**实现语言**: C


#### RNAmmer (2007)

核糖体 RNA 基因预测工具，利用隐马尔可夫模型从基因组序列中精确识别 5S、16S 和 23S rRNA 基因及其前体。
该方法是微生物基因组注释流程中的重要组件，为系统发育分析和宏基因组分类提供必需的 rRNA 序列信息。

**用途**: 基因组中核糖体 RNA 基因的精确预测
**时间复杂度**: O(n * s)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/nar/gkm160](https://doi.org/10.1093/nar/gkm160)
**相关工具**: Barrnap, BLAST, SILVA
**标签**: `rrna` `gene-prediction` `hmm` `ribosomal`
**难度**: 进阶 (Intermediate)
**实现语言**: Perl, C


## 群体遗传学 (Population Genetics)

分析群体遗传结构和进化的算法


### 主成分与群体结构 (PCA & Population Structure)

降维和群体结构推断方法


#### PCA for Population Structure (2006)

主成分分析在群体遗传学中的应用，通过降维将高维基因型数据投影到低维空间，
揭示群体的遗传结构和祖源成分。该方法计算高效，是探索群体结构的标准工具。

**用途**: 群体遗传结构的降维可视化和祖源推断
**时间复杂度**: O(n * m * k)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1038/ng1847](https://doi.org/10.1038/ng1847)
**实现**: [https://github.com/chrchang/plink-ng](https://github.com/chrchang/plink-ng)
**相关工具**: EIGENSOFT, PLINK, smartpca
**标签**: `pca` `population-structure` `ancestry` `dimensionality-reduction`
**难度**: 入门 (Beginner)
**实现语言**: C, R


#### ADMIXTURE (2009)

基于最大似然估计的群体遗传结构推断工具，使用交替最小化算法加速计算，
在大规模数据集上比 STRUCTURE 快数十倍。该方法可推断个体的祖源成分比例，
适用于群体遗传学和人类遗传学研究。

**用途**: 快速推断群体祖源成分比例
**时间复杂度**: O(n * m * k)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1146/annurev-genom-090210-110729](https://doi.org/10.1146/annurev-genom-090210-110729)
**实现**: [https://github.com/alexandr1223/ancestry](https://github.com/alexandr1223/ancestry)
**相关工具**: STRUCTURE, fastSTRUCTURE, frappe
**标签**: `ancestry` `maximum-likelihood` `population-structure` `fast`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### STRUCTURE (2000)

经典的贝叶斯群体结构推断方法，使用马尔可夫链蒙特卡洛采样估计个体的群体
分配概率和祖源比例。该方法可处理混合群体和复杂群体结构，是群体遗传学的
基准方法。

**用途**: 贝叶斯群体结构推断和祖源分配
**时间复杂度**: O(n * m * k * g)
**空间复杂度**: O(n * k)
**论文**: [https://doi.org/10.1534/genetics.103.020701](https://doi.org/10.1534/genetics.103.020701)
**相关工具**: ADMIXTURE, fastSTRUCTURE, InStruct
**标签**: `bayesian` `mcmc` `population-structure` `classic`
**难度**: 进阶 (Intermediate)
**实现语言**: C


### 全基因组关联分析 (Genome-Wide Association Study)

基因型与表型关联分析方法


#### PLINK (2007)

全基因组关联分析的综合工具集，提供基因型数据管理、质量控制、关联分析、
群体分层校正和多基因风险评分等功能。该工具是遗传学数据分析的标准平台，
支持大规模基因组数据的高效处理。

**用途**: 全基因组关联分析和基因组数据管理
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1086/519795](https://doi.org/10.1086/519795)
**实现**: [https://github.com/chrchang/plink-ng](https://github.com/chrchang/plink-ng)
**相关工具**: BOLT-LMM, SAIGE, GCTA
**标签**: `gwas` `association` `qc` `standard`
**难度**: 入门 (Beginner)
**实现语言**: C++


#### BOLT-LMM (2015)

基于线性混合模型的大规模全基因组关联分析工具，使用高效的统计方法校正
群体分层和亲缘关系。该方法可处理数十万样本的关联分析，是大规模生物银行
数据分析的首选工具。

**用途**: 大规模线性混合模型关联分析
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1038/ng.3190](https://doi.org/10.1038/ng.3190)
**实现**: [https://github.com/broadinstitute/bolt](https://github.com/broadinstitute/bolt)
**相关工具**: GCTA, SAIGE, REGENIE
**标签**: `lmm` `gwas` `scalable` `biobank`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### SAIGE (2018)

针对不平衡表型的大规模关联分析工具，使用混合模型和 saddleback 近似方法
校正群体结构。该方法特别适合罕见变异和稀有表型的关联分析。

**用途**: 处理不平衡表型的大规模关联分析
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1038/s41588-018-0184-y](https://doi.org/10.1038/s41588-018-0184-y)
**实现**: [https://github.com/saige](https://github.com/saige)
**相关工具**: BOLT-LMM, REGENIE, PLINK
**标签**: `gwas` `mixed-model` `rare-variant` `unbalanced`
**难度**: 进阶 (Intermediate)
**实现语言**: R, C++


#### REGENIE (2021)

两阶段回归框架的大规模关联分析工具，先用全基因组回归预测个体的基因背景，
再进行逐位点的关联检验。该方法计算效率极高，适用于百万级别的生物银行数据。

**用途**: 两阶段大规模全基因组关联分析
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1038/s41588-021-00870-7](https://doi.org/10.1038/s41588-021-00870-7)
**实现**: [https://github.com/rgcgithub/regenie](https://github.com/rgcgithub/regenie)
**相关工具**: BOLT-LMM, SAIGE, GCTA
**标签**: `gwas` `scalable` `two-stage` `biobank`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


### 选择信号检测 (Selection Signature Detection)

检测自然选择留下的遗传信号


#### Tajima's D (1989)

经典的中性检验统计量，通过比较核苷酸多样性与分离位点数来检测群体是否
偏离中性进化假设。负值提示正选择或群体扩张，正值提示平衡选择或群体收缩。

**用途**: 检测群体是否偏离中性进化
**时间复杂度**: O(n * L)
**空间复杂度**: O(L)
**论文**: [https://doi.org/10.1093/oxfordjournals.molbev.a040563](https://doi.org/10.1093/oxfordjournals.molbev.a040563)
**相关工具**: VCFtools, popgenome, scikit-allel
**标签**: `neutrality-test` `selection` `classic` `population-genetics`
**难度**: 入门 (Beginner)
**实现语言**: R, Python


#### Selscan (2014)

高效的选择信号扫描工具，实现基于单倍型的 iHS 和 XP-EHH 等经典选择检验
统计量。该方法可检测正在进行或近期完成的正选择事件。

**用途**: 基于单倍型的选择信号检测
**时间复杂度**: O(n * m)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1093/bioinformatics/btu514](https://doi.org/10.1093/bioinformatics/btu514)
**实现**: [https://github.com/szpiech/selscan](https://github.com/szpiech/selscan)
**相关工具**: SweeD, hapbin, CMS
**标签**: `selection` `haplotype` `ihs` `xp-ehh`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### HapFLK (2013)

基于单倍型和 FLD 统计量的选择信号检测方法，利用群体间的遗传分化信息检测
选择事件。该方法对局部适应的选择信号检测灵敏度高，适用于多群体比较研究。

**用途**: 多群体间的选择信号检测
**时间复杂度**: O(n * m * K)
**空间复杂度**: O(m * K)
**论文**: [https://doi.org/10.1371/journal.pgen.1003911](https://doi.org/10.1371/journal.pgen.1003911)
**实现**: [https://github.com/popgenmethods/hapflk](https://github.com/popgenmethods/hapflk)
**相关工具**: Selscan, SweeD, PCAdapt
**标签**: `selection` `haplotype` `population-differentiation` `fld`
**难度**: 高级 (Advanced)
**实现语言**: Python, Fortran


#### PCAdapt (2016)

基于主成分分析的离群值检测方法，用于识别对群体结构有异常贡献的受选择位点。
该方法无需预先定义群体标签，可自动检测局部适应的遗传标记。

**用途**: 基于 PCA 的选择信号和离群值检测
**时间复杂度**: O(n * m * k)
**空间复杂度**: O(n * m)
**论文**: [https://doi.org/10.1093/molbev/msw055](https://doi.org/10.1093/molbev/msw055)
**实现**: [https://github.com/bcm-uga/pcadapt](https://github.com/bcm-uga/pcadapt)
**相关工具**: BayeScan, OutFLANK, Selscan
**标签**: `selection` `pca` `outlier-detection` `local-adaptation`
**难度**: 进阶 (Intermediate)
**实现语言**: R, C++


#### BayeScan (2008)

基于贝叶斯方法的群体分化 Fst 离群值检测工具，通过分解 Fst 为群体特异性和
位点特异性两部分来识别受选择的位点。该方法可控制假阳性率，适用于基因组扫描。

**用途**: 贝叶斯 Fst 离群值检测识别选择位点
**时间复杂度**: O(m * k * n)
**空间复杂度**: O(m * k)
**论文**: [https://doi.org/10.1093/molbev/msn067](https://doi.org/10.1093/molbev/msn067)
**相关工具**: PCAdapt, OutFLANK, BayEnv
**标签**: `selection` `bayesian` `fst` `outlier-detection`
**难度**: 进阶 (Intermediate)
**实现语言**: C++, Pascal


## 空间组学 (Spatial Omics)

保留空间信息的组学数据分析算法


### 空间转录组学 (Spatial Transcriptomics)

空间分辨的基因表达分析方法


#### Seurat Spatial (2021)

Seurat 框架的空间转录组分析模块，提供空间表达数据的标准化、降维、
空间聚类和空间可变基因检测。该方法整合了图像信息和表达数据，可发现
组织的空间表达模式。

**用途**: 空间转录组数据的整合分析
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1016/j.cell.2021.04.048](https://doi.org/10.1016/j.cell.2021.04.048)
**实现**: [https://github.com/satijalab/seurat](https://github.com/satijalab/seurat)
**相关工具**: Scanpy, Giotto, SPARK
**标签**: `spatial` `clustering` `integration` `multi-modal`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### Giotto Suite (2021)

综合性空间组学分析框架，支持 Visium、MERFISH、SLIDE-seq 等多种平台的数据
分析。提供空间聚类、空间基因集富集、细胞通讯推断和交互式可视化等功能。

**用途**: 多平台空间组学综合分析框架
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41467-021-24778-8](https://doi.org/10.1038/s41467-021-24778-8)
**实现**: [https://github.com/drieslab/Giotto](https://github.com/drieslab/Giotto)
**相关工具**: Seurat, Scanpy, Squidpy
**标签**: `spatial` `multi-platform` `comprehensive` `interactive`
**难度**: 进阶 (Intermediate)
**实现语言**: R, Python


#### Squidpy (2021)

专注于空间组学数据分析的 Python 工具包，提供空间邻域图构建、空间富集分析、
细胞通讯推断和图像分析等功能。该工具与 Scanpy 深度集成，支持多种空间平台。

**用途**: 空间组学数据的图分析和图像整合
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41592-021-01358-2](https://doi.org/10.1038/s41592-021-01358-2)
**实现**: [https://github.com/scverse/squidpy](https://github.com/scverse/squidpy)
**相关工具**: Scanpy, Giotto, stLearn
**标签**: `spatial` `graph-analysis` `cell-interaction` `image-analysis`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### SPARK (2019)

基于广义线性混合模型的空间可变基因检测方法，通过建模空间表达模式的
零膨胀和过度离散特征来识别空间相关表达的基因。该方法统计学基础扎实，
假阳性控制良好。

**用途**: 统计学方法检测空间可变基因
**时间复杂度**: O(g * n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41467-019-13318-4](https://doi.org/10.1038/s41467-019-13318-4)
**实现**: [https://github.com/xzhoulab/SPARK](https://github.com/xzhoulab/SPARK)
**相关工具**: SpatialDE, trendsceek, SPARK-X
**标签**: `spatial` `spatially-variable-gene` `statistical` `glm`
**难度**: 进阶 (Intermediate)
**实现语言**: R


#### SPARK-X (2021)

SPARK 的快速版本，基于非参数协方差函数检验检测空间可变基因。该方法
无需分布假设，计算效率显著优于 SPARK，适用于大规模空间转录组数据。

**用途**: 快速非参数空间可变基因检测
**时间复杂度**: O(g * n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/s13059-021-02404-0](https://doi.org/10.1186/s13059-021-02404-0)
**实现**: [https://github.com/xzhoulab/SPARK](https://github.com/xzhoulab/SPARK)
**相关工具**: SPARK, SpatialDE, MERINGUE
**标签**: `spatial` `fast` `non-parametric` `scalable`
**难度**: 进阶 (Intermediate)
**实现语言**: R


#### SpatialDE (2018)

基于高斯过程回归的空间可变基因检测方法，通过拟合空间表达的协方差函数
来检测基因表达是否具有空间模式。该方法可同时识别周期性和非周期性的
空间表达模式。

**用途**: 高斯过程方法检测空间表达模式
**时间复杂度**: O(g * n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/nmeth.4636](https://doi.org/10.1038/nmeth.4636)
**实现**: [https://github.com/Teichlab/SpatialDE](https://github.com/Teichlab/SpatialDE)
**相关工具**: SPARK, trendsceek, merfish
**标签**: `spatial` `gaussian-process` `pattern-detection` `probabilistic`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### stLearn (2021)

整合空间距离、组织学图像和基因表达信息的空间转录组分析方法，通过空间
距离权重和图像特征增强聚类和轨迹推断的准确性。

**用途**: 整合组织图像的空间转录组分析
**时间复杂度**: O(c * g)
**空间复杂度**: O(c * g)
**论文**: [https://doi.org/10.1038/s41467-021-21961-3](https://doi.org/10.1038/s41467-021-21961-3)
**实现**: [https://github.com/BiomedicalMachineLearning/stLearn](https://github.com/BiomedicalMachineLearning/stLearn)
**相关工具**: Squidpy, Giotto, Seurat
**标签**: `spatial` `image-integration` `trajectory` `clustering`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


### 空间蛋白质组学 (Spatial Proteomics)

空间分辨的蛋白质组分析方法


#### CellChat (2021)

基于配体-受体相互作用数据库推断细胞间通讯的方法，可从单细胞或空间转录组
数据中识别显著的细胞通讯通路。该方法整合了信号通路信息，提供通讯网络的
可视化和功能推断。

**用途**: 基于配体-受体互作的细胞通讯推断
**时间复杂度**: O(c^2 * g)
**空间复杂度**: O(c^2)
**论文**: [https://doi.org/10.1038/s41467-021-21246-9](https://doi.org/10.1038/s41467-021-21246-9)
**实现**: [https://github.com/sqjin/CellChat](https://github.com/sqjin/CellChat)
**相关工具**: CellPhoneDB, NicheNet, squidpy
**标签**: `cell-communication` `ligand-receptor` `signaling` `network`
**难度**: 进阶 (Intermediate)
**实现语言**: R


#### Cellpose (2020)

基于深度学习的细胞分割算法，使用 U-Net 架构自动检测图像中的细胞边界。
该方法提供预训练模型，支持多种细胞类型和成像模式，是空间蛋白质组学
图像分析的基础工具。

**用途**: 基于深度学习的细胞图像分割
**时间复杂度**: O(p)
**空间复杂度**: O(p)
**论文**: [https://doi.org/10.1038/s41592-020-01018-z](https://doi.org/10.1038/s41592-020-01018-z)
**实现**: [https://github.com/MouseLand/cellpose](https://github.com/MouseLand/cellpose)
**相关工具**: Stardist, Mesmer, CellProfiler
**标签**: `segmentation` `deep-learning` `cell-detection` `imaging`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### StarDist (2018)

基于星形凸多边形的细胞核和细胞分割方法，使用深度学习预测每个像素到
边界的距离。该方法对密集排列的细胞核分割效果优异，常用于组织切片图像分析。

**用途**: 基于星形凸多边形的细胞分割
**时间复杂度**: O(p)
**空间复杂度**: O(p)
**论文**: [https://doi.org/10.1007/978-3-030-00934-2_30](https://doi.org/10.1007/978-3-030-00934-2_30)
**实现**: [https://github.com/stardist/stardist](https://github.com/stardist/stardist)
**相关工具**: Cellpose, Mesmer, Ilastik
**标签**: `segmentation` `deep-learning` `cell-nuclei` `star-convex`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


## 图基因组学 (Graph Genomics)

基于图结构表示和分析基因组的算法


### 泛基因组 (Pangenome)

构建和分析泛基因组图的方法


#### Minigraph (2020)

基于 minimizer 的图基因组构建和比对工具，可将多个基因组组装整合为一个
保留结构变异的图结构。该方法支持线性序列到图的高效比对，是泛基因组
分析的核心工具。

**用途**: 构建泛基因组图和图上比对
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btaa743](https://doi.org/10.1093/bioinformatics/btaa743)
**实现**: [https://github.com/lh3/minigraph](https://github.com/lh3/minigraph)
**相关工具**: vg, Minimap2, PGGB
**标签**: `pangenome` `graph-alignment` `minimizer` `structural-variant`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### Cactus (2011)

基于祖先引导的全基因组比对和泛基因组图构建方法，使用 progressive cactus
算法处理多物种间的共线性关系。该方法可构建大规模的全基因组比对和泛基因组
参考图。

**用途**: 多物种全基因组比对和泛基因组构建
**时间复杂度**: O(n^2 * k)
**空间复杂度**: O(n * k)
**论文**: [https://doi.org/10.1101/gr.123356.111](https://doi.org/10.1101/gr.123356.111)
**实现**: [https://github.com/ComparativeGenomicsToolkit/cactus](https://github.com/ComparativeGenomicsToolkit/cactus)
**相关工具**: Minigraph, PGGB, Mauve
**标签**: `pangenome` `alignment` `progressive` `multi-species`
**难度**: 高级 (Advanced)
**实现语言**: C, Python


#### odgi (2020)

泛基因组图的优化工具包，提供图的压缩存储、遍历、去环化、分块和可视化
功能。该方法支持对大规模泛基因组图进行高效操作和分析。

**用途**: 泛基因组图的存储、操作和可视化
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btaa767](https://doi.org/10.1093/bioinformatics/btaa767)
**实现**: [https://github.com/pangenome/odgi](https://github.com/pangenome/odgi)
**相关工具**: PGGB, VG, seqwish
**标签**: `pangenome` `graph-operations` `visualization` `sorting`
**难度**: 进阶 (Intermediate)
**实现语言**: C++


#### seqwish (2020)

从全对全比对结果构建无损变异图的工具，将比对中的所有对齐关系编码为
图结构。该方法是 PGGB 工作流的核心组件，保证不丢失任何序列和比对信息。

**用途**: 从比对结果构建无损变异图
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1093/bioinformatics/btaa767](https://doi.org/10.1093/bioinformatics/btaa767)
**实现**: [https://github.com/ekg/seqwish](https://github.com/ekg/seqwish)
**相关工具**: PGGB, odgi, Minigraph
**标签**: `pangenome` `graph-construction` `alignment-to-graph` `lossless`
**难度**: 高级 (Advanced)
**实现语言**: C++


### 变异图 (Variation Graph)

基于变异图的序列分析方法


#### HiFiBD (2022)

专为 PacBio HiFi 数据设计的泛基因组图分型方法，利用图结构中的变异信息
提高低频变异的检测灵敏度。该方法可直接在泛基因组图上进行比对和分型。

**用途**: 泛基因组图上的 HiFi 数据分型
**时间复杂度**: O(n * d)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/s41587-022-01347-y](https://doi.org/10.1038/s41587-022-01347-y)
**相关工具**: VG, Minigraph, GraphAligner
**标签**: `variation-graph` `hifi` `genotyping` `pangenome`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### PanVC (2023)

基于泛基因组图的变异检测流程，将比对、变异检测和分型步骤整合到图框架中。
该方法可减少参考基因组偏差，提高结构区域的变异检测准确性。

**用途**: 基于泛基因组图的端到端变异检测
**时间复杂度**: O(n * m)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1186/s13059-023-03029-1](https://doi.org/10.1186/s13059-023-03029-1)
**相关工具**: VG, Minigraph, GATK
**标签**: `pangenome` `variant-calling` `genotyping` `pipeline`
**难度**: 高级 (Advanced)
**实现语言**: C++, Python


#### VG (Variation Graph) (2017)

基于变异图的基因组分析工具包，将基因组序列和群体变异编码为有向图结构，
支持图上的序列比对和变异检测。该方法可处理参考基因组偏差，提供更公平
的比对和变异调用。

**用途**: 基于变异图的序列比对和变异检测
**时间复杂度**: O(n log n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1038/nbt.3820](https://doi.org/10.1038/nbt.3820)
**实现**: [https://github.com/vgteam/vg](https://github.com/vgteam/vg)
**相关工具**: Minigraph, GCSA2, GraphAligner
**标签**: `variation-graph` `alignment` `variant-calling` `pangenome`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### GCSA2 (2017)

基于广义压缩后缀数组的图索引方法，将变异图上的所有路径编码为可搜索的
索引结构，支持高效的 k-mer 搜索和精确匹配。该方法是 VG 工具包的核心
索引引擎。

**用途**: 变异图的高效 k-mer 索引
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btw513](https://doi.org/10.1093/bioinformatics/btw513)
**实现**: [https://github.com/jltsiren/gcsa2](https://github.com/jltsiren/gcsa2)
**相关工具**: VG, Minigraph, GraphAligner
**标签**: `indexing` `k-mer` `compressed-suffix-array` `variation-graph`
**难度**: 高级 (Advanced)
**实现语言**: C++


#### GraphAligner (2019)

专为泛基因组图设计的长读段比对工具，使用种子扩展和动态规划在变异图上
进行精确的序列比对。该方法可处理复杂的图拓扑结构，对长读段数据的
比对效果优于线性比对器。

**用途**: 泛基因组图上的长读段比对
**时间复杂度**: O(n * d)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btz161](https://doi.org/10.1093/bioinformatics/btz161)
**实现**: [https://github.com/maickrau/GraphAligner](https://github.com/maickrau/GraphAligner)
**相关工具**: VG, Minimap2, vg-deconstruct
**标签**: `graph-alignment` `long-read` `variation-graph` `seed-extend`
**难度**: 高级 (Advanced)
**实现语言**: C++


## 蛋白质语言模型 (Protein Language Model)

基于大规模预训练模型的蛋白质分析算法


### 蛋白质语言模型预训练 (Protein Language Model Pretraining)

蛋白质序列的语言模型和表征学习方法


#### ESM-2 (2022)

Meta AI 开发的蛋白质语言模型，使用 Transformer 架构在数亿条蛋白质序列上
预训练。该模型学习到的表征包含丰富的进化和结构信息，可用于下游任务
如接触预测、功能预测和结构推断。

**用途**: 基于 Transformer 的蛋白质序列表征学习
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574)
**实现**: [https://github.com/facebookresearch/esm](https://github.com/facebookresearch/esm)
**相关工具**: ProtTrans, Ankh, ProGen
**标签**: `language-model` `transformer` `representation-learning` `pretrained`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### ProtTrans (2021)

基于多种 Transformer 架构（T5、BERT、XLNet 等）的蛋白质语言模型集合，
在 UniRef 和 BFD 等大规模数据库上预训练。该模型可生成高质量的蛋白质
序列表征，支持迁移学习用于各种下游任务。

**用途**: 多架构蛋白质语言模型预训练表征
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1073/pnas.2103670118](https://doi.org/10.1073/pnas.2103670118)
**实现**: [https://github.com/agemagician/ProtTrans](https://github.com/agemagician/ProtTrans)
**相关工具**: ESM-2, Ankh, ProtGPT2
**标签**: `language-model` `transfer-learning` `representation-learning` `t5`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### ProtBERT (2020)

基于 BERT 架构的蛋白质语言模型，在 UniRef100 上预训练，学习氨基酸序列
的上下文相关表征。该模型可用于蛋白质家族分类、亚细胞定位预测和
翻译后修饰位点预测等任务。

**用途**: 基于 BERT 的蛋白质序列表征学习
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1109/TCBB.2021.3095196](https://doi.org/10.1109/TCBB.2021.3095196)
**实现**: [https://github.com/agemagician/ProtTrans](https://github.com/agemagician/ProtTrans)
**相关工具**: ESM-2, ProtTrans, UniRep
**标签**: `language-model` `bert` `sequence-embedding` `pretrained`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### Ankh (2023)

基于 T5 架构优化的蛋白质语言模型，使用更高效的预训练策略和数据增强
方法，在多个下游任务上达到与 ESM-2 相当的性能。该模型参数量更小，
推理效率更高。

**用途**: 高效轻量的蛋白质语言模型
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.48550/arXiv.2301.06568](https://doi.org/10.48550/arXiv.2301.06568)
**实现**: [https://github.com/agemagician/Ankh](https://github.com/agemagician/Ankh)
**相关工具**: ESM-2, ProtTrans, ProtBERT
**标签**: `language-model` `lightweight` `efficient` `t5-architecture`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


### 蛋白质功能预测 (Protein Function Prediction)

基于语言模型的蛋白质功能和性质预测


#### ESMFold (2023)

基于 ESM-2 语言模型的端到端蛋白质结构预测方法，无需多序列比对即可从
单条氨基酸序列直接预测三维结构。该方法推理速度比 AlphaFold 快一个数量级，
适合大规模蛋白质组的结构预测。

**用途**: 基于语言模型的快速端到端结构预测
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574)
**实现**: [https://github.com/facebookresearch/esm](https://github.com/facebookresearch/esm)
**相关工具**: AlphaFold, OmegaFold, RoseTTAFold
**标签**: `structure-prediction` `single-sequence` `fast` `language-model`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### ProteinMPNN (2022)

基于消息传递神经网络的蛋白质序列设计方法，从给定的蛋白质骨架结构出发
设计满足该结构的氨基酸序列。该方法在序列恢复率和实验成功率上大幅优于
传统的 Rosetta 设计方法。

**用途**: 基于图神经网络的蛋白质序列设计
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1126/science.add2187](https://doi.org/10.1126/science.add2187)
**实现**: [https://github.com/dauparas/ProteinMPNN](https://github.com/dauparas/ProteinMPNN)
**相关工具**: Rosetta, RFdiffusion, ESM
**标签**: `protein-design` `inverse-folding` `graph-neural-network` `sequence-design`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### RFdiffusion (2023)

基于扩散模型的蛋白质结构生成方法，可从随机噪声逐步去噪生成全新的蛋白质
骨架结构。该方法支持条件生成（如指定结合位点），是蛋白质从头设计的
突破性工具。

**用途**: 基于扩散模型的蛋白质结构从头生成
**时间复杂度**: O(n^2 * T)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8)
**实现**: [https://github.com/RosettaCommons/RFdiffusion](https://github.com/RosettaCommons/RFdiffusion)
**相关工具**: ProteinMPNN, RoseTTAFold, Chroma
**标签**: `diffusion-model` `protein-design` `structure-generation` `de-novo`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### ProGen (2020)

基于条件语言模型的蛋白质序列生成方法，可按指定的功能标签和结构条件
生成具有目标属性的新蛋白质序列。该方法生成的序列具有天然蛋白的特性，
可通过实验验证其功能。

**用途**: 条件可控的蛋白质序列生成
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1101/2020.03.07.982272](https://doi.org/10.1101/2020.03.07.982272)
**实现**: [https://github.com/salesforce/progen](https://github.com/salesforce/progen)
**相关工具**: ProteinMPNN, RFdiffusion, ESM
**标签**: `generative` `protein-design` `conditional-generation` `transformer`
**难度**: 高级 (Advanced)
**实现语言**: Python


#### DeepSEA (2015)

基于深度卷积神经网络的 DNA 序列功能预测方法，直接从序列预测染色质特征
和变异的功能效应。该方法开创了基于深度学习的序列功能预测领域，是
基因组学深度学习的经典模型。

**用途**: 基于深度学习的 DNA 序列功能预测
**时间复杂度**: O(n * d)
**空间复杂度**: O(d)
**论文**: [https://doi.org/10.1038/nmeth.3547](https://doi.org/10.1038/nmeth.3547)
**实现**: [https://github.com/FunctionLab/DeepSEA](https://github.com/FunctionLab/DeepSEA)
**相关工具**: Basset, DanQ, Enformer
**标签**: `deep-learning` `functional-prediction` `chromatin` `variant-effect`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


#### ESM-1v (2021)

基于 ESM 框架的蛋白质变异效应预测方法，利用语言模型的似然度评估
氨基酸替换对蛋白质功能的影响。该方法无需训练即可在零样本模式下预测
致病性变异，性能接近实验测量。

**用途**: 基于语言模型的蛋白质变异效应零样本预测
**时间复杂度**: O(n^2 * d)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1101/2021.07.09.450648](https://doi.org/10.1101/2021.07.09.450648)
**实现**: [https://github.com/facebookresearch/esm](https://github.com/facebookresearch/esm)
**相关工具**: EVE, AlphaMissense, PolyPhen
**标签**: `variant-effect` `zero-shot` `pathogenicity` `language-model`
**难度**: 进阶 (Intermediate)
**实现语言**: Python


---

## 🛠️ CLI Commands | 命令行工具

```bash
# Search for algorithms | 搜索算法
python -m awesome_bioinfo search "alignment"

# Get algorithm details | 获取算法详情
python -m awesome_bioinfo info smith-waterman

# Compare two algorithms | 比较两个算法
python -m awesome_bioinfo compare smith-waterman needleman-wunsch

# Export data to JSON | 导出数据
python -m awesome_bioinfo export --format json > algorithms.json

# Generate MkDocs site | 生成 MkDocs 文档站点
python -m awesome_bioinfo mkdocs

# Generate README | 生成 README
python -m awesome_bioinfo generate
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

## 📚 Citation | 引用

If you use this project in your research, please cite it as:

如果您在研究中使用了本项目，请按以下方式引用：

```bibtex
@software{awesome_bioinfo_algorithms,
  title = {Awesome Bioinformatics Algorithms},
  author = {{LessUp Community}},
  year = {2025},
  url = {https://github.com/LessUp/awesome-bioinfo-algorithms}
}
```

Or see [CITATION.cff](CITATION.cff) for more citation formats.

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
- ✅ Copy, modify, distribute / 复制、修改、分发
- ✅ Use for commercial purposes / 用于商业目的
- ✅ No attribution required / 无需署名

---

<p align="center">
  <b>Made with ❤️ by the community</b><br>
  © 2025-2026 <a href="https://github.com/LessUp">LessUp</a> Community
</p>
