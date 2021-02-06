---
title: Debian系统安装Swap虚拟内存设置
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/acv.jpg
'
date: 2020-05-16 20:31:37
tags: Linux
categories: 虚拟内存
---
我玩的服务器大多数内存比较小，有的时候执行一些任务会搞得 out of memory ，这个时候就需要设置虚拟内存，最好的方法就是用萌鼠大佬的一键脚本。

> wget https://www.moerats.com/usr/shell/swap.sh && bash swap.sh

但是有的时候执行完了会报错，这个时候就要麻烦一下，自己设置了

# 新增swap区

* 创建一个 文件作为swap区：
```bash
dd if=/dev/zero of=/swapfile1 bs=1024 count=2000000
```
名字为/swapfile1，大小为bs*count = 1024*2000000=2G，count代表的是大小，我这里是2G。
* 将其转化为swap文件：
```
mkswap /swapfile1
```
* 将其改为只有root权限才能修改（这个可以不弄）
```bash
# chown root:root /swapfile1
# chmod 0600 /swapfile1
```
* 将其激活：
```bash
swapon /swapfile1
```
* 如果想要系统重启后生效，可以打开/etc/fstab在最后面加上一行：
```bash
nano /etc/fstab

/swapfile1 swap swap defaults 0 0
```
# 更改swap区大小

在网上没找到更多办法，有一个傻办法：

1、通过上述的1～5步重建一个swap区，然后激活；

2、先通过swapoff命令将之前的swap区失效，然后rm掉：
```bash
swapoff /swapfile1
```