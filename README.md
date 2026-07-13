<p align="center">
  <img src="docs/assets/brand-mark.svg" width="112" alt="PythonIDE logo" />
</p>

<h1 align="center">PythonIDE for iOS</h1>

<p align="center">
  <strong>在 iPhone 和 iPad 上编写、运行并交付 Python 工作流</strong><br/>
  Python 3.14.6、科学计算、Notebook、AI Agent、MiniApp、Widget、SSH、Git 与 iOS 原生能力。
</p>

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304"><img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on the App Store" height="40" /></a>
  &nbsp;
  <a href="https://pythonide.xin/docs/"><img src="https://img.shields.io/badge/Documentation-pythonide.xin-3776AB?style=for-the-badge&logo=readthedocs&logoColor=white" alt="PythonIDE documentation" height="40" /></a>
  &nbsp;
  <a href="https://github.com/Python-IDE/PythonIDE-iOS"><img src="https://img.shields.io/github/stars/Python-IDE/PythonIDE-iOS?style=for-the-badge&logo=github" alt="GitHub stars" height="40" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.6-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.14.6" />
  <img src="https://img.shields.io/badge/iOS%20%2F%20iPadOS-16.2%2B-black?style=flat-square&logo=apple" alt="iOS and iPadOS 16.2 or later" />
  <img src="https://img.shields.io/badge/Native%20Packages-45-0A7E8C?style=flat-square" alt="45 native packages" />
  <img src="https://img.shields.io/badge/Pure%20Python%20Packages-63-F2C94C?style=flat-square" alt="63 pure Python packages" />
</p>

## 关于这个仓库

这是 PythonIDE 的官方产品介绍与公开文档仓库，承载官网、用户文档和公开项目入口。App 的完整商业源代码不在此仓库公开。

PythonIDE 不只是移动端代码编辑器。它把脚本从“写完并运行”继续连接到 Notebook、AI Agent、MiniApp、桌面开发、小组件、快捷指令、SSH、Git、WebDAV 和社区分享，让 Python 能成为 iOS 工作流的一部分。

```text
编辑代码 -> 本地运行 -> Agent 修改与验证 -> 接入 MiniApp / Widget / Shortcuts / Server
```

## 主要能力

| 工作流 | 能力 |
|---|---|
| **编辑与运行** | 多文件项目、语法高亮、查找替换、补全、Lint、交互式输入、ANSI/Rich、图片、图表与 HTML 输出 |
| **Notebook** | 打开和编辑 `.ipynb`，运行 Code 单元格，展示 Markdown、图片和结构化输出 |
| **AI Agent** | 读取和修改项目文件、运行 Python、分析错误、调用 Git/SSH/MiniApp/网页及原生工具；支持平台额度与 BYOK |
| **MiniApp / AppUI** | 使用 Python 构建带原生界面的移动工具，支持创建、预览、调试、导入、导出和桌面协作开发 |
| **Widget 与自动化** | 主屏和锁屏小组件、Control Center 控件、Live Activity、App Intents、Siri、快捷指令与 Share Extension |
| **远程开发** | SSH 终端、SFTP、服务器监控、部署、WebDAV，以及 Git 状态、提交、分支、远端、stash 和冲突处理 |
| **iOS 原生能力** | 相册、相机、位置、通讯录、日历、通知、语音、运动、蓝牙、HealthKit、音乐、触感等 Python 接口 |
| **桌面开发** | 通过 `npx pythonide-cli start` 连接 VS Code、Cursor、Zed 等桌面编辑器，并在真实 iPhone/iPad Runtime 中运行 |

## Python 3.14.6 运行时

PythonIDE 当前内置 Python 3.14.6，并预装 45 个包含原生代码的发行包和 63 个纯 Python 发行包。用户仍可通过 PyPI 或 Wheel 安装更多兼容的纯 Python 包。

### 主要科学计算与开发包

| 包 | 当前内置版本 | 用途 |
|---|---:|---|
| NumPy | 2.4.6 | 数组与数值计算 |
| SciPy | 1.18.0 | 科学计算与优化 |
| pandas | 3.0.3 | 表格与数据分析 |
| Matplotlib | 3.9.4 | 数据可视化 |
| OpenCV (headless) | 5.0.0.93 | 计算机视觉与图像处理 |
| scikit-learn | 1.9.0 | 机器学习 |
| Pillow | 12.3.0 | 图像处理 |
| pygame | 2.6.1 | 2D 图形、动画与交互 |
| cryptography | 49.0.0 | 密码学能力 |
| lxml | 6.1.1 | XML/HTML 处理 |
| aiohttp | 3.14.1 | 异步 HTTP |
| FastAPI | 0.139.0 | API 开发 |
| openai | 2.44.0 | OpenAI API 客户端 |
| pypdf | 6.14.2 | PDF 处理 |
| ReportLab | 5.0.0 | PDF 生成 |

