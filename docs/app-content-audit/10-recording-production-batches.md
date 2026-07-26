# 面向开发者的批量录制分组

用户系列按学习路径组织；本文件按环境组织，两者不可混用。

| Batch | 固定环境 | 一次准备后录制内容 | 重置方法 |
|---|---|---|---|
| B01 新用户本地 | iPhone 17 Pro Simulator、中文、浅色、游客、无权限弹窗、本机工作区 | C-P0-02、输入/Traceback、分享、文件管理、包管理 UI | 重置 Demo 工作区快照 |
| B02 导入/文件 | 同设备；准备 Files/Share 源文件、`.zip`、`.enc`、`.miniapp` | C-P0-03、C-P0-08、Archive、回收站 | 清 Share Inbox/Trash，恢复文件集 |
| B03 AI 免费登录 | Simulator、测试账号、托管额度、`请求批准` | Agent 首次、安全审批、Diff、历史 | 删除测试会话并恢复 Repo Snapshot |
| B04 AI Pro/BYOK | Pro 测试账号、无真实 Key 画面、MCP Mock | 模型配置、Skill/MCP/Memory、Call Pack | 注入占位 Keychain，重置连接 |
| B05 MiniApp 视觉 | Simulator、横竖屏各一、固定高质量项目 | C-P0-07、AppUI/HTML/WebBridge、Widget 宣传素材 | 恢复 MiniApp Seed |
| B06 网站/社区 | 登录测试账号、Pro 与免费各一、稳定网络、匿名作品 | C-P0-09、社区安装/发布、审核状态 | 服务端测试项目与站点一键清理 |
| B07 Widget 系统表面 | Simulator iOS 18/26、固定 Snapshot | Home/Lock Widget、Live Activity、Control Center | 删除 Widget 配置/结束 Activity |
| B08 SSH/Git/WebDAV | 专用临时服务器、仓库、凭据、浅色、勿扰 | SSH 指纹/Terminal/SFTP/Deploy、Git 全链、WebDAV 冲突 | 服务端脚本重置；轮换密钥 |
| B09 真机权限 | 专用 iPhone、匿名 Apple ID、按权限分批 | 相机/麦克风/照片、Face ID、NFC、BLE、HealthKit、Bonjour、通知 | `simctl privacy reset` 不适用；真机在系统设置逐项重置/换测试包 |
| B10 iPad 专属 | iPad Simulator/真机、横屏、键盘、相同 Demo | 多栏、拖放、外接键盘、桌面开发、大画布 | 恢复同一 Demo Snapshot |

## 批量顺序

1. 先录所有无需登录/无需网络的 B01/B02；画面最稳定。
2. 再录同一登录会话的 B03/B04/B06，减少认证和额度重置。
3. 同一视觉 Demo 连录 B05/B07，可复用结果画面。
4. 远端环境只开放一个录制窗口完成 B08，随后销毁凭据。
5. 真机权限集中一天完成 B09；不要在每个教程中反复重置隐私。

## 多语言与主题

先产无文字母片 + 中文简体字幕。英文只重录 UI 文案高度/布局明显变化的成片；否则复用母片并换旁白/字幕。深色模式只为 App Store/官网补“效果证明”镜头，不为每条教程做双版本。iPad 只补布局、拖放和键盘专属流程。
