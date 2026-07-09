# Garmin to Notion Context

This context defines the project-specific language used in the documentation. It keeps the English and Chinese wording aligned for Garmin-to-Notion synchronization concepts.

## Language

**Garmin Activity / Garmin 活动**:
A workout or activity record pulled from Garmin Connect and synchronized into Notion.
_Avoid_: Workout only, exercise only, Garmin data

**Personal Record / 个人记录**:
A best-performance result extracted from Garmin activity data, such as fastest 1K or longest ride.
_Avoid_: PR only, achievement, milestone

**Daily Steps / 每日步数**:
An optional daily step count dataset that can be synchronized into a Notion database.
_Avoid_: Steps only, pedometer data

**Sleep Data / 睡眠数据**:
An optional sleep dataset from Garmin that can be synchronized into a Notion database.
_Avoid_: Sleep tracker, sleep metrics only

**Garmin Authentication Token / Garmin 认证令牌**:
A token generated after Garmin login that lets the workflow reuse an authenticated session.
_Avoid_: Password, credential, auth JSON

**Environment Secret / 环境 Secret**:
A protected configuration value stored in GitHub Actions secrets and read by the sync workflow.
_Avoid_: Environment variable only, config value

**Notion Integration / Notion integration**:
The Notion API connection that grants this project access to selected Notion databases.
_Avoid_: Notion app, Notion plugin

**Notion Database / Notion 数据库**:
The target Notion database that receives synchronized Garmin data.
_Avoid_: Table only, page only