<details>
<summary><strong>查看全部 45 个原生/C 扩展发行包</strong></summary>

`MarkupSafe`, `Pillow`, `PyYAML`, `SciPy`, `aiohttp`, `argon2-cffi`, `argon2-cffi-bindings`, `bcrypt`, `bitarray`, `brotli`, `cffi`, `contourpy`, `coverage`, `cryptography`, `cytoolz`, `frozenlist`, `greenlet`, `httptools`, `jiter`, `kiwisolver`, `lru-dict`, `lxml`, `matplotlib`, `mmh3`, `msgpack`, `msgspec`, `multidict`, `numpy`, `opencv-python-headless`, `pandas`, `pygame`, `pyrsistent`, `rapidjson`, `regex`, `ruamel.yaml`, `scikit-learn`, `setproctitle`, `simplejson`, `toolz`, `tornado`, `ujson`, `wrapt`, `xxhash`, `yarl`, `zstandard`。

</details>

内置包会随 App 版本更新。上表对应当前仓库中的运行时清单，清单更新日期为 2026-07-11。

## AI Agent 与 Skills

Agent 可以围绕真实项目执行多步骤任务：读取上下文、修改文件、运行代码、观察输出，并根据错误继续修复。模型既可以使用 PythonIDE 提供的额度，也可以使用用户自己的 API Key 或兼容服务商。

官方 Skills 仓库提供面向 Codex、Cursor 和 Claude Code 的 PythonIDE 开发知识，包括 AppUI、Widget、自动化、iOS 原生能力和场景开发：

```bash
npx skills add Python-IDE/pythonide-skills
```

详见 [PythonIDE Agent 开发文档](https://pythonide.xin/docs/pages/agent-development-index/) 与 [PythonIDE Skills](https://github.com/Python-IDE/pythonide-skills)。

## 文档

| 主题 | 入口 |
|---|---|
| 文档首页 | [pythonide.xin/docs](https://pythonide.xin/docs/) |
| AppUI / MiniApp | [AppUI 文档](https://pythonide.xin/docs/collections/appui/) |
| Widget | [Widget 文档](https://pythonide.xin/docs/collections/widget/) |
| iOS 原生模块 | [iOS 原生模块](https://pythonide.xin/docs/collections/ios-native/) |
| 自动化与扩展 | [自动化与扩展](https://pythonide.xin/docs/collections/automation-extension/) |
| Agent 开发 | [Agent 开发索引](https://pythonide.xin/docs/pages/agent-development-index/) |
| C 扩展模块 | [C 扩展说明](https://pythonide.xin/docs/pages/c-extensions-module/) |
| 隐私政策 | [Privacy Policy](https://pythonide.xin/privacy/) |

## Python-IDE 组织

| 仓库 | 职责 |
|---|---|
| [PythonIDE-iOS](https://github.com/Python-IDE/PythonIDE-iOS) | PythonIDE 产品介绍、官网和公开文档 |
| [pythonide-skills](https://github.com/Python-IDE/pythonide-skills) | 官方 Agent Skills 与安装入口 |
| [pythonide-link](https://github.com/Python-IDE/pythonide-link) | Universal Links、分享预览、远程导入与 MCP OAuth 回调 |
| [.github](https://github.com/Python-IDE/.github) | 组织主页、贡献指南、安全策略和 Issue 模板 |

## 安装与支持

- [在 App Store 下载 PythonIDE](https://apps.apple.com/app/id6753987304)
- [提交问题或功能建议](https://github.com/Python-IDE/PythonIDE-iOS/issues)
- [查看安全报告方式](https://github.com/Python-IDE/.github/blob/main/SECURITY.md)
- [加入 Telegram 社区](https://t.me/pythonzwb)

系统要求：iOS/iPadOS 16.2 或更高版本。

---

<p align="center">
  <strong>PythonIDE</strong><br/>
  Python on iPhone and iPad, connected to real workflows.
</p>
