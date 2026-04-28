<h1 align="center">Awesome Bioinformatics Algorithms</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml"><img src="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/"><img src="https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github" alt="Documentation"></a>
  <a href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg" alt="License"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/blob/main/CITATION.cff"><img src="https://img.shields.io/badge/Cite%20Me-APA-blue" alt="Citation"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Algorithms-195-blue.svg" alt="Algorithms">
  <img src="https://img.shields.io/badge/Categories-16-green.svg" alt="Categories">
  <img src="https://img.shields.io/badge/Tags-392-orange.svg" alt="Tags">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python">
</p>

<p align="center">
  <b>🧬 A curated collection of bioinformatics algorithms with complexity analysis</b>
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> • 
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/">📖 Documentation Site</a> • 
  <a href="CONTRIBUTING.md">🤝 Contributing</a> • 
  <a href="#-citation">📚 Citation</a>
</p>

---

## ✨ Highlights

<table>
<tr>
<td width="50%">

**🎯 For Researchers**
- 195+ curated algorithms
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

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Install dependencies (includes MkDocs support)
pip install -e ".[dev,docs]"

# Validate data
python -m awesome_bioinfo validate

# Show statistics
python -m awesome_bioinfo stats
```

---

## 📊 Statistics

| Metric | Value |
|:-------|------:|
| Total Algorithms | **195** |
| Categories | **16** |
| Unique Tags | **392** |

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Sequence Alignment](#sequence-alignment)
- [Sequence Assembly](#sequence-assembly)
- [Variant Calling](#variant-calling)
- [Gene Expression Analysis](#gene-expression-analysis)
- [Protein Structure Prediction](#protein-structure-prediction)
- [Phylogenetics](#phylogenetics)
- [Functional Annotation](#functional-annotation)
- [Data Compression](#data-compression)
- [Single-Cell Genomics](#single-cell-genomics)
- [Metagenomics](#metagenomics)
- [Epigenomics](#epigenomics)
- [Gene Prediction](#gene-prediction)
- [Population Genetics](#population-genetics)
- [Spatial Omics](#spatial-omics)
- [Graph Genomics](#graph-genomics)
- [Protein Language Model](#protein-language-model)

</details>

---

## Category Overview

| Category | Algorithms | Description |
|----------|------------|-------------|
| Sequence Alignment | 19 | Algorithms for comparing and aligning biological sequences |
| Sequence Assembly | 14 | Algorithms for reconstructing complete sequences from short reads |
| Variant Calling | 14 | Algorithms for detecting genomic variations |
| Gene Expression Analysis | 12 | Algorithms for analyzing gene expression levels |
| Protein Structure Prediction | 14 | Algorithms for predicting protein 3D structures |
| Phylogenetics | 12 | Algorithms for building and analyzing evolutionary trees |
| Functional Annotation | 12 | Algorithms for predicting gene and protein functions |
| Data Compression | 10 | Algorithms for compressing bioinformatics data |
| Single-Cell Genomics | 15 | Algorithms for single-cell genomics and transcriptomics |
| Metagenomics | 14 | Algorithms for microbial community genomics |
| Epigenomics | 6 | Algorithms for analyzing epigenetic modifications |
| Gene Prediction | 12 | Algorithms for gene structure prediction and annotation |
| Population Genetics | 12 | Algorithms for population genetic structure and evolution |
| Spatial Omics | 10 | Algorithms for spatially-resolved omics data |
| Graph Genomics | 9 | Algorithms based on graph representations of genomes |
| Protein Language Model | 10 | Protein analysis using large-scale pre-trained models |


---

## Featured Algorithms

### Sequence Alignment <a id="sequence-alignment"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Pairwise Alignment**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| ⭐ BLAST | 1990 | O(mn) | O(mn) | `heuristic` `database-search` `classic` |
| ⭐ Smith-Waterman | 1981 | O(mn) | O(mn) | `dynamic-programming` `local-alignment` `classic` |
| ⭐ Needleman-Wunsch | 1970 | O(mn) | O(mn) | `dynamic-programming` `global-alignment` `classic` |
| 🆕 WFA2-lib | 2023 | O(ns) | O(s) | `wavefront` `adaptive` `ultra-fast` |
| Minimap2 | 2018 | O(n) | O(n) | `minimizer` `long-read` `versatile` |

*[View all 14 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Multiple Sequence Alignment**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Clustal Omega | 2011 | O(n * L^2) | O(n * L) | `multiple-alignment` `guide-tree` `progressive` |
| Kalign | 2005 | O(n^2 * L) | O(n * L) | `multiple-alignment` `fast` `wu-manber` |
| MUSCLE | 2004 | O(n^2 * L) | O(n * L) | `multiple-alignment` `iterative` `refinement` |
| MAFFT | 2002 | O(n * L * log L) | O(n * L) | `fft` `multiple-alignment` `scalable` |
| POA | 2002 | O(n^2 * L^2) | O(n * L^2) | `multiple-alignment` `partial-order` `graph-based` |


### Sequence Assembly <a id="sequence-assembly"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**De Novo Assembly**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 Verkko | 2023 | O(n log n) | O(n) | `t2t` `hybrid` `hifi` |
| Hifiasm | 2021 | O(n log n) | O(n) | `hifi` `haplotype-aware` `long-read` |
| Shasta | 2020 | O(n) | O(n) | `long-read` `fast` `run-length` |
| Flye | 2019 | O(n log n) | O(n) | `repeat-graph` `long-read` `ont` |
| Wtdbg2 | 2019 | O(n) | O(n) | `long-read` `fuzzy-bruijn` `fast` |

*[View all 12 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Reference-Guided Assembly**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| RagTag | 2022 | O(n log n) | O(n) | `reference-based` `scaffolding` `assembly-polishing` |
| Reference-Guided Assembly | 2011 | O(n log n) | O(n) | `reference-based` `scaffolding` `resequencing` |


### Variant Calling <a id="variant-calling"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**SNV Detection**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 DeepSomatic | 2024 | O(n * r) | O(r) | `deep-learning` `somatic` `cancer` |
| Clair3 | 2022 | O(n * r) | O(r) | `long-read` `nanopore` `pacbio` |
| Octopus | 2021 | O(n * h) | O(h) | `bayesian` `haplotype` `germline-somatic` |
| DeepVariant | 2018 | O(n * r) | O(r) | `deep-learning` `cnn` `snp` |
| Strelka2 | 2018 | O(n * r) | O(r) | `somatic` `germline` `fast` |

*[View all 8 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Structural Variants**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 Sniffles2 | 2023 | O(n * c) | O(n) | `structural-variant` `long-read` `breakpoint` |
| cuteSV | 2020 | O(n * c) | O(n) | `structural-variant` `long-read` `clustering` |
| GRIDSS | 2017 | O(n * c) | O(n) | `structural-variant` `breakend` `assembly-based` |
| Manta | 2016 | O(n * c) | O(c) | `structural-variant` `graph-assembly` `clinical` |
| SvABA | 2016 | O(n * c) | O(c) | `structural-variant` `somatic` `assembly-based` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*


### Gene Expression Analysis <a id="gene-expression-analysis"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Expression Quantification**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Salmon | 2017 | O(n) | O(t) | `selective-alignment` `quantification` `rna-seq` |
| Kallisto | 2016 | O(n) | O(t) | `pseudoalignment` `quantification` `rna-seq` |
| tximport | 2016 | O(n * t) | O(g) | `import` `summarization` `offset-correction` |
| StringTie | 2015 | O(n) | O(g) | `transcript-assembly` `quantification` `rna-seq` |
| STAR | 2013 | O(n) | O(g) | `rna-seq` `splice-aware` `alignment` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Differential Expression**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Sleuth | 2017 | O(n * g) | O(g) | `differential-expression` `bootstrap` `rna-seq` |
| NOISeq | 2015 | O(n * g) | O(g) | `differential-expression` `non-parametric` `noiseq` |
| DESeq2 | 2014 | O(n * g) | O(g) | `rna-seq` `differential-expression` `negative-binomial` |
| limma-voom | 2014 | O(n * g) | O(g) | `differential-expression` `precision-weight` `linear-model` |
| Ballgown | 2014 | O(n * g) | O(g) | `differential-expression` `fpkm` `transcript-level` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*


### Protein Structure Prediction <a id="protein-structure-prediction"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Ab Initio Prediction**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 AlphaFold3 | 2024 | O(n^2) | O(n^2) | `deep-learning` `structure-prediction` `multi-modal` |
| 🆕 Chai-1 | 2024 | O(n^2) | O(n^2) | `structure-prediction` `multi-modal` `drug-discovery` |
| 🆕 Boltz-1 | 2024 | O(n^2) | O(n^2) | `structure-prediction` `open-source` `diffusion` |
| 🆕 ESMFold | 2023 | O(n^2) | O(n^2) | `language-model` `single-sequence` `fast` |
| OmegaFold | 2022 | O(n^2) | O(n^2) | `language-model` `single-sequence` `structure-prediction` |

*[View all 9 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Template-Based Modeling**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 Foldseek | 2023 | O(n) | O(n) | `structure-search` `fast` `3Di` |
| I-TASSER | 2008 | O(n^3) | O(n^2) | `threading` `template-based` `fragment-assembly` |
| TM-align | 2005 | O(n^3) | O(n^2) | `structure-alignment` `rmsd` `classic` |
| Rosetta | 2003 | O(n^3) | O(n^2) | `energy-function` `monte-carlo` `protein-design` |
| MODELLER | 1993 | O(n^2) | O(n^2) | `homology-modeling` `template-based` `comparative-modeling` |


### Phylogenetics <a id="phylogenetics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Distance Methods**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| ⭐ Neighbor-Joining | 1987 | O(n^3) | O(n^2) | `distance-based` `tree-building` `classic` |
| FastTree | 2010 | O(n * s * log n) | O(n * s) | `tree-building` `approximate-likelihood` `scalable` |

**Character-Based Methods**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| IQ-TREE 2 | 2020 | O(n^2 * s) | O(n * s) | `maximum-likelihood` `model-finder` `partition` |
| RAxML-NG | 2019 | O(n^2 * s * r) | O(n * s) | `maximum-likelihood` `scalable` `ultrafast-bootstrap` |
| ASTRAL | 2018 | O(n * m) | O(n * m) | `species-tree` `summary-method` `coalescent` |
| RevBayes | 2016 | O(n^2 * s * r) | O(n * s) | `bayesian` `probabilistic-programming` `flexible` |
| IQ-TREE | 2015 | O(n^2 * s) | O(n * s) | `maximum-likelihood` `model-selection` `ultrafast-bootstrap` |

*[View all 10 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*


### Functional Annotation <a id="functional-annotation"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Homology-Based**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| ⭐ BLAST-based Annotation | 1990 | O(mn) | O(m) | `sequence-similarity` `database-search` `classic` |
| Bakta | 2021 | O(n) | O(n) | `prokaryotic` `annotation` `standardized` |
| KofamKOALA | 2020 | O(n * m) | O(m) | `kegg` `orthology` `annotation` |
| OrthoFinder | 2019 | O(n^2) | O(n^2) | `orthology` `comparative-genomics` `gene-family` |
| eggNOG-mapper | 2017 | O(n * m) | O(m) | `orthology` `go-annotation` `kegg` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Domain-Based**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| SignalP | 2019 | O(n) | O(n) | `signal-peptide` `deep-learning` `secretion` |
| InterProScan | 2014 | O(m * d) | O(m) | `multi-database` `domain-detection` `go-annotation` |
| InterPro | 2014 | O(m * d) | O(m) | `database` `domain` `protein-family` |
| HMMER | 2011 | O(mn) | O(m) | `hmm` `domain-detection` `remote-homology` |
| PfamScan | 2011 | O(mn) | O(m) | `domain-detection` `pfam` `protein-family` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*


### Data Compression <a id="data-compression"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Specialized Compression**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Genozip | 2021 | O(n) | O(1) | `multi-format` `high-ratio` `random-access` |
| SPRING Compress | 2020 | O(n log n) | O(n) | `fastq` `reordering` `high-ratio` |
| SPRING | 2019 | O(n) | O(n) | `fastq` `specialized-compression` `high-ratio` |
| MANGO | 2018 | O(n) | O(n) | `reference-free` `genome-compression` `context-modeling` |
| Orione | 2015 | O(n) | O(1) | `reference-assisted` `fastq` `sam` |

*[View all 8 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**General Compression**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| BGZF and Tabix | 2011 | O(n) | O(1) | `block-compression` `indexing` `random-access` |
| GZIP for FASTQ | 1992 | O(n) | O(1) | `lossless` `general-purpose` `standard` |


### Single-Cell Genomics <a id="single-cell-genomics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Cell Clustering & Annotation**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 scVI-tools | 2023 | O(c * g * e) | O(c * g) | `variational-autoencoder` `deep-learning` `batch-correction` |
| scArches | 2022 | O(c * g * e) | O(c * g) | `reference-mapping` `transfer-learning` `surgery` |
| CellTypist | 2022 | O(c * g) | O(c * g) | `cell-type` `annotation` `logistic-regression` |
| scANVI | 2021 | O(c * g * e) | O(c * g) | `semi-supervised` `annotation` `deep-learning` |
| SCENIC | 2020 | O(c * g^2) | O(c * g) | `regulatory-network` `transcription-factor` `grn` |

*[View all 10 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Preprocessing**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| alevin-fry | 2022 | O(n * k) | O(g) | `quantification` `memory-efficient` `simpleaf` |
| STARsolo | 2021 | O(n * g) | O(c * g) | `preprocessing` `alignment` `umi` |
| kallisto | bustools | 2021 | O(n * k) | O(g) | `preprocessing` `pseudoalignment` `fast` |
| Alevin | 2019 | O(n * g) | O(c * g) | `preprocessing` `umi` `lightweight-mapping` |
| Cell Ranger | 2017 | O(n * g) | O(c * g) | `10x-genomics` `preprocessing` `umi` |


### Metagenomics <a id="metagenomics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Taxonomic Profiling**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 MetaPhlAn 4 | 2023 | O(n * m) | O(m) | `marker-gene` `profiling` `enhanced` |
| Kraken2 | 2019 | O(n * k) | O(d) | `k-mer` `classification` `fast` |
| QIIME 2 | 2019 | O(n * d) | O(n) | `pipeline` `microbiome` `diversity` |
| MetaBAT 2 | 2019 | O(n * c) | O(n) | `binning` `metagenome` `adaptive` |
| mOTUs | 2017 | O(n * m) | O(m) | `marker-gene` `profiling` `universal` |

*[View all 9 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Functional Profiling**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| metaPOST | 2021 | O(n * c) | O(n) | `post-processing` `refinement` `assembly` |
| MetaBAT 2 | 2019 | O(n * c) | O(n) | `binning` `mags` `coverage` |
| HUMAnN 3 | 2018 | O(n * d) | O(d) | `functional-profiling` `pathway` `gene-families` |
| MaxBin 2 | 2016 | O(n * c) | O(n) | `binning` `expectation-maximization` `mags` |
| HUMAnN | 2014 | O(n * d) | O(d) | `pathway-analysis` `gene-family` `functional` |


### Epigenomics <a id="epigenomics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**ChIP-seq Analysis**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| HMMRATAC | 2019 | O(n) | O(n) | `atac-seq` `hmm` `peak-calling` |
| ChromHMM | 2012 | O(n * s^2) | O(n * s) | `hmm` `chromatin-state` `histone` |
| MACS2 | 2008 | O(n) | O(n) | `peak-calling` `chip-seq` `histone` |

**Methylation Analysis**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| DSS | 2014 | O(n * s) | O(n) | `methylation` `beta-binomial` `dmr` |
| methylKit | 2012 | O(n * s) | O(n) | `methylation` `differential-analysis` `rrbs` |
| Bismark | 2011 | O(n * g) | O(g) | `bisulfite-seq` `methylation` `cpg` |


### Gene Prediction <a id="gene-prediction"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Eukaryotic Gene Prediction**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| BRAKER | 2016 | O(n * g) | O(n) | `pipeline` `evidence-based` `automated` |
| MAKER | 2008 | O(n * g) | O(n) | `annotation-pipeline` `evidence-based` `eukaryotic` |
| AUGUSTUS | 2005 | O(n * s^2) | O(n * s) | `gene-prediction` `eukaryotic` `hmm` |
| SNAP | 2004 | O(n * s) | O(n) | `semi-hmm` `ab-initio` `eukaryotic` |
| AUGUSTUS | 2003 | O(n * s^2) | O(n * s) | `ghmm` `ab-initio` `exon-intron` |

**Prokaryotic Gene Prediction**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Prodigal | 2010 | O(n) | O(n) | `prokaryotic` `self-training` `metagenome` |
| Prodigal | 2010 | O(n) | O(n) | `gene-prediction` `prokaryotic` `fast` |
| RNAmmer | 2007 | O(n * s) | O(n) | `rrna` `gene-prediction` `hmm` |
| GeneMark-ES | 2005 | O(n) | O(n) | `gene-prediction` `hmm` `prokaryotic` |
| GLIMMER | 1998 | O(n) | O(n) | `interpolated-markov-model` `prokaryotic` `gene-finding` |

*[View all 7 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*


### Population Genetics <a id="population-genetics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Selection Signature Detection**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| ⭐ Tajima's D | 1989 | O(n * L) | O(L) | `neutrality-test` `selection` `classic` |
| PCAdapt | 2016 | O(n * m * k) | O(n * m) | `selection` `pca` `outlier-detection` |
| Selscan | 2014 | O(n * m) | O(n * m) | `selection` `haplotype` `ihs` |
| HapFLK | 2013 | O(n * m * K) | O(m * K) | `selection` `haplotype` `population-differentiation` |
| BayeScan | 2008 | O(m * k * n) | O(m * k) | `selection` `bayesian` `fst` |

**Genome-Wide Association Study**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| REGENIE | 2021 | O(n * m) | O(n * m) | `gwas` `scalable` `two-stage` |
| SAIGE | 2018 | O(n * m) | O(n * m) | `gwas` `mixed-model` `rare-variant` |
| BOLT-LMM | 2015 | O(n * m) | O(n * m) | `lmm` `gwas` `scalable` |
| PLINK | 2007 | O(n * m) | O(n * m) | `gwas` `association` `qc` |

**PCA & Population Structure**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| ADMIXTURE | 2009 | O(n * m * k) | O(n * m) | `ancestry` `maximum-likelihood` `population-structure` |
| PCA for Population Structure | 2006 | O(n * m * k) | O(n * m) | `pca` `population-structure` `ancestry` |
| STRUCTURE | 2000 | O(n * m * k * g) | O(n * k) | `bayesian` `mcmc` `population-structure` |


### Spatial Omics <a id="spatial-omics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Spatial Transcriptomics**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Seurat Spatial | 2021 | O(c * g) | O(c * g) | `spatial` `clustering` `integration` |
| Giotto Suite | 2021 | O(c * g) | O(c * g) | `spatial` `multi-platform` `comprehensive` |
| Squidpy | 2021 | O(c * g) | O(c * g) | `spatial` `graph-analysis` `cell-interaction` |
| SPARK-X | 2021 | O(g * n) | O(n) | `spatial` `fast` `non-parametric` |
| stLearn | 2021 | O(c * g) | O(c * g) | `spatial` `image-integration` `trajectory` |

*[View all 7 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Spatial Proteomics**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| CellChat | 2021 | O(c^2 * g) | O(c^2) | `cell-communication` `ligand-receptor` `signaling` |
| Cellpose | 2020 | O(p) | O(p) | `segmentation` `deep-learning` `cell-detection` |
| StarDist | 2018 | O(p) | O(p) | `segmentation` `deep-learning` `cell-nuclei` |


### Graph Genomics <a id="graph-genomics"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Variation Graph**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 PanVC | 2023 | O(n * m) | O(n) | `pangenome` `variant-calling` `genotyping` |
| HiFiBD | 2022 | O(n * d) | O(n) | `variation-graph` `hifi` `genotyping` |
| GraphAligner | 2019 | O(n * d) | O(n) | `graph-alignment` `long-read` `variation-graph` |
| VG (Variation Graph) | 2017 | O(n log n) | O(n) | `variation-graph` `alignment` `variant-calling` |
| GCSA2 | 2017 | O(n) | O(n) | `indexing` `k-mer` `compressed-suffix-array` |

**Pangenome**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| Minigraph | 2020 | O(n log n) | O(n) | `pangenome` `graph-alignment` `minimizer` |
| odgi | 2020 | O(n) | O(n) | `pangenome` `graph-operations` `visualization` |
| seqwish | 2020 | O(n^2) | O(n^2) | `pangenome` `graph-construction` `alignment-to-graph` |
| Cactus | 2011 | O(n^2 * k) | O(n * k) | `pangenome` `alignment` `progressive` |


### Protein Language Model <a id="protein-language-model"></a>
<a href="#table-of-contents">↑ Back to Top</a>

**Protein Function Prediction**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 ESMFold | 2023 | O(n^2) | O(n^2) | `structure-prediction` `single-sequence` `fast` |
| 🆕 RFdiffusion | 2023 | O(n^2 * T) | O(n^2) | `diffusion-model` `protein-design` `structure-generation` |
| ProteinMPNN | 2022 | O(n^2 * d) | O(n^2) | `protein-design` `inverse-folding` `graph-neural-network` |
| ESM-1v | 2021 | O(n^2 * d) | O(n^2) | `variant-effect` `zero-shot` `pathogenicity` |
| ProGen | 2020 | O(n^2 * d) | O(n^2) | `generative` `protein-design` `conditional-generation` |

*[View all 6 algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*

**Protein Language Model Pretraining**

| Algorithm | Year | Time | Space | Tags |
|-----------|------|------|-------|------|
| 🆕 Ankh | 2023 | O(n^2 * d) | O(n^2) | `language-model` `lightweight` `efficient` |
| ESM-2 | 2022 | O(n^2 * d) | O(n^2) | `language-model` `transformer` `representation-learning` |
| ProtTrans | 2021 | O(n^2 * d) | O(n^2) | `language-model` `transfer-learning` `representation-learning` |
| ProtBERT | 2020 | O(n^2 * d) | O(n^2) | `language-model` `bert` `sequence-embedding` |



---

## 🛠️ CLI Commands

```bash
# Search for algorithms
python -m awesome_bioinfo search "alignment"

