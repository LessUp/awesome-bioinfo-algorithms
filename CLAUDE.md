# CLAUDE.md

> AI 助手项目上下文。

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
  data_store.py            # 数据存储
  readme_generator.py      # 生成 README.md（从模板）
  generate_docs.py         # 生成 VitePress 文档 (docs/zh/, docs/en/)
  link_checker.py          # 异步检查 URL
  __main__.py              # CLI 入口（python -m awesome_bioinfo）

templates/
  algorithm_template.yaml  # 新条目模板
  readme_template.md       # README 模板

schemas/
  algorithm-schema.json    # JSON Schema（validate 命令使用）

openspec/specs/            # 规范文档（可选参考）

docs/                      # VitePress 文档站点（Git Pages）
  .vitepress/config.ts     # VitePress 配置
  zh/                      # 中文文档
  en/                      # 英文文档
```

## 生成输出（禁止手动编辑）

| 文件/目录 | 生成命令 |
|---|---|
| `README.md` | `python -m awesome_bioinfo generate` |
| `docs/zh/`, `docs/en/` | `python -m awesome_bioinfo vitepress` |

数据或模板变更后须重新生成并验证无漂移：

```bash
python -m awesome_bioinfo generate
python -m awesome_bioinfo vitepress
cd docs && npm run build
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

- 不要修改 `README.md` 或 `docs/`（生成文件）
- `data/categories.yaml` 变更后，所有引用该分类的算法文件都需同步更新

## 代码风格

- **行宽**：100 字符
- **Lint**：ruff (E, F, W, I, N, UP, B, C4 规则)
- **类型检查**：mypy（渐进式严格模式）
- **格式化**：遵循 ruff 规则

## 测试覆盖

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

---

*最后更新：2026-05-24*
