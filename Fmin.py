# F min.py
import math
print("拉动斜面上的物体最小力计算")
print("Made by THH")
key = eval(input("输入注册码："))
keyrun = key ** 3 / 7
if (keyrun % 1323)==0:
    switch=eval(input("已激活！输入1继续"))
    while switch == 1:
        m = eval(input("输入质量："))
        alpha = eval(input("输入倾角度数"))
        sinalpha = math.sin(math.pi / 180 * alpha)
        cosalpha = math.cos(math.pi / 180 * alpha)
        print("材料        μ")
        print("铝-铝       1.05")
        print("铝-不锈钢    0.61")
        print("黄铜-铁      0.3")
        print("青铜-铁      0.22")
        print("橡胶-铁      0.49")
        print("铜-铜        1")
        print("铜-不锈钢     0.36")
        print("玻璃-玻璃    0.4")
        print("玻璃-金属    0.6")
        miu = eval(input("据表输入动摩擦因数:"))
        Fmin = m * 9.8 * sinalpha + m * 9.8 * cosalpha * miu
        print(Fmin, "N")
    else:
        print("已退出！")

    #doing

else:
    print("错误的注册码")
input()

