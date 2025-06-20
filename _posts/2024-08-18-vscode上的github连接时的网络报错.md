---
layout: post
title: "vscode上的github连接时的网络报错"
date: 2024-08-18 14:45:13 +0800
categories: [零碎问题及解决]
tags: [vscode, github, 端口代理, 网络超时]
---

在 vscode 上向 GitHub 拉取或推送时，若发生以下报错

```bash
OpenSSL SSL_connect: Connection was reset in connection to github.com:443
```

则是 git 请求时端口出现问题。
可以先用命令

```bash
git config --global --get http.proxy
git config --global --get https.proxy
```

查看自己的通过 http 和 https 发出 git 请求时是从哪个端口发出的，如果按上面的报错码，则应该是 443 端口。

再在本地计算机到`设置->使用代理服务器`，查看自己的代理端口，如果是使用 clash for windows 代理，那么代理端口应该是 7890，在 vscode 终端输入命令

```zsh
git config --global http.proxy 127.0.0.1:7890
git config --global https.proxy 127.0.0.1:7890
```

修改 git 访问端口成功，此时你的 git 访问就可以通过代理来访问了，不再发生网络问题了。

对了，注意 clash 的`rule`里面，`微软服务`的节点不是`direct`。
