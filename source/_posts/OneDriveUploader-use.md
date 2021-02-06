---
title: OneDrive 上传工具 OneDriveUploader
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/64360477_p0.jpg'
date: 2020-08-29 19:36:03
tags: 教程
categories: OneDrive
---
```
更新
【2019.12.21】
 支持跳过网盘中已存在的同名文件。

【2019.12.20】
目前同时支持国际版、个人版(家庭版)、中国版(世纪互联)。

【2019.12.15】
修复授权失败、上传文件大小为0等问题。
现已支持arm、x86、x64平台的系统。

【2019.11.29】
新增多线程上传、MacOS客户端。
修复了一个致命bug，建议之前装过的更新下程序。
功能
支持上传文件和文件夹到指定目录，并保持上传前的目录结构。
支持命令参数使用，方便外部程序调用。
支持自定义上传分块大小。
支持多线程上传(多文件同时上传)。
支持根据文件大小动态调整重试次数，对抗不好的网络环境。
使用
Github地址：https://github.com/MoeClub/OneList/tree/master/OneDriveUploader
```
这里只详细说下Linux的用法，Windows后面大概说下。

Windows、MacOS系统下载地址→[传送门](https://github.com/MoeClub/OneList/tree/master/OneDriveUploader/amd64)，直接将程序下载到本地后，按照下面方法进行授权、初始化，然后就可以使用命令上传了。

# 授权认证
点击右侧URL登录并授权，授权地址→[【国际版、个人版(家庭版)】](https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=78d4dc35-7e46-42c6-9023-2d39314433a5&response_type=code&redirect_uri=http://localhost/onedrive-login&response_mode=query&scope=offline_access%20User.Read%20Files.ReadWrite.All)、[【中国版(世纪互联)】](https://login.chinacloudapi.cn/common/oauth2/v2.0/authorize?client_id=dfe36e60-6133-48cf-869f-4d15b8354769&response_type=code&redirect_uri=http://localhost/onedrive-login&response_mode=query&scope=offline_access%20User.Read%20Files.ReadWrite.All)。

授权后会获取一个localhost开头打不开的链接，这里复制好整个链接地址，包括localhost。

# 安装OneDriveUploader
```bash
#64位系统下载
wget https://raw.githubusercontent.com/MoeClub/OneList/master/OneDriveUploader/amd64/linux/OneDriveUploader -P /usr/local/bin/
#32位系统下载
wget https://raw.githubusercontent.com/MoeClub/OneList/master/OneDriveUploader/i386/linux/OneDriveUploader -P /usr/local/bin/
#arm架构下载
wget https://raw.githubusercontent.com/MoeClub/OneList/master/OneDriveUploader/arm/linux/OneDriveUploader -P /usr/local/bin/

#给予权限
chmod +x /usr/local/bin/OneDriveUploader

#可选 软链接 类似于 Windows 的快捷方式
ln -s /usr/local/bin/OneDriveUploader /usr/bin/OneDriveUploader
```
# 初始化配置
```bash
#国际版，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader -a "url"

#个人版(家庭版)，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader -ms -a "url"

#中国版(世纪互联)，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader -cn -a "url"
```
如果提示`Init config file: /path/to/file/auth.json`类似信息，则初始化成功。

# 使用命令
```c
Usage of OneDriveUploader:
  -a string
        // 初始化授权
        Setup and Init auth.json.
  -b string
        // 自定义上传分块大小, 可以提高网络吞吐量, 受限于磁盘性能和网络速度.
        Set block size. [Unit: M; 5<=b<=60;] (default "10")
  -c string
        // 配置文件路径
        Config file. (default "auth.json")
  -n string
        // 上传单个文件时,在网盘中重命名
        Rename file on upload to remote.
  -r string
        // 上传到网盘中的某个目录, 默认: 根目录
        Upload to reomte path.
  -s string
        // *必要参数, 要上传的文件或文件夹
        Upload item.
  -t string
        // 线程数, 同时上传文件的个数. 默认: 2
        Set thread num. (default "2")
  -f
        // 开关(推荐)
        // 加上 -f 参数，强制读取 auth.json 中的块大小配置和多线程配置.
        // 不加 -f 参数, 每次覆盖保存当前使用参数到 auth.json 配置文件中.
        Force Read config form config file. [BlockSize, ThreadNum]
  -skip
        // 开关
        // 跳过上传网盘中已存在的同名文件. (默认不跳过)
        Skip exist file on remote.
  -cn
        // 开关
        // 授权中国版(世纪互联), 需要此参数.
        OneDrive by 21Vianet.
  -ms
        // 开关
        // 授权个人版(家庭版), 需要此参数.
        OneDrive by Microsoft.
```
## 命令示例
```bash
#将当前目录下的mm00.jpg文件上传到OneDrive网盘根目录
OneDriveUploader -c /path/to/file/auth.json -s "mm00.jpg"

#将当前目录下的mm00.jpg文件上传到OneDrive网盘根目录，并改名为mm01.jpg
OneDriveUploader -c /path/to/file/auth.json -s "mm00.jpg" -n "mm01.jpg"

#将当前目录下的Download文件夹上传到OneDrive网盘根目录
OneDriveUploader -c /path/to/file/auth.json -s "Download" 

#将当前目录下的Download文件夹上传到OneDrive网盘Test目录中
OneDriveUploader -c /path/to/file/auth.json -s "Download" -r "Test"

#将同目录下的Download文件夹上传到OneDriv网盘Test目录中，使用10线程
OneDriveUploader -c /path/to/file/auth.json -t 10 -s "Download" -r "Test"

#将同目录下的Download文件夹上传到OneDrive网盘Test目录中，使用15线程，并设置分块大小为20M
OneDriveUploader -c /path/to/file/auth.json -t 15 -b 20 -s "Download" -r "Test"
```
`/path/to/file/auth.json`为初始化时，生成的auth.json绝对路径地址，本文默认`/root/auth.json`，自行调整。

注意：如果你之前上传手动中断过，再上传的时候，请使用-skip参数，默认会跳过你已经上传过的文件/文件夹。

# Aria2自动上传
同样的这里也会提供个配套的Aria2自动上传脚本
上传脚本代码如下：
```bash
#!/bin/bash

GID="$1";
FileNum="$2";
File="$3";
MaxSize="15728640";
Thread="3";  #默认3线程，自行修改，服务器配置不好的话，不建议太多
Block="20";  #默认分块20m，自行修改
RemoteDIR="";  #上传到Onedrive的路径，默认为根目录，如果要上传到MOERATS目录，""里面请填成MOERATS
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
  ${Uploader} -c "${Config}" -t "${Thread}" -b "${Block}" -s "${FileLoad}" -r "${RemoteDIR}" -skip
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
这里就随便补充下Windows使用，先下载程序文件，下载地址→传送门。

比如我将exe文件放到D盘，然后使用Win+R，输入CMD运行，调出窗口后，使用命令：
```cmd
#进入D盘
cd /d D:\

#国际版初始化，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader.exe -a "url"

#个人版(家庭版)初始化，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader.exe -ms -a "url"

#中国版(世纪互联)初始化，将url换成你上面复制的授权地址，包括http://loaclhost。
OneDriveUploader.exe -cn -a "url"
```
然后上传命令和上面一样，只需要把`OneDriveUploader`改成`OneDriveUploader.exe`即可。
