# MircoPython - IO
#### 📖 [English document](https://github.com/aJantes/MircoPython-IO/blob/master/English_Document.md)
![](album/bit.gif)
> 硬件介绍：
1. [BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/README.md)
2. 直插式led

# 控制IO

IO 在计算机中指Input/Output,也就是输入和输出，简称 IO 口

## **控制IO口的输入与输出**

IO 口 硬件相关函数 [pin 模块](https://github.com/aJantes/MicroPython-IO/blob/master/source/pins.py)。在调用相关函数前，需要先导入对应的库。
## 主要函数
1. `pin1.is_touched()`:

例如：
 ```
 if pin1.is_touched():
    执行语句1
 ```
判断 1 号标签上的引脚是否被触摸，如被触摸则执行语句1

2. `pin2.write_digital()`:

例如：`pin2.write_digital(1)` 在 2 号标签的引脚输出高电平; `pin2.write_digital(0)` 在 2 号标签引脚输出低电平。


## ** IO 口例子**
1. [shy.py](https://github.com/aJantes/MircoPython-IO/blob/master/example/shy.py)   -害羞的板子
2. [blink.py](https://github.com/aJantes/MircoPython-IO/blob/master/example/blink.py) -led 闪烁



