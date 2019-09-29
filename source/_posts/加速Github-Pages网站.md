---
title: 利用jsDelivr和Cloudflare加速Github Pages网站
top: false
cover: false
toc: true
mathjax: false
date: 2019-09-29 20:56:30
password:
summary:
tags: 
    - Github Pages
    - 加速
    - jsdelivr
    - Cloudflare
categories: 加速
---
# 利用jsDelivr和Cloudflare加速Github Pages网站
最近觉得学的东西不少，但是我从来没有记录过，最近正好因为新建了个博客，热乎劲还没过去，所以写点什么。

我比较穷，不想买个服务器，买了也浪费，同时又想写博客。还不想通过CSDN，简书之类的“广告网站”来写东西（最近发现在手机上用Chrome浏览器看简书的内容的时候会有弹屏广告，而且关不掉，遂放弃了简书）。突然想起了好久之前看过的Github Pages，于是照着网上的教程进行了梳理，最终创建了一个我还比较满意的博客。只是有一个很严重的缺陷，就是国内访问太慢了，查了很多教程，发现都是些接入国内CDN的教程，国内CDN不仅贵，而且你不备案是不能用的。对于我这样一个没啥需求的用户，还得做网站备案，太麻烦了。于是想能不能曲线救国，最终找到了一个比较有效，能提高Github Pages速度的方法，还不用花钱（可能要花点，但是不多）。
## 效果

先上效果（两个网页均是通过 **清空缓存并硬性重新加载** 方式来测试的）

![这是我用的主题的作者给的示例站，直到35000ms的时候才算是正式加载完成](https://i.loli.net/2019/09/29/f9ij6oYm83UpadG.png)

![这是本站加载速度，8000ms的时候就基本上加载完成](https://i.loli.net/2019/09/29/obNetxyrPZQ5fHR.png)

对于速度，大家可以自行测试，本站和 [blinkfox.github.io](https://blinkfox.github.io) 使用的是同一套模板，对方9.9s时还没跳到主页，我站8s就已经全部加载完成。那我做了什么改动呢？

## 第一步——压缩图片

刚开始的时候没有头绪，因为不知道Github Pages能换域名。我一想，图片是显示的大头，先从压缩图片开始做起，刚好有一个公司 [TinyPNG](https://tinypng.com/) 提供了接口。首先我们需要打开它的官网，点击上面的 *Developer API*，输入你的名字和Email就可以获得每月500次的免费试用API的资格，你放心，这个量对于我们这种写小博客的人来说是非常够用的。申请完了之后要写个压缩的小程序。对于我来说，做个小程序还是轻而易举的，我在这里使用python来简单写写。根据官方文档说明，你首先需要下载它的库
> `pip install --upgrade tinify`

然后就可以应用我这个遍历程序啦(突然发现被我删啦，重新写吧)
```python

import tinify
import os
tinify.key = "YOUR_API_KEY"


def tinify_all_pic(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            tinify_all_pic(path)
        if os.path.isfile(path):
            suffix = os.path.splitext(path)[-1]
            if suffix == '.png' or suffix == '.jpg':
                print(path)
                source = tinify.from_file(path)
                source.to_file(path)

tinify_all_pic(r"themes\hexo-theme-matery\source")
# 这里是用我存放资源的一个文件夹做示范，根据你们的文件夹不同进行相应的更换

```

压缩率通常在50%以上（特别是你用超过1M以上的图片的时候），这样你在加载的时候不就提高50%的加载速度了嘛😂（不是）。

这样操作之后你的加载速度可以提高至少20%以上（一些模板资源也被压缩了，有些图片没法用网页URL来代替）。

