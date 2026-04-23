<h1 align="center">Awesome Bioinformatics Algorithms</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml"><img src="https://github.com/LessUp/awesome-bioinfo-algorithms/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://lessup.github.io/awesome-bioinfo-algorithms/"><img src="https://img.shields.io/badge/Docs-GitHub%20Pages-blue?logo=github" alt="Documentation"></a>
  <a href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg" alt="License"></a>
  <a href="https://github.com/LessUp/awesome-bioinfo-algorithms/blob/main/CITATION.cff"><img src="https://img.shields.io/badge/Cite%20Me-APA-blue" alt="Citation"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Algorithms-{{ total_algorithms }}-blue.svg" alt="Algorithms">
  <img src="https://img.shields.io/badge/Categories-{{ total_categories }}-green.svg" alt="Categories">
  <img src="https://img.shields.io/badge/Tags-{{ total_tags }}-orange.svg" alt="Tags">
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
- {{ total_algorithms }}+ curated algorithms
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

# Install dependencies
pip install -e ".[dev]"

# Validate data
python -m awesome_bioinfo validate

# Show statistics
python -m awesome_bioinfo stats
```

---

## 📊 Statistics

| Metric | Value |
|:-------|------:|
| Total Algorithms | **{{ total_algorithms }}** |
| Categories | **{{ total_categories }}** |
| Unique Tags | **{{ total_tags }}** |

---

## 📑 Table of Contents

{{ toc }}

---

{{ category_overview }}

---

{{ featured_content }}

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
