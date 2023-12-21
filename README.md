# 真寻电棍活字印刷术插件

该项目基于 [大电老师活字印刷 otto-hzys](https://github.com/HanaYabuki/otto-hzys) 数据源，提供活字印刷功能的插件。支持本地部署和爬虫功能。

## 使用方法

1. 首先，在配置文件中设置以下参数：
```
DOWNLOAD_PATH: # 存放下载的音频文件的文件夹
WEBSITE: https://otto-hzys.hanayabuki.cf # 从哪里活字印刷
```

2. 在插件目录下创建`audio`文件夹。

3. 使用以下命令调用插件：
    ```
    /otto 活字印刷文本 是否使用原声大碟
    ```
    例如：
    - `/otto 我阐述你的梦` ----> 使用原声大碟。
    - `/otto 我阐述你的梦 False/false` ----> 不使用原声大碟。

注意：执行速度慢是因为使用了无头浏览器，因本人的愚笨暂时没有更快的方法。

## 配置

参数：

- `DOWNLOAD_PATH`: 存放下载的音频文件的文件夹路径。
- `WEBSITE`: 活字印刷数据源的网址。

## 贡献

欢迎贡献代码、提出问题或建议。如果你有任何问题，请提出 issue。

