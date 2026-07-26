# 功能证据矩阵

## 置信度规则

- A 已确认：真实 UI/导航入口 + 业务实现，或本轮动态运行。
- B 高可信推断：实现与文案完整，但未成功走通动态流程。
- C 待确认：仅部分实现、Feature Flag、测试或文案。
- D 不可达或疑似废弃：有代码但普通用户路径未找到。
- E 内部功能：Debug、测试、Preview 或管理员用途。

L1 证据至少为两种独立来源；L3 继承其 L2 行的 UI/导航/实现证据，并以 `03-complete-feature-inventory.md` 的具体符号为补充。JSON 中保留每条 L3 的证据键。

## L1 总证据

| L1 | 证据 1 | 证据 2 | 结论 |
|---|---|---|---|
| F01 | `HomeView+ListView.swift:385-700`（UI/Menu） | `ShareExtension/ShareViewController.swift:80-179,616-1028`（扩展/业务） | A |
| F02 | `ContentView+EditorViews.swift:300-900`（UI/手势） | `EditorSettingsView.swift:58-318`（设置/文案） | A |
| F03 | `ContentView.swift:430-500,850-980`（路由/Sheet） | `ContentView+Debugging.swift:1-560`、Runtime Tests（实现/测试） | A |
| F04 | `AIChatPageView.swift`、`AIChatInputBarComponents.swift:430-820`（UI） | `AgentRuntime/Tools/ToolBroker.swift`、Agent Tests（实现/测试） | A |
| F05 | `MiniAppLauncherView.swift`、`MiniAppEditorView*.swift`（UI） | `MiniAppStore+*.swift`、MiniApp Tests（业务/测试） | A |
| F06 | `WidgetStudioView.swift`（UI） | `PythonScriptActivityWidget/*.swift` + AppIntent metadata 构建（扩展/动态构建） | A |
| F07 | `NativeModulesGuideView.swift:1-560`（用户文档） | `Integrations/*Bridge.swift` + Entitlements（实现/权限） | B（逐能力不同） |
| F08 | `TerminalTabView.swift`、`ServerEditView.swift`、`SFTPFileView.swift`（UI） | `NSRemoteShell`/`SSHConnectionManager.swift` + Tests（实现/测试） | A/B |
| F09 | `GitRepositoryView*.swift`（UI） | `GitService*.swift` + Git Tests（实现/测试） | A/B |
| F10 | `ScriptLibraryNextPreviewView.swift:120-539`（UI/路由） | `WebsiteOnlineView.swift:757-928`、Community/Website API（UI/API） | A/B |
| F11 | `SettingsHomeModels.swift:40-65`、`ToolCatalog.swift:3-74`（UI Catalog） | `AppDataManagerView.swift:45-350`、`SettingsGeneralViews.swift:80-700`（业务） | A |
| F12 | `PythonIDEAccountLoginView`/Profile（UI） | `ProMembershipSheet.swift:10-132` + StoreKit Managers（购买实现） | A/B |

## L2 → L3 追踪矩阵

