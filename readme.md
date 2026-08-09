# 🔬 Numbered Image Utility (NIU) [Beta]

<div align="center">
  <p>一个轻量的编号图片管理与对比工具</p>
  <p>A lightweight tool for managing and comparing numbered image datasets.</p>
</div>

---
>开发模式 / Development Mode: Vibe Coding
>
>本项目与 Google/Gemma-4-26B-a4b（Q6_K）共同创作完成。
>This project was co-created with Google/Gemma-4-26B-a4b (Q6_K).
---

## 📖 项目简介 / Project Introduction

### 中文
**编号图片实用小工具** 是专为实验数据管理设计的轻量化工具。它解决了具有编号的图片查看、备注以及多图对比时的效率问题，支持通过系统化的图片编号以及标签 (Tag) 进行快速检索。通过自动化的缩略图同步技术，它能在保证对比选择界面极速预览的同时，最大限度地降低内存占用。

### English
**Numbered Image Utility** is a lightweight tool specifically designed for experimental data management. It solves efficiency issues in viewing, annotating, and comparing large sets of numbered images. It supports rapid searching via systematic numbering and custom tags. Through automated thumbnail synchronization, it provides lightning-fast previews during comparison while minimizing memory footprint.

---

## ✨ 核心功能 / Key Features

- **🌐 多语言与多项目 (Localization & Multi-Project)**
  - 支持一键在中英文环境下无缝切换。
  - 支持通过不同的项目进行隔离管理，实现多组实验数据并行处理。
  - *One-click switching between Chinese and English. Supports managing multiple independent projects simultaneously.*

- **🔍 灵活的信息管理 (Flexible Information Management)**
  - **极速检索**：支持通过文件名（编号）或标签进行精准搜索。
  - **在线编辑**：支持实时修改图片备注、生成日期及添加/删除标签。
  - *Fast searching via numbering or tags; supports real-time editing of notes, generation dates, and tags.*

- **⚡ 高性能同步引擎 (Smart Sync Engine)**
  - 基于文件系统监听，自动生成 WebP 格式缩略图。
  - 基于 `IntersectionObserver` 的按需加载技术，支持海量图片流畅滚动。
  - *Automatic WebP thumbnail generation via file system watching. Uses IntersectionObserver for seamless lazy loading.*

- **⇄ 对比模式 (Advanced Comparison Mode)**
  - 支持多图同时展示、自由缩放 (Zoom) 与平移 (Pan)，并支持锁定位置进行微调。
  - 支持拖拽式重新排序布局。
  - *Supports multi-image viewing, free zooming/panning, and image locking for precise adjustment. Includes drag-and-drop reordering.*

- **📊 批量数据管理 (Batch Data Management)**
  - 通过 Excel 或 CSV 文件快速导入/导出备注、日期与标签。
  - 支持选择性导出“内容为空”的行，方便针对性补全缺失信息。
  - 支持单独下载错误记录，无需手动筛选。
  - *Quickly import/export image notes, dates, and tags via Excel or CSV. Supports selective export of empty rows and downloading error logs for rapid correction.*

---

## 📏 编号图片命名规范 / Image Numbering Convention (Critical)

为了实现自动分组、快速搜索和高效排序，所有图片文件必须遵循以下命名协议。请务必严格遵守，否则功能将无法正常工作。

To enable automatic grouping, rapid searching, and efficient sorting, all image files **must** follow the naming protocol below. Failure to do so will result in broken functionality.

### 📐 格式定义 / Format Definition

文件名必须采用 **`[前缀]-[编号].[后缀]`** 的结构：
Filenames must follow the **`[Prefix]-[Sequence].[Extension]`** structure:

> **`Example: T001-01.jpg`**

### 🔍 规则详解 / Detailed Rules

1.  **分隔符 (Delimiter)**: 前缀与数字之间**必须**使用一个连字符 `-` 进行连接。
    The prefix and the sequence number **must** be separated by a single hyphen `-`.
