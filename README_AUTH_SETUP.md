# Step 4 — Generate a Garmin Authentication Token :key:

# 步骤 4 — 生成 Garmin 认证令牌 :key:

This is part of the [Getting Started](README.md#getting-started-dart) guide. You'll generate a token that proves to Garmin you are logged in. The workflow will reuse it automatically on every run without ever prompting for credentials again.

这是[快速开始](README.md#getting-started-dart)指南的一部分。你将生成一个令牌，用来向 Garmin 证明你已经登录。该工作流会在每次运行时自动复用这个令牌，不会再次要求你输入凭据。

## Prerequisites :hammer_and_wrench:

## 前置条件 :hammer_and_wrench:

* [`uv`](https://docs.astral.sh/uv/getting-started/installation/) installed on your machine.
* 你的机器上已安装 [`uv`](https://docs.astral.sh/uv/getting-started/installation/)。

## Generate the token :computer:

## 生成令牌 :computer:

Open a terminal and run the following command:

打开终端并运行以下命令：

```shell
uv run https://raw.githubusercontent.com/chloevoyer/garmin-to-notion/main/scripts/generate-garmin-token.py
```

You will be prompted for:

系统会提示你输入：

1. Your Garmin email
2. 你的 Garmin 邮箱
3. Your Garmin password (hidden while typing)
4. 你的 Garmin 密码（输入时会隐藏）
5. Your 2FA code, if applicable (from your authenticator app or SMS)
6. 你的双重认证验证码（如适用，来自认证器应用或短信）

Once complete, the script will print your token between two lines of `=` signs.

完成后，脚本会在两行 `=` 符号之间打印你的令牌。

**Copy the entire JSON block** — everything from the opening `{` to the closing `}`, inclusive.

**复制完整的 JSON 块**，也就是从开头的 `{` 到结尾的 `}`，包括这两个大括号本身。

> **Getting a 429 error?** Garmin blocks certain IP ranges (VPNs, corporate networks, some ISPs) on their login endpoint. If this happens, try
>
> **遇到 429 错误？** Garmin 会在登录端点屏蔽某些 IP 范围（VPN、公司网络、部分 ISP）。如果发生这种情况，可以尝试：
>
> * disabling your VPN.
> * 关闭 VPN。
> * running the command while connected to your phone's mobile hotspot.
> * 连接手机热点后再运行该命令。
>
> Once the token is generated, this no longer matters — the daily sync never re-authenticates from scratch.
>
> 令牌生成后，这个问题就不再重要，因为每日同步不会从头重新认证。

## Add the token to GitHub :lock:

## 将令牌添加到 GitHub :lock:

* Go to your fork of this repository on GitHub.
* 在 GitHub 上进入你 fork 的这个仓库。
* Click the **Settings** tab.
* 点击 **Settings** 选项卡。
* In the left sidebar, go to **Secrets and variables → Actions**.
* 在左侧边栏进入 **Secrets and variables → Actions**。
* Click **New repository secret**.
* 点击 **New repository secret**。
  * **Name:** `GARMIN_AUTH_TOKEN`
  * **Name：** `GARMIN_AUTH_TOKEN`
  * **Value:** paste the token you copied above
  * **Value：** 粘贴你上面复制的令牌
* Click **Add secret**.
* 点击 **Add secret**。

Once done, continue to [Step 5 — Set Environment Secrets](README.md#5-set-environment-secrets).

完成后，继续执行[步骤 5 — 设置环境 Secret](README.md#5-set-environment-secrets)。

## Token expiry :hourglass:

## 令牌过期 :hourglass:

The token refreshes itself automatically on each run. You should never need to repeat this process unless you change your Garmin password or explicitly revoke access from your Garmin account settings.

该令牌会在每次运行时自动刷新。除非你修改了 Garmin 密码，或在 Garmin 账号设置中明确撤销了访问权限，否则通常不需要重复此流程。

If the workflow suddenly fails with a **401 error**, this means Garmin has invalidated your session — most likely because you changed your Garmin password or Garmin detected unusual activity on your account. Simply repeat the steps above to generate a new token and update the secret.

如果工作流突然因 **401 错误**失败，说明 Garmin 已使你的会话失效，最可能的原因是你修改了 Garmin 密码，或 Garmin 检测到账号存在异常活动。只需重复上述步骤生成新令牌，并更新 secret 即可。
