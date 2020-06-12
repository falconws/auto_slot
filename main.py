import sys
import time
import pyautogui

from datetime import datetime


class AutoSlot:
    """Need change Minecraft setting below
    設定 -> 操作設定 -> マウス設定 -> Raw入力: オフ"""
    def __init__(self):
        self.toraden_icon = 'resource/toraden_icon.png'
        self.return_server_list = 'resource/return_server_list.png'

    def spin(self):
        seconds_of_charge_coin = 40

        # 30 minutes = 1800 seconds
        # check_server_count is 45
        check_server_count = int(1800 / seconds_of_charge_coin)
        count = 0
        while True:
            print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Spinning...')
            pyautogui.mouseDown(button='right')
            time.sleep(seconds_of_charge_coin)  # wait spinning ...
            count += 1
            print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} check count: {count}/{check_server_count}')
            if count >= check_server_count:
                count = 0
                position_of_return_server_list = self.is_server_closed()
                if position_of_return_server_list:
                    pyautogui.mouseUp(button='right')
                    self.reconnect_server(position_of_return_server_list)

            pyautogui.mouseUp(button='right')
            self.buy_coin(32)

    @staticmethod
    def buy_coin(number):
        pyautogui.press('t')  # open command bar
        pyautogui.press('backspace')  # remove t
        command = f'/coin buy {number}'
        pyautogui.write(command, interval=0.01)
        pyautogui.press('enter')
        print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} {command}')

    def is_server_closed(self):
        print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Is server closed?')
        # https://github.com/asweigart/pyautogui/issues/441
        return pyautogui.locateCenterOnScreen(self.return_server_list)

    def reconnect_server(self, position_of_return_server_list):
        print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Try reconnect server.')
        pyautogui.click(position_of_return_server_list, button='left')
        for i in range(1, 51):
            position_of_toraden_icon = pyautogui.locateCenterOnScreen(self.toraden_icon)
            pyautogui.click(position_of_toraden_icon, button='left')
            time.sleep(15)
            position_of_reconnect_fail_return_server_list = self.is_server_closed()
            if position_of_reconnect_fail_return_server_list:
                print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Reconnect failed. try count: {i}')
                pyautogui.click(position_of_reconnect_fail_return_server_list, button='left')
            else:
                # Success reconnect server
                print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Success reconnect server.')
                return

        # Server is down, exit program.
        print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} Server is down.')
        sys.exit(0)


if __name__ == '__main__':
    time.sleep(5)
    AutoSlot().spin()

