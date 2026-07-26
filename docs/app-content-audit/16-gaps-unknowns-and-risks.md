# 缺口、未知项、风险与反向覆盖检查

## 关键未确认项

1. 生产服务端状态：社区投稿/审核、网站发布与回滚、托管 AI 额度、邀请奖励无法仅由客户端保证；需测试账号和可控服务端环境。
2. StoreKit 商品与地区价格：代码可确认订阅/终身/恢复流程，实际在售 SKU、价格、试用资格需 App Store Connect/TestFlight 验证。
3. 真机能力：NFC、HealthKit、Bluetooth、相机实时采集、Face ID、真实通知/Live Activity、局域网 Bonjour、MusicKit/WeatherKit 未全部在本轮真机逐项走通。
4. 远端环境：SSH/SFTP/Monitor/Deploy、WebDAV ETag 冲突、Git provider collaboration 需要准备好的服务器与仓库。
5. iCloud 冲突与跨设备同步：静态实现与 Entitlement 已确认，尚需两台设备同时修改测试。
6. 多语言完整性：存在多语资源，但不同 `.lproj` 覆盖度不同；本轮没有逐条人工校对全部翻译。
7. 网站功能受 `WebsiteDeploymentFeatureAvailability.isVisible` 条件控制；需确认 Release 当前开关与服务端上线策略。
8. `AgentRunFeatureFlags.backgroundRunnerEnabled` 默认关闭；Live Activity 默认开启。后台 Agent 不应作为当前普遍可用能力宣传。
9. 自动化测试当前不可运行：测试 Target 在 `PythonHighlightQueryTests.swift:99,132` 编译失败；在修复前，不能用本轮结果证明回归测试通过。
10. Simulator 仅确认启动封面，未完成根 Tab 和核心旅程动态遍历；所有功能可达性结论仍以静态双证据为主。

## 未归类项目表

| 项目 | 发现位置 | 解释/归类 |
|---|---|---|
| 社区/网站管理员页面 | `ScriptAdminView.swift`、`WebsiteAdminView.swift` | E 内部功能；需要隐藏触发与服务端管理员认证 |
| Website UI Preview Host | `pythonideApp.swift:440-448` | E Debug-only；可用于截图回归，不是用户功能 |
| UI Test 脚本注入 | `pythonideApp.swift:1370-1390` | E 测试辅助；可演化为录制模式基础 |
| Debug 邀请深链 | `Notifications.swift:53-81` | E Debug-only，不算 Release 深链 |
| 后台 Agent Runner | `AgentRunFeatureFlags.backgroundRunnerEnabled` | C 待确认/条件关闭；默认关闭，不计普通用户 L3，也不用于宣传 |
| AI 内部 Feature Flags | `AIFeatureFlags.swift` | 实现策略；仅用户可感知且默认开启的结果映射到 F04 |
| Preview/Fixture/Seed | Tests、MiniApps、SampleFilesProvider | 证据/Demo 候选，不计用户功能；首次样例文件属于 F01 L4 |
| 本地性能诊断 | `PerformanceDiagnostics.swift` | 内部质量能力；未发现用于证明产品路径的远端 Analytics 事件 |
| 第三方包源码/测试 | `PythonSitePackages`、Packages、vendor tests | 实现依赖，不逐项归类为 App 功能 |
| 独立 CLI/VS Code 扩展 | `pythonide-cli` | F05 桌面开发配套；不是 iOS App 内独立页面 |

未发现无法解释的用户可见 View；发现 1 个 C 条件关闭项、0 个 D 不可达/疑似废弃项和 4 组 E 内部项，均已明确标记。

## 20 项反向覆盖检查

| # | 检查项 | 结论 |
|---|---|---|
| 1 | 每个 App Target/Extension | 已归类 6/6 |
| 2 | 每个主要导航目的地 | 根 Tab、首页、设置、AI、远程、社区、Widget 已映射 |
| 3 | 每个用户可见 View/ViewController | 按用户任务聚合；未机械逐 View 计数 |
| 4 | Toolbar/Menu/Context/Swipe | 已纳入文件、编辑器、MiniApp、网站、SSH/WebDAV、Git、下载等 L3/L4 |
| 5 | 手势 | Swipe、长按、拖放、捏合、双击、键盘、Accessibility 已索引 |
| 6 | 系统权限 | `Info.plist` 每项已映射 F04/F07/F11 |
| 7 | Entitlement | iCloud、App Group、Sign in with Apple、HealthKit、WeatherKit、NFC、Associated Domain、App Attest 已解释 |
| 8 | Feature Flag | AI 内部 Flags、网站可见性、后台 Agent 已分类 |
| 9 | 订阅/付费限制 | iCloud、自定义 AI、网站、SSH、Widget、外部导入等 Gate 已标 L4；精确 SKU 待商店验证 |
| 10 | 主要本地化 | String Catalog 与主要语言组已映射真实 UI 名称 |
| 11 | UI Test 流程 | AppUI Swipe/Delete/Pin/Drag、性能脚本、启动已纳入证据；不冒充完整旅程覆盖 |
| 12 | Analytics 事件 | 未发现远端产品 Analytics；本地性能 Trace 不作为用户功能证据 |
| 13 | 只有代码无 UI | 管理员、Debug Preview、默认关闭后台 Agent 已列出 |
| 14 | 只有 UI 无业务 | 未发现明确孤立项；网站/社区仍受服务端可用性制约 |
| 15 | 重复/同义功能 | 首页终端与终端 Tab、设置隐藏 Tab 入口、分享/导入多入口合并为同一用户能力 |
| 16 | 废弃/隐藏/实验/开发者专用 | 已列 E/D/C，并从宣传清单排除 |
| 17 | 服务端有客户端无入口 | 管理 API 仅内部页面；不计普通用户功能 |
| 18 | 特定账号/权限/数据状态 | 已作为 L4：游客/登录、免费/Pro、空/有数据、权限允许/拒绝、在线/离线 |
| 19 | iPad/横屏/键盘/Widget/扩展 | 已单列录制环境与扩展能力 |
| 20 | 无法分类的用户可见代码 | 0；未归类表中的全部条件、内部与辅助项目均已解释 |

## 反方审计后的修订

- 将 `ScriptAdminView` 从社区普通功能移除，标 E。
- 将默认关闭的后台 Agent 从 A 降为 C。
- 把文件 Preview、Archive、SQLite 归入“查看/交付资产”，避免按页面重复计数。
- 把 Share Extension、Document Picker、Files App 和首页导入合并为“导入现有资产”的入口变体。
- 把 iOS 16/18/26 Tab 实现视为 L4 平台变体，不重复计功能。
- 第一批删除了纯视觉但上手价值低的 Widget 炫技片，保留 Agent/MiniApp/网站为价值证明，并加入包安装、报错恢复和加密分享。
- 简单设置项改为 T1/T2，不再为每项生产视频。

## 风险处置

- 录制前建立测试账号矩阵：游客、免费登录、Pro、管理员（仅内部验证）。
- 为远程类准备一次性 Host/Repo/WebDAV，录制后轮换密钥并销毁数据。
- 系统权限每条视频从确定状态开始；首次授权弹窗单独录原子片段。
- 所有删除/覆盖镜头使用可重置 Demo 数据；不在真实仓库录 Git discard/reset。
- Release 前另做 Privacy Manifest、App Store metadata 与 SKU 配置核对；这超出本轮只读产品功能审计的动态权限。
