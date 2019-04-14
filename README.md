# Document

- 前提准备：[第一次使用必看](https://github.com/aJantes/Initialize-the-board/blob/master/readme.md)
- 硬件介绍：[BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/readme.md)
- 编程工具：[pycharm](https://github.com/aJantes/use-pycharm/blob/master/readme.md)


## 如何控制板子IO口的输入输出

IO 在计算机中指Input/Output,也就是输入和输出，简称 IO 口

![io](album/io.png)

- 各种 IO 接口都不尽相同，有些特殊的接口是要更大一些，而且一般来说，它附近也会印有标签方便用户理解，如这块板子的底部是按照 0/1/2/3V/GND 的顺序分布在金手指上（计算机中大多都是是从 0 开始计算的）

- 在这个 microbit 的模块中，将板子的接口定义为 pinN 对象，其中 N 代表接口的数值，所以 0 号接口也就叫做 pin0 对象，当然也可以通过 import machine 的 Pin 重新定义自己喜欢的引脚名称

### “害羞”的板子

- 今天要实现的功能为，触摸板子的引脚并让它做出对应的反应

- 准备的代码如下：
[shy.py](https://github.com/aJantes/to-contro-IO/blob/master/shy.py)

- 运行效果如下图：

 ![touched_io](album/touched_io.gif)

- 需要注意的是，因为我们人体（手）有静电，可能会影响到ADC采样

### 灯的 ON 或 OFF

- 元件（LED）正极接电源正极（+），元件（LED）负极接电源负极（-）
- 长端为LED正极，短端为LED负极

 ![leds](album/leds.jpg)

- 准备的代码如下：[blink.py](https://github.com/aJantes/to-contro-IO/blob/master/blink.py)


- 运行效果如下图：

![blink](album/blink.gif)



