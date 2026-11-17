<p align="center">
  <img src="docs/assets/brand-mark.svg" width="112" alt="PythonIDE logo" />
</p>

<h1 align="center">PythonIDE for iOS</h1>

<p align="center">
  <strong>在 iPhone 和 iPad 上编写、运行 Python，并发布网站</strong><br/>
  Python 3.15.2、HTML/CSS/JavaScript、Notebook、AI Agent、MiniApp、Widget、SSH、Git 与 iOS 原生能力。
</p>

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304"><img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on the App Store" height="40" /></a>
  &nbsp;
  <a href="https://pythonide.xin/docs/"><img src="https://img.shields.io/badge/Documentation-pythonide.xin-3776AB?style=for-the-badge&logo=readthedocs&logoColor=white" alt="PythonIDE documentation" height="40" /></a>
  &nbsp;
  <a href="https://github.com/Python-IDE/PythonIDE-iOS"><img src="https://img.shields.io/github/stars/Python-IDE/PythonIDE-iOS?style=for-the-badge&logo=github" alt="GitHub stars" height="40" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.15.2-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.15.2" />
  <img src="https://img.shields.io/badge/iOS%20%2F%20iPadOS-16.2%2B-black?style=flat-square&logo=apple" alt="iOS and iPadOS 16.2 or later" />
  <img src="https://img.shields.io/badge/Bundled%20Packages-104-0A7E8C?style=flat-square" alt="104 bundled packages" />
</p>

## 关于这个仓库

这是 PythonIDE 的官方产品介绍与公开文档仓库，承载官网、用户文档和公开项目入口。App 的完整商业源代码不在此仓库公开。

PythonIDE 支持在 iPhone 和 iPad 上运行 Python 脚本和 Notebook，编辑、预览多文件 Web 项目，并把静态网站发布成可分享的短链接。AI Agent、MiniApp、小组件、快捷指令、SSH、Git 和 WebDAV 可以接入同一套开发工作流。

```text
Python / HTML / CSS / JavaScript → 本地运行与预览 → Agent 修改与验证
HTML 项目 → 部署 → 分享网站短链
Python 脚本 → MiniApp / Widget / Shortcuts
```

## 主要能力

| 工作流 | 能力 |
|---|---|
| **Python 编辑、运行与调试** | 多文件项目、语法高亮、查找替换、补全、Lint、交互式输入、ANSI/Rich、图片与图表输出，以及断点、单步执行、调用栈和变量查看 |
| **HTML / CSS / JavaScript** | 多文件 Web 项目、HTML/CSS 离线补全与格式化、相对资源路径补全、即时预览，以及 console、资源加载、Promise 和 fetch 错误检查 |
| **网站发布** | 在「部署」页发布静态 HTML 网站，生成短链接。通过「我的网站」管理站点和查看额度 |
| **Notebook** | 打开和编辑 `.ipynb`，运行 Code 单元格，展示 Markdown、图片和结构化输出 |
| **AI Agent** | 读取和修改项目文件、运行 Python、分析错误、调用 Git/SSH/MiniApp/网页及原生工具；支持平台额度与 BYOK |
| **MiniApp / AppUI** | 使用 Python 构建带原生界面的移动工具，支持创建、预览、调试、导入、导出和桌面协作开发 |
| **Widget 与自动化** | 主屏和锁屏小组件、Control Center 控件、Live Activity、App Intents、Siri、快捷指令与 Share Extension |
| **远程开发** | SSH 终端、SFTP、服务器监控、部署、WebDAV，以及 Git 状态、提交、分支、远端、stash 和冲突处理 |
| **iOS 原生能力** | 相册、相机、位置、通讯录、日历、通知、语音、运动、蓝牙、HealthKit、音乐、触感等 Python 接口 |
| **桌面开发** | 通过 `npx pythonide-cli start` 连接 VS Code、Cursor、Zed 等桌面编辑器，并在真实 iPhone/iPad Runtime 中运行 |

## HTML / CSS / JavaScript 工作流

