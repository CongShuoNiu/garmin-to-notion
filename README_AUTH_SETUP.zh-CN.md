# 步骤 4 — 生成 Garmin 认证令牌 :key:

这是[快速开始](README.zh-CN.md#快速开始-dart)指南的一部分。你将生成一个令牌，用来向 Garmin 证明你已经登录。该工作流会在每次运行时自动复用这个令牌，不会再次要求你输入凭据。

## 前置条件 :hammer_and_wrench:

* 你的机器上已安装 [`uv`](https://docs.astral.sh/uv/getting-started/installation/)。

## 生成令牌 :computer:

打开终端并运行以下命令：

```shell
uv run https://raw.githubusercontent.com/chloevoyer/garmin-to-notion/main/scripts/generate-garmin-token.py
```

系统会提示你输入：

1. 你的 Garmin 邮箱
2. 你的 Garmin 密码（输入时会隐藏）
3. 你的双重认证验证码（如适用，来自认证器应用或短信）

完成后，脚本会在两行 `=` 符号之间打印你的令牌。
**复制完整的 JSON 块**，也就是从开头的 `{` 到结尾的 `}`，包括这两个大括号本身。

> **遇到 429 错误？** Garmin 会在登录端点屏蔽某些 IP 范围（VPN、公司网络、部分 ISP）。如果发生这种情况，可以尝试：
>
> * 关闭 VPN。
> * 连接手机热点后再运行该命令。
>
> 令牌生成后，这个问题就不再重要，因为每日同步不会从头重新认证。

## 将令牌添加到 GitHub :lock:

* 在 GitHub 上进入你 fork 的这个仓库
* 点击 **Settings** 选项卡
* 在左侧边栏进入 **Secrets and variables → Actions**
* 点击 **New repository secret**
  * **Name：** `GARMIN_AUTH_TOKEN`
  * **Value：** 粘贴你上面复制的令牌
* 点击 **Add secret**

完成后，继续执行[步骤 5 — 设置环境 Secret](README.zh-CN.md#5-设置环境-secret)。

## 令牌过期 :hourglass:

该令牌会在每次运行时自动刷新。除非你修改了 Garmin 密码，或在 Garmin 账号设置中明确撤销了访问权限，否则通常不需要重复此流程。

如果工作流突然因 **401 错误**失败，说明 Garmin 已使你的会话失效，最可能的原因是你修改了 Garmin 密码，或 Garmin 检测到账号存在异常活动。只需重复上述步骤生成新令牌，并更新 secret 即可。
