# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Validate](https://github.com/YOUR_USERNAME/awesome-bioinformatics-algorithms/actions/workflows/validate.yml/badge.svg)](https://github.com/YOUR_USERNAME/awesome-bioinformatics-algorithms/actions/workflows/validate.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

> 🧬 生物信息学算法概要汇总 | A curated list of bioinformatics algorithms

本项目收集和整理生物信息学领域常用的算法，提供算法的简要介绍、复杂度分析和相关资源链接，帮助开发者快速了解和选择合适的算法。

This project collects and organizes commonly used algorithms in bioinformatics, providing brief introductions, complexity analysis, and related resource links to help developers quickly understand and choose appropriate algorithms.

## 📊 统计 | Statistics

- 📊 算法总数 (Total Algorithms): 17
- 📁 分类数量 (Categories): 8
- 🏷️ 标签数量 (Tags): 51

## 📑 目录 | Table of Contents

- [序列比对 (Sequence Alignment)](#序列比对)
- [序列组装 (Sequence Assembly)](#序列组装)
- [变异检测 (Variant Calling)](#变异检测)
- [基因表达分析 (Gene Expression Analysis)](#基因表达分析)
- [蛋白质结构预测 (Protein Structure Prediction)](#蛋白质结构预测)
- [系统发育分析 (Phylogenetics)](#系统发育分析)
- [功能注释 (Functional Annotation)](#功能注释)
- [数据压缩 (Data Compression)](#数据压缩)

---

## 序列比对 (Sequence Alignment)

用于比较和对齐生物序列的算法


#### Smith-Waterman

经典的局部序列比对算法，使用动态规划方法找出两条序列之间相似性最高的局部区域。
该算法保证找到最优的局部比对结果，适用于检测序列中的保守区域和功能域。

**用途**: 局部序列比对，寻找序列间的相似区域
**时间复杂度**: O(mn)
**空间复杂度**: O(mn)
**论文**: [https://doi.org/10.1016/0022-2836(81)90087-5](https://doi.org/10.1016/0022-2836(81)90087-5)
**实现**: [https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library](https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library)
**相关工具**: BLAST, FASTA, SSEARCH
**标签**: `dynamic-programming` `local-alignment` `classic`


#### Needleman-Wunsch

全局序列比对的经典算法，使用动态规划对两条完整序列进行端到端比对。
该算法找出最优的全局对齐方案，适用于比较相似长度的同源序列。

**用途**: 全局序列比对
**时间复杂度**: O(mn)
**空间复杂度**: O(mn)
**论文**: [https://doi.org/10.1016/0022-2836(70)90057-4](https://doi.org/10.1016/0022-2836(70)90057-4)
**相关工具**: EMBOSS needle, Clustal
**标签**: `dynamic-programming` `global-alignment` `classic`


#### Burrows-Wheeler Transform Alignment

基于 Burrows-Wheeler 变换的序列比对算法，通过构建 BWT 索引实现快速的短读段比对。
该方法在保持高准确性的同时大幅提升比对速度，是现代测序数据分析的核心算法。

**用途**: 高通量测序数据的快速比对
**时间复杂度**: O(n)
**空间复杂度**: O(n)
**论文**: [https://doi.org/10.1093/bioinformatics/btp324](https://doi.org/10.1093/bioinformatics/btp324)
**实现**: [https://github.com/lh3/bwa](https://github.com/lh3/bwa)
**相关工具**: BWA, Bowtie, HISAT2
**标签**: `bwt` `indexing` `short-read` `high-throughput`


## 序列组装 (Sequence Assembly)

从短读段重建完整序列的算法


#### De Bruijn Graph Assembly

基于 De Bruijn 图的序列组装算法，将测序读段分解为 k-mer，构建有向图进行组装。
该方法特别适合处理高通量测序产生的大量短读段，是现代基因组组装的核心方法。

**用途**: 从短读段重建基因组序列
**时间复杂度**: O(n)
**空间复杂度**: O(k * 4^k)
**论文**: [https://doi.org/10.1073/pnas.98.17.9748](https://doi.org/10.1073/pnas.98.17.9748)
**实现**: [https://github.com/voutcn/megahit](https://github.com/voutcn/megahit)
**相关工具**: SPAdes, MEGAHIT, Velvet
**标签**: `graph-based` `k-mer` `de-novo` `short-read`


#### Overlap-Layout-Consensus (OLC)

经典的序列组装方法，通过三个步骤完成组装：计算读段间的重叠、构建布局图、生成一致序列。
该方法适合处理长读段数据，能够产生高质量的组装结果。

**用途**: 长读段序列组装
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1101/gr.101360.109](https://doi.org/10.1101/gr.101360.109)
**相关工具**: Canu, Flye, Miniasm
**标签**: `overlap` `long-read` `de-novo` `classic`


## 变异检测 (Variant Calling)

检测基因组变异的算法


#### GATK HaplotypeCaller

基于局部重组装的变异检测算法，通过在活跃区域进行局部单倍型组装来发现变异。
该方法能够同时检测 SNP 和 Indel，是目前最广泛使用的变异检测工具之一。

**用途**: 检测 SNP 和小型 Indel 变异
**时间复杂度**: O(n * r)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1038/ng.806](https://doi.org/10.1038/ng.806)
**实现**: [https://github.com/broadinstitute/gatk](https://github.com/broadinstitute/gatk)
**相关工具**: GATK, Picard, BWA
**标签**: `haplotype` `snp` `indel` `germline`


#### FreeBayes

基于贝叶斯统计的变异检测算法，使用单倍型作为基本单位进行变异调用。
该方法支持多倍体样本，能够检测复杂的变异模式，计算效率较高。

**用途**: 基于贝叶斯的变异检测
**时间复杂度**: O(n * h)
**空间复杂度**: O(h)
**论文**: [https://arxiv.org/abs/1207.3907](https://arxiv.org/abs/1207.3907)
**实现**: [https://github.com/freebayes/freebayes](https://github.com/freebayes/freebayes)
**相关工具**: VCFtools, BCFtools
**标签**: `bayesian` `haplotype` `polyploid` `snp`


## 基因表达分析 (Gene Expression Analysis)

分析基因表达水平的算法


#### DESeq2

基于负二项分布的差异表达分析算法，使用收缩估计来提高方差估计的稳定性。
该方法特别适合处理小样本量的 RNA-seq 数据，是目前最广泛使用的差异表达分析工具之一。

**用途**: RNA-seq 数据的差异表达分析
**时间复杂度**: O(n * g)
**空间复杂度**: O(g)
**论文**: [https://doi.org/10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8)
**实现**: [https://bioconductor.org/packages/DESeq2](https://bioconductor.org/packages/DESeq2)
**相关工具**: edgeR, limma, Bioconductor
**标签**: `rna-seq` `differential-expression` `negative-binomial` `statistical`


#### Kallisto

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


#### AlphaFold

基于深度学习的蛋白质结构预测算法，使用注意力机制和进化信息预测蛋白质三维结构。
该方法在 CASP14 竞赛中取得突破性成果，预测精度接近实验测定水平。

**用途**: 从氨基酸序列预测蛋白质三维结构
**时间复杂度**: O(n^2)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)
**实现**: [https://github.com/deepmind/alphafold](https://github.com/deepmind/alphafold)
**相关工具**: ColabFold, ESMFold, RoseTTAFold
**标签**: `deep-learning` `attention` `structure-prediction` `breakthrough`


#### Rosetta

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


#### Neighbor-Joining

基于距离矩阵的系统发育树构建算法，通过迭代地合并最近邻节点来构建无根树。
该方法计算速度快，适合处理大规模数据集，是最常用的距离法建树算法之一。

**用途**: 快速构建系统发育树
**时间复杂度**: O(n^3)
**空间复杂度**: O(n^2)
**论文**: [https://doi.org/10.1093/oxfordjournals.molbev.a040454](https://doi.org/10.1093/oxfordjournals.molbev.a040454)
**相关工具**: MEGA, PHYLIP, RapidNJ
**标签**: `distance-based` `tree-building` `classic`


#### Maximum Likelihood Phylogeny

基于最大似然法的系统发育推断算法，通过优化进化模型参数来寻找最可能的树拓扑。
该方法统计学基础扎实，能够提供可靠的分支支持度评估。

**用途**: 统计学方法构建系统发育树
**时间复杂度**: O(n^2 * s * r)
**空间复杂度**: O(n * s)
**论文**: [https://doi.org/10.1093/sysbio/syq010](https://doi.org/10.1093/sysbio/syq010)
**实现**: [https://github.com/stamatak/standard-RAxML](https://github.com/stamatak/standard-RAxML)
**相关工具**: RAxML, IQ-TREE, PhyML
**标签**: `maximum-likelihood` `statistical` `tree-building`


## 功能注释 (Functional Annotation)

预测基因和蛋白质功能的算法


#### BLAST-based Annotation

基于序列相似性的功能注释方法，通过与已知功能序列数据库比对来推断未知序列的功能。
该方法是最基础和广泛使用的功能注释策略，适用于各类生物序列的初步功能预测。

**用途**: 基于序列相似性的功能预测
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2)
**实现**: [https://blast.ncbi.nlm.nih.gov/](https://blast.ncbi.nlm.nih.gov/)
**相关工具**: BLAST+, UniProt, InterPro
**标签**: `sequence-similarity` `database-search` `classic` `annotation`


#### HMMER

基于隐马尔可夫模型的序列分析算法，使用概率模型检测远程同源序列和蛋白质结构域。
该方法比简单的序列比对更敏感，能够发现进化距离较远的同源关系。

**用途**: 蛋白质结构域识别和远程同源检测
**时间复杂度**: O(mn)
**空间复杂度**: O(m)
**论文**: [https://doi.org/10.1371/journal.pcbi.1002195](https://doi.org/10.1371/journal.pcbi.1002195)
**实现**: [http://hmmer.org/](http://hmmer.org/)
**相关工具**: Pfam, InterProScan, SMART
**标签**: `hmm` `domain-detection` `remote-homology` `probabilistic`


## 数据压缩 (Data Compression)

压缩生物信息学数据的算法


#### GZIP for FASTQ

基于 DEFLATE 算法的通用数据压缩方法，广泛用于压缩 FASTQ 格式的测序数据。
该方法压缩比适中，兼容性好，是生物信息学数据存储的标准压缩格式。

**用途**: 测序数据的通用压缩
**时间复杂度**: O(n)
**空间复杂度**: O(1)
**论文**: [https://doi.org/10.17487/RFC1952](https://doi.org/10.17487/RFC1952)
**相关工具**: gzip, pigz, bgzip
**标签**: `lossless` `general-purpose` `standard` `fastq`


#### CRAM

专为比对数据设计的参考序列压缩格式，通过存储与参考序列的差异实现高压缩比。
该方法可将 BAM 文件压缩至原大小的 40-60%，是大规模测序项目的首选存储格式。

**用途**: 比对数据的高效压缩存储
**时间复杂度**: O(n)
**空间复杂度**: O(r)
**论文**: [https://doi.org/10.1093/nar/gkq1373](https://doi.org/10.1093/nar/gkq1373)
**实现**: [https://github.com/samtools/htslib](https://github.com/samtools/htslib)
**相关工具**: samtools, htslib, cramtools
**标签**: `reference-based` `alignment` `bam` `efficient`


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

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

本项目采用 [CC0 1.0 通用](https://creativecommons.org/publicdomain/zero/1.0/deed.zh) 许可协议，您可以自由地复制、修改、分发和使用本项目。

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). You are free to copy, modify, distribute and use this project.