| L2 / 覆盖 L3 | 主要证据（路径:行；符号） | 类型 | 置信度 |
|---|---|---|---|
| F01.01 / .01–.03 | `pythonide/Home/NewFileFlowSheet.swift`；`ShareExtension/ShareViewController.swift:80-179,616-1028` | UI、扩展、业务、本地化 | A |
| F01.02 / .01–.03 | `HomeView+RowViews.swift`（`contextMenu`/`swipeActions`）；`HomeView+ListView.swift:385-700` | UI、手势、业务 | A |
| F01.03 / .01–.03 | `WorkspaceRoot.swift`；`ExternalFolderManager.swift`；`HomeView+FileOps.swift` | 数据模型、权限、业务 | A/B |
| F01.04 / .01–.02 | `TrashSheet.swift`；`TrashFolderArchiver.swift`；外部目录删除实现 | UI、业务、本地化 | A/B |
| F01.05 / .01–.02 | `QuickLookPreview.swift`；`ArchiveBrowserView.swift`；`EncryptedFileShare.swift`；`ScriptQRSheet.swift` | UI、业务、Crypto | A |
| F02.01 / .01–.03 | `RunestoneTextView*.swift`；`ContentView+EditorViews.swift`；Editor tests | UI、实现、测试 | A/B |
| F02.02 / .01–.03 | `ContentView+EditorViews.swift:300-470`；`KeyboardToolbar`；搜索控制器 | UI、键盘、Accessibility | A |
| F02.03 / .01–.03 | `NotebookEditorView*.swift`；`NotebookCellView*.swift`；Notebook Tests | UI、业务、测试 | A |
| F02.04 / .01–.02 | `MarkdownPreviewView.swift`；`CSVPreviewView.swift`；`WebPreviewView.swift` | UI、业务、权限 | A |
| F02.05 / .01–.02 | `EditorSettingsView.swift:58-318`；`BackgroundSettingsView.swift:10-261` | 设置、本地化 | A |
| F03.01 / .01–.03 | `ContentView+RunAndNavigation.swift`；运行按钮 `contextMenu` | UI、运行服务 | A |
| F03.02 / .01–.03 | `ConsoleOutputView*.swift`；`OutputMediaPreview.swift`；Traceback routing | UI、业务 | A |
| F03.03 / .01–.03 | `ContentView+Debugging.swift`；Debugger tests；长运行 Alert | UI、测试、业务 | A |
| F03.04 / .01–.02 | `ContentView+RunHistory.swift`；`BackgroundTaskManager.swift:1-500`；`LiveActivityManager.swift` | UI、后台、系统能力 | A/B |
| F03.05 / .01–.02 | `PackageManagerView.swift`；`PackageManagerCoordinator.swift`；PackageManager tests | UI、网络、测试 | A |
| F04.01 / .01–.03 | `AIChatPageView.swift`；`AIChatConversationNavigationView.swift`；Session Store | UI、存储 | A |
| F04.02 / .01–.03 | `AIChatAttachmentComponents.swift`；`AIChatImagePickerViews.swift`；`AI/Voice/*` | UI、权限、业务 | A |
| F04.03 / .01–.03 | `AgentRuntime/Tools/ToolBroker.swift`；`AIApplyCoordinator.swift`；`AIValidationCoordinator.swift` | Agent、业务、测试 | A |
| F04.04 / .01–.02 | `AIConfigFormView.swift`；`AISettingsManager.swift`；`AICallPackSheet.swift` | UI、Keychain、API、StoreKit | A/B |
| F04.05 / .01–.02 | `AISkillsManagerView.swift`；`AIMCPServer*.swift`；`AgentMemorySettingsViews.swift`；Native runtimes | UI、配置、权限 | A |
| F05.01 / .01–.03 | `MiniAppLauncherView.swift`；`MiniAppStore+Import.swift`；`MiniAppCollectionsHomeSection.swift` | UI、业务、测试 | A |
| F05.02 / .01–.03 | `MiniAppEditorView*.swift`；MiniApp settings/resources | UI、文件系统 | A |
| F05.03 / .01–.03 | `MiniAppRunnerView.swift`；`MiniAppWebBridge*.swift`；AppUI renderer | UI、Runtime、Schema | A/B |
| F05.04 / .01–.02 | `MiniAppStore+Export.swift`、`+TrashRestore.swift`；`MiniAppAccessService.swift` | 业务、Crypto、Biometric | A |
| F05.05 / .01–.02 | `DesktopDev/*.swift`；`pythonide-cli/README.md`；Bonjour Info.plist | UI、协议、系统能力 | B |
| F06.01 / .01–.03 | `WidgetStudioView.swift`；`WidgetWorkbench*.swift`；Widget Tests | UI、业务、测试 | A |
| F06.02 / .01–.03 | `PythonWidgetV2ContentWidget.swift`；`WidgetV2Core.swift`；IntentExtension | WidgetKit、AppIntent | A |
| F06.03 / .01–.03 | `PythonScriptActivityWidget.swift`、`AgentRunActivityWidget.swift`、`GitSyncActivityWidget.swift` | ActivityKit、扩展 | A/B |
| F06.04 / .01–.02 | `ControlCenterWidget.swift`；`Info.plist` UIApplicationShortcutItems | 系统入口、构建 | A |
| F06.05 / .01–.02 | `Automation/AppShortcutsProvider.swift` + 10 Intent 文件；SpotlightIndexer | AppIntents、Spotlight、构建 metadata | A |
| F07.01 / .01–.03 | `AppUIRenderer/*.swift`；`UIBridge*.swift`；`SceneBridge*.swift` | Bridge、Schema、文档 | A/B |
| F07.02 / .01–.03 | `LocationBridge.swift`、`MotionBridge.swift`、`BluetoothBridge.swift`、`NFCBridge.swift`、`HealthBridge.swift` | 系统 API、Entitlement | B |
| F07.03 / .01–.03 | `NativeModules/Photos`；`AudioRecorderBridge.swift`；`VisionBridge.swift`；`MusicBridge.swift`；`ShazamBridge.swift` | 权限、实现 | B |
| F07.04 / .01–.02 | `ContactsModule.swift`；`CalendarBridge.swift`；`NotificationBridge.swift`；`BiometricBridge.swift`；`KeychainBridge.swift` | 权限、安全、实现 | A/B |
| F07.05 / .01–.02 | `NetworkBridge.swift`；`WebSocketBridge.swift`；`HttpServerBridge.swift`；`BackgroundDownloadBridge.swift`；其余 Bridge | 网络、后台、系统 UI | A/B |
| F08.01 / .01–.03 | `ServerCardView.swift`、`ServerEditView.swift`；`SSHHostTrustSheet.swift`；Keychain | UI、安全、业务 | A |
| F08.02 / .01–.03 | `TerminalTabView.swift`；`SSHConnectionManager.swift`；`SwiftTerm` | UI、网络、终端 | A |
| F08.03 / .01–.03 | `SFTPFileView.swift`、`SFTPFileEditorView.swift`、`SFTPViewModel.swift` | UI、SFTP、文件 | A |
| F08.04 / .01–.02 | `ServerMonitorView.swift`；`DeployView.swift` | UI、SSH 命令 | B |
| F08.05 / .01–.02 | SSH Key/Snippet views/stores；NSRemoteShell tests | UI、Keychain、测试 | A |
| F08.06 / .01–.02 | `WebDAV/*.swift`；WebDAV Tests | UI、HTTP、ETag、测试 | A |
| F09.01 / .01–.03 | `GitRepository*.swift`；`GitService` init/clone/discovery | UI、libgit2 | A |
| F09.02 / .01–.03 | Git status/diff/staging views；GitDiff Tests | UI、业务、测试 | A |
| F09.03 / .01–.03 | Commit/history/detail views；Git history tests | UI、业务 | A/B |
| F09.04 / .01–.03 | Branch/Tag/Stash sheets and services | UI、业务 | A/B |
| F09.05 / .01–.02 | Remote/auth/sync services；`GitSyncActivityController.swift` | 网络、Keychain、ActivityKit | A |
| F09.06 / .01–.02 | Conflict editor/resolver；provider checks clients | UI、业务、API | A/B |
| F10.01 / .01–.03 | `ScriptLibraryNextPreviewView.swift:120-539`；deep-link API | UI、导航、API | A |
| F10.02 / .01–.03 | `ScriptDetailView.swift:230-430`；`ScriptLibraryActionSupport.swift:871-960` | UI、Runtime、Share | A |
| F10.03 / .01–.03 | `ScriptLibraryNextPreviewView.swift:1704-3935`；Community API | UI、账号、通知 | A/B |
| F10.04 / .01–.02 | `ScriptSubmissionView.swift`；ProjectPackageStore；API upload models | UI、打包、API | A/B |
| F10.05 / .01–.02 | `WebsiteOnlineView.swift:757-928`；`WebsiteManagementSheet.swift:45-161`；Service | UI、API、付费 Gate | A |
| F11.01 / .01–.03 | `ToolCatalog.swift:3-25`；`CodecToolView`、`JSONToolView`、`APITestToolView` | UI、业务 | A |
| F11.02 / .01–.03 | `ToolCatalog.swift:27-45`；QR/ImageURL/HTMLImage views | UI、相册/相机、Web | A |
| F11.03 / .01–.03 | `ToolCatalog.swift:47-74`；Timestamp/Base/Regex/Download views | UI、网络、后台 | A |
| F11.04 / .01–.02 | `SettingsGeneralViews.swift:279-410`；Editor/Console/Background settings | 设置、手势、本地化 | A |
| F11.05 / .01–.02 | `AppDataManagerView.swift:45-350`；`SettingsGeneralViews.swift:80-167,568-700`；Docs/Feedback | UI、数据、安全 | A |
| F12.01 / .01–.03 | `PythonIDEAccountLoginView`、Profile Setup/Edit `:3436-3935`；SessionStore | UI、Sign in with Apple、API | A |
| F12.02 / .01–.03 | `ProMembershipSheet.swift:10-132`；IAP/Entitlement managers | UI、StoreKit、业务 | A/B |
| F12.03 / .01–.03 | `ProMembershipSheet.swift:18-87`；Website quota；PaidFeatureGate | Paywall、Gate、API | A/B |
| F12.04 / .01–.02 | `DonationView.swift`；`DonationHonorManager` | UI、StoreKit | A/B |
| F12.05 / .01–.03 | `ReferralInviteView.swift:13-220,516-718`；ReferralState/API | UI、API、本地化 | A/B |

## 动态证据

- `xcodebuild -list` 成功解析工程、Target、Scheme 和全部 Swift Package。
- Debug `pythonide` 在 iPhone 17 Pro / iOS 26.5 Simulator 完整构建成功，三个扩展均参与构建。
- AppIntents metadata 在构建中生成并训练 10 个 Locale；确认 Shortcut phrases 不是只存在于源文件。
- 测试未执行：测试 Target 在编译 `pythonideTests/PythonHighlightQueryTests.swift:99,132` 时因 `.zero` 缺少可推断上下文而失败（exit 65）。本轮只读审计未修复该生产仓库问题。
- Simulator 安装并启动到 PythonIDE 启动封面，但后续 `simctl` 调用挂起，未完成根 Tab 与用户流程遍历；因此没有任何 L3 仅凭本次启动升级为“动态确认”。
- 服务端、账号、远端主机与真机专属项不因构建成功升级为动态 A。
