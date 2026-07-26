# 导航、页面与功能映射

## 根入口

`pythonideApp` 的 `@main` 入口位于 `pythonide/AppShell/pythonideApp.swift:119`；`WindowGroup` 创建 `RootTabView`，见 `pythonide/AppShell/pythonideApp.swift:253-306`。根部同时处理 App Lock、启动封面、URL、Quick Action、Share Extension Inbox、App Intent 输出和 Widget 命令。

## 根 Tab 地图

| TabID | 用户文案 | 默认状态 | 根页面 | 主要功能 |
|---|---|---|---|---|
| `home` | 首页 | 固定可见 | `HomeView` | F01–F03、F05、F09 |
| `agent` | Agent | 默认可见，可隐藏/重排 | `SearchTabAIChatLayer` | F04 |
| `terminal` | 终端 | 默认可见，可隐藏/重排 | `TerminalTabView` | F03、F08、F09、F11 工具 |
| `settings` | 设置 | 固定可见 | `SettingsView` | F04–F12 配置入口 |
| `community` | 社区 | 默认可见，可隐藏/重排 | `ScriptLibraryNextPreviewView` | F10 |
| `widget` | 小组件 | 默认隐藏，可启用/重排 | `WidgetSettingsView`/Studio | F06 |

证据：`pythonide/AppShell/RootTabView.swift:218-260,1327-1515`；`pythonide/Settings/SettingsGeneralViews.swift:336-410`。可选 Tab 隐藏后，设置搜索提供 Agent、社区与终端兜底入口，见 `SettingsHomeModels.swift:55-59`。

## 首页导航树

```text
首页
├─ 工作区：此 iPhone / iCloud / 外部文件夹
├─ 文件与文件夹列表
│  ├─ 源码编辑器（py/js/html/css/json/md/txt/csv…）
│  ├─ Notebook 编辑器（ipynb）
│  ├─ Markdown / CSV / SVG / HTML 预览
│  ├─ 图片 / 音频 / 视频 / PDF / Office Quick Look
│  ├─ Archive 浏览与解压
│  └─ SQLite 浏览
├─ MiniApp 集合与 Launcher
├─ Git 仓库页
├─ 回收站
├─ 本地终端 / 包管理
└─ 新建菜单：文件、Notebook、文件夹、MiniApp、导入、扫码、外部文件夹、WebDAV
```

关键条件入口：长按运行按钮显示“清空后运行/追加运行”；行上下文菜单提供重命名、复制、移动、压缩、打包 MiniApp、加密分享等；Swipe 负责置顶/取消置顶与删除。不能仅靠主工具栏发现这些能力。

## 编辑器跨页结构

`ContentView` 不是单一功能页：同一容器根据文件类型组合代码编辑、输出、Notebook、Web Preview、Git、AI Review、Debugger、Profiler、Widget Preview、参数与设置 Sheet。多文件 Tab、查找替换、断点、错误回溯跳转和键盘快捷键跨多个子视图协作。

## Agent 导航树

```text
Agent
├─ 新对话 / 历史 / 搜索 / 重命名 / 删除
├─ 工作区选择（此 iPhone、iCloud、外部文件夹）
├─ 输入：文本、相机、照片、文件、语音、Skill、MCP
├─ 模型与推理强度 / 批准模式
├─ 执行时间线：计划、工具请求、输出、Diff、验证、Apply
└─ 设置
   ├─ PythonIDE 账号 / 托管额度
   ├─ 自定义服务商、模型与 API Key
   ├─ Skills
   ├─ MCP Servers
   ├─ Shortcuts Connectors
   └─ Memory
```

## 终端与远程导航树

`TerminalTabView.SSHNavDestination` 将同一 Tab 分为本地终端、服务器列表、SSH Terminal、SFTP、监控、部署、密钥和片段。WebDAV 从新建菜单或设置/文件流程进入独立浏览器。SSH 主机指纹通过根级 `SSHHostTrustSheet` 统一确认。

## 社区与网站

