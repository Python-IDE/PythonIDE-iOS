<p align="center">
  <img src="docs/assets/brand-mark.svg" width="112" alt="PythonIDE logo" />
</p>

<h1 align="center">PythonIDE for iOS</h1>

<p align="center">
  <strong>iPhone / iPad 上的 Python 工作台</strong><br/>
  本地运行 Python 3.13，用 AI Agent 处理项目任务，并把脚本接入小组件、MiniApp、SSH、Git 和社区脚本库。
</p>

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304">
    <img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on App Store" height="40" />
  </a>
  &nbsp;
  <a href="https://github.com/jinwandalaohu66/PythonIDE-iOS">
    <img src="https://img.shields.io/github/stars/jinwandalaohu66/PythonIDE-iOS?style=for-the-badge&logo=github" alt="GitHub stars" height="40" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/iOS-16.2+-blue?style=flat-square" alt="iOS 16.2+" />
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python" alt="Python 3.13" />
  <img src="https://img.shields.io/badge/Swift-5.9-FA7343?style=flat-square&logo=swift" alt="Swift" />
  <img src="https://img.shields.io/badge/AI-Agent-6D5DFB?style=flat-square" alt="AI Agent" />
  <img src="https://img.shields.io/badge/Widgets-MiniApps-F2C94C?style=flat-square" alt="Widgets and MiniApps" />
  <img src="https://img.shields.io/badge/SSH-Git-22C55E?style=flat-square" alt="SSH and Git" />
</p>

---

## What is PythonIDE?

PythonIDE is a mobile Python workspace for iPhone and iPad. It is not only a code editor or a local Python runner: it connects scripts with AI Agent workflows, widgets, MiniApps, remote servers, Git repositories, iOS automation, and a script community.

The goal is simple:

```text
Write a script
  -> run and inspect it locally
  -> ask Agent to edit, debug, or complete the task
  -> turn the result into a Widget, MiniApp, Shortcut, server workflow, or shared script
```

PythonIDE is built for mobile scenarios where a script should become something you can run, reuse, automate, display, deploy, or share directly from iPhone / iPad.

---

## Highlights

| Area | What it brings to PythonIDE |
|---|---|
| **AI Agent** | AI chat, inline edits, project task execution, cross-file read/write, Python execution, tool calling, BYOK and platform quota |
| **Widgets** | Python script widgets, Widget Studio, preview, Home Screen / Lock Screen widgets, Control Center controls, Live Activity / Dynamic Island |
| **MiniApp** | MiniApp launcher, editor, packaging, import/export, AppUI / HTML / WebBridge runtimes, hidden libraries, logs |
| **SSH / Server** | SSH connections, terminal, SFTP file manager, server monitoring, deployment, key management, command snippets |
| **Git / WebDAV** | Repository status, diff, staging, commits, sync, history, branches, remotes, stash, tags, conflict handling, WebDAV remote files |
| **Script Community** | Browse, categorize, view details, import, run, submit, review, like, and discover scripts from other users |

---

## Core Workflows

### AI-assisted project work

Use Agent when a task is larger than a single edit. It can inspect project files, modify code, run Python, read output, continue from errors, and coordinate with tools such as Git, SSH, MiniApp, web, or native capability adapters.

| Workflow | Example |
|---|---|
| Fix a failing script | Read traceback, locate files, patch code, rerun Python |
| Modify a project | Create or update multiple files with context |
| Prepare a MiniApp | Generate AppUI / HTML structure and connect script logic |
| Work with remote tasks | Combine project context with SSH / SFTP workflows |
| Control model usage | Use platform quota or bring your own API key |

### From script to system entry

Some scripts are not meant to stay in the console. PythonIDE gives them mobile entry points:

| Output form | Good for |
|---|---|
| **Widget** | Daily data, status cards, counters, dashboards, quick glance information |
| **Control Center** | Fast script actions and controls |
| **Live Activity / Dynamic Island** | Long-running tasks and visible run status |
| **Shortcuts / App Intents** | Script automation from Siri, Shortcuts, and system actions |
| **Share Extension** | Import or process content shared from other apps |
| **MiniApp** | Script tools that need UI, forms, lists, logs, or packaging |

### Real project and server workflows

PythonIDE also connects local scripts with real development infrastructure:

| Area | Capabilities |
|---|---|
| **Git** | Status, diff, staging, commit, sync, history, branch, remote, stash, tags, conflict handling |
| **SSH** | Terminal, command snippets, password/key auth, deployment, server monitoring |
| **SFTP** | Remote browsing, upload/download, remote editing, batch operations |
| **WebDAV** | Remote directories, upload/download, remote editing, favorites, cache, certificate pinning |
| **SQLite** | Local database browsing and inspection workflows |

---

## Feature Overview

