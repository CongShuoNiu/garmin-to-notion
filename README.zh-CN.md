# Garmin 到 Notion 集成 :watch:

本项目会将你的 Garmin 活动和个人记录连接到 Notion 数据库，让你可以在一个地方持续追踪自己的运动表现指标。

> [!IMPORTANT]
> **现有用户：** Garmin 于 2025 年 3 月加强了身份认证机制，导致此前的邮箱/密码登录流程失效。你需要将自己的 fork 同步到最新变更，并迁移到新的基于令牌的认证方式。操作说明请参阅 [README_AUTH_SETUP.zh-CN.md](README_AUTH_SETUP.zh-CN.md)。完成迁移后，可以移除 `GARMIN_EMAIL` 和 `GARMIN_PASSWORD` 这两个 secret。

## 功能 :sparkles:

  🔄 将 Garmin 活动实时自动同步到 Notion
  📊 追踪详细活动指标（距离、配速、心率）
  🎯 提取并追踪个人记录（最快 1 公里、最长骑行等）
  👣 可选的每日步数追踪
  😴 可选的睡眠数据追踪
  🤖 配置完成后即可零人工干预自动运行
  📱 兼容所有 Garmin 活动类型和设备
  🔧 设置简单，说明清晰，所需编码工作很少

## 前置条件 :hammer_and_wrench:

- 一个已开通 API 访问能力的 Notion 账号。
- 一个用于拉取活动数据的 Garmin Connect 账号。
- 如果你希望将 Peloton 训练同步到 Garmin，请参阅 [peloton-to-garmin](https://github.com/philosowaffle/peloton-to-garmin)。

## 快速开始 :dart:

你可以在我的 Notion 模板[这里](https://chloevoyer.notion.site/Set-up-Guide-17915ce7058880559a3ac9f8a0720046)查看详细的分步指南。

如果你是更熟悉技术配置的用户，可以按以下步骤设置该集成：

### 1. Fork 这个 GitHub 仓库

### 2. 复制我的 [Notion 模板](https://www.notion.so/templates/fitness-tracker-738)

* 保存你的 Activities 和 Personal Records 数据库 ID（步骤 4 会用到）
  * 可选：Daily Steps 数据库 ID
  * 查看 URL：`notion.so/username/[string-of-characters]`
  * 数据库 ID 是 `username/` 之后、`?v` 之前的全部内容

### 3. 创建 Notion 令牌

* 前往 [Notion Integrations](https://www.notion.so/profile/integrations)。
* [创建](https://developers.notion.com/docs/create-a-notion-integration)一个新的 integration，并复制 integration token。
* 将该 integration [分享](https://www.notion.so/help/add-and-manage-connections-with-the-api#enterprise-connection-settings)给 Notion 中的目标数据库。

### 4. 生成 Garmin 认证令牌

* 按照 [README_AUTH_SETUP.zh-CN.md](README_AUTH_SETUP.zh-CN.md) 中的说明生成并配置你的 `GARMIN_AUTH_TOKEN`。

### 5. 设置环境 Secret

* 需要定义的环境 secret：
  * `GARMIN_AUTH_TOKEN`（见步骤 4）
  * `NOTION_TOKEN`
  * `NOTION_DB_ID`
  * `NOTION_PR_DB_ID`
  * `NOTION_STEPS_DB_ID`（可选）
  * `NOTION_SLEEP_DB_ID`（可选）

### 6. 运行脚本（如果不使用自动化工作流）

* 运行 [garmin-activities.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/garmin-activities.py)，将你的 Garmin 活动同步到 Notion。

```shell
python garmin-activities.py
```

* 运行 [personal-records.py](https://github.com/chloevoyer/garmin-to-notion/blob/main/personal-records.py)，提取活动记录（例如最快跑步、最长骑行）。

```shell
python personal-records.py
```

## 示例配置 :pencil:

你可以通过修改环境变量和 Notion 数据库设置，让脚本适配自己的需求。

下面是我的 Notion 仪表盘截图：

![garmin-to-notion-template](https://github.com/user-attachments/assets/b37077cc-fe87-466f-9424-8ba9e4efa909)

我的 Notion 模板可免费使用，你可以在[这里](https://www.notion.so/templates/fitness-tracker-738)复制到自己的 Notion。

## 致谢 :raised_hands:

- 参考字典和示例可在 [cyberjunky/python-garminconnect](https://github.com/cyberjunky/python-garminconnect.git) 中找到。
- 本项目受 [n-kratz/garmin-notion](https://github.com/n-kratz/garmin-notion.git) 启发。

## 贡献 :handshake:

欢迎贡献！如果你发现 bug 或想添加功能，欢迎提交 issue 或 pull request。也非常感谢任何形式的资金支持 :blush:

<a href="https://www.buymeacoffee.com/cvoyer" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## :copyright: 许可证

本项目采用 MIT License 授权。更多详情请参阅 LICENSE 文件。
