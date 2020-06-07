import sys
import time
import pyautogui


class AutoSlot:
    """Need change Minecraft setting below
    設定 -> 操作設定 -> マウス設定 -> Raw入力: オフ"""
    def __init__(self):
        self.toraden_icon = 'resource/toraden_icon.png'
        self.return_server_list = 'resource/return_server_list.png'

    def spin(self, check_server=False):
        seconds_of_charge_coin = 40

        # 30 minutes = 1800 seconds
        # check_server_count is 45
        check_server_count = 1800 / seconds_of_charge_coin
        count = 0
        while True:
            print('Spinning...')
            pyautogui.mouseDown(button='right')
            time.sleep(seconds_of_charge_coin)  # wait spinning ...
            # time.sleep(120)  # wait spinning ...
            pyautogui.mouseUp(button='right')
            pyautogui.press('t')  # open command bar
            pyautogui.press('backspace')  # remove t
            command = '/coin buy 32'
            # command = '/coin buy 64'
            pyautogui.write(command, interval=0.01)
            pyautogui.press('enter')
            print(command)
            if not check_server:
                continue

            count += 1
            if count >= check_server_count:
                position_of_return_server_list = self.is_server_closed()
                if position_of_return_server_list:
                    self.reconnect_server(position_of_return_server_list)
                count = 0

    def is_server_closed(self):
        print('Is server closed?')
        # https://github.com/asweigart/pyautogui/issues/441
        return pyautogui.locateCenterOnScreen(self.return_server_list)

    def reconnect_server(self, position_of_return_server_list):
        print('Try reconnect server.')
        pyautogui.click(position_of_return_server_list, button='left')
        for i in range(50):
            position_of_toraden_icon = pyautogui.locateCenterOnScreen(self.toraden_icon)
            pyautogui.click(position_of_toraden_icon, button='left')
            time.sleep(15)
            position_of_reconnect_fail_return_server_list = self.is_server_closed()
            if position_of_reconnect_fail_return_server_list:
                print(f'Reconnect failed. try count: {i + 1}')
                pyautogui.click(position_of_reconnect_fail_return_server_list, button='left')
            else:
                # Success reconnect server
                print('Success reconnect server.')
                return

        # Server is down, exit program.
        print('Server is down.')
        sys.exit(0)


if __name__ == '__main__':
    time.sleep(5)
    # AutoSlot().spin()
    AutoSlot().spin(True)  # check server closed
