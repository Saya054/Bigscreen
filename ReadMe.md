# 伙伴业务支持部大屏看板

本项目是一套基于 Flask 的数据可视化大屏，看板从 MySQL 中读取业务支撑相关指标，通过 HTML/CSS/JavaScript 与 ECharts 展示热线、支持网、社区、IM 及绩效等核心数据。项目内置数据采集脚本，可定时从第三方接口拉取最新指标并落库，支持搭建在本地或局域网环境中进行展示。

## 技术栈
- **后端**：Flask、Flask-CORS，提供页面渲染与 JSON API。
- **数据层**：MySQL（表结构见 `sql/table.sql`，示例数据见 `sql/data.sql`），通过 PyMySQL 访问。
- **数据采集**：脚本基于 `requests`、`schedule` 与自研封装，从外部接口拉取并写入库表。
- **前端大屏**：Jinja2 模板 + 原生 HTML/CSS/JS，图表使用 ECharts。
- **辅助库**：pyecharts（生成图表数据）、openpyxl（部分测试脚本）、streamlit（原型页，非必需）。

## 目录速览
- `app.py`：Flask 入口，定义页面及数据接口。
- `templates/index.html`：大屏主页面模板。
- `static/`：静态资源（CSS、JS、图片、ECharts 脚本等）。
- `Config/`：`config.ini` 读写以及 JSON 配置解析。
- `Data/Datadriver/`：MySQL 访问封装。
- `Data/Dataquery/`：对外提供的查询函数，供 API 调用。
- `Data/Datadown/`：数据同步脚本（调用外部接口并写库）。
- `DCharts/` 与 `Performance/`：对接各类业务接口、处理原始指标。
- `sql/`：数据库表结构与初始化数据。
- `pages/`：Streamlit 实验页面（看板运行不依赖，可忽略）。
- `log.txt`：运行日志（体积较大，可按需清理）。

## 环境要求
- Python ≥ 3.8
- MySQL 5.7 或 8.0，具备读写权限
- 操作系统：推荐 Windows（项目内默认配置为 `D:\bigdata`），Linux 亦可但需调整路径

### Python 依赖
```
Flask
Flask-Cors
pymysql
requests
schedule
pyecharts
openpyxl        # 仅调试脚本需要
streamlit       # 仅 pages 原型页需要
```
建议使用虚拟环境，手动 `pip install`，或自行整理 `requirements.txt`。

## 安装与初始化
1. **克隆项目**：`git clone` 或直接拷贝到目标机器。
2. **创建虚拟环境**（可选）：`python -m venv venv && venv\Scripts\activate`。
3. **安装依赖**：按照上文列表执行 `pip install <package>`。
4. **准备数据库**：
   - 新建数据库 `jxbigdata`（或在 `config.ini` 中修改名称）。
   - 执行 `sql/table.sql` 创建表结构。
   - 如需演示数据，可导入 `sql/data.sql`。
5. **配置 `config.ini`**：
   - `SQL-config`：配置 MySQL 连接信息。
   - `Web-config`：指向存放外部接口配置的 JSON 文件（URL、Headers、人员映射等）。
   - 目前代码默认读取 `D:\bigdata\config.ini` 及对应 JSON；如路径不同，请同步修改 `app.py`、`dataupdates.py` 等文件内的 `cfpath`。
6. **准备接口 JSON**：根据各自业务系统填写 `json/` 目录下的示例文件（如 `hotline_backend/hotlineUrl.json`、`issue_support/backend/backendUrl.json` 等），包含接口地址、认证信息、人员编号映射等敏感数据。

## 运行大屏
```bash
python app.py
```
启动后，默认在 `http://localhost:5000/` 提供页面与数据接口。部署到服务器时，可将 `host` 设置为实际 IP，并考虑使用 Nginx/Uwsgi 等方式上线。

### 可用接口
以下 REST 接口返回 JSON 数据，前端通过轮询刷新：

