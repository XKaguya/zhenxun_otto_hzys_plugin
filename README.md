# zhenxun_otto_hzys_plugin
真寻电棍活字印刷术插件

数据源：
[大电老师活字印刷 otto-hzys](https://github.com/HanaYabuki/otto-hzys)

支持本地部署以及爬虫。

## 调用方法
```
/otto 活字印刷文本 是否使用原声大碟
如：
/otto 我阐述你的梦
是原声大碟。
/otto 我阐述你的梦 False/false
则是活字印刷。
```

## 配置
```
Otto:
# OTTO活字印刷术
# DOWNLOAD_PATH: 存放下载的音频文件的文件夹
# WEBSITE: 从哪里活字印刷
DOWNLOAD_PATH: 
WEBSITE: https://otto-hzys.hanayabuki.cf
```

执行速度慢是因为用了无头浏览器，个人没有想法还怎么更快。
