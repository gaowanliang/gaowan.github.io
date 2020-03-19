---
title: 从零开始实现hexo博客的在线编辑（未完成）
reward: true
toc: true
date: 2019-11-19 09:18:16
tags:
categories: 博客
---
⚠ 本教程需要服务器（VPS），Serverless版本正在探索，请大家耐心等待
# 前言
我今年五月参加的微信小程序开发赛获得了全国三等奖，微信赠了我1k的优惠券
![](https://i.loli.net/2019/11/19/4RsvXH2zO8mJn5w.png)
![](https://i.loli.net/2019/11/19/gW7O9TXAD1PMZiY.png)
不过这个优惠券只能购买没有优惠过的服务器，所以1k优惠券也是了了，最后在我的精打细算下，买了一年零三个月的服务器。买来不能闲置着不用啊，于是我准备构建一个在线写hexo的平台，这样就可以摆脱平台的束缚，在任意环境下都可以进行写作了。由于这个服务器是新购置的，所以我从零开始写一下相关的内容。
# 配置相关环境
## ~~Nignx~~(Nginx比较麻烦，下面更新caddy的)
配置Nignx是关键，虽然很俗，但是这个活不能不干。其实也可以有很多选择，比如Caddy，~~Apache~~（这年头个人搭建网站还有人用Apache吗，配置巨麻烦）

Debian apt 自带的 Nginx 太老，可以通过更新源的方式来解决

```bash
echo deb http://nginx.org/packages/debian/ stretch nginx | sudo tee /etc/apt/sources.list.d/nginx.list
wget http://nginx.org/keys/nginx_signing.key && sudo apt-key add nginx_signing.key 
sudo apt update && apt install nginx -y
```

到这一部分就完成了最新稳定版的 Nginx 的安装。需要注意的是，这一步安装的 Nginx 和系统自带的 Nginx 的配置目录略有区别，可以用一下几个简单的命令修正：
```bash
sudo mkdir /etc/nginx/{sites-available,sites-enabled}
sudo mv /etc/nginx/conf.d/* /etc/nginx/sites-available
sudo rmdir -f /etc/nginx/conf.d/
sudo perl -pi -e 's/conf.d/sites-enabled/g' /etc/nginx/nginx.conf
```
当然这个没必要，我就没弄

最后出现这个就是成功了
![](https://i.loli.net/2019/11/19/fWvASTeK84U6xLa.png)

## NodeJS
NodeJS是最重要的，没有Nginx也得有NodeJS，这是我们写博客的关键，Debian自带的NodeJS还是比较老的，推荐用 [nvm](https://github.com/nvm-sh/nvm) 安装
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash
```
然后**关闭再打开终端**，就可以用了

我目前NodeJS最新版是12.13.0，输入
```bash
nvm install 12.13.0
```
就安装了NodeJS 12.13.0版本

![](https://i.loli.net/2019/11/19/CN5elIwdTfQYVmZ.png)



## git
git 直接用 apt 安装就行了，这个不再赘述。
```bash
apt install git
```

# 工作区配置

## 把你的博客源文件上传Github

为了多端同步，也为了防止服务器不好上传你的文件，这个时候就需要将你的博客的源文件文件上传到GitHub，由于Hexo会吃掉你博客的master分支，这个时候就需要先创建一个分支。在你博客源文件的文件夹下打开Git bash，输入下面的命令
```bash
git checkout -b inside
```

这样就创建了一个inside分支，因为我这个博客的主题就是inside。然后`git push`到GitHub上，本地这边的工作就完成了。

## 在服务器上把你的源代码clone下来
由于服务器是全新的，我就按全新的来说，首先输入下面命令：
```bash
git config --global user.name "你GitHub的用户名"

git config --global user.email "你GitHub注册时用的邮箱"

ssh-keygen -t rsa -C "你GitHub注册时用的邮箱"
```
默认回车即可，然后输入`cat /root/.ssh/id_rsa.pub`，然后把输出的东西整个复制出来
![](https://cdn.jsdelivr.net/gh/gaowanliang/p/img/20191127204816.png)
打开[github](https://github.com)，在头像下面点击`settings`，再点击`SSH and GPG keys`，新建一个SSH，Title随便。

把刚才输出的一串复制到key里即可

输入`ssh -T git@github.com`，问Are you sure you want to continue connecting (yes/no)?时输入yes，如果出现你的用户名，那就成功了。


```bash
git config --system user.name "你GitHub的用户名"

git config --system user.email "你GitHub注册时用的邮箱"

ssh-keygen -t rsa -C "你GitHub注册时用的邮箱"
```