2.  **前缀 (Prefix)**: 可以是任意字母数字组合（例如：`T`, `SampleA`, `Exp01`）。 前缀可以是由连字符 `-` 分隔的多段组合（例如：`Exp-A-B-01` 中的前缀是 `Exp-A-B`）。系统会将最后一个连字符之前的所有内容识别为该组的前缀，系统会根据这个前缀自动进行“分组”管理。
    The prefix can be any alphanumeric combination (e.g., `T`, `SampleA`, `Exp01`). The prefix can be a multi-segment string separated by hyphens (e.g., in `Exp-A-B-01`, the prefix is `Exp-A-B`).The system uses this prefix to automatically "group" your images.
3.  **编号 (Sequence)**: 连字符后的部分应为数字或序列号。
    The part after the hyphen should be a number or sequence identifier.
4.  **禁止特殊符号 (No Special Characters)**: 文件名中除了用于分隔的 `-` 之外，请勿使用空格、下划线 `_` 或其他特殊符号，以免影响搜索逻辑。
    Do not use spaces, underscores `_`, or other special characters in the filename, as they may interfere with the search and grouping logic.

### ✅ 正确 vs 错误示例 / Correct vs Incorrect Examples

| 类型 / Type | 文件名 / Filename | 结果 / Result |
| :--- | :--- | :--- |
| **✅ 正确 (Correct)** | `T001-01.jpg` | 识别为前缀 `T001`，编号 `01` ✅ |
| **✅ 正确 (Correct)** | `SampleA-123.png` | 识别为前缀 `SampleA`，编号 `123` ✅ |
| **✅ 正确 (Correct)** | `EXP-A-01.png` | 识别为前缀 `EXP-A`，编号 `01` ✅ |
| **❌ 错误 (Incorrect)** | `T001_01.jpg` | 缺少分隔符 `-` 导致无法分组 ❌ |
| **❌ 错误 (Incorrect)** | `T001 01.jpg` | 使用了空格，会导致搜索失效 ❌ |
| **❌ 错误 (Incorrect)**| `T001.jpg` | 缺少编号部分，无法进行排序 ❌ |

> [!CAUTION]
> ### ⚠️ 重要警告 / CRITICAL WARNING !!!
> 
> **本程序将图片文件名视为唯一的识别编码。一旦您在文件系统中手动更改了文件名，所有原标题下的数据（备注、日期、标签）都【不会】自动迁移至新名称下！请务必在放入 `images/` 文件夹前核对好文件名，并养成定期备份数据的习惯。**
> 
> *This utility treats filenames as the unique identifiers. If you rename a file in your file system, all associated metadata (notes, dates, tags) will **NOT** be automatically migrated to the new filename! Please double-check your filenames before placing them into the `images/` folder and always keep regular backups of your data.*

---

## 📂 多项目并行管理说明 / Notes for Multi-Project Management (Advanced)

如果你有多个不同的实验任务需要同时进行，你可以为每个任务运行一个独立的实例（程序副本）。系统会自动为每个项目创建独立的文件夹结构和数据库，实现数据的物理隔离。

If you need to manage multiple experimental tasks simultaneously, you can run independent instances for each. The system will automatically create separate folder structures and databases for each project, ensuring complete data isolation.

### 如何操作 / How to use:

通过在启动命令中指定不同的 `--project` 名称和可用的 `--port` 端口，即可实现并行运行：
Run different projects in parallel by specifying unique `--project` names and available `--port` numbers:


# 实例 1 (Instance 1):
python app.py --project experiment_A --port 5001

# 实例 2 (Instance 2 - 在另一个终端窗口运行):
python app.py --project experiment_B --port 5002


项目 A 的所有数据将存储在 projects/experiment_A/ 下。
项目 B 的所有数据将存储在 projects/experiment_B/ 下。
Data for Project A will be stored in projects/experiment_A/, and Project B in projects/experiment_B/.

---

### 📥 数据准备 / Data Preparation
在使用软件前，请按照以下目录结构放置您的图片：
Before using the software, please organize your images according to the following structure:
```
projects/
└── [your_project_name]/
    └── images/  <-- 📸 请把图片放在这里 (Place images here)
        ├── T001-01.jpg
        ├── T001-02.jpg
        └── ...
```

**重要提示**：请将您的图片文件放入项目文件夹下的 `images/` 子目录中（例如：`projects/project_name/images/`），程序才能正确识别并加载它们。如果想删除图片，也直接从此文件夹中删除，请注意数据备份！

