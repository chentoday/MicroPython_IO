from microbit import *

while True:
    pin2.write_digital(1)
    sleep(200)
    pin2.write_digital(0)
    sleep(1000)

    # 1. 使用 pin2 引脚进行输出 1 ， 这会让 LED 存在变成高电平，
    # 简单认为上就是这个引脚有电压了，效果相当于直接接了电源正极。（原理上应该理解为两个引脚之间形成电势差）

    # 2. 首先先将其点亮，即为 `pin2.write_digital(1)`，之后使用 `sleep(200) ` 让板子休息 200 毫秒

    # 3. 然后就将其熄灭，也就是 `pin2.write_digital(0)`，之后再休息 1000 毫秒，也就是 1 秒。