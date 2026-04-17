---
title: Home
layout: home
nav_order: 1
description: "Awesome Bioinformatics Algorithms — A curated list of bioinformatics algorithms"
permalink: /en/
---

# Awesome Bioinformatics Algorithms
{: .fs-9 }

🧬 A curated list of bioinformatics algorithms — providing concise introductions, complexity analysis, and related resource links.
{: .fs-6 .fw-300 }

This project collects and organizes commonly used algorithms in bioinformatics, helping researchers and developers quickly understand and choose appropriate algorithms for their needs. All content is community-driven and open source.
{: .fs-4 .text-grey-dk-100 }

[Explore Algorithms](https://github.com/LessUp/awesome-bioinfo-algorithms#sequence-alignment){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[API Documentation]({% link en/api.md %}){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Development Guide]({% link en/development.md %}){: .btn .btn-outline .fs-5 .mb-4 .mb-md-0 }

---

## 📊 Statistics

We currently maintain **201 algorithms** across **16 categories**, providing comprehensive coverage of the bioinformatics landscape.

| Metric | Count |
|:-------|------:|
| Total Algorithms | **201** |
| Categories | **16** |
| Unique Tags | **399** |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Git

### Installation

```bash
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
pip install -e ".[dev]"
```

### Core Commands

```bash
# Generate README from data
python -m awesome_bioinfo generate

# Validate data integrity
python -m awesome_bioinfo validate

# View statistics
python -m awesome_bioinfo stats

# Search algorithms
python -m awesome_bioinfo search "alignment"

# Get algorithm details
python -m awesome_bioinfo info smith-waterman
```

---

## 📚 Documentation

| Document | Description |
|:---------|:------------|
| [API Documentation]({% link en/api.md %}) | Public API reference and code examples |
| [Development Guide]({% link en/development.md %}) | Project structure, environment setup, and architecture |
| [FAQ]({% link en/faq.md %}) | Frequently asked questions and troubleshooting |
| [Contributing Guide]({% link en/contributing.md %}) | How to add algorithms, branch conventions, and PR workflow |
| [Changelog]({% link en/changelog.md %}) | Version release history |
| [Security Policy]({% link en/security.md %}) | Vulnerability reporting and handling process |

---

## 🌐 Language Selection

- [English]({% link en/index.md %}) (Current)
- [中文]({% link zh/index.md %}) (Chinese)

---

## 🏷️ Algorithm Categories

### Sequence Analysis
- **Sequence Alignment** — Pairwise and multiple sequence alignment algorithms
- **Sequence Assembly** — De novo and reference-guided assembly methods
- **Variant Calling** — SNV detection and structural variant algorithms

### Expression & Function
- **Gene Expression Analysis** — Quantification and differential expression
- **Functional Annotation** — Homology-based and domain-based methods

### Omics Technologies
- **Single-Cell Genomics** — Preprocessing and cell clustering
- **Metagenomics** — Taxonomic and functional profiling
- **Epigenomics** — ChIP-seq and methylation analysis
- **Spatial Omics** — Spatial transcriptomics and proteomics

### Structure & Evolution
- **Protein Structure Prediction** — Ab initio and template-based modeling
- **Phylogenetics** — Distance and character-based methods

### Advanced Topics
- **Population Genetics** — GWAS, PCA, and selection analysis
- **Graph Genomics** — Pangenome and variation graphs
- **Protein Language Models** — Pre-training and function prediction

---

## 🤝 Contributing

We welcome contributions in the following areas:

- 🆕 Adding new algorithms
- 📝 Improving existing descriptions
- 🔗 Adding reference links
- 🐛 Bug fixes

Please read our [Contributing Guide]({% link en/contributing.md %}) for detailed instructions.

---

## 📖 Related Resources

| Resource | Description |
|:---------|:------------|
| [Rosalind](http://rosalind.info/) | Bioinformatics algorithm learning platform |
| [NCBI](https://www.ncbi.nlm.nih.gov/) | National Center for Biotechnology Information |
| [EBI](https://www.ebi.ac.uk/) | European Bioinformatics Institute |
| [Bioconductor](https://www.bioconductor.org/) | R bioinformatics toolkit |
| [Galaxy](https://usegalaxy.org/) | Open bioinformatics analysis platform |
| [BioStars](https://www.biostars.org/) | Bioinformatics Q&A community |
| [scverse](https://scverse.org/) | Single-cell analysis Python ecosystem |

---

## 📄 License

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). 
You are free to copy, modify, distribute and use this project for any purpose.

---

© 2025-2026 LessUp Community
