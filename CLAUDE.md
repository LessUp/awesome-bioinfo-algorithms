# CLAUDE.md

> AI 助手项目上下文。权威来源优先级见下方层级表。

## 权威来源层级

1. `openspec/specs/` — 需求与设计的唯一真相来源
2. `data/` — 算法与分类数据（`algorithms/*.yaml`, `categories.yaml`）
3. `awesome_bioinfo/` — 实现，需与 specs 保持一致
4. `mkdocs/` — 公开文档（MkDocs Material），唯一权威文档渠道
5. `.github/copilot-instructions.md` — Copilot 工作流规则（何时走 OpenSpec、何时直接编辑）

## OpenSpec-Driven Development

本项目遵循 **OpenSpec** 进行规范驱动开发（SDD）。`openspec/specs/` 目录是所有需求的唯一来源。

### OpenSpec 工作流

1. **提出变更**：使用 `/opsx:propose <idea>` 创建变更提案
2. **审查规范**：实现前阅读 `openspec/specs/` 中相关规范
3. **实现任务**：使用 `/opsx:apply` 实现提案中的任务
4. **归档完成**：使用 `/opsx:archive` 完成归档并更新规范

### OpenSpec 命令

| 命令 | 说明 |
|------|------|
| `/opsx:propose <idea>` | 创建新变更提案（含规范、设计、任务） |
| `/opsx:apply` | 实现当前变更提案中的任务 |
| `/opsx:archive` | 归档已完成的变更并更新规范 |

### 规范能力

| 能力 | 位置 | 用途 |
|------|------|------|
| product-vision | `openspec/specs/product-vision/spec.md` | WHAT to build - 产品需求 |
| core-architecture | `openspec/specs/core-architecture/spec.md` | HOW to build - 技术设计 |
| cli-interface | `openspec/specs/cli-interface/spec.md` | CLI 命令契约 |
| algorithm-schema | `openspec/specs/algorithm-schema/spec.md` | YAML 数据模式 |
| testing-strategy | `openspec/specs/testing-strategy/spec.md` | 测试需求 |

### 何时使用提案 vs 直接编辑

| 情况 | 操作 |
|------|------|
| 修复 typo、更新 URL、添加单个算法条目 | 直接编辑，无需提案 |
| 新增 CLI 命令、修改校验规则 | `/opsx:propose` → `/opsx:apply` → `/opsx:archive` |
| 任何涉及多个规范或 Python 模块的变更 | `/opsx:propose` → `/opsx:apply` → `/opsx:archive` |
| 更新已合并代码对应的规范 | 直接编辑规范，无需提案 |

### 分支策略

保持分支轻量化：

- **小修复**（数据条目、文档、单文件编辑）：直接提交到默认分支（当前为 `master`）
- **非小变更**（新功能、重构、多文件）：创建短生命周期分支 `<type>/<short-description>`（如 `feat/add-blast-entry`），通过 PR 合并，合并后删除分支
- 避免长生命周期分支，变更应足够小以在一两天内合并
- 合并后若 `data/` 或模板有变更，需重新生成输出（见下方）

### 何时使用 `/review`

在以下情况下，合并前调用 `/review`：

- 变更涉及 `awesome_bioinfo/` 中的 Python 逻辑
- 变更修改了 `openspec/specs/` 中的规范
- 变更添加或删除了分类
- 不确定实现是否与规范匹配

对于纯数据添加（通过 `validate` 的新算法 YAML 条目）和文档 typo 修复，可跳过 `/review`。

### MCP vs CLI Skills

- **MCP 用于外部 GitHub 状态**：仓库元数据、issues/PRs、Actions 运行/日志等远程设置
- **本地 CLI Skills 用于仓库内维护循环**：源数据已在检出中

当前高价值本地 skills：
- `verify` — 快速 lint + typecheck 检查
- `updating-algorithm-data` — 分类/算法 YAML 变更、验证、重新生成、生成输出漂移检查

## 架构简图

```
data/
  categories.yaml          # 16 个顶级分类定义
  algorithms/*.yaml        # 每类一个文件，顶级键 algorithms:

awesome_bioinfo/           # 核心 Python 包
  schema.py                # 数据类: Category, AlgorithmEntry, Reference
  algorithm_registry.py    # 加载、索引、搜索
  category_manager.py      # 分类层级查询
  validate.py              # 字段规则验证（含 JSON Schema）
  data_io.py               # YAML/JSON 导入导出
  readme_generator.py      # 生成 README.md（从模板）
  generate_mkdocs.py       # 生成 mkdocs/docs/
  __main__.py              # CLI 入口（python -m awesome_bioinfo）
  search.py / info_cmd.py / compare.py / export_cmd.py / link_checker.py

templates/
  algorithm_template.yaml  # 新条目模板
  readme_template.md       # README 模板

schemas/
  algorithm-schema.json    # JSON Schema（validate 命令使用）

openspec/specs/            # 需求规格（各子目录含 spec.md）
```

## 生成输出（禁止手动编辑）