在 App 里编辑和检查网页，准备好后即可从项目的「部署」页发布。

- 编辑 HTML、CSS 与 JavaScript 多文件项目
- 使用 HTML/CSS 离线智能补全、格式化和相对资源路径补全
- 即时预览页面，并加载项目中的本地图片、脚本、样式与其他资源
- 在内置控制台查看 console 输出及资源加载、Promise 和 fetch 错误
- 发布后复制短链接，在浏览器打开或与他人分享

[查看网站部署教程](https://pythonide.xin/website/) · [浏览网站广场](https://pythonide.xin/showcase/)

## Python 3.15.2 运行时

App Store 版 1.8.1 内置 Python 3.15.2 和 104 个发行包。可通过 PyPI 或 Wheel 安装其他兼容的纯 Python 包。

### 主要科学计算与开发包

| 包 | 内置版本 | 用途 |
|---|---:|---|
| NumPy | 2.5.2.post1 | 数组与数值计算 |
| SciPy | 1.18.1 | 科学计算与优化 |
| pandas | 3.1.1 | 表格与数据分析 |
| Matplotlib | 3.9.4 | 数据可视化 |
| OpenCV (headless) | 5.1.0+pythonide.1 | 计算机视觉与图像处理 |
| scikit-learn | 1.9.1 | 机器学习 |
| Pillow | 13.0.0 | 图像处理 |
| pygame | 2.6.1 | 2D 图形、动画与交互 |
| cryptography | 49.0.0 | 密码学能力 |
| lxml | 6.1.1 | XML/HTML 处理 |
| aiohttp | 3.14.5 | 异步 HTTP |
| MLX | 0.32.4 | 设备端数组计算和模型推理，需 iOS 17 或更高版本 |

<details>
<summary><strong>查看全部 104 个内置发行包</strong></summary>

`aiofiles`、`aiogram`、`aiohappyeyeballs`、`aiohttp`、`annotated-types`、`anyio`、`argon2-cffi`、`argon2-cffi-bindings`、`asttokens`、`attrs`、`av`、`bcrypt`、`bitarray`

`black`、`Brotli`、`certifi`、`cffi`、`charset-normalizer`、`click`、`contourpy`、`coverage`、`cryptography`、`cycler`、`cytoolz`、`decorator`、`dulwich`

`executing`、`fonttools`、`frozenlist`、`greenlet`、`h11`、`h5py`、`httpcore`、`httptools`、`httpx`、`idna`、`ipython`、`ipython_pygments_lexers`、`jiter`

`joblib`、`kiwisolver`、`libyaml`、`lru-dict`、`lxml`、`magic-filter`、`MarkupSafe`、`matplotlib`、`matplotlib-inline`、`mlx`、`mmh3`、`msgpack`、`msgspec`

`multidict`、`mypy_extensions`、`narwhals`、`numpy`、`opencv-python-headless`、`packaging`、`pandas`、`pathspec`、`pexpect`、`pillow`、`platformdirs`、`prompt_toolkit`、`propcache`

`protobuf`、`ptyprocess`、`pure_eval`、`pycparser`、`pycryptodome`、`pydantic`、`pydantic_core`、`pygame`、`pyparsing`、`pyrsistent`、`python-dateutil`、`python-rapidjson`、`pytz`

`PyYAML`、`regex`、`ruamel.yaml.clib`、`safetensors`、`scikit-learn`、`scipy`、`sentencepiece`、`setproctitle`、`simplejson`、`six`、`sniffio`、`stack-data`、`threadpoolctl`

`tokenizers`、`toolz`、`tornado`、`traitlets`、`typing_extensions`、`typing-inspection`、`ujson`、`urllib3`、`wcwidth`、`wrapt`、`xxhash`、`yarl`、`zstandard`

</details>

[查看原生扩展及系统兼容说明](https://pythonide.xin/docs/pages/c-extensions-module/)。

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
| 网站发布 | [部署教程](https://pythonide.xin/website/) |
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
