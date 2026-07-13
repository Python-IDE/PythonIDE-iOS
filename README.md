<p align="center">
  <img src="docs/assets/brand-mark.svg" width="112" alt="PythonIDE logo" />
</p>

<h1 align="center">PythonIDE for iOS</h1>

<p align="center">
  <strong>iPhone / iPad 上的 Python 工作台</strong><br/>
  本地运行 Python 3.13，用 AI Agent 处理项目任务，编辑 Notebook，并把脚本接入小组件、MiniApp、桌面开发、SSH、Git 和社区脚本库。
</p>

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304">
    <img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on App Store" height="40" />
  </a>
  &nbsp;
  <a href="https://pythonide.xin/docs/">
    <img src="https://img.shields.io/badge/Docs-pythonide.xin-3776AB?style=for-the-badge" alt="PythonIDE docs" height="40" />
  </a>
  &nbsp;
  <a href="https://github.com/Python-IDE/PythonIDE-iOS">
    <img src="https://img.shields.io/github/stars/Python-IDE/PythonIDE-iOS?style=for-the-badge&logo=github" alt="GitHub stars" height="40" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/iOS-16.2+-blue?style=flat-square" alt="iOS 16.2+" />
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python" alt="Python 3.13" />
  <img src="https://img.shields.io/badge/Swift-5.9-FA7343?style=flat-square&logo=swift" alt="Swift" />
  <img src="https://img.shields.io/badge/AI-Agent-6D5DFB?style=flat-square" alt="AI Agent" />
  <img src="https://img.shields.io/badge/Widget-MiniApp-F2C94C?style=flat-square" alt="Widget and MiniApp" />
  <img src="https://img.shields.io/badge/Notebook-ipynb-F37626?style=flat-square" alt="Notebook" />
  <img src="https://img.shields.io/badge/Desktop-npx-2EA44F?style=flat-square" alt="Desktop npx" />
  <img src="https://img.shields.io/badge/SSH-Git-22C55E?style=flat-square" alt="SSH and Git" />
</p>

---

## 项目定位

PythonIDE 不是只把桌面 IDE 缩小到手机屏幕里。它更像是一套 iOS 上的 Python 工作流：你可以在 iPhone / iPad 上管理文件、编辑代码、运行脚本、编辑 Notebook、安装库、让 AI Agent 处理项目任务，也可以继续把脚本做成小组件、MiniApp、快捷指令自动化、服务器脚本或社区作品，并通过桌面开发桥接到电脑编辑器。

核心目标是让 Python 脚本不只停在编辑器和控制台里：

```text
写脚本
  -> 本地运行和调试
  -> 让 AI Agent 修改、验证和修复
  -> 接入 Notebook / Widget / MiniApp / Desktop / Shortcuts / SSH / Git / 社区脚本库
```

---

## 核心能力

| 能力 | 说明 |
|---|---|
| **AI Agent** | AI 聊天、行内编辑、Agent 执行项目任务、跨文件读写、运行 Python、工具调用、BYOK 与平台额度 |
| **Notebook** | 打开和编辑 `.ipynb` 文件，支持 Markdown / Code 单元格、运行状态、输出展示、空 Notebook 初始化和 Notebook JSON 兼容处理 |
| **小组件 / Widget** | Python 脚本小组件、Widget Studio、预览、桌面/锁屏组件、Control Center 控件、Live Activity / 灵动岛 |
| **MiniApp** | MiniApp 启动器、创建、编辑、打包、导入导出、AppUI / HTML / WebBridge 运行、隐藏库、日志中心 |
| **桌面开发 / npx CLI** | 通过 `npx pythonide-cli start` 连接电脑工作区，在 VS Code / Cursor / Zed 等桌面编辑器中修改 MiniApp，并同步回 iPhone / iPad 的真实 PythonIDE 运行环境 |
| **SSH / 服务器** | SSH 连接、终端、SFTP 文件管理、服务器监控、部署、密钥管理、命令片段 |
| **Git / WebDAV** | 仓库状态、diff、暂存、提交、同步、历史、分支、远端、stash、tags、冲突处理；WebDAV 远程文件 |
| **社区 / 脚本库** | 脚本浏览、分类、详情、导入、运行、投稿、审核、点赞、用户资料 |
| **本地 Python 环境** | Python 3.13、本地运行、JavaScriptCore、HTML 预览、Rich/ANSI 输出、图片/图表/HTML 内联输出 |

---

## 典型工作流

### 让 Agent 处理项目任务

当任务不只是改一行代码时，Agent 可以读取项目、修改文件、运行 Python、查看输出，并根据错误继续修复。

