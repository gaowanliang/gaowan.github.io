---
title: 使用wget和caddy等简单快速的转移服务器之间的文件
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/photo_2021-02-23_00-04-19.jpg'
cover: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/photo_2021-02-23_00-04-19.jpg'
date: 2021-02-23 00:01:03
tags:
categories:
---

主要命令
```bash
echo "XXX.XX {
    root * /home/xxx
    file_server browse
}" >> /usr/local/caddy/Caddyfile
```
```bash
wget -r -np -nH -R index.html -L -N --no-use-server-timestamps https://XXX.XX
```
可以搭配cloudflare加速转移