---
title: Awesome Bioinformatics Algorithms
hide:
  - navigation
  - toc
---

<!-- Hero Section -->
<div class="hero-section" style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, var(--md-primary-fg-color--lightest) 0%, var(--md-default-bg-color) 50%, var(--md-accent-fg-color--lightest) 100%); border-radius: 20px; margin: 2rem 0;">

# <span class="gradient-text" style="font-size: 3.5rem; font-weight: 800;">🧬 Awesome Bioinformatics Algorithms</span>

<p style="font-size: 1.5rem; color: var(--md-default-fg-color--light); max-width: 800px; margin: 1.5rem auto;">
  A curated collection of <strong>201 bioinformatics algorithms</strong> <br>
  with complexity analysis, implementation links, and comprehensive documentation
</p>

<div class="stat-cards" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; max-width: 700px; margin: 2rem auto;">

<div class="stat-card" style="background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: var(--md-shadow-md);">
  <div class="stat-number" style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, var(--md-primary-fg-color), var(--md-accent-fg-color)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">201</div>
  <div class="stat-label" style="color: var(--md-default-fg-color--light); margin-top: 0.5rem;">Algorithms</div>
</div>

<div class="stat-card" style="background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: var(--md-shadow-md);">
  <div class="stat-number" style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, var(--md-primary-fg-color), var(--md-accent-fg-color)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">16</div>
  <div class="stat-label" style="color: var(--md-default-fg-color--light); margin-top: 0.5rem;">Categories</div>
</div>

<div class="stat-card" style="background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: var(--md-shadow-md);">
  <div class="stat-number" style="font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, var(--md-primary-fg-color), var(--md-accent-fg-color)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">399</div>
  <div class="stat-label" style="color: var(--md-default-fg-color--light); margin-top: 0.5rem;">Tags</div>
</div>

</div>

<div class="hero-cta" style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 2rem;">

[Explore Algorithms](algorithms/index.md){ .md-button .md-button--primary }

[Browse by Category](categories/index.md){ .md-button .md-button--secondary }

[View on GitHub](https://github.com/LessUp/awesome-bioinfo-algorithms){ .md-button .md-button--secondary target="_blank" }

</div>

</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git

# Install dependencies
pip install -e ".[dev]"

# Search for algorithms
python -m scripts search "sequence alignment"
```

---

## 📚 Featured Categories

<div class="grid cards" markdown>

-   :material-dna:{ .lg .middle } __Sequence Alignment__

    ---

    Algorithms for comparing and aligning biological sequences
    
    - Smith-Waterman
    - BLAST
    - Bowtie2
    - Minimap2
    
    [:octicons-arrow-right-24: Explore](categories/sequence-alignment.md)

-   :material-assemble:{ .lg .middle } __Sequence Assembly__

    ---

    De novo and reference-guided assembly methods
    
    - SPAdes
    - Canu
    - Flye
    - Hifiasm
    
    [:octicons-arrow-right-24: Explore](categories/assembly.md)

-   :material-chart-bar:{ .lg .middle } __Variant Calling__

    ---

    Detection of genomic variants
    
    - GATK
    - DeepVariant
    - Strelka2
    - Clair3
    
    [:octicons-arrow-right-24: Explore](categories/variant-calling.md)

-   :material-cell:{ .lg .middle } __Protein Structure__

    ---

    Protein structure prediction algorithms
    
    - AlphaFold
    - ESMFold
    - RoseTTAFold
    - OmegaFold
    
    [:octicons-arrow-right-24: Explore](categories/protein-structure.md)

-   :material-grid:{ .lg .middle } __Single-Cell Analysis__

    ---

    Single-cell genomics algorithms
    
    - Seurat
    - Scanpy
    - scVI
    - Monocle3
    
    [:octicons-arrow-right-24: Explore](categories/single-cell.md)

-   :material-brain:{ .lg .middle } __Protein Language Models__

    ---

    AI-powered protein analysis
    
    - ESM-2
    - ProtTrans
    - Ankh
    - ProteinBERT
    
    [:octicons-arrow-right-24: Explore](categories/protein-language-model.md)

</div>

---

## 🔍 Popular Algorithms

| Algorithm | Category | Time Complexity | Best For |
|:----------|:---------|:----------------|:---------|
| [Smith-Waterman](algorithms/smith-waterman.md) | Alignment | O(m×n) | Local alignment |
| [BLAST](algorithms/blast.md) | Alignment | O(n) | Database search |
| [AlphaFold](algorithms/alphafold.md) | Structure | N/A | Protein folding |
| [STAR](algorithms/star.md) | Expression | O(n) | RNA-seq alignment |
| [Seurat](algorithms/seurat.md) | Single-Cell | N/A | Cell clustering |
| [DeepVariant](algorithms/deepvariant.md) | Variant Calling | N/A | Deep learning calling |

---

## ✨ Features

<div class="grid" markdown>

-   __Comprehensive Coverage__

    ---

    201 algorithms across 16 categories with detailed complexity analysis

-   __Bilingual Documentation__

    ---

    Full support for English and Chinese languages

-   __Powerful Search__

    ---

    Fast, intelligent search with suggestions and highlighting

-   __Open Source__

    ---

    CC0 1.0 Universal license - free for any use

-   __CLI Tools__

    ---

    Search, compare, and export algorithms from command line

-   __Auto-Generated__

    ---

    README and docs generated from structured YAML data

</div>

---

## 🛠️ CLI Commands

```bash
# Search algorithms
python -m scripts search "alignment"

# Get algorithm details
python -m scripts info smith-waterman

# Compare algorithms
python -m scripts compare smith-waterman needleman-wunsch

# Export data
python -m scripts export --format json > algorithms.json

# View statistics
python -m scripts stats
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for details.

- 🆕 Add new algorithms
- 📝 Improve descriptions
- 🔗 Add reference links
- 🐛 Fix bugs
- 📚 Improve documentation

---

## 📄 License

This project is licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain).

You are free to copy, modify, distribute and use this project for any purpose.

---

<div style="text-align: center; padding: 2rem 0;">
  <p><strong>Made with ❤️ by the <a href="https://github.com/LessUp">LessUp Community</a></strong></p>
  <p style="color: var(--md-default-fg-color--light);">© 2025-2026</p>
</div>