| 场景 | Agent 可以做什么 |
|---|---|
| 修复脚本报错 | 读取 traceback，定位文件，修改代码，重新运行 |
| 跨文件任务 | 读取多个文件后统一修改、创建或整理项目结构 |
| MiniApp / Widget 接入 | 生成结构、连接脚本逻辑、辅助调试 |
| 远程任务 | 配合 SSH / SFTP / Git 工作流处理服务器或项目问题 |
| 模型使用 | 支持平台额度，也支持自带 API Key |

### 把脚本变成 iOS 入口

很多脚本不是为了运行一次，而是为了长期使用。PythonIDE 提供多个移动端出口：

| 出口 | 适合场景 |
|---|---|
| **控制台** | 临时运行、调试、查看 Rich / ANSI / 图片 / 图表 / HTML 输出 |
| **Widget** | 每日数据、状态卡片、进度、统计、主屏/锁屏信息 |
| **Control Center** | 快速触发脚本或控制动作 |
| **Live Activity / 灵动岛** | 长任务状态、运行进度、可见反馈 |
| **快捷指令 / App Intents** | Siri、自动化、运行脚本、运行剪贴板代码、查询输出 |
| **Share Extension** | 从其他 App 分享内容进入 PythonIDE 处理 |
| **MiniApp** | 带界面的小工具、表单、列表、日志、状态反馈 |

### 在桌面继续开发 MiniApp

PythonIDE 支持通过 `pythonide-cli` 把 iPhone / iPad 上的 MiniApp 项目连接到电脑工作区：

```bash
npx pythonide-cli start
```

电脑端负责打开编辑器、同步项目和监听文件保存；iPhone / iPad 端负责运行真实 PythonIDE runtime。这样可以在 VS Code / Cursor / Zed 等桌面编辑器中写 MiniApp，同时保留 AppUI、Widget、iOS 原生模块等运行能力。

### 接入真实项目和服务器

PythonIDE 也可以处理更接近开发者工作流的任务：

| 工作流 | 能力 |
|---|---|
| **Git** | 状态、diff、暂存、提交、同步、历史、分支、远端、stash、tags、冲突处理 |
| **SSH** | 连接服务器、交互式终端、命令片段、部署、服务器监控 |
| **SFTP** | 远程目录、上传下载、远程编辑、批量操作 |
| **WebDAV** | 远程目录、上传下载、远程编辑、收藏、缓存、证书固定 |
| **SQLite** | 本地数据库浏览和检查 |

---

## 功能总览

| 模块 | 能力 |
|---|---|
| **首页 / 文件管理** | 本地文件、文件夹、导入、外部文件夹、搜索、排序、置顶、颜色标记、批量操作、回收站、文件预览 |
| **代码编辑器** | Python / JS / HTML / CSS / JSON / Markdown，语法高亮、快捷输入栏、查找替换、Jedi 补全、Python lint、AI 行内编辑 |
| **Notebook** | `.ipynb` 文件解析、空 Notebook 初始化、Markdown / Code 单元格、输出展示、运行状态、raw JSON 查看、兼容性测试样例 |
| **运行与控制台** | Python 3.13 本地运行、JavaScriptCore 运行、HTML 预览、交互式 input、Rich/ANSI 输出、图片/图表/HTML 内联输出、错误跳转和修复入口 |
| **AI Agent** | AI 聊天、Agent 执行项目任务、跨文件读写、运行 Python、Git / SSH / MiniApp / 网页 / 原生能力工具调用、BYOK 和平台额度 |
| **社区 / 脚本库** | 脚本浏览、分类、详情、导入、运行、投稿、审核、点赞、用户资料 |
| **MiniApp** | 启动器、创建、编辑、打包、导入导出、AppUI / HTML / WebBridge 运行、隐藏库、日志中心 |
| **桌面开发** | `npx pythonide-cli start`、二维码/Bonjour 连接、可信服务器、项目同步、桌面文件监听、MiniApp/AppUI 预览、stdout/stderr/traceback 回传、VS Code companion |
| **小组件 / Widget** | Python 脚本小组件、Widget Studio、预览、桌面/锁屏组件、Control Center 控件、Live Activity / 灵动岛 |
| **SSH / 服务器** | SSH 连接、终端、SFTP 文件管理、服务器监控、部署、密钥管理、命令片段 |
| **Git** | 仓库状态、diff、暂存、提交、同步、历史、分支、远端、stash、tags、冲突处理 |
| **WebDAV** | WebDAV 服务器、远程目录、上传下载、远程编辑、批量操作、收藏、缓存、证书固定 |
| **工具箱** | 编解码、JSON、API 调试、二维码、图片 URL、HTML 转图片、时间戳、进制转换、正则、直链下载 |
| **Python 库管理** | 内置 Python 包、C 扩展包、Wheel 安装、PyPI 搜索安装、包推荐 |
| **iOS 原生模块** | `photos`、`contacts`、`location`、`motion`、`speech`、`notification`、`vision`、`device`、`network`、`haptics`、`calendar`、`bluetooth`、`health`、`sound`、`websocket` 等 |
| **快捷指令 / 自动化** | App Intents、运行脚本、运行剪贴板代码、保存文本为脚本、查询运行状态/输出、停止运行、x-callback-url |
| **设置 / 个性化 / 安全 / 付费** | AI 设置、外观、编辑器、控制台、小组件、隐私安全、App 锁、Keychain、换图标、BYOK / Premium / 捐赠权益、帮助反馈、开发者文档 |
| **支撑板块** | Share Extension 分享导入、SQLite 浏览器、开发者文档中心、AgentSkillsV2 技能系统 |

