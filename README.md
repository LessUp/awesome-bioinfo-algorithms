# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Validate](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/validate.yml/badge.svg)](https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/validate.yml)
[![Docs](https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github)](https://lessup.github.io/awesome-bioinfo-algorithms/)

简体中文 | [English](README.en.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Algorithms](https://img.shields.io/badge/algorithms-54-blue.svg)](#-统计--statistics)
[![Categories](https://img.shields.io/badge/categories-12-green.svg)](#-统计--statistics)

> 🧬 生物信息学算法概要汇总 | A curated list of bioinformatics algorithms

本项目收集和整理生物信息学领域常用的算法，提供算法的简要介绍、复杂度分析和相关资源链接，帮助开发者快速了解和选择合适的算法。

This project collects and organizes commonly used algorithms in bioinformatics, providing brief introductions, complexity analysis, and related resource links to help developers quickly understand and choose appropriate algorithms.

## 🚀 快速开始 | Quick Start

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

- 📊 算法总数 (Total Algorithms): **54**
- 📁 分类数量 (Categories): **12**
- 🏷️ 标签数量 (Tags): **139**

## 📑 目录 | Table of Contents

- [序列比对 (Sequence Alignment)](#序列比对-sequence-alignment)
- [序列组装 (Sequence Assembly)](#序列组装-sequence-assembly)
- [变异检测 (Variant Calling)](#变异检测-variant-calling)
- [基因表达分析 (Gene Expression Analysis)](#基因表达分析-gene-expression-analysis)
- [蛋白质结构预测 (Protein Structure Prediction)](#蛋白质结构预测-protein-structure-prediction)
- [系统发育分析 (Phylogenetics)](#系统发育分析-phylogenetics)
- [功能注释 (Functional Annotation)](#功能注释-functional-annotation)
- [数据压缩 (Data Compression)](#数据压缩-data-compression)
- [单细胞基因组学 (Single-Cell Genomics)](#单细胞基因组学-single-cell-genomics)
- [宏基因组学 (Metagenomics)](#宏基因组学-metagenomics)
- [表观基因组学 (Epigenomics)](#表观基因组学-epigenomics)
- [基因预测 (Gene Prediction)](#基因预测-gene-prediction)

---

## 序列比对 (Sequence Alignment)

用于比较和对齐生物序列的算法


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


## 序列组装 (Sequence Assembly)

从短读段重建完整序列的算法


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


## 变异检测 (Variant Calling)

检测基因组变异的算法


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


## 基因表达分析 (Gene Expression Analysis)

分析基因表达水平的算法


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


## 蛋白质结构预测 (Protein Structure Prediction)

预测蛋白质三维结构的算法


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


## 系统发育分析 (Phylogenetics)

构建和分析进化树的算法


#### Neighbor-Joining (1987)

基于距离矩阵的系统发育树构建算法，通过迭代地合并最近邻节点来构建无根树。
该方法计算速度快，适合处理大规模数据集，是最常用的距离法建树算法之一。

**用途**: 快速构建系统发育树
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1093/oxfordjournals.molbev.a040454](https://doi.org/10.1093/oxfordjournals.molbev.a040454)
**相关工具**: MEGA, PHYLIP, RapidNJ
**标签**: `distance-based` `tree-building` `classic`


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


## 功能注释 (Functional Annotation)

预测基因和蛋白质功能的算法


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


## 数据压缩 (Data Compression)

压缩生物信息学数据的算法


#### GZIP for FASTQ (1992)

基于 DEFLATE 算法的通用数据压缩方法，广泛用于压缩 FASTQ 格式的测序数据。
该方法压缩比适中，兼容性好，是生物信息学数据存储的标准压缩格式。

**用途**: 测序数据的通用压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.17487/RFC1952](https://doi.org/10.17487/RFC1952)
**相关工具**: gzip, pigz, bgzip
**标签**: `lossless` `general-purpose` `standard` `fastq`


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


## 单细胞基因组学 (Single-Cell Genomics)

单细胞水平的基因组和转录组分析算法


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


## 宏基因组学 (Metagenomics)

微生物群落的基因组分析算法


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


## 表观基因组学 (Epigenomics)

分析表观遗传修饰的算法


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


## 基因预测 (Gene Prediction)

基因结构预测和基因组注释算法


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


## 🤝 贡献 | Contributing

欢迎贡献！我们接受以下类型的贡献：

We welcome contributions! We accept the following types of contributions:

- 🆕 添加新算法 | Add new algorithms
- 📝 改进现有描述 | Improve existing descriptions
- 🔗 添加参考链接 | Add reference links
- 🐛 修复错误 | Fix errors

请阅读 [贡献指南](CONTRIBUTING.md) 了解详情。

Please read the [Contributing Guide](CONTRIBUTING.md) for details.

## � 文档 | Documentation

📘 **在线文档** → [lessup.github.io/awesome-bioinfo-algorithms](https://lessup.github.io/awesome-bioinfo-algorithms/)

- [API 文档 | API Reference](https://lessup.github.io/awesome-bioinfo-algorithms/API.html)
- [开发指南 | Development Guide](https://lessup.github.io/awesome-bioinfo-algorithms/DEVELOPMENT.html)
- [常见问题 | FAQ](https://lessup.github.io/awesome-bioinfo-algorithms/FAQ.html)
- [贡献指南 | Contributing](https://lessup.github.io/awesome-bioinfo-algorithms/contributing.html)
- [变更日志 | Changelog](https://lessup.github.io/awesome-bioinfo-algorithms/changelog.html)

## �📚 相关资源 | Related Resources

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
