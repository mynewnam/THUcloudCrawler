# THUcloudCrawler

## 项目说明

清华云盘爬虫软件，依照2023 SAST暑期培训学习制作。

## 环境依赖

推荐使用`python 3.10`作为运行环境：
```
conda create -n crawler python=3.10
conda activate crawler
pip install -r requirements.txt
```

## 使用方式

在命令行中输入以下语句以运行本程序：
```
python THUcloudCrawler.py -u <url>
```
+ `-u`: 表示需要爬取的清华云盘共享链接，基本形式为：`https://cloud.tsinghua.edu.cn/d/xxx/`

程序启动后，将按照共享链接中的文件组织形式将所有文件下载至当前目录。因此，推荐新建空白文件夹作为存储目录，并在该目录中运行本程序完成下载。

## 其他说明

+ 本项目没有考虑如何处理加密的共享链接；
+ 本项目为个人练习，未经过大量实例进行调试，如有错误及改进建议，欢迎大家批评指正。