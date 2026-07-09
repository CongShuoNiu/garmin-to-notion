[![Sync Garmin to Notion](https://github.com/chloevoyer/garmin-to-notion/actions/workflows/sync_garmin_to_notion.yml/badge.svg?branch=main)](https://github.com/chloevoyer/garmin-to-notion/actions/workflows/sync_garmin_to_notion.yml)

# Garmin to Notion Integration :watch:

# Garmin 到 Notion 集成 :watch:

This project connects your Garmin activities and personal records to your Notion database, allowing you to keep track of your performance metrics in one place.

本项目会将你的 Garmin 活动和个人记录连接到 Notion 数据库，让你可以在一个地方持续追踪自己的运动表现指标。

> [!IMPORTANT]
> **Existing users:** Garmin tightened their authentication in March 2025, breaking the previous email/password login flow. You will need to sync your fork with the latest changes and migrate to the new token-based authentication. See [README_AUTH_SETUP.md](README_AUTH_SETUP.md) for instructions. Your `GARMIN_EMAIL` and `GARMIN_PASSWORD` secrets can be removed once done.
>
> **现有用户：** Garmin 于 2025 年 3 月加强了身份认证机制，导致此前的邮箱/密码登录流程失效。你需要将自己的 fork 同步到最新变更，并迁移到新的基于令牌的认证方式。操作说明请参阅 [README_AUTH_SETUP.md](README_AUTH_SETUP.md)。完成迁移后，可以移除 `GARMIN_EMAIL` 和 `GARMIN_PASSWORD` 这两个 secret。

## Features :sparkles:

## 功能 :sparkles:

* 🔄 Automatically sync Garmin activities to Notion in real time
* 🔄 将 Garmin 活动实时自动同步到 Notion
* 📊 Track detailed activity metrics (distance, pace, heart rate)
* 📊 追踪详细活动指标（距离、配速、心率）
* 🎯 Extract and track personal records (fastest 1K, longest ride)
* 🎯 提取并追踪个人记录（最快 1 公里、最长骑行等）
* 👣 Optional daily steps tracker
* 👣 可选的每日步数追踪
* 😴 Optional sleep data tracker
* 😴 可选的睡眠数据追踪
* 🤖 Zero-touch automation once configured
* 🤖 配置完成后即可零人工干预自动运行
* 📱 Compatible with all Garmin activities and devices
* 📱 兼容所有 Garmin 活动类型和设备
* 🔧 Easy setup with clear instructions and minimal coding required
* 🔧 设置简单，说明清晰，所需编码工作很少

## Prerequisites :hammer_and_wrench:

## 前置条件 :hammer_and_wrench:

* A Notion account with API access.
* 一个已开通 API 访问能力的 Notion 账号。
* A Garmin Connect account to pull activity data.
* 一个用于拉取活动数据的 Garmin Connect 账号。
* If you wish to sync your Peloton workouts with Garmin, see [peloton-to-garmin](https://github.com/philosowaffle/peloton-to-garmin).
* 如果你希望将 Peloton 训练同步到 Garmin，请参阅 [peloton-to-garmin](https://github.com/philosowaffle/peloton-to-garmin)。

## Getting Started :dart:

## 快速开始 :dart:

A detailed step-by-step guide is provided on my Notion template [here](https://chloevoyer.notion.site/Set-up-Guide-17915ce7058880559a3ac9f8a0720046).

你可以在我的 Notion 模板[这里](https://chloevoyer.notion.site/Set-up-Guide-17915ce7058880559a3ac9f8a0720046)查看详细的分步指南。

For more advanced users, follow these steps to set up the integration:

如果你是更熟悉技术配置的用户，可以按以下步骤设置该集成：

### 1. Fork this GitHub Repository

### 1. Fork 这个 GitHub 仓库

### 2. Duplicate my [Notion Template](https://www.notion.so/templates/fitness-tracker-738)

### 2. 复制我的 [Notion 模板](https://www.notion.so/templates/fitness-tracker-738)

* Save your Activities and Personal Records database ID (you will need it for step 4).
* 保存你的 Activities 和 Personal Records 数据库 ID（步骤 4 会用到）。
* Optional: Daily Steps database ID.
* 可选：Daily Steps 数据库 ID。
* Look at the URL: `notion.so/username/[string-of-characters]`.
* 查看 URL：`notion.so/username/[string-of-characters]`。
* The database ID is everything after your `username/` and before `?v`.
* 数据库 ID 是 `username/` 之后、`?v` 之前的全部内容。

### 3. Create Notion Token

### 3. 创建 Notion 令牌

* Go to [Notion Integrations](https://www.notion.so/profile/integrations).
* 前往 [Notion Integrations](https://www.notion.so/profile/integrations)。
* [Create](https://developers.notion.com/docs/create-a-notion-integration) a new integration and copy the integration token.
* [创建](https://developers.notion.com/docs/create-a-notion-integration)一个新的 integration，并复制 integration token。
* [Share](https://www.notion.so/help/add-and-manage-connections-with-the-api#enterprise-connection-settings) the integration with the target database in Notion.
* 将该 integration [分享](https://www.notion.so/help/add-and-manage-connections-with-the-api#enterprise-connection-settings)给 Notion 中的目标数据库。

### 4. Generate a Garmin Authentication Token

### 4. 生成 Garmin 认证令牌

* Follow the instructions in [README_AUTH_SETUP.md](README_AUTH_SETUP.md) to generate and configure your `GARMIN_AUTH_TOKEN`.
* 按照 [README_AUTH_SETUP.md](README_AUTH_SETUP.md) 中的说明生成并配置你的 `GARMIN_AUTH_TOKEN`。

### 5. Set Environment Secrets

### 5. 设置环境 Secret

* Environment secrets to define:
* 需要定义的环境 secret：
  * `GARMIN_AUTH_TOKEN` (see step 4)
  * `GARMIN_AUTH_TOKEN`（见步骤 4）
  * `NOTION_TOKEN`
  * `NOTION_TOKEN`
  * `NOTION_DB_ID`
  * `NOTION_DB_ID`
  * `NOTION_PR_DB_ID`
  * `NOTION_PR_DB_ID`
  * `NOTION_STEPS_DB_ID` (optional)
  * `NOTION_STEPS_DB_ID`（可选）
  * `NOTION_SLEEP_DB_ID` (optional)
  * `NOTION_SLEEP_DB_ID`（可选）

### 6. Run Scripts (if not using automatic workflow)

### 6. 运行脚本（如果不使用自动化工作流）

* Run [garmin-activities.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/garmin-activities.py) to sync your Garmin activities to Notion.
* 运行 [garmin-activities.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/garmin-activities.py)，将你的 Garmin 活动同步到 Notion。

```shell
python garmin-activities.py
```

* Run [person-records.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/personal-records.py) to extract activity records (e.g., fastest run, longest ride).
* 运行 [person-records.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/personal-records.py)，提取活动记录（例如最快跑步、最长骑行）。

```shell
python personal-records.py
```

## Example Configuration :pencil:

## 示例配置 :pencil:

You can customize the scripts to fit your needs by modifying environment variables and Notion database settings.

你可以通过修改环境变量和 Notion 数据库设置，让脚本适配自己的需求。

Here is a screenshot of what my Notion dashboard looks like:

下面是我的 Notion 仪表盘截图：

![garmin-to-notion-template](https://github.com/user-attachments/assets/b37077cc-fe87-466f-9424-8ba9e4efa909)

My Notion template is available for free and can be duplicated to your Notion [here](https://www.notion.so/templates/fitness-tracker-738).

我的 Notion 模板可免费使用，你可以在[这里](https://www.notion.so/templates/fitness-tracker-738)复制到自己的 Notion。

## Acknowledgements :raised_hands:

## 致谢 :raised_hands:

* Reference dictionary and examples can be found in [cyberjunky/python-garminconnect](https://github.com/cyberjunky/python-garminconnect.git).
* 参考字典和示例可在 [cyberjunky/python-garminconnect](https://github.com/cyberjunky/python-garminconnect.git) 中找到。
* This project was inspired by [n-kratz/garmin-notion](https://github.com/n-kratz/garmin-notion.git).
* 本项目受 [n-kratz/garmin-notion](https://github.com/n-kratz/garmin-notion.git) 启发。

## Contributing :handshake:

## 贡献 :handshake:

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request. Financial contributions are also greatly appreciated :blush:

欢迎贡献！如果你发现 bug 或想添加功能，欢迎提交 issue 或 pull request。也非常感谢任何形式的资金支持 :blush:

<a href="https://www.buymeacoffee.com/cvoyer" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## :copyright: License

## :copyright: 许可证

This project is licensed under the MIT License. See the LICENSE file for more details.

本项目采用 MIT License 授权。更多详情请参阅 LICENSE 文件。
