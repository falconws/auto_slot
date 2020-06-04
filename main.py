import sys
import time
import pyautogui


class AutoSlot:
    """Need change Minecraft setting below
    設定 -> 操作設定 -> マウス設定 -> Raw入力: オフ"""
    def __init__(self):
        pass

    @staticmethod
    def spin():
        while True:
            pyautogui.mouseDown(button='right')
            time.sleep(120)  # wait spinning ...
            pyautogui.mouseUp(button='right')
            pyautogui.press('t')  # open command bar
            pyautogui.press('backspace')  # remove t
            command = '/coin buy 64'
            pyautogui.write(command)
            pyautogui.press('enter')


if __name__ == '__main__':
    time.sleep(5)
    AutoSlot().spin()
