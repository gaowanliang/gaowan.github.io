---
title: 优雅的批量重命名文件
reward: true
toc: true
thumbnail: 'https://cdn.jsdelivr.net/gh/gaowanliang/p/img/72940468_p0.png'
date: 2020-11-22 12:53:47
tags: 教程
categories:
---




```bash
for /f "delims=" %%f in ('dir /a /b *.mp3') do(
    ren "%%f" "N1-%%~nxf"
)
pause
```

```bash
for /f "delims=" %%f in ('dir /a /b *.mp3') do(
    ren "%%f" "%%~nf-N2%%~xf"
)
pause
```


```bash
for /f "delims=" %%f in ('dir /a /b *.mp3') do(
    ren "%%f" "%%~nf-N2%%~xf"
)
pause
```

```bash
set a=0

setlocal EnableDelayedExpansion

for /f "delims=" %%f in ('dir /a /b *.*') do (
    if not "%%~nxf"=="%~nx0" (
        set /A a+=1
        ren "%%f" "动漫!a!%%~xf"
    )
)
pause
```

```bash
setlocal enabledelayedexpansion
for /f "delims=" %%i in ('dir /b *[Sakurato.Sub] *') do (
    set var=%%i
    set var=!var:[Sakurato.Sub] =!
    ren "%%i" "!var!"
)
pause
```

```bash
DIR *.* /B > list.csv
```


```bash
="ren "&A1&" "&B1&C1&".docx"
```