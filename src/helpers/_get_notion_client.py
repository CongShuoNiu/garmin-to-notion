import os
from dataclasses import dataclass

from notion_client import Client


@dataclass(frozen=True)
class NotionDatabases:
    activities: str
    personal_records: str
    sleep: str
    daily_steps: str


def get_notion_client() -> tuple[Client, NotionDatabases]:
    """初始化 Notion 客户端并校验数据库 secret 配置。"""
    print("Initializing Notion client...")

    notion_databases = NotionDatabases(
        activities=os.getenv("NOTION_DB_ID"),
        personal_records=os.getenv("NOTION_PR_DB_ID"),
        sleep=os.getenv("NOTION_SLEEP_DB_ID"),
        daily_steps=os.getenv("NOTION_STEPS_DB_ID"),
    )

    notion_token = os.getenv("NOTION_TOKEN")
    _validate_notion_configuration(notion_token, notion_databases)

    notion_client = Client(auth=notion_token)

    print("Notion client initialized.")

    return notion_client, notion_databases


def _validate_notion_configuration(notion_token: str | None, notion_databases: NotionDatabases) -> None:
    """在调用 Notion API 前发现 token 和 database ID 填反等配置错误。"""
    if not notion_token:
        raise ValueError("NOTION_TOKEN is required. It should be the Internal Integration Token.")

    required_database_ids = {
        "NOTION_DB_ID": notion_databases.activities,
        "NOTION_PR_DB_ID": notion_databases.personal_records,
    }
    optional_database_ids = {
        "NOTION_SLEEP_DB_ID": notion_databases.sleep,
        "NOTION_STEPS_DB_ID": notion_databases.daily_steps,
    }

    for secret_name, database_id in required_database_ids.items():
        _validate_required_database_id(secret_name, database_id)

    for secret_name, database_id in optional_database_ids.items():
        if database_id:
            _validate_database_id(secret_name, database_id)


def _validate_required_database_id(secret_name: str, database_id: str | None) -> None:
    """校验必填 Notion database ID 是否存在且不是 integration token。"""
    if not database_id:
        raise ValueError(f"{secret_name} is required. It should be a Notion database ID, not an integration token.")

    _validate_database_id(secret_name, database_id)


def _validate_database_id(secret_name: str, database_id: str) -> None:
    """校验 Notion database ID，避免把 ntn_ 开头的 token 填进 DB secret。"""
    if database_id.startswith("ntn_"):
        raise ValueError(
            f"{secret_name} is set to a Notion integration token. "
            f"Move this value to NOTION_TOKEN and set {secret_name} to the actual Notion database ID."
        )
