# 需要自己去截取围观的那个图片

import pyautogui
import time


def weiguan():
    time.sleep(0.2)    # 等待 1 秒

    # 围观
    left, top, width, height = pyautogui.locateOnScreen('weiguan.PNG')   # 寻找围观
    center = pyautogui.center((left, top, width, height))    # 寻找中心点
    print("找到对象", center)
    pyautogui.click(center)    # 点击


if __name__ == "__main__":
    while True:
        if pyautogui.locateOnScreen('weiguan.PNG'):
            weiguan()
        else:
            print("未找到可点击对象...")
            print("下一页")
            pyautogui.scroll(-300)