| Module | Capabilities |
|---|---|
| **Home / File Management** | Local files and folders, import, external folders, search, sorting, pinning, color labels, batch actions, trash, preview |
| **Code Editor** | Python / JavaScript / HTML / CSS / JSON / Markdown editing, syntax highlighting, shortcut bar, find & replace, Jedi completion, Python lint, AI inline edits |
| **Runtime & Console** | Local Python 3.13, JavaScriptCore, HTML preview, interactive `input()`, Rich / ANSI output, inline images, charts and HTML, error jump and repair entry |
| **AI Agent** | AI chat, Agent execution, cross-file read/write, Python execution, Git / SSH / MiniApp / web / native tool calling, BYOK and platform quota |
| **Community / Script Library** | Browse scripts, categories, details, import, run, submit, review, like, user profiles |
| **MiniApp** | Launcher, creation, editing, packaging, import/export, AppUI / HTML / WebBridge runtime, hidden libraries, log center |
| **Widgets** | Python script widgets, Widget Studio, preview, Home Screen / Lock Screen widgets, Control Center controls, Live Activity / Dynamic Island |
| **SSH / Server** | SSH connection, terminal, SFTP file manager, monitoring, deployment, key management, command snippets |
| **Git** | Repository status, diff, staging, commit, sync, history, branch, remote, stash, tags, conflict handling |
| **WebDAV** | WebDAV server, remote directories, upload/download, remote editing, batch operations, favorites, cache, certificate pinning |
| **Toolbox** | Encoding/decoding, JSON, API debugging, QR code, image URL, HTML to image, timestamp, base conversion, regex, direct download |
| **Package Management** | Built-in Python packages, C extension packages, Wheel install, PyPI search/install, package recommendations |
| **iOS Native Modules** | `photos`, `contacts`, `location`, `motion`, `speech`, `notification`, `vision`, `device`, `network`, `haptics`, `calendar`, `bluetooth`, `health`, `sound`, `websocket`, and more |
| **Shortcuts / Automation** | App Intents, run script, run clipboard code, save text as script, query run status/output, stop run, x-callback-url |
| **Settings / Security / Personalization** | AI settings, appearance, editor, console, widgets, privacy, app lock, Keychain, app icons, BYOK, Premium, donation benefits, help and feedback |
| **Supporting Modules** | Share Extension import, SQLite browser, developer docs center, AgentSkillsV2 skill system |

---

## Local Runtime

PythonIDE includes a local Python runtime designed for iOS:

| Runtime area | Details |
|---|---|
| **Python** | Python 3.13 local execution with standard library support |
| **JavaScript** | JavaScriptCore execution for `.js` workflows |
| **HTML** | WKWebView preview for HTML files and local assets |
| **Console** | Interactive input, ANSI/Rich output, media previews, error jump |
| **Packages** | Built-in packages, C extensions, pure Python wheels, Wheel import, PyPI search/install |

The runtime is the foundation. The larger goal is to let scripts continue into Agent tasks, widgets, MiniApps, automation, remote workflows, and shared community scripts.

---

## Documentation

Detailed API references and implementation guides live in the repository docs. Start here:

| Topic | Link |
|---|---|
| Developer Docs Site | [docs/](docs/) |
| AppUI / MiniApp | [appui.md](pythonide/Docs/appui.md), [miniapp-appui-api-index.md](pythonide/Docs/miniapp-appui-api-index.md), [miniapp-choose-runtime.md](pythonide/Docs/miniapp-choose-runtime.md) |
| Widget API | [widget-api-index.md](pythonide/Docs/widget-api-index.md), [widget-api-reference.md](pythonide/Docs/widget-api-reference.md), [widget-quickstart-publish.md](pythonide/Docs/widget-quickstart-publish.md) |
| iOS Native Modules | [modules-index.md](pythonide/Docs/modules-index.md), [ios-native.md](pythonide/Docs/ios-native.md) |
| Shortcuts / Automation | [shortcuts-guide.md](pythonide/Docs/shortcuts-guide.md), [shortcuts-module.md](pythonide/Docs/shortcuts-module.md) |
| JavaScript Runtime | [js-api.md](pythonide/Docs/js-api.md) |
| C Extensions | [c-extensions-module.md](pythonide/Docs/c-extensions-module.md) |
| Agent Skills | [AgentSkillsV2/](AgentSkillsV2/) |
| Community API | [community-function/API.md](community-function/API.md) |

---

## Install

<p align="center">
  <a href="https://apps.apple.com/app/id6753987304">
    <img src="https://img.shields.io/badge/App%20Store-Download-black?style=for-the-badge&logo=apple" alt="Download on App Store" height="44" />
  </a>
</p>

| Requirement | Detail |
|---|---|
| **System** | iOS 16.2 or later |
| **Device** | iPhone and iPad |
| **Distribution** | App Store |
| **AI usage** | Platform quota and BYOK are supported |

---

## Screenshots

For current screenshots and feature previews, visit the App Store page:

[View PythonIDE on the App Store](https://apps.apple.com/app/id6753987304)

Recommended repository screenshot set:

| Screenshot | Purpose |
|---|---|
| Home / Files | Show file management and project entry |
| Editor + Console | Show coding, execution, Rich output, error jump |
| AI Agent | Show project task execution and diff/apply flow |
| Widget Studio | Show script result turning into widgets |
| MiniApp | Show script tool with UI |
| SSH / Git | Show real project and server workflow |
| Community | Show script discovery, import, and running |

---

## Community & Feedback

| Channel | Link |
|---|---|
| Telegram | [iOS 端 Py 编程 IDE](https://t.me/pythonzwb) |
| Feature requests | [GitHub Discussions](https://github.com/jinwandalaohu66/PythonIDE-iOS/discussions) |
| Issues | [GitHub Issues](https://github.com/jinwandalaohu66/PythonIDE-iOS/issues) |
| App Store | [PythonIDE on App Store](https://apps.apple.com/app/id6753987304) |

---

## Support Development

If PythonIDE is useful to you:

- Star this repository so more developers can discover the project.
- Leave an App Store review.
- Send feedback from the app so issues can be reproduced with the right context.
- Support development through the in-app donation / Premium options.

---

<p align="center">
  <strong>PythonIDE</strong><br/>
  Mobile Python workspace for scripts, Agent workflows, widgets, MiniApps, servers, Git, and community scripts.
</p>
