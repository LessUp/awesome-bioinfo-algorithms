# 2026-01-08 项目检查与修复记录

## 变更概述

- 修复 README 生成器目录（TOC）锚点链接问题，确保 TOC 链接可正确跳转到对应标题。
- 将文档与模板中的 GitHub 仓库占位符替换为实际仓库 `LessUp/awesome-bioinfo-algorithms`。
- 修复/完善 `pyproject.toml` 元数据与覆盖率配置。

## 变更明细

- `scripts/readme_generator.py`
  - 修复 TOC 链接中多余空格导致的无效锚点。
  - TOC 锚点改为基于完整标题（`中文名 (English Name)`）生成，以匹配实际标题生成的锚点。

- `pyproject.toml`
  - 更新 `project.urls` 为实际仓库地址。
  - 更新 `authors` 占位信息。
  - 修正 `tool.coverage.report.exclude_lines` 中 `__main__` 匹配规则。

- `README.md`
  - 更新 GitHub Actions 徽章链接为实际仓库地址。
  - 修复目录（TOC）各分类锚点链接，匹配 GitHub 生成的标题锚点。

- `templates/readme_template.md`
  - 更新 GitHub Actions 徽章链接为实际仓库地址。

- `docs/DEVELOPMENT.md`
  - 更新克隆仓库命令为实际仓库地址与目录名。

- `docs/FAQ.md`
  - 更新克隆仓库命令为实际仓库地址与目录名。

- `.kiro/specs/project-enhancement/design.md`
  - 更新 `project.urls` 示例为实际仓库地址。

- `.kiro/specs/project-enhancement/tasks.md`
  - 将任务描述中残留的 `YOUR_USERNAME` 字样改为更准确的表述。
