# CLAUDE.md

> AI 助手项目上下文。权威来源优先级见下方层级表。

## 权威来源层级

1. `openspec/specs/` — 需求与设计的唯一真相来源
2. `data/` — 算法与分类数据（`algorithms/*.yaml`, `categories.yaml`）
3. `awesome_bioinfo/` — 实现，需与 specs 保持一致
4. `mkdocs/` — 公开文档（MkDocs Material），唯一权威文档渠道
5. `.github/copilot-instructions.md` — Copilot 工作流规则（何时走 OpenSpec、何时直接编辑）

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
