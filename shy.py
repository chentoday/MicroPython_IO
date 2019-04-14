from microbit import *
while True:
    if pin1.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

# 一只手触摸在 1 号标签的引脚上，就可以能看到板子的图像变了，如果你松开了，它又会再次变化
# 反复运行 `pin1.is_touched()` 来判断这个引脚是否有被触摸到（原理是 ADC 采样）