# 2026-01-08 项目检查与修复

**日期**: 2026-01-08  
**类型**: 维护 / Maintenance

---

## 变更摘要

修复 README 生成器目录锚点链接，替换占位符，完善项目元数据。

## 详细变更

### README 生成器修复

| 文件 | 问题 | 修复 |
|------|------|------|
| `scripts/readme_generator.py` | TOC 链接多余空格 | 修复无效锚点 |
| `scripts/readme_generator.py` | TOC 锚点不匹配 | 基于完整标题生成锚点 |

### 占位符替换

| 文件 | 变更 |
|------|------|
| `pyproject.toml` | 更新 `project.urls` 为实际仓库地址 |
| `pyproject.toml` | 更新 `authors` 信息 |
| `README.md` | 更新徽章链接 |
| `templates/readme_template.md` | 更新徽章链接 |
| `docs/DEVELOPMENT.md` | 更新克隆命令 |
| `docs/FAQ.md` | 更新克隆命令 |

### 配置修复

| 文件 | 变更 |
|------|------|
| `pyproject.toml` | 修正 `tool.coverage.report.exclude_lines` 匹配规则 |

## 影响范围

- `scripts/readme_generator.py`
- `pyproject.toml`
- `README.md`
- `templates/readme_template.md`
- `docs/DEVELOPMENT.md`
- `docs/FAQ.md`