| 路径 | 说明 | 数据来源 |
| --- | --- | --- |
| `/` | 渲染大屏页面 | 模板 `templates/index.html` |
| `/issuerank` | 支持网当日答题排行 Top5 | 表 `jx_issue` |
| `/webimrank` | IM 当日有效对话排行 Top5 | 表 `jx_webim` |
| `/communityrank` | 社区回帖排行 Top5 | 表 `jx_community` |
| `/hotline` | 热线当日接听详情（条形图） | 表 `jx_hotline` |
| `/hotlineweek` | 热线本周呼入情况（折柱混搭图） | 表 `jx_hotlineweek` |
| `/webimweek` | IM 本周会话情况 | 表 `jx_webimweek` |
| `/kpi` | 绩效完成度列表 | 表 `jx_statistics` |
| `/topkpi` | 绩效最佳人员 | 表 `jx_statistics` |
| `/tophotline` | 热线接听第一名 | 表 `jx_hotline` |
| `/topissue` | 支持网答题第一名 | 表 `jx_issue` |
| `/topwebim` | IM 有效会话第一名 | 表 `jx_webim` |
| `/topcommunity` | 社区回复第一名 | 表 `jx_community` |
| `/topstudy` | 学习成长积分第一名 | 表 `jx_otherstat` |

接口返回的数据结构基本为列表（数组）或单条记录，前端脚本 `static/js/js.js` 负责解析并渲染成图表或表格。

## 数据同步脚本
`dataupdates.py` 用于定时刷新数据库内的各类指标：
- 加载 `config.ini` 与 `json/` 参数，调用封装在 `DCharts/DataApi.py`、`Performance/*` 中的接口。
- 逐一更新 `jx_hotline`、`jx_issue`、`jx_community`、`jx_webim`、`jx_statistics`、`jx_otherstat`、`jx_hotlineweek`、`jx_webimweek` 等表。
- 默认 `while True` 循环，每 180 秒自动拉一次数据；如需改为计划任务，可自行调整逻辑或使用外部调度。
- 运行方式：
  ```bash
  python dataupdates.py
  ```
  如需写入日志，可结合系统计划任务或新增日志配置（脚本中包含 `logging` 初始化示例）。

> **注意**：拉取外部接口需要正确的 URL、Headers、Cookie、人员映射等敏感信息，请在部署环境自行维护，切勿将真实凭证提交到版本库。

## 配置文件说明
- `config.ini`
  - `[SQL-config]`：数据库连接信息。
  - `[Web-config]`：各业务接口所需的 JSON 路径。
  - `[Base-config]`、`[Other-config]`：系统级别的基础配置，可按实际场景补充。
- `json/` 目录：按业务类型区分，包含接口地址、请求头、请求体、人员映射等。例如：
  - `hotline_backend/hotlineUrl.json`：热线接口地址。
  - `hotline_backend/hotlineHeader.json`：请求头。
  - `hotline_backend/hotlinePerson.json`：人员姓名到 ID 的映射。
  - 其他子目录形式相同，可根据外部系统实际返回结构调整。

## 开发与调试建议
- **虚拟数据**：如无真实接口，可在数据库中直接写入测试数据，前端即可加载展示。
- **接口调试**：若修改 SQL 或接口逻辑，建议先在 `Data/Dataquery/WebQuery.py` 中以 `__main__` 方式测试。
- **路径统一**：建议统一使用绝对路径或在配置文件里维护根目录，避免硬编码 `D:\bigdata` 带来的跨平台问题。
- **日志**：`log.txt` 体积较大，可定期归档或清理；如在生产使用，请结合日志轮转策略。
- **Streamlit 页面**：`pages/page_2.py` 为实验组件，若需要额外看板或测试界面，可在 Streamlit 环境下运行 `streamlit run pages/page_2.py`。

## 常见问题
- **前端中文显示异常**：确保浏览器编码为 UTF-8，静态资源路径无误。
- **接口返回空数组**：检查数据库是否有数据、SQL 是否执行成功，以及 `config.ini` 是否指向正确的数据库。
- **外部接口请求失败**：核对 `json/` 配置中的 URL、Headers、Cookies 是否过期；必要时添加异常日志便于排查。
- **定时任务重复写入**：当前更新逻辑为 `UPDATE`，不会新增数据；如需保留历史记录，请自行扩展对应表结构与写入方式。

至此，大屏看板的核心说明已完整覆盖，可根据自身业务继续扩展指标、优化展示效果或集成更多数据源。祝使用顺利！
