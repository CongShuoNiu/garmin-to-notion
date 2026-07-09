# Garmin to Notion Context

This context defines the project-specific language used in the documentation. It keeps the English and Chinese wording aligned for Garmin-to-Notion synchronization concepts.

## Language

**Garmin Activity / Garmin 活动**:
A workout or activity record pulled from Garmin Connect and synchronized into Notion.
_Avoid_: Workout only, exercise only, Garmin data

**Activity Type / Activity Type**:
The top-level Notion select value used by the sync workflow to query and write Garmin activities. For unmapped Garmin activity types, the workflow uses Garmin's formatted activity type directly, such as `Tennis V2`.
_Avoid_: Subactivity Type, Activity Name

**Subactivity Type / Subactivity Type**:
The secondary Notion select value used to preserve a more specific Garmin activity subtype. It may match Activity Type when Garmin only provides one useful type value.
_Avoid_: Activity Type, Activity Name

**Activity Name / Activity Name**:
The human-readable title of one Garmin activity instance in Notion, such as `Tennis`.
_Avoid_: Activity Type, Subactivity Type

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

**GitHub Actions Secret / GitHub Actions Secret**:
A sensitive protected configuration value stored in GitHub Actions secrets, such as `NOTION_TOKEN` or `GARMIN_AUTH_TOKEN`.
_Avoid_: Database ID, public config value, variable

**GitHub Actions Variable / GitHub Actions Variable**:
A non-sensitive workflow configuration value stored in GitHub Actions variables, such as Notion database IDs.
_Avoid_: Secret, token

**Notion Integration / Notion integration**:
The Notion API connection that grants this project access to selected Notion databases.
_Avoid_: Notion app, Notion plugin

**Notion Integration Token / Notion integration token**:
The `ntn_...` secret value that authenticates the Notion integration.
_Avoid_: Database ID, page ID

**Notion Database / Notion 数据库**:
The target Notion database that receives synchronized Garmin data.
_Avoid_: Table only, page only

**Notion Database ID / Notion database ID**:
The ID copied from a Notion database URL before the `?v=` view parameter.
_Avoid_: `ntn_...` token, view ID, connection ID
