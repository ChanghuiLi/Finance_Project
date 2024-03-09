import time

import pyautogui
import random

# 设置鼠标移动的间隔时间（单位：秒）
interval_time = 290

# 循环执行移动鼠标的操作
while True:
    # 移动鼠标到一个随机位置
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    pyautogui.moveTo(random_x, random_y, duration=0.5)

    # 等待一段时间
    time.sleep(interval_time)