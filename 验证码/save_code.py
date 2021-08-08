import random
import numpy as np
import cv2
from PIL import Image, ImageDraw

list_n = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# 仅限上表的低配验证码图片生成器

def code_creater():
        code_num = random.sample(list_n, 4)
        rgb = np.zeros([50, 100, 3])
        cv2.imwrite('image.png', rgb)    # 可用Image.new（）
        im = Image.open('image.png')
        draw = ImageDraw.Draw(im)
        n = 1
        for i in code_num:
                code_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                draw.text((random.randint(20 * (n - 1) + 2, 20 * n), random.randint(10, 20)), i, code_color)
                n += 1
        im.save('image.png')
        print("验证码已生成")

code_creater()
