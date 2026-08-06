# AGENTS.md

AI 助手工作指引。详细架构与模块说明见 [`CLAUDE.md`](CLAUDE.md)。

## 项目

精选生物信息学算法 awesome-list：YAML 数据 + Python CLI（`awesome_bioinfo` 包）+ 自动生成的中文 README。轻量、业余维护。

## 核心规则

- `README.md` 由 `python -m awesome_bioinfo generate` 从 `templates/readme_template.md` 生成，**禁止手工编辑**。
- 改 `data/` 或 `templates/` 后必须重新生成并确认无漂移：`python -m awesome_bioinfo generate && git diff --exit-code -- README.md`。
- 数据真相源在 `data/algorithms/*.yaml` 与 `data/categories.yaml`。

## 常用命令

```bash
python -m awesome_bioinfo validate          # 数据变更前必过
python -m awesome_bioinfo stats
python -m awesome_bioinfo search <query>
python -m awesome_bioinfo info <id>
python -m awesome_bioinfo compare <id1> <id2>
python -m awesome_bioinfo export --format json
python -m awesome_bioinfo generate          # 生成 README.md
python -m awesome_bioinfo check-links       # 检查条目 URL 有效性

ruff check awesome_bioinfo tests
pytest tests/ -v --tb=short
```

## 算法条目

- 必填：`id`（lowercase-hyphenated，全局唯一）、`name`、`description`（50-500 字）、`purpose`、`time_complexity`（`O(...)`）、`category`
- `category`/`subcategory` 必须存在于 `data/categories.yaml`
- 模板：`templates/algorithm_template.yaml`