---

## 文档入口

优先阅读在线文档站点，跳转路径比 GitHub 源文件更适合用户阅读：

| 主题 | 在线文档 |
|---|---|
| **文档首页** | [pythonide.xin/docs](https://pythonide.xin/docs/) |
| **AppUI / MiniApp** | [AppUI 文档集合](https://pythonide.xin/docs/collections/appui/) |
| **Widget 小组件** | [Widget 文档集合](https://pythonide.xin/docs/collections/widget/) |
| **iOS 原生模块** | [iOS 原生模块集合](https://pythonide.xin/docs/collections/ios-native/) |
| **快捷指令 / 自动化 / 扩展** | [自动化与扩展集合](https://pythonide.xin/docs/collections/automation-extension/) |
| **ui 模块** | [ui 文档集合](https://pythonide.xin/docs/collections/ui/) |
| **scene / turtle** | [scene 文档集合](https://pythonide.xin/docs/collections/scene/) |
| **Widget API 参考** | [widget API reference](https://pythonide.xin/docs/pages/widget-api-reference/) |
| **AppUI 示例** | [AppUI cookbook](https://pythonide.xin/docs/pages/appui-cookbook-index/) |
| **JS API** | [JavaScript API](https://pythonide.xin/docs/pages/js-api/) |
| **C 扩展模块** | [C extensions](https://pythonide.xin/docs/pages/c-extensions-module/) |

仓库内源码文档入口：

| 类型 | 仓库路径 |
|---|---|
| Python 模块源文档 | [pythonide/Docs](pythonide/Docs/) |
| 桌面开发 CLI | [pythonide-cli/README.md](pythonide-cli/README.md) |
| VS Code Companion | [pythonide-cli/vscode-extension/README.md](pythonide-cli/vscode-extension/README.md) |
| AgentSkillsV2 技能系统 | [AgentSkillsV2](AgentSkillsV2/) |
| 社区 API | [community-function/API.md](community-function/API.md) |

---

## 安装

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304">
    <img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on App Store" height="44" />
  </a>
</p>

| 要求 | 说明 |
|---|---|
| **系统** | iOS 16.2 或更高版本 |
| **设备** | iPhone / iPad |
| **分发** | App Store |
| **AI 使用** | 支持平台额度和 BYOK |

---

## 截图

当前界面截图和功能预览以 App Store 页面为准：

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304">
    <img src="https://img.shields.io/badge/App%20Store-查看截图-black?style=for-the-badge&logo=apple" alt="View screenshots on App Store" height="44" />
  </a>
</p>

---

## 社区与反馈

| 渠道 | 链接 |
|---|---|
| Telegram | [iOS 端 Py 编程 IDE](https://t.me/pythonzwb) |
| 功能建议 | [GitHub Discussions](https://github.com/Python-IDE/PythonIDE-iOS/discussions) |
| 问题反馈 | [GitHub Issues](https://github.com/Python-IDE/PythonIDE-iOS/issues) |
| App Store | [PythonIDE on App Store](https://apps.apple.com/app/id6753987304) |

---

## 支持开发

如果 PythonIDE 对你有帮助，可以通过这些方式支持后续开发：

- 给这个仓库点 Star，让更多开发者看到项目。
- 在 App Store 留下评价。
- 通过应用内反馈发送问题和建议。
- 通过应用内 Premium / 捐赠权益支持开发。

---

<p align="center">
  <strong>PythonIDE</strong><br/>
  iPhone / iPad 上的 Python 工作台。
</p>
