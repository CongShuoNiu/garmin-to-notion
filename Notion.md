# Notion Setup Guide

Source Notion page: https://app.notion.com/p/Set-up-Guide-686d6fc9e3cb82d8a39501805a213752

This guide explains how to prepare Notion for the Garmin to Notion sync workflow. It keeps the English and Chinese instructions together so the GitHub repository remains usable even when the original Notion page is unavailable.

## 1. Duplicate the Notion Template

1. Open the Notion setup guide or the fitness tracker template linked from the project README.
2. Duplicate the template into your own Notion workspace.
3. Confirm that the duplicated workspace contains the databases you want to sync:
   - Activities
   - Personal Records
   - Daily Steps, optional
   - Sleep Data, optional

## 2. Create a Notion Integration

1. Open [Notion Integrations](https://www.notion.so/profile/integrations).
2. Create a new internal integration.
3. Copy the integration token.
4. Store it as the GitHub Actions secret `NOTION_TOKEN`.

## 3. Share Databases with the Integration

For each Notion database you want this project to write to:

1. Open the database in Notion.
2. Click **Share**.
3. Invite the integration you created.
4. Confirm that the integration has permission to read and update the database.

## 4. Collect Database IDs

Open each target database and copy its database ID from the URL.

Example URL:

```text
https://www.notion.so/workspace/1234567890abcdef1234567890abcdef?v=...
```

The database ID is the long string after the workspace name and before `?v`.

Configure these GitHub Actions variables or secrets. Database IDs are not sensitive, so repository variables are recommended. The workflow reads variables first and falls back to secrets.

| Secret | Required | Description |
| --- | --- | --- |
| `NOTION_DB_ID` | Yes | Activities database ID |
| `NOTION_PR_DB_ID` | Yes | Personal Records database ID |
| `NOTION_STEPS_DB_ID` | No | Daily Steps database ID |
| `NOTION_SLEEP_DB_ID` | No | Sleep Data database ID |

## 5. Generate the Garmin Token

For Garmin China accounts, use the token script from this fork. It sets `is_cn=True`.

```shell
uv run https://raw.githubusercontent.com/CongShuoNiu/garmin-to-notion/main/scripts/generate-garmin-token.py
```

Copy the full JSON token printed by the script and save it as the GitHub Actions secret `GARMIN_AUTH_TOKEN`.

If your Garmin account does not use two-factor authentication, press Enter when the script asks for `MFA code`.

## 6. Configure GitHub Actions Secrets and Variables

In your GitHub repository:

1. Go to **Settings**.
2. Open **Secrets and variables -> Actions**.
3. Add secrets for sensitive values:
   - `GARMIN_AUTH_TOKEN`
   - `NOTION_TOKEN`
4. Add variables for database IDs:
   - `NOTION_DB_ID`
   - `NOTION_PR_DB_ID`
5. Add optional variables if you use those databases:
   - `NOTION_STEPS_DB_ID`
   - `NOTION_SLEEP_DB_ID`

## 7. Run the Sync

You can run the GitHub Actions workflow manually if `workflow_dispatch` is enabled, or run the scripts locally:

```shell
python src/workflows/garmin-activities.py
python src/workflows/personal-records.py
python src/workflows/daily-steps.py
python src/workflows/sleep-data.py
```

## Troubleshooting

- `429` from Garmin usually means the current IP is rate limited. Stop retrying, disable VPN or proxy, and try a mobile hotspot.
- `401` usually means the Garmin token is invalid or expired. Generate a new `GARMIN_AUTH_TOKEN`.
- Missing Notion rows usually means the integration was not shared with the target database or the database ID secret is wrong.
- For Garmin China accounts, both token generation and runtime sync must use `is_cn=True`. This repository already sets it in the token script and shared Garmin client helper.

---

# Notion 设置指南

来源 Notion 页面：https://app.notion.com/p/Set-up-Guide-686d6fc9e3cb82d8a39501805a213752

本指南说明如何为 Garmin 到 Notion 同步工作流准备 Notion。这里把英文和中文说明放在同一个 GitHub 文件中，即使原始 Notion 页面暂时无法访问，也可以直接按仓库文档完成配置。

## 1. 复制 Notion 模板

1. 打开项目 README 中链接的 Notion 设置指南或 fitness tracker 模板。
2. 将模板复制到你自己的 Notion 工作区。
3. 确认复制后的工作区包含你需要同步的数据库：
   - Activities
   - Personal Records
   - Daily Steps，可选
   - Sleep Data，可选

## 2. 创建 Notion Integration

1. 打开 [Notion Integrations](https://www.notion.so/profile/integrations)。
2. 创建一个新的 internal integration。
3. 复制 integration token。
4. 将它保存为 GitHub Actions secret：`NOTION_TOKEN`。

## 3. 将数据库分享给 Integration

对每一个需要写入的 Notion 数据库执行以下操作：

1. 在 Notion 中打开该数据库。
2. 点击 **Share**。
3. 邀请你刚创建的 integration。
4. 确认 integration 拥有读取和更新该数据库的权限。

## 4. 收集数据库 ID

打开每一个目标数据库，并从 URL 中复制数据库 ID。

示例 URL：

```text
https://www.notion.so/workspace/1234567890abcdef1234567890abcdef?v=...
```

数据库 ID 是 workspace 名称之后、`?v` 之前的长字符串。

需要配置以下 GitHub Actions variables 或 secrets。数据库 ID 不属于敏感信息，推荐放到仓库 Variables。当前 workflow 会优先读取 Variables，再回退读取 Secrets。

| Secret | 是否必需 | 说明 |
| --- | --- | --- |
| `NOTION_DB_ID` | 是 | Activities 数据库 ID |
| `NOTION_PR_DB_ID` | 是 | Personal Records 数据库 ID |
| `NOTION_STEPS_DB_ID` | 否 | Daily Steps 数据库 ID |
| `NOTION_SLEEP_DB_ID` | 否 | Sleep Data 数据库 ID |

## 5. 生成 Garmin Token

如果你使用 Garmin 中国区账号，请使用当前 fork 中的 token 脚本。该脚本已经设置 `is_cn=True`。

```shell
uv run https://raw.githubusercontent.com/CongShuoNiu/garmin-to-notion/main/scripts/generate-garmin-token.py
```

复制脚本打印出的完整 JSON token，并保存为 GitHub Actions secret：`GARMIN_AUTH_TOKEN`。

如果 Garmin 账号没有开启双重认证，脚本提示 `MFA code` 时直接回车即可。

## 6. 配置 GitHub Actions Secrets 和 Variables

在你的 GitHub 仓库中：

1. 进入 **Settings**。
2. 打开 **Secrets and variables -> Actions**。
3. 将敏感值添加到 Secrets：
   - `GARMIN_AUTH_TOKEN`
   - `NOTION_TOKEN`
4. 将数据库 ID 添加到 Variables：
   - `NOTION_DB_ID`
   - `NOTION_PR_DB_ID`
5. 如果使用可选数据库，再添加 Variables：
   - `NOTION_STEPS_DB_ID`
   - `NOTION_SLEEP_DB_ID`

## 7. 运行同步

如果仓库启用了 `workflow_dispatch`，可以手动运行 GitHub Actions workflow；也可以在本地运行脚本：

```shell
python src/workflows/garmin-activities.py
python src/workflows/personal-records.py
python src/workflows/daily-steps.py
python src/workflows/sleep-data.py
```

## 常见问题

- Garmin 返回 `429` 通常表示当前 IP 被限流。停止连续重试，关闭 VPN 或代理，并尝试使用手机热点。
- `401` 通常表示 Garmin token 无效或过期。重新生成 `GARMIN_AUTH_TOKEN`。
- Notion 没有写入数据，通常是 integration 没有分享给目标数据库，或数据库 ID secret 配错。
- Garmin 中国区账号要求 token 生成和运行时同步都使用 `is_cn=True`。当前仓库已经在 token 脚本和统一 Garmin client helper 中完成设置。