# Get algorithm details
python -m awesome_bioinfo info smith-waterman

# Compare two algorithms
python -m awesome_bioinfo compare smith-waterman needleman-wunsch

# Export data to JSON
python -m awesome_bioinfo export --format json > algorithms.json

# Generate MkDocs site
python -m awesome_bioinfo mkdocs

# Generate README
python -m awesome_bioinfo generate
```

---

## 📚 Resources

### Learning Platforms
- [Rosalind](http://rosalind.info/) — Bioinformatics algorithm learning
- [NCBI](https://www.ncbi.nlm.nih.gov/) — National Center for Biotechnology
- [EBI](https://www.ebi.ac.uk/) — European Bioinformatics Institute

### Tools & Communities
- [Bioconductor](https://www.bioconductor.org/) — R bioinformatics toolkit
- [Galaxy](https://usegalaxy.org/) — Open analysis platform
- [BioStars](https://www.biostars.org/) — Bioinformatics Q&A
- [scverse](https://scverse.org/) — Single-cell Python ecosystem

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Contribution Types

- 🆕 **Add new algorithms**
- 📝 **Improve descriptions**
- 🔗 **Add references**
- 🐛 **Report and fix bugs**
- 📚 **Improve documentation**

---

## 📚 Citation

If you use this project in your research, please cite it as:

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

## 📄 License

<p align="center">
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" alt="CC0">
  </a>
</p>

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain).

You are free to:
- ✅ Copy, modify, distribute
- ✅ Use for commercial purposes
- ✅ No attribution required

---

<p align="center">
  <b>Made with ❤️ by the community</b><br>
  © 2025-2026 <a href="https://github.com/LessUp">LessUp</a> Community
</p>
