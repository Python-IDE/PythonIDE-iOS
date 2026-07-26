# 仓库、工程与 Target 地图

## 扫描范围与方法

检查了 `git ls-files` 的 64,122 个受版本控制文件，并交叉扫描工程文件、主 App、三个扩展、测试、内置 Python 包、Swift Package、本地化、文档、示例、Fixtures、Feature Flag、Entitlement 与 App Store/发布资料。第三方源码不逐个记为产品功能，但其被主 Target 链接的用户价值已映射。

主要命令：`git ls-files`、`find`、`rg`、`xcodebuild -list`、`xcodebuild -showdestinations`、`xcodebuild build`、`xcodebuild test`、`xcrun simctl`。完整构建结果见本文件末尾与 `16-gaps-unknowns-and-risks.md`。

## Xcode 容器

- Project：`Py编程IDE.xcodeproj`
- Workspace：`Py编程IDE.xcodeproj/project.xcworkspace`
- 共享 Scheme：`pythonide`
- 依赖带出的 Scheme：`MarkdownUI`，不是产品 App Scheme
- Build Configuration：`Debug`、`Release`
- 最低系统：iOS 16.2
- 设备族：iPhone + iPad

证据：`Py编程IDE.xcodeproj/project.pbxproj`；`Py编程IDE.xcodeproj/xcshareddata/xcschemes/pythonide.xcscheme`；动态 `xcodebuild -list`。

## Target 分类

| Target | 类型 | 用户能力 | 归类 | 状态 |
|---|---|---|---|---|
| `Python IDE` | 主 App | 全部 L1 | F01–F12 | 主 Scheme 构建入口 |
| `PythonScriptActivityWidgetExtension` | WidgetKit 扩展 | Home/Lock Screen Widget、Live Activity、Control Center | F06 | 用户功能 |
| `ShareExtension` | Share Extension | 从其他 App 导入文件、文本、URL、图片、MiniApp 包 | F01 | 用户功能 |
| `WidgetIntentExtension` | Intent Extension | iOS 16 旧式 Widget 槽位选择 | F06 | 用户功能，兼容路径 |
| `Py编程IDETests` | Unit Test | 验证模型、存储、运行、AI、Git、SSH、Widget 等 | 证据来源 | 非用户功能 |
| `Py编程IDEUITests` | UI Test | AppUI 手势回归、性能脚本、启动截图 | 证据来源 | 非用户功能 |

主 App 的 Target dependency graph 明确嵌入三个扩展。证据：动态构建输出 `Target dependency graph (107 targets)`。

## 平台与呈现差异

- iPhone：主录制平台；竖屏为默认内容规格。
- iPad：支持 Split/Popover、外接键盘、多栏与大画布；高级编辑、文件拖放、桌面开发需补录。
- iOS 16：旧 Tab/旧 Widget Intent 兼容路径。
- iOS 18：隐藏系统 Tab + 自定义 Tab Chrome；Control Center 控件可用。
- iOS 26：系统 Tab 与部分新 UI/材质路径。
- Apple Silicon Mac：`xcodebuild -showdestinations` 显示 Designed for iPad/iPhone；不是独立 macOS 产品承诺。
- 未发现 watchOS、visionOS、独立 Mac Catalyst Target。

## Swift Package 与本地组件

主要用户价值映射：

- `Runestone` + `TreeSitterLanguages`：多语言编辑、语法高亮、缩进、查找替换。
- `SwiftTerm` + `NSRemoteShell` + `libssh2-spm` + `OpenSSL`：本地/SSH 终端、SFTP 与安全连接。
- `libgit2-spm`：Git 本地操作。
- `PythonIDEKit` + `mcp-swift-sdk`：Agent 核心与 MCP。
- `Nuke`、`MarkdownUI`：网络图片、Markdown 渲染。
- `Lottie`、`SwiftUI-Shimmer`：品牌与加载视觉，不单独计为用户功能。
- `KeyboardToolbar`：编辑器/终端快捷键条。

