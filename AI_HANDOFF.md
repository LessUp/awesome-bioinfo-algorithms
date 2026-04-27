# AI Handoff Document

> 本文档为 GLM 模型或其他 AI 助手提供项目交接信息。
> 最后更新：2026-04-27

## 项目状态概要

**项目名称**: Awesome Bioinformatics Algorithms  
**版本**: 1.0.2  
**状态**: 生产就绪，已完成全面重构

### 核心指标

| 指标 | 数值 |
|------|------|
| 算法条目 | 195+ |
| 分类数量 | 16 个顶级分类 + 32 个子分类 |
| 标签数量 | 392 个 |
| 测试覆盖率 | 89% |
| Python 版本 | 3.9-3.12 |

---

## 2026-04-27 重构变更摘要

### 已完成的修复

1. **URL 修复** - 将所有 `github.com/shane` 改为正确的 `github.com/LessUp`
2. **版本同步** - mkdocs.yml 版本号与 pyproject.toml 统一为 1.0.2
3. **冗余清理** - 删除 `scripts/` 目录和 `generate_readme.py`
4. **技能整合** - 删除 `.github/skills/` 中的重复 OpenSpec 技能
5. **类型注解** - 为 8 个函数添加返回类型注解
6. **代码优化** - 使用 `DIFFICULTY_LABELS_BILINGUAL` 替换重复的难度映射
7. **配置完善** - 添加 `pyrightconfig.json`

### 修改的文件

```
mkdocs/mkdocs.yml              # URL 和版本修复
mkdocs/overrides/main.html     # URL 修复
awesome_bioinfo/generate_mkdocs.py  # URL 和代码优化
awesome_bioinfo/link_checker.py     # URL 修复
awesome_bioinfo/algorithm_registry.py  # 类型注解
awesome_bioinfo/readme_generator.py    # 类型注解
awesome_bioinfo/validate.py            # 类型注解
awesome_bioinfo/category_manager.py    # 类型注解
awesome_bioinfo/data_io.py             # 类型注释
```

### 删除的文件

```
scripts/                       # 整个目录
awesome_bioinfo/generate_readme.py
tests/test_generate_readme.py
.github/skills/openspec-*
```

---

## 项目架构

```
awesome-bioinfo-algorithms/
├── awesome_bioinfo/       # 核心 Python 包
│   ├── schema.py          # 数据模型
│   ├── algorithm_registry.py  # 算法注册表
│   ├── category_manager.py    # 分类管理
│   ├── validate.py        # 数据验证
│   ├── data_io.py         # 导入导出
│   ├── readme_generator.py    # README 生成
│   ├── generate_mkdocs.py    # MkDocs 生成
│   └── __main__.py        # CLI 入口
├── data/
│   ├── categories.yaml    # 16 个分类定义
│   └── algorithms/*.yaml  # 算法数据文件
├── tests/                 # 测试套件 (89% 覆盖率)
├── mkdocs/                # 文档站点
├── openspec/              # OpenSpec 规范
└── .claude/skills/        # Claude 技能
```

---

## 关键命令

### 开发验证

```bash
# 快速验证
ruff check awesome_bioinfo tests
mypy awesome_bioinfo

# 运行测试
pytest tests/ -v

# 带覆盖率
pytest tests/ --cov=awesome_bioinfo --cov-report=term-missing
```

### CLI 操作

```bash
# 数据验证
python -m awesome_bioinfo validate

# 生成 README
python -m awesome_bioinfo generate

# 生成 MkDocs
python -m awesome_bioinfo mkdocs

# 搜索算法
python -m awesome_bioinfo search "alignment"
```

---

## 待办事项 (可选)

以下任务为可选改进，不影响项目核心功能：

1. **测试覆盖** - 为 `generate_mkdocs.py` 和 `link_checker.py` 添加单元测试
2. **GitHub 仓库** - 使用 `gh` CLI 更新仓库描述和 topics
3. **清理 .worktrees** - 删除 `.worktrees/final-state/` 如果不再需要

---

## 技术约束

### 代码规范

- **行宽**: 100 字符
- **Lint**: ruff (E, F, W, I, N, UP, B, C4)
- **类型检查**: mypy (渐进式严格模式)
- **测试覆盖**: 最低 85%

### 数据约束

- **算法 ID**: 小写字母 + 连字符 (如 `smith-waterman`)
- **描述长度**: 50-500 字符
- **编码**: UTF-8
- **格式**: YAML

---

## 联系方式

- **仓库**: https://github.com/LessUp/awesome-bioinfo-algorithms
- **文档**: https://lessup.github.io/awesome-bioinfo-algorithms/

---

*此文档由 Claude (Opus 4) 于 2026-04-27 创建*