***Important***: Please place your image files into the `images/` subdirectory of your project folder (e.g., `projects/project_name/images/`) so that the system can detect and load them correctly.To delete images, simply remove them from this folder. Please ensure you have a data backup!


---

## ⚠️ 使用限制与免责声明 / Limitations & Disclaimer

> [!IMPORTANT]
> **本项目目前处于 Beta 测试阶段，采用 "Vibe Coding" (快速原型开发) 模式构建。**
> 
> ### 中文
> 本软件旨在提供快速的个人实验数据处理方案，并非工业级生产环境工具。为了保证运行稳定性，建议遵循以下指导：
> 1. **图片大小**：建议单个图片文件控制在 **50MB** 以内。
> 2. **数据集规模**：建议单项目图片数量保持在 **10,000 张** 以内。
> 3. **支持格式**：目前支持的图片格式为：**PNG, JPG, JPEG, WEBP**（不支持 HEIC 等格式）。
> 4. **编号规则**：图片应采用“字母数字组合-数字”的命名结构（例如 `T001-01.jpg`），前缀可扩展，但必须以 `-` 连接数字且不能包含特殊符号。
> 5. **数据备份**：请务必及时进行源图片备份，**不得将本软件文件夹作为唯一的存储场所**。本软件不承担任何数据丢失的责任。
> ⚠️ **提示**：本项目代码由 AI 辅助生成，使用者请自行评估其质量与安全性。

> [!IMPORTANT]
> **This project is currently in its "Beta" stage and was developed using a "Vibe Coding" (Rapid Prototyping) approach.**
> 
> ### English
> This software is designed for personal rapid experimental data processing and is not intended for mission-critical production environments. For optimal stability, please follow these guidelines:
> 1. **Image Size**: It is recommended that individual images be kept under **50MB**.
> 2. **Dataset Scale**: It is recommended to keep the number of images per project under **10,000**.
> 3. **Supported Formats**: Currently supports **PNG, JPG, JPEG, and WEBP** (HEIC and others are not supported).
> 4. **Naming Convention**: Filenames should follow an "alphanumeric-number" structure (e.g., `T001-01.jpg`). The prefix is extensible but must be separated from the number by a hyphen (`-`) and should not contain special symbols.
> 5. **Data Backup**: Always maintain backups of your original images. **Do not use this software's directory as your sole storage medium.** The author is not responsible for any data loss.
> ⚠️ **Notice**: This project's code was AI-assisted. Users are advised to review and test the code before use.

---

## 🚀 快速开始 / Getting Started

### 1. 环境要求 / Prerequisites
- Python 3.8+
- `pip install flask pandas openpyxl watchdog Pillow python-dotenv`

### 2. 安装与运行 / Installation & Running

#### **第一步：克隆仓库 (Clone the repo)**
```bash
git clone https://github.com/nqy-exp/Numbered-Image-Utility.git
cd Numbered-Image-Utility
```

#### **第二步：设置虚拟环境 (Setup Virtual Environment - Recommended)**
*建议使用虚拟环境以隔离依赖。 / Highly recommended to use a venv to isolate dependencies.*

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **第三步：安装依赖 (Install Dependencies)**
```bash
pip install -r requirements.txt
```

#### **第四步：安全配置 (Security Configuration)**
在项目根目录下手动创建一个名为 `.env` 的文件，并填入以下内容（请自行设置一个随机字符串）：
*Create a `.env` file in the project root and add the following (use your own random string):*

```text
SECRET_KEY=your_random_secret_string_here
```

#### **第五步：运行程序 (Run the app)**
```bash
# 指定项目名称和端口 (Specify project name and port)
python app.py --project my_project --port 5001
```

*(多个项目可以分配不同端口并行运行 / You can run multiple projects in parallel by assigning different ports.)*

#### **第六步：放入图片开始使用 Place image files and start using **
访问 http://127.0.0.1:5001 ，或者是其他设定端口，然后开始使用。
*Go to http://127.0.0.1:5001 or other settled port, then begin to use.*

---
### 🚀 快速体验 / Quick Demo
配有demo演示项目，直接运行以下命令，即可进入带有预置演示数据的项目进行体验：
*A demo project is included. Simply run the following command to launch a project preloaded with demo data for hands-on experience:*

```bash
python app.py --project demo_project --port 5001
```