还解析到远端依赖 `swift-nio`、`swift-log`、`swift-collections`、`swift-async-algorithms`、`swiftui-introspect`、`cmark-gfm` 等。精确版本来自动态 `xcodebuild -list` 输出。

## 系统配置与 Entitlement

| 系统能力 | 证据 | 用户功能映射 |
|---|---|---|
| iCloud Documents / KV | `Config/Xcode/Python IDE*.entitlements` | F01 iCloud 工作区、跨设备文件/设置 |
| App Group `group.app.pythonide` | 主 App 与扩展 Entitlement | F01 Share Inbox；F06 Widget 数据交换 |
| Associated Domains | `applinks:link.pythonide.xin` | F05/F10 深链安装或打开社区内容 |
| Sign in with Apple | Entitlement + `PythonIDEAccountLoginView` | F12 账号 |
| HealthKit / WeatherKit | Entitlement + Bridge | F07 Python 原生模块/Agent 工具 |
| NFC Tag Reading | Entitlement + `NFCBridge` | F07 NFC |
| Live Activities | `Info.plist` + ActivityKit 代码 | F06 脚本/Agent/Git 运行状态 |
| Background fetch/processing/audio | `Info.plist` + `BackgroundTaskManager` | F03/F06 后台运行与刷新 |
| Local Network / Bonjour | `Info.plist` + DesktopDev | F05 桌面开发发现与连接 |
| Document Browser / File Sharing | `Info.plist` | F01 Files App 与外部导入 |

主 App `Info.plist` 还声明相机、相册、麦克风、语音、定位、蓝牙、通讯录、日历、提醒事项、运动、Face ID、通知、Apple Music 等用途。每项均在 F04 或 F07 找到实际代码映射；权限存在不等于用户已经授权。

## 本地化与文档资源

- String Catalog：`Localizable.xcstrings`
- 传统本地化：`zh-Hans`、`zh-Hant`、`en`、`ja`、`ko`、`ru` 等；覆盖度不完全相同。
- Widget 扩展有独立多语言资源。
- `README.md`、`Documentation/Internal/FINAL_RELEASE_AUDIT.md`、开发者文档 Manifest、Help 文案、MiniApp 示例均用于交叉核对，但不会单凭营销文案把功能标成 A。

## 构建与测试记录

| 项目 | 命令摘要 | 结果 |
|---|---|---|
| 工程枚举 | `xcodebuild -list -project Py编程IDE.xcodeproj` | 成功；确认 6 Target、2 Configuration、2 Scheme |
| 目的地枚举 | `xcodebuild -showdestinations ... -scheme pythonide` | 成功；iOS 16.2/17.5/18.1/26.5 Simulator 与真机可用 |
| Debug Simulator 构建 | `xcodebuild -project Py编程IDE.xcodeproj -scheme pythonide -configuration Debug -destination 'platform=iOS Simulator,id=3D29BCB0-173B-4191-B80A-9EF9E8BEE7C3' -derivedDataPath /private/tmp/pythonide-content-audit-derived CODE_SIGNING_ALLOWED=NO build` | 成功；iPhone 17 Pro / iOS 26.5；依赖图 107 Targets；主 App 与三个扩展均构建/嵌入 |
| 单元/UI 测试 | 同目的地执行 `xcodebuild ... test` | 失败（exit 65），测试未执行：`pythonideTests/PythonHighlightQueryTests.swift:99,132` 的 `.zero` 缺少可推断上下文；这是测试 Target 编译阻断，本轮按只读约束未修复 |
| Simulator 启动 | 安装构建产物后启动 `app.xinmini.PythonIDE` | 仅确认 PythonIDE 启动封面；后续 `simctl` 截图/启动调用挂起，未完成根 Tab 与核心流程遍历，因此不把静态功能升级为动态确认 |

首次沙箱内 `xcodebuild -list` 因 SwiftPM/Xcode 缓存与 CoreSimulator 权限失败；在获准访问 Xcode 缓存后成功。这是环境限制，不是项目故障。
