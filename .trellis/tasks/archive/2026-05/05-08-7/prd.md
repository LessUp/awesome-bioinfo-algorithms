# PRD: 架构深化 — 7 项重构改进

## 背景

基于架构审查，识别出 7 个深化机会，旨在提升代码的 **Locality**（变更集中）和 **Leverage**（接口杠杆），同时改善测试性和 AI 可导航性。

## 目标

1. 消除浅模块（接口复杂度接近实现复杂度）
2. 集中分散的逻辑（Locality）
3. 显式化隐式依赖
4. 删除死代码

## 改进清单

### 1. Validator 分类依赖泄漏

**现状**：`Validator` 类同时承担字段格式验证和分类关系验证，导致验证顺序隐式耦合。

**目标**：
- `Validator` 只负责字段格式验证（纯函数）
- 分类验证归入 `CategoryManager`
- 验证逻辑可独立测试

**涉及文件**：
- `awesome_bioinfo/validate.py`
- `awesome_bioinfo/algorithm_registry.py`
- `awesome_bioinfo/category_manager.py`

---

### 2. CLI Wrapper 浅模块

**现状**：`search.py`, `info_cmd.py`, `compare.py`, `export_cmd.py` 只包含一个函数，接口复杂度接近实现复杂度。

**目标**：
- 合并浅模块到 `__main__.py`，或
- 深化命令类（让命令类承担布局检查和加载职责）

**涉及文件**：
- `awesome_bioinfo/__main__.py`
- `awesome_bioinfo/search.py`
- `awesome_bioinfo/info_cmd.py`
- `awesome_bioinfo/compare.py`
- `awesome_bioinfo/export_cmd.py`

---

### 3. 数据加载多路径问题

**现状**：理解"如何加载算法数据"需要在 4 个地方跳转，`generate_mkdocs.py` 绕过 `AlgorithmRegistry` 直接操作 YAML。

**目标**：
- 引入 `DataStore` 门面类作为单一数据加载入口
- 统一 `generate_mkdocs.py` 使用 `DataStore`
- 删除 `data_io.py` 中的死代码

**涉及文件**：
- `awesome_bioinfo/data_store.py`（新建）
- `awesome_bioinfo/algorithm_registry.py`
- `awesome_bioinfo/data_io.py`
- `awesome_bioinfo/generate_mkdocs.py`
- `awesome_bioinfo/__main__.py`

---

### 4. generate_mkdocs.py 的单体函数问题

**现状**：函数接收原始 `dict` 而非领域对象，绕过类型安全；未复用 `ReadmeGenerator` 逻辑。

**目标**：
- 使用 `AlgorithmEntry` 和 `Category` 领域对象
- 提取 HTML 模板到独立模块
- 复用 `ReadmeGenerator` 的辅助方法

**涉及文件**：
- `awesome_bioinfo/generate_mkdocs.py`
- `awesome_bioinfo/templates/mkdocs/`（新建，存放 HTML 模板）

---

### 5. Registry/Manager 初始化的隐式顺序依赖

**现状**：`AlgorithmRegistry` 和 `CategoryManager` 独立初始化，但验证时存在隐式依赖。

**目标**：
- 显式建模依赖关系
- 引入门面类 `AwesomeBioinfo` 管理所有组件

**涉及文件**：
- `awesome_bioinfo/core.py`（新建，包含 `AwesomeBioinfo` 门面类）
- `awesome_bioinfo/__main__.py`

---

### 6. 纯函数提取的可疑模式

**现状**：`compare.py` 的 `_resolve()` 等函数被提取仅为测试性，但收益有限。

**目标**：
- 评估是否内联，或
- 提取领域类型（如 `AlgorithmLookup`）而非纯函数

**涉及文件**：
- `awesome_bioinfo/compare.py`
- `awesome_bioinfo/search.py`

---

### 7. data_io.py 的缓存死代码

**现状**：`_cached_yaml_load()` 和 `_cached_load_algorithm_file()` 从未被调用。

**目标**：删除死代码。

**涉及文件**：
- `awesome_bioinfo/data_io.py`

---

## 验收标准

1. 所有测试通过：`pytest tests/ -v`
2. Lint 通过：`ruff check awesome_bioinfo tests`
3. 类型检查通过：`mypy awesome_bioinfo --ignore-missing-imports`
4. 无功能回退：验证、搜索、生成等核心功能行为不变
5. 测试覆盖率保持 ≥ 85%

## 风险评估

- **风险**：重构可能引入回归 bug
- **缓解**：每项改进后运行完整测试套件，确保增量验证

## 时间估算

- 每项改进：30-60 分钟
- 总计：4-6 小时