然后访问 http://127.0.0.1:5001，你就能立即看到完整的管理效果！
*Then go to http://127.0.0.1:5001 to instantly see the complete management system at work!*

---

### 📖 在线交互式指南与演示 / Online Interactive Manual & Demo

> [!TIP]
> **想要更直观地了解如何使用、查看操作截图或常见问题？请点击下方链接：**
> *For a intuitive guide, including screenshots and FAQ, please visit:*
> > [!NOTE]
> **在线交互式指南正在建设中... / Online Interactive Manual is under construction.**
> 
> 一旦完成，您可以通过下方链接查看详细教程与常见问题：
> Once completed, you can access detailed tutorials and FAQ via the link below:
> 👉 **[点击这里查看使用说明/Click Here to Visit the User Guide](https://nqy-exp.github.io/niu/)**


---

## 🤝 贡献与衍生 / Contributing & Forking

本项目采用 **MIT License** 开源。

由于本项目目前定位为个人实验原型，为了保持代码的纯粹性与稳定性，**我不接受直接的 Pull Requests (PR)**。

如果你有了改进想法，或者想基于本项目开发自己的版本，欢迎通过以下方式进行：
1. **Fork 本仓库**：点击 GitHub 顶部的 "Fork" 按钮，将项目复制到你自己的账号下。
2. **自由开发**：你可以随意修改代码、添加功能或进行二次开发，并发布你自己的版本。

这种方式能让每个人都拥有完全的控制权，同时也避免了合并代码带来的复杂性。欢迎大家通过 Fork 的方式来延续这个项目的生命力！

---

This project is open-sourced under the **MIT License**. 

As this is a personal experimental prototype, **I do not accept direct Pull Requests (PRs)**. This allows me to maintain the core stability and original design of the tool.

If you find a bug, have an improvement idea, or want to build your own version based on this project, please feel free to:
1. **Fork this repository**: Click the "Fork" button at the top of this page to create your own copy.
2. **Develop independently**: You are free to modify the code, add features, or even create a completely new product from this base.

This approach empowers everyone to have full control over their own versions while keeping the original project clean and lightweight. I welcome everyone to keep the spirit of this tool alive through forking!

---

## 💬 反馈与沟通 / Feedback & Communication

本项目由个人开发，目前处于实验阶段。我非常欢迎大家提出改进建议或报告 Bug，但由于个人精力有限且倾向于异步沟通，请遵循以下方式：

This project is an experimental-stage tool. I welcome all feedback, bug reports, and suggestions for improvement. To keep communication efficient and non-intrusitive, please follow these guidelines:

1. **遇到 Bug 或建议？请使用 Issues** 
   请不要直接提交 Pull Request (PR)，也不要在社交媒体上私信我。请直接在 GitHub 的 **[Issues]** 页面创建一个新的 Issue，描述清楚你遇到的问题或想法。我会定期查看并进行处理。
   **Found a bug or have an idea?** Please do not submit a Pull Request directly. Instead, please open a new **[Issue]** on GitHub to describe the problem or your suggestion. This allows me to review it at my own pace.

2. **关于代码改进 (Discussion over PRs)**
   如果你有更高级的方案或优化建议，请先在 Issue 中进行讨论。如果我觉得可行，我会邀请你进一步探讨；如果我决定采用，我会参考你的思路进行实现。
   **Suggestions for improvements:** If you have a more advanced implementation or optimization idea, please start a discussion in an Issue first. I will review it and may implement it if it aligns with the project's direction.

3. **关于交流方式 (Communication Style)**
   我更倾向于通过 GitHub Issues 进行异步交流，不接受即时聊天。可以通过邮件联系我。感谢你的理解与支持！
   **Please note:** I prefer asynchronous communication via GitHub Issues rather than real-time chat. Also can reach out via email. Thank you for understanding!

   📧 **nqy.pro@outlook.com**

---

> I genuinely believe that AI represents a convergence of humanity's collective intelligence. So in a sense, this project was born from collaboration with the wisdom of all.
>
> 我真诚地认为，AI 是人类集体智慧的凝聚。因此这个项目，某种意义上也是与全人类的智慧合作而生。

<div align="right">
  <i>Created by Niu Qiyue</i>
</div>
---