- 社区：搜索 → 最新投稿/官方精选/分类 → `ScriptDetailView` → 预览、运行、安装/保存、作者、互动。
- 发布：社区右上角 `发布作品` → 类型/项目选择 → 内容、截图、说明、协议 → 上传/审核状态。
- 个人中心：资料、头像、作品、投稿状态、获赞、退出与注销账号。
- 网站：打开 HTML 文件 → 顶部 `部署`/`更新` → 登录与项目扫描 → 新建或关联已有网站 → 发布 → 打开/分享/下线/恢复/部署记录/回滚/删除。

证据：`ScriptLibraryNextPreviewView.swift:120-228,423-539`；`WebsiteOnlineView.swift:757-928`；`MyWebsitesView.swift:170-380`；`WebsiteManagementSheet.swift:45-161`。

## 设置导航

一级真实 UI 名称：`AI 助手`、`我的网站`、`应用数据`、`外观`、`桌面开发`、`编辑器`、`终端`、`小组件`、`开发工具`、`隐私与安全`、`开发者文档`、`帮助与反馈`、`支持项目`。证据：`pythonide/Settings/SettingsHomeModels.swift:40-65`。

## 系统外部入口

- URL Scheme：`pythonide://`、`minip://`。
- Universal Link：`https://link.pythonide.xin/...`。
- Home Screen Quick Actions：AI 对话、快速运行、运行剪贴板、新建文件。
- App Shortcuts：运行代码/脚本/剪贴板、在 App 中运行、停止、状态、最后输出、新建、保存文本、打开脚本。
- Spotlight：索引可运行脚本/实体（系统版本条件）。
- Files / Document Picker：导入、外部文件夹、文档浏览。
- Share Sheet：批量导入并打开/浏览/预览/解密，MiniApp 安装预览或仅保存。
- Widget/Live Activity/Control Center：打开 App、刷新、运行、继续查看状态。

## 手势与辅助操作索引

| 手势/操作 | 页面 | 功能 |
|---|---|---|
| 行左/右 Swipe | 文件、回收站、社区会话、网站、下载等 | 置顶、删除、恢复、分享、上下线 |
| 长按标题 2 秒 | 社区标题 | 打开管理员页；E 内部功能，不计普通用户功能 |
| Context Menu | 文件、MiniApp、社区作品、网站、服务器 | 预览、复制、移动、分享、管理等 |
| 拖放 | 文件/外部目录、Tab/Widget 预览、列表 | 移动/导入/排序/调整抽屉 |
| 捏合 | 编辑器、终端、图片/图表/网页 | 字号或缩放（取决于页面） |
| 双击 | 输出图片/图表等 | 快速预览/放大 |
| 外接键盘 | 编辑器、Notebook、Agent、终端 | 运行、停止、发送、查找、Notebook Cell 操作 |
| Accessibility Action | 多文件 Tab、列表动作、按钮 | 关闭、运行、移动等替代入口 |

## 无正常用户入口或受限页面

| 项目 | 分类 | 说明 |
|---|---|---|
| `ScriptAdminView` / `WebsiteAdminView` | E 内部功能 | 社区标题长按 2 秒可触发，但仍需管理员服务端验证；不作为普通用户教程 |
| `WebsiteDeployUIPreviewHost` | E 内部功能 | 仅 `#if DEBUG` + `-WebsiteDeployUIPreview`/`-WebsiteManagementUIPreview` |
| UI Test 脚本注入 | E 内部功能 | `PYTHONIDE_UI_TEST_*` 启动环境，仅测试/录制辅助候选 |
| Debug 邀请深链 | E 内部功能 | `SettingsDeepLinkNavigator` 被 `#if DEBUG` 包围 |
| `AgentRunFeatureFlags.backgroundRunnerEnabled` | C 待确认 | 默认关闭；不要宣传为所有用户可用的后台 Agent |

其余 Preview、Fixture、Seed、Mock 只作为证据或 Demo 数据候选，未计为用户页面。
