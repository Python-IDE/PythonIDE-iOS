# Tutorial / Demo / Recording Mode 建议

## 当前已有能力

| 能力 | 现状与证据 | 可用于录制 |
|---|---|---|
| Sample/Seed | `SampleFilesProvider.createIfNeeded()` 在 `pythonideApp.swift:260-269`；Notebook/Pygame/Scene/MiniApp 示例 | 可提供固定起始文件，但不是完整 Tutorial Mode |
| UI Test 脚本注入 | `PYTHONIDE_UI_TEST_MODE`、`...SCRIPT_B64`、`...DELAY_MS`，`pythonideApp.swift:1370-1390` | 可自动打开/运行固定脚本 |
| 跳过启动封面 | `PYTHONIDE_UI_TEST_SKIP_LAUNCH_COVER` | 可减少批量录制等待 |
| Debug Website Preview | `-WebsiteDeployUIPreview`、`-WebsiteManagementUIPreview`，`pythonideApp.swift:440-448` | 可稳定录网站 UI 状态；Debug-only |
| Desktop Deep Link | `DesktopDevDeepLinkRouter.dispatchLaunchArgumentIfNeeded()` | 可进入桌面开发场景 |
| Fixtures/Mocks/Previews | Tests、MiniApp、Widget、网站 Preview models | 可复用数据定义，不能直接宣称是用户 Demo Mode |
| 一键重置/统一页面跳转/冻结时间 | 未发现完整产品级实现 | 建议新增 Debug/UITest-only Recording Profile |
| 权限/订阅状态模拟 | 测试与部分 Manager 可注入，未发现统一 UI | 建议统一，不进入 Release UI |

结论：仓库已有很好的“种子 + 启动参数”基础，但没有完整 Tutorial/Demo Mode。值得实现一个小型 `RecordingProfile`，而不是长期维护独立视频工程或复制一套业务 UI。

## 建议项

| 建议 | 工作量 | 节省的录制工作 | 值得 | 风险/约束 |
|---|---|---|---|---|
| `-RecordingProfile first-run|agent|miniapp|website|git` | M | 一键准备 P0/Batches，减少导航与误状态 | 是，最高 | 仅 Debug/UITest 编译；Release 忽略 |
| `-RecordingRoute <stable-id>` 深链到首页/编辑器/Agent/包管理/MiniApp/网站 | M | 重录单个原子片段无需走前置 | 是 | 路由 ID 与页面解耦；不得绕过真实权限/付费逻辑用于产品演示 |
| `-RecordingReset demo-v1` 恢复匿名工作区/Repo/MiniApp/Widget | M | 每次重录从同一状态开始 | 是 | 只删除专用容器中的 Demo 数据，绝不作用真实数据 |
| 冻结日期、时区、随机 ID、图表和网络响应 | S–M | 结果画面稳定，多语言可复用 | 是 | Mock 与真实服务协议漂移要有契约测试 |
| AI 固定计划/Diff/验证回放 | M | Agent P0 从不可预测变可重复 | 是 | 明示为演示数据；真实教程另保留联网版验证 |
| 网站/社区 Mock 状态：空、发布中、成功、配额、驳回 | M | 不依赖服务端和审核等待 | 是 | 不得用于声称服务端已动态成功；只录 UI 教学分支 |
| 免费/Pro/旧终身/额度耗尽 Entitlement Fixture | S | 一次录完 Gate/Paywall 分支 | 是 | StoreKit 购买成功仍需 Sandbox 实测 |
| 权限状态 Profile：未询问/允许/拒绝/受限 | M | 真机权限日大幅减时 | 部分 | Simulator 模拟不替代 NFC/BLE/HealthKit 真机验证 |
| 离线/超时/冲突错误注入 | M | 可稳定录包管理、WebDAV、Git/SSH 排错 | 是，第二阶段 | 错误必须来自真实错误映射，不自创文案 |
| 禁用分析/通知/外部弹窗 | S | 清洁画面、不污染生产数据 | 是 | 保留本地必要日志；不改变用户流程 |
| 一键清除账号/服务端 Demo 数据 | L | 网站/社区/邀请批量录制 | 视后端投入 | 必须限定测试环境和白名单账号 |

## 安全设计

- 编译层：`#if DEBUG || UITEST`；Release 不注册路由、不解析参数、不包含调试菜单文案。
- 数据层：Recording 容器单独根目录，启动时验证路径前缀；重置只触达该目录。
- 网络层：Mock base URL 只在签名为 Debug 且参数明确时启用；禁止携带生产 Token。
- 遥测层：Recording Session 标记并本地丢弃产品分析；本仓库未发现通用远端 Analytics，但 AI/服务端调用仍需测试环境隔离。
- 视觉层：状态栏、日期和匿名姓名固定；所有 Screenshot/视频可自动跑隐私关键词扫描。

## 推荐最小实现顺序

先做 S 级：跳过封面、冻结时间、隐藏弹窗、Demo v1；再做 M 级：稳定路由、Agent 回放、重置。权限与服务端错误模拟留到第二批，避免为少量视频过度建设。
