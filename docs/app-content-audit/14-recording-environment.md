# 录制环境判断

## 总体结论

- Simulator 即可：F01–F06 大多数 App 内流程、F08/F09 的 UI 与网络流程、F10 网站/社区（测试服务可用时）、F11 工具、F12 账号页面/StoreKit Sandbox UI。
- 真机更合适：MiniApp 图形性能、Haptics、Live Activity 最终效果、局域网桌面开发、相机/麦克风质量、外接键盘、系统 Share/Widget 最终视觉。
- 必须真机：NFC、Bluetooth/BLE 外设、HealthKit 真实数据、真实 Face ID/Touch ID 行为、真实相机/视频采集、设备传感器、真实推送、MusicKit/Shazam 端到端、设备间/局域网发现的最终验证。
- 当前无法判断：AlarmKit/部分新系统 API 的实际设备可用性与地区/Entitlement；先标待确认。

## L1 环境矩阵

| 领域 | Simulator | 真机补录 | iPad/方向 | 说明 |
|---|---|---|---|---|
| F01 文件 | 主要流程即可 | Files Provider/iCloud 跨设备更合适 | iPad 拖放/多栏；横屏补录 | Share Extension 可模拟器，外部 Provider 需真实 App 时用真机 |
| F02 编辑 | 即可 | 键盘手感/性能更合适 | iPad 横屏+外接键盘专版 | 大字体用截图回归，非每条视频 |
| F03 运行 | 即可 | 长任务/性能/音频更合适 | Notebook 图表可 iPad 横屏 | Live Activity 最终展示真机更可信 |
| F04 AI | 即可 | 相机/语音/Apple Intelligence 真机 | iPad 可补项目协作 | 固定回放降低服务波动 |
| F05 MiniApp | 即可 | Pygame/Scene/传感器/局域网更合适或必须 | 视觉项目可能横屏；iPad 大画布 | 纯 AppUI 宣传 Simulator 足够 |
| F06 Widget | Simulator 可配置 | App Store 成片建议真机 | iPhone 竖屏；iPad 只做布局差异 | Control Center 需 iOS 18+ |
| F07 原生能力 | UI/拒绝态可模拟 | NFC/BLE/Health/Face ID/传感器/真实推送必须 | 视模块 | 不把“有权限”一律判真机，HTTP/PDF/Keychain 可模拟器 |
| F08 远程 | Simulator 即可 | 局域网/键盘/真实网络更合适 | iPad 横屏终端值得补 | 使用专用 Host，不录真实 IP/Key |
| F09 Git | Simulator 即可 | 无必须真机 | iPad Diff 分栏可补 | 远端网络真实但不依赖硬件 |
| F10 社区/网站 | Simulator 即可 | Share 最终效果可真机 | 无必须 iPad | 依赖测试账号/服务端，不依赖硬件 |
| F11 工具设置 | 大多即可 | QR 相机、相册、App Lock 真机 | 无需普遍补 iPad | 静态设置优先图文 |
| F12 账号购买 | Simulator/Sandbox 可录流程 | Apple 登录/StoreKit 最终验收真机 | 无 | 价格不可烧入长期视频 |

## 权限逐项

| 权限/能力 | 录制判断 | 原因 |
|---|---|---|
| Camera / Video | 必须真机做最终教程 | Simulator 可注入图片但不能证明真实采集 |
| Photos | Simulator 即可；真机更合适 | Picker/授权可模拟，真实图库注意隐私 |
| Microphone / Speech | 真机更合适 | Simulator 输入和音频路由不稳定 |
| Location | Simulator 即可演示路径；真机补真实移动 | `simctl location` 可模拟 |
| Motion | 必须真机最终验证 | Simulator 无真实传感器 |
| Bluetooth/BLE | 必须真机 | Simulator 不提供真实外设链路 |
| NFC | 必须真机 | Simulator 不支持 Tag Reading |
| Contacts/Calendar/Reminders | Simulator 即可 | 可使用匿名样例库和权限重置 |
| HealthKit | 必须真机最终验证 | 模拟器 UI 不代表真实健康数据/授权行为 |
| Face ID/Touch ID | Simulator 可演示成功/失败；真机最终 | `simctl biometric` 可模拟，最终交互需设备 |
| Notifications | 本地通知 Simulator 即可；真实 push 必须真机 | APNs/设备 Token 链路 |
| Live Activities | Simulator 可开发；宣传建议真机 | 锁屏/Dynamic Island 最终观感 |
| Local Network/Bonjour | 真机更合适 | Simulator 与 Mac 网络拓扑不等同用户环境 |
| WeatherKit/MusicKit/Shazam | 真机更合适/部分必须 | Entitlement、订阅、地区、麦克风与账号状态 |

## 语言、主题与可访问性

- 中文简体和英文分别录需要展示真实文字的完整教程；其他语言先字幕本地化，不承诺全量重录。
- 无文字原子素材优先复用；系统 Picker/Alert 文案无法后期替换时再按语言重录。
- 浅色主教程；深色只录一组营销/外观对比。不要双倍维护所有教程。
- 大字体/VoiceOver：制作一篇图文可访问性指南 + 自动截图检查；只有控件布局/Accessibility Action 专属流程才单独录。
- iOS 16/18/26：新用户教程以当前主版本为准；旧系统只在入口明显不同（Tab、Widget、Control Center）时补 10–20 秒差异片段。
