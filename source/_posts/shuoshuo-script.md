---
title: 说说一键自动批量删除脚本
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/76322190_p0.png'
cover: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/76322190_p0.png'
date: 2020-03-10 11:55:40
tags: 工具
categories: 工具
---
详细使用教程请见：https://www.bilibili.com/video/av95148891/

```javascript
// 网站：user.qzone.qq.com

var temp = true;

function clickDel() {
    try {
        document.querySelector('.app_canvas_frame').contentDocument.querySelector('.del_btn').click();
    } catch{
        var a = document.querySelector('.app_canvas_frame').contentDocument.querySelector('.mod_pagenav_main').querySelectorAll('.c_tx');
        a[a.length - 1].click();
        temp = false;
        setTimeout(clickDel, 2000);
    }
    setTimeout(clickYes, temp ? 2000 : 5000);
    temp = true;
}
function clickYes() {
    document.querySelector('.qz_dialog_layer_btn').click();
    setTimeout(clickDel, 2000);
}
if (confirm("是不是要删除说说")) {
    setTimeout(function () {
        document.querySelectorAll("a[tabindex]")[8].click();
        setTimeout(clickDel, 2000);
    }, 3000);
}
```