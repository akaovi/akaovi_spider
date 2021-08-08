# 大致流程
# 1、找窗口
# 2、将需要发送的信息放在剪切板
# 3、用SendMessage模拟粘贴
# 4、模拟enter 发送

import win32gui
import win32con
import win32clipboard as w

# 发送的消息
msg = "嘎"
# 窗口名字
name = "代码测试"  # 需要发送的qq聊天窗口的名字
# 输入到剪切板
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()
# 获取窗口句柄
handle = win32gui.FindWindow(None, name)

# 开始运行
n = 0
while True:
    if n < 500:   # 好像10+会崩溃
        # 粘贴
        win32gui.SendMessage(handle, 770, 0, 0)   # 模拟粘贴键
        # 模拟enter发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        n += 1
        print(n)  # 检验代码运行了吗
    else:
        break
