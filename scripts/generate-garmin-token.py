# /// script
# requires-python = ">=3.12"
# dependencies = ["garminconnect>=0.3.3"]
# ///
import getpass
import pathlib

from garminconnect import Garmin

# 该脚本只用于首次生成 GARMIN_AUTH_TOKEN；日常同步会复用生成后的 token。
client = Garmin(
    input("Garmin email: "),
    getpass.getpass("Garmin password: "),
    # 中国区 Garmin 账号需要使用 Garmin China 登录端点生成 token。
    is_cn=True,
    # 如果 Garmin 账号没有开启双重认证，看到 MFA code 提示时直接回车即可。
    prompt_mfa=lambda: input("MFA code: "),
)
client.login("~/.garminconnect")

# garminconnect 会把登录后的 token 写入 ~/.garminconnect/garmin_tokens.json。
token = pathlib.Path.home().joinpath(".garminconnect", "garmin_tokens.json").read_text()

print()
print("=" * 60)
print("SUCCESS! Copy everything between the lines below")
print("(the whole block, starting and ending with curly braces)")
print("=" * 60)
print(token)
print("=" * 60)
