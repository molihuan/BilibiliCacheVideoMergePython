

<p align="center">
<img src="https://s2.loli.net/2022/12/14/WoYwfehDNHbMzIZ.png" alt="Banner" />
</p>
<h1 align="center">HLB站缓存合并</h1>

[![license: Apache-2.0 (shields.io)](https://img.shields.io/badge/license-Apache--2.0-brightgreen)](https://github.com/molihuan/mlhfileselectorlib/blob/master/LICENSE)[![Star](https://img.shields.io/github/stars/molihuan/BilibiliCacheVideoMergePython.svg)](https://github.com/molihuan/BilibiliCacheVideoMergePython)[![bilibili: 玲莫利 (shields.io)](https://img.shields.io/badge/bilibili-玲莫利-orange)](https://space.bilibili.com/454222981)[![CSDN: molihuan (shields.io)](https://img.shields.io/badge/CSDN-molihuan-blue)](https://blog.csdn.net/molihuan)

<h3 align="center">提供Bilibili缓存视频合并的工具</h3>
<p align="center">将Bilibili缓存文件合并导出为MP4，支持windows、mac、linux，支持B站手机客户端缓存，支持B站电脑客户端缓存</p>
<p align="center">Merge and export Bilibili cache files into MP4, support caching on B-station mobile client and B-station computer client</p>


## 说明

此软件是为了帮助网友合并哔哩哔哩缓存视频，将bilibili缓存视频合并导出为mp4，支持windows、mac、linux，你可以将它理解为一个专用的格式工厂，并不涉及破解相关内容，仅仅用于学习技术交流，严禁用于商业用途，如有侵权请联系我删档，对你带来困惑和不便我深感抱歉。


## 特性

- [x] 合并(导出)B站缓存(有声音视频，仅音频)
- [x] 支持B站手机客户端缓存
- [x] 支持B站电脑客户端缓存

## 前言

#### 在开始之前可以给项目一个Star吗？非常感谢，你的支持是我唯一的动力。欢迎Star和Issues!

#### 我们需要你的Pr

#### 项目地址：
##### [Github地址](https://github.com/molihuan/BilibiliCacheVideoMergePython)
##### [Gitee地址](https://gitee.com/molihuan/BilibiliCacheVideoMergePython)

## 注意

- 此软件存放的目录不能有空格或特殊字符
- 读取缓存视频的目录不能有空格或特殊字符
- 输出目录不能有空格或特殊字符
- 它不依赖网络这个不确定的因素，它只依赖本地缓存文件，只要本地有缓存文件，那么它就可以工作，需要和官方APP（手机版/电脑版均可）配合使用，官方APP进行缓存，它操作缓存文件进行合并导出mp4

## 下载链接：[跳转](https://github.com/molihuan/BilibiliCacheVideoMergePython/releases)

Linux版本：使用ubuntu-22.04.2-amd64打包，你的系统版本低不保证可用，如有问题请下载源码自行打包

Mac版本：使用macOS ventura 13.4.1版本打包，你的系统版本低不保证可用，如有问题请下载源码自行打包

Windows：使用Win 10打包，你的系统版本低不保证可用，如有问题请下载源码自行打包

## 界面:

[![Beafdcf310e77efb3.png](https://z4a.net/images/2023/07/22/Beafdcf310e77efb3.png)](https://z4a.net/image/VBY2Pp)

![HLBTool2.png](https://z4a.net/images/2023/11/08/HLBTool2.png)

![HLBTool3.png](https://z4a.net/images/2023/11/08/HLBTool3.png)

![HLBTool4.png](https://z4a.net/images/2023/11/08/HLBTool4.png)

[![B.png](https://z4a.net/images/2023/07/22/B.png)](https://z4a.net/image/VBYgjE)

## 写在前面

### [查看](./res/md/statement.md)

## 软件更新

- 优先级 1 (最快):交流群群文件(没有问题请不要加)
- 优先级 2 (次之):网盘链接：
安卓版：https://wwa.lanzouo.com/b016uhb5g
密码:MLH
电脑版：https://wwa.lanzouo.com/b016vmouf
密码:MLH
- 优先级 3 :Github(https://github.com/molihuan/BilibiliCacheVideoMergePython)
- 优先级 4 :软件内

## 问题反馈

##### 因为有你软件才更加完善

请使用模板反馈问题，这样可以帮助开发者快速定位和解决问题，谢谢配合，爱你萌萌哒~^o^~

##### 反馈模板:

类别：(必填，0、优化建议。1、打开软件就闪退。2、无论什么视频合并都失败或闪退。3、合并个别视频失败或闪退。4、主页空白无法加载哔哩哔哩缓存视频。5、其他问题)

设备信息：(必填)

描述：(必填，越详细越好)

怎样触发bug：(选填)

视频链接：(选填，如果视频已经下架则把本地缓存文件打包压缩发我邮箱)



## 软件下载:

https://github.com/molihuan/BilibiliCacheVideoMergePython/releases

## 打包

理论上支持Win 10/Linux/Mac

#### 第一步

在你的平台上安装python3.8.0以上（推荐安装和我一样的版本python3.8.6，避免一些未知的错误）

安装依赖库

```sh
#图形库依赖
pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple

#打包依赖(任选其一，或者都安装，推荐新手使用pyinstaller。nuitka还需要其他的配置比较麻烦)
#推荐
pip install pyinstaller
#可选
pip install nuitka
```

#### 第二步

下载源码

#### 第三步

使用python运行main.py看是否成功

没成功就自己看哪里有问题（该导库的导库，该引入依赖的引入依赖，自己解决）

编译打包：运行script下面的packagescript.py，自行打包，打包后的文件在script下面（作者分别在Win10，Ubuntu22,Mac14.3.1打包成功）

## 开发环境

qt5.15.2

(ffmpeg4.3.2)

python3.8.6

```sh
#图形库依赖
pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple

#打包依赖
pip install pyinstaller
pip install nuitka
```

## 特别鸣谢

- [Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6 (github.com)](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)
- https://gitee.com/l2063610646/bilibili-convert
- https://www.bilibili.com/video/BV1gv4y1M7yn/

开源项目或教程以及其依赖项目。

## LICENSE 

```
Copyright [2023] molihuan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```



