# 原子录屏素材库

## 命名与目录

文件名：`AREA__TASK__STATE__DEVICE__LOCALE__V01.mp4`，例如 `RUN__FIRST_SUCCESS__IPHONE17PRO__ZH-HANS__V01.mp4`。

```text
recording-library/
├─ 00_manifest/manifest.csv + app-version.json
├─ 01_clean-masters/AREA/YEAR-MONTH/*.mov
├─ 02_touch-overlays/click-longpress-swipe/
├─ 03_audio/zh-Hans/en/
├─ 04_subtitles/zh-Hans/en/
├─ 05_projects/tutorial/marketing/
├─ 06_exports/channel/aspect-ratio/
└─ 99_retired/APP_VERSION/
```

Manifest 字段：文件名、功能 ID、起止状态、App/iOS/设备/语言/账号/权益/权限、Demo 数据版本、使用成片、重录原因、替代版本、校验人。Git 只存 Manifest/字幕/小型模板；大视频用对象存储，保留不可变版本，不覆盖 `V01`。

## 原子片段

所有片段无旁白、无渠道文字，首尾各留 0.5 秒；“含触点”指可导出独立触点版，纯净母片仍保留。

| ID / 片段名 | 功能 | 起始 → 结束 | 最佳时长 | 触点 | 可复用成片 | Demo / 重录条件 |
|---|---|---|---|---|---|---|
| A01 `HOME__OPEN_NEW_MENU` | F01.01 | 首页→新建菜单 | 2s | 是 | 01/02/03 | 本机工作区；`+`或菜单变 |
| A02 `FILE__CREATE_PYTHON` | F01.01.01 | 菜单→空编辑器 | 5s | 是 | 01/02 | `hello.py`；文案/表单变 |
| A03 `EDITOR__TYPE_HELLO` | F02.01 | 空编辑器→代码完成 | 4s | 可选 | 01/02 | 固定代码；字体/键盘布局变 |
| A04 `RUN__SUCCESS_OUTPUT` | F03.01/.02 | 编辑器→成功输出 | 4s | 是 | 01/02/04 | 固定输出；运行/输出 UI 变 |
| A05 `IMPORT__DOCUMENT_PICKER` | F01.01.03 | 新建菜单→导入完成 | 6s | 是 | 03 | zip；入口/Picker 变 |
| A06 `ARCHIVE__BROWSE_EXTRACT` | F01.05.01 | Archive→内容/解压 | 5s | 是 | 03 | 固定 zip；Archive UI 变 |
| A07 `WORKSPACE__CONNECT_EXTERNAL` | F01.03.02 | 菜单→外部根 | 7s | 是 | 03 | DemoProject；授权/入口变 |
| A08 `WORKSPACE__SWITCH_ROOT` | F01.03 | 根选择器→目标根 | 3s | 是 | 03/文件系列 | 匿名根名；根 UI 变 |
| A09 `PACKAGE__SEARCH_DETAIL` | F03.05.01 | 包管理→兼容详情 | 5s | 是 | 04 | 固定 PyPI cache；详情变 |
| A10 `PACKAGE__INSTALL_SUCCESS` | F03.05.01 | 安装→完成 | 6s | 是 | 04/宣传 | Pure Wheel；进度/结果变 |
| A11 `CONSOLE__INPUT_SUBMIT` | F03.02.01 | 等待输入→输出 | 5s | 是 | 05/入门 | 固定脚本；输入栏变 |
| A12 `TRACEBACK__JUMP_FIX` | F03.02.03 | Traceback→错误行 | 4s | 是 | 05/排错 | 固定行号；链接/编辑器变 |
| A13 `RUN__FORCE_STOP` | F03.03.03 | 长运行提示→已停止 | 5s | 是 | 05/安全 | 安全循环；Alert 变 |
| A14 `AGENT__SELECT_WORKSPACE` | F04.01.01 | 新对话→绑定项目 | 4s | 是 | 01/06 | DemoProject；顶部 UI 变 |
| A15 `AGENT__PLAN_CONFIRM` | F04.03 | 计划→`确认修改工作区文件？`→`修改一次` | 7s | 是 | 06/宣传 | 固定响应；确认框/文案变 |
| A16 `AGENT__REVIEW_DIFF` | F04.03.03 | Diff 顶→审查完成 | 6s | 是/滑动 | 06/宣传 | 固定 Patch；Diff UI 变 |
| A17 `AGENT__ACCEPT_VALIDATE` | F04.03.03 | `接受`→验证通过 | 5s | 是 | 01/06 | Mock validation；状态变 |
| A18 `MINIAPP__CONVERT_SCRIPT` | F05.01.02 | 文件行→MiniApp 编辑器 | 7s | 是/长按 | 01/07 | weather seed；菜单/表单变 |
| A19 `MINIAPP__RUN_INTERACT` | F05.03 | 编辑器→交互结果 | 8s | 是/滑动 | 01/07/官网 | 冻结数据；视觉/运行 UI 变 |
| A20 `MINIAPP__SHARE_PACKAGE` | F05.04.01 | 项目→Share Sheet | 4s | 是 | 07/08 | 匿名包；菜单/Sheet 变 |
| A21 `FILE__ENCRYPT_DECRYPT` | F01.05.02 | 文件→`.enc`→原文件 | 10s | 是/长按 | 08/安全 | 假密码；加密 UI 变 |
| A22 `WEBSITE__DEPLOY_SUCCESS` | F10.05.01 | 可发布→成功 | 7s | 是 | 01/09/宣传 | 测试站；API/UI 变 |
| A23 `WEBSITE__OPEN_PUBLIC` | F10.05.02 | 站点卡→浏览器 | 4s | 是 | 01/09/官网 | 固定页；URL/结果变 |
| A24 `WEBSITE__UPDATE_SAME_URL` | F10.05.01 | 改标题→更新结果 | 7s | 是 | 09/宣传 | 同站点；更新 UI 变 |
| A25 `WEBSITE__HISTORY_ROLLBACK` | F10.05.02 | 管理→部署记录 | 5s | 是 | 09/Pro | 两版本；配额/历史变 |
| A26 `WIDGET__PUBLISH_TO_HOME` | F06.01/.02 | Snapshot→桌面 Widget | 8s | 是 | 产品演示/第二批 | 固定 Snapshot；系统 UI 变 |
| A27 `GIT__STAGE_COMMIT_PUSH` | F09.02/.03/.05 | Status→同步完成 | 10s | 是 | 远程系列/宣传 | 临时 repo；Git UI 变 |
| A28 `SSH__TRUST_CONNECT` | F08.01/.02 | Server→Terminal | 8s | 是 | 远程系列 | 专用 Host；指纹/UI 变 |

## 素材复用规则

- 教程使用触点版；官网/社交优先纯净版，触点不超过两处。
- 同一母片不得烧入中文标题；标题/字幕在成片工程中叠加。
- 只有一个原子片段失效时，只重录该片段并更新 Manifest 的 `supersedes`。
- 登录/权限/支付/系统 Widget 等 OS 表面单独录，不与 App 内动作黏成不可拆母片。
