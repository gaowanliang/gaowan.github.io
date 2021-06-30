---
title: OneDrive 上传工具 OneDriveUploader
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/64360477_p0.jpg'
cover: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/64360477_p0.jpg'
date: 2021-04-02 19:36:03
tags: 教程
categories: OneDrive
---
```
更新

【2021.04.02】
目前同时支持国际版、个人版(家庭版)。

【2021.04.01】
修复授权失败、上传文件大小为0等问题。
现已支持arm、x86、x64平台的系统。

【2021.03.27】
新增多线程上传、MacOS客户端。
修复了一个致命bug，建议之前装过的更新下程序。

功能

支持上传文件和文件夹到指定目录，并保持上传前的目录结构。
支持命令参数使用，方便外部程序调用。
支持自定义上传分块大小。
支持多线程上传(多文件同时上传)。
支持根据文件大小动态调整重试次数，对抗不好的网络环境。
可以使用Telegram Bot实时监控上传进度
Github地址：https://github.com/gaowanliang/OneDriveUploader
```
萌咖大佬写了一个 [非常好的版本](https://github.com/MoeClub/OneList/tree/master/OneDriveUploader) ，可惜并没有开源，而且已经好久都没有更新了。这个项目作为从 [DownloadBot](https://github.com/gaowanliang/DownloadBot) 中独立出来的一个简易上传工具，使得上传到OneDrive更加方便。

这里只详细说下Linux的用法，Windows后面大概说下。

Windows、MacOS系统下载地址→[传送门](https://github.com/gaowanliang/OneDriveUploader/releases)，直接将程序下载到本地后，按照下面方法进行授权、初始化，然后就可以使用命令上传了。

# 授权认证
点击右侧URL登录并授权，授权地址→[【国际版、个人版(家庭版)】](https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=ad5e65fd-856d-4356-aefc-537a9700c137&response_type=code&redirect_uri=http://localhost/onedrive-login&response_mode=query&scope=offline_access%20User.Read%20Files.ReadWrite.All)

授权后会获取一个localhost开头打不开的链接，这里复制好整个链接地址，包括localhost。

# 安装OneDriveUploader
打开这个界面，选择适合你系统的版本：https://github.com/gaowanliang/OneDriveUploader/releases

这里以Linux 64位为例，当前最新版本为v1.4-fix，应该下载 OneDriveUploader_Linux_x86_64.tar.gz 这个文件
```bash
# 下载文件
wget https://github.com/gaowanliang/OneDriveUploader/releases/download/v1.4-fix/OneDriveUploader_Linux_x86_64.tar.gz
# 解压文件
tar -zxvf OneDriveUploader_Linux_x86_64.tar.gz -C /usr/local/bin/

# 给予权限
chmod +x /usr/local/bin/OneDriveUploader

# 可选 软链接 类似于 Windows 的快捷方式
ln -s /usr/local/bin/OneDriveUploader /usr/bin/OneDriveUploader
```
# 初始化配置
```bash
#国际版，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader -a "url" -l zh-CN

#个人版(家庭版)，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader -a "url" -v 1 -l zh-CN

```
如果提示`注册成功`类似信息，则初始化成功。

# 使用命令
```c
Usage of OneDriveUploader:
  -a string
        // 初始化授权
        Setup and Init auth.json.
  -b string
        // 自定义上传分块大小, 可以提高网络吞吐量, 受限于磁盘性能和网络速度.
  -c string
        // 配置文件路径

  -r string
        // 上传到网盘中的某个目录, 默认: 根目录
  -l string
        // 软件语言
  -f string
        // *必要参数, 要上传的文件或文件夹
  -t string
        // 线程数, 同时上传文件的个数. 默认: 3
  -to int
        //单个数据包超时时间，默认为60s
  -tgbot string
        //使用Telegram机器人实时监控上传，此处需填写机器人的access token，形如123456789:xxxxxxxxx，输入时需使用双引号包裹。当写入内容为“1”时，使用配置文件中的BotKey和UserID作为载入项
  -uid string
        // 使用Telegram机器人实时监控上传，此处需填写接收人的userID，形如123456789
  -m int
        // 选择模式，0为替换OneDrive中同名文件，1为跳过，默认为0
  -v int
        // 选择版本，其中0为国际版，1为个人版(家庭版)，默认为0
```
## 命令示例
```bash
# 一些示例:

# 将同目录下的 mm00.jpg 文件上传到 OneDrive 网盘根目录
OneDriveUploader -c xxx.json -f "mm00.jpg"

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录
OneDriveUploader -c xxx.json -f "Download" 

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘Test目录中
OneDriveUploader -c xxx.json -f "Download" -r "Test"

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 10 线程
OneDriveUploader -c xxx.json -t 10 -f "Download" 

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 10 线程，并跳过同名文件
OneDriveUploader -c xxx.json -t 10 -f "Download" -m 1

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 10 线程，同时设置超时时间为30秒
OneDriveUploader -c xxx.json -t 10 -f "Download" -to 30

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 10 线程，同时使用 Telegram Bot 实时监控上传进度
OneDriveUploader -c xxx.json -t 10 -f "Download" -tgbot "123456:xxxxxxxx" -uid 123456789

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 10 线程，同时使用配置文件中的 Telegram Bot 参数载入程序实时监控上传进度（前提是配置文件中含有Telegram Bot 的参数）
OneDriveUploader -c xxx.json -t 10 -f "Download" -tgbot "1"

# 将同目录下的 Download 文件夹上传到 OneDrive 网盘根目录中, 使用 15 线程, 并设置分块大小为 20M
OneDriveUploader -c xxx.json -t 15 -b 20 -f "Download" 

```
`/urs/local/auth.json`为初始化时，生成的*.json绝对路径地址，本文默认`/root/auth.json`，自行调整。


# Aria2自动上传
同样的这里也会提供个配套的Aria2自动上传脚本
上传脚本代码如下：
```bash
#!/bin/bash

GID="$1";
FileNum="$2";
File="$3";
MaxSize="157286400";
Thread="3";  #默认3线程，自行修改，服务器配置不好的话，不建议太多
Block="20";  #默认分块20m，自行修改
RemoteDIR="";  #上传到Onedrive的路径，默认为根目录，如果要上传到Test目录，""里面请填成Test
LocalDIR="/www/download/";  #Aria2下载目录，记得最后面加上/
Uploader="/usr/local/bin/OneDriveUploader";  #上传的程序完整路径，默认为本文安装的目录
Config="/root/auth.json";  #初始化生成的配置auth.json绝对路径，参考第3步骤生成的路径


if [[ -z $(echo "$FileNum" |grep -o '[0-9]*' |head -n1) ]]; then FileNum='0'; fi
if [[ "$FileNum" -le '0' ]]; then exit 0; fi
if [[ "$#" != '3' ]]; then exit 0; fi

function LoadFile(){
  if [[ ! -e "${Uploader}" ]]; then return; fi
  IFS_BAK=$IFS
  IFS=$'\n'
  tmpFile="$(echo "${File/#$LocalDIR}" |cut -f1 -d'/')"
  FileLoad="${LocalDIR}${tmpFile}"
  if [[ ! -e "${FileLoad}" ]]; then return; fi
  ItemSize=$(du -s "${FileLoad}" |cut -f1 |grep -o '[0-9]*' |head -n1)
  if [[ -z "$ItemSize" ]]; then return; fi
  if [[ "$ItemSize" -ge "$MaxSize" ]]; then
    echo -ne "\033[33m${FileLoad} \033[0mtoo large to spik.\n";
    return;
  fi
  ${Uploader} -c "${Config}" -t "${Thread}" -b "${Block}" -f "${FileLoad}" -r "${RemoteDIR}"
  if [[ $? == '0' ]]; then
    rm -rf "${FileLoad}";
  fi
  IFS=$IFS_BAK
}
LoadFile;
```
编辑好上传脚本后，可以检测下脚本编码是否正确，比如我脚本路径为`/root/upload.sh`，使用命令：
```bash
bash /root/upload.sh
```
如果无任何输出，则正确，反之输出类似$'r': command not found错误，则需要转换下编码格式，具体步骤如下。

先安装dos2unix：
```bash
#CentOS系统
yum install dos2unix -y

#Debian/Ubuntu系统
apt install dos2unix -y
再转换编码：

#后面为脚本路径
dos2unix /root/upload.sh
```
# Windows使用
这里就随便补充下Windows使用，先下载程序文件，下载地址→[传送门](https://github.com/gaowanliang/OneDriveUploader/releases)。

比如我将exe文件放到D盘，然后使用Win+R，输入CMD运行，调出窗口后，使用命令：
```cmd
#进入D盘
cd /d D:\

#国际版初始化，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader.exe -a "url" -l zh-CN

#个人版(家庭版)初始化，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader.exe -a "url" -v 1 -l zh-CN

```
然后上传命令和上面一样，只需要把`OneDriveUploader`改成`OneDriveUploader.exe`即可。