| 文件/目录 | 生成命令 |
|---|---|
| `README.md` | `python -m awesome_bioinfo generate` |
| `mkdocs/docs/` | `python -m awesome_bioinfo mkdocs` |

数据或模板变更后须重新生成并验证无漂移：

```bash
python -m awesome_bioinfo generate && python -m awesome_bioinfo mkdocs
git diff --exit-code -- README.md mkdocs/docs/
```

**`README.zh-CN.md` 为手动维护，永远不要自动覆写。**

## 常用命令

```bash
# 验证与统计
python -m awesome_bioinfo validate          # 数据 PR 必须通过
python -m awesome_bioinfo stats

# 查询
python -m awesome_bioinfo search <query>
python -m awesome_bioinfo info <id>
python -m awesome_bioinfo compare <id1> <id2>
python -m awesome_bioinfo export --format json

# Lint / 类型检查 / 测试
ruff check awesome_bioinfo tests && mypy awesome_bioinfo --ignore-missing-imports
pytest tests/ -v --tb=short
```

## 算法条目规则

- **必填**：`id`, `name`, `description`, `purpose`, `time_complexity`, `category`
- `description`：50–500 字符（trimmed）
- `id`：全局唯一，小写字母 + 连字符（如 `smith-waterman`）
- `tags`：小写字母 + 连字符
- `category` / `subcategory`：必须存在于 `data/categories.yaml`
- `difficulty`：`beginner` | `intermediate` | `advanced`
- `time_complexity` / `space_complexity`：须匹配 `O(...)` 模式
- 模板：`templates/algorithm_template.yaml`

**可选字段**：
- `space_complexity`, `year`, `paper_url`, `implementation_url`
- `related_tools`, `tags`, `subcategory`, `difficulty`, `language`
- `references`（扩展资料列表）
- `description_en`, `purpose_en`（英文翻译）

### 添加新算法

1. 复制模板：`templates/algorithm_template.yaml`
2. 创建文件：`data/algorithms/<category>.yaml`（追加到现有文件或新建）
3. 填写字段，确保描述长度 50-500 字符
4. 运行验证：`python -m awesome_bioinfo validate`
5. 生成 README：`python -m awesome_bioinfo generate`

## 命名与代码约定

- 算法/分类 ID：lowercase-hyphenated
- Python 模块：snake_case；数据类：PascalCase
- 行宽 100（Ruff）；mypy `ignore_missing_imports = true`
- YAML 文件编码 UTF-8；双语支持通过 `*_en` 可选字段

## Git 约定

- 默认分支：`master`
- 提交信息：Conventional Commits
- PR 合并前：CI 运行 lint、typecheck、tests

## 常见陷阱

- `scripts/` 已废弃，改用 `python -m awesome_bioinfo`
- `docs/` 目录已移除，MkDocs 在 `mkdocs/` 下
- 不要修改 `README.md` 或 `mkdocs/docs/`（生成文件）
- 添加/删除分类是 spec 级变更，需走 `/opsx:propose`
- `data/categories.yaml` 变更后，所有引用该分类的算法文件都需同步更新

## 全局规范与约定

### 代码风格

- **行宽**：100 字符
- **Lint**：ruff (E, F, W, I, N, UP, B, C4 规则)
- **类型检查**：mypy（渐进式严格模式）
- **格式化**：遵循 ruff 规则

### 命名约定

- **算法 ID**：小写字母 + 连字符（如 `smith-waterman`）
- **分类 ID**：小写字母 + 连字符（如 `sequence-alignment`）
- **Python 模块**：snake_case
- **数据类**：PascalCase（如 `AlgorithmEntry`）

### 数据约定

- **编码**：UTF-8
- **格式**：YAML（算法文件使用 `algorithms:` 顶级键）
- **双语支持**：中文为主，可选 `*_en` 英文字段

### Git 工作流

- **主分支**：`master`
- **提交信息**：遵循 Conventional Commits
- **PR 检查**：CI 运行 lint、typecheck、tests

### 测试覆盖

- **最低覆盖率**：85%
- **测试框架**：pytest + hypothesis（属性测试）
- **测试位置**：`tests/` 目录，命名 `test_*.py`

## 关键文件清单

| 文件 | 用途 |
|------|------|
| [`pyproject.toml`](pyproject.toml) | 项目配置、依赖、工具设置 |
| [`data/categories.yaml`](data/categories.yaml) | 16 个顶级分类定义 |
| [`data/algorithms/*.yaml`](data/algorithms/) | 16 个分类的算法数据文件 |
| [`templates/algorithm_template.yaml`](templates/algorithm_template.yaml) | 新算法条目模板 |
| [`templates/readme_template.md`](templates/readme_template.md) | README 生成模板 |

## 项目统计

- **版本**：1.0.2
- **算法数量**：195 条目
- **分类数量**：16 个顶级分类 + 子分类
- **标签数量**：392 个
- **Python 模块**：15 个核心文件
- **测试文件**：15 个
- **测试覆盖率**：89%

---

*此文档由 AI 上下文初始化流程自动生成，最后更新：2026-04-27*
