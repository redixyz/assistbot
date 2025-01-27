import pyautogui
import config
import tkinter.messagebox as mb
import webbrowser
pyautogui.FAILSAFE = False
from screeninfo import get_monitors
import subprocess

def volume_down():
    pyautogui.press('volumedown')
#===================================================
def volumemute():
    pyautogui.press("volumemute")
#===================================================
def volume_up():
    pyautogui.press("volumeup")
#===================================================
def next():
    pyautogui.press('nexttrack')
#===================================================
def prev():
    pyautogui.press('prevtrack')
#===================================================
def play():
    pyautogui.press('playpause')
#===================================================
def shutdown():
    subprocess.call("shutdown /s /f /t 0 ", creationflags=0x08000000) #Выключение компьютера
#===================================================
def reboot():
    subprocess.call("shutdown /r /f /t 0 ", creationflags=0x08000000) #Перезагрузка компьютера
#===================================================
def show_timer():
    monitors = get_monitors()
    #print(monitors)
    try:
        match config.SCREEN_CONFIG:
            case 11:
                left_monitor = monitors[1]
                center_x = left_monitor.x + left_monitor.width / 2
                center_y = left_monitor.y + left_monitor.height / 2
            case 12:
                center_monitor = monitors[0]
                center_x = center_monitor.x + center_monitor.width / 2
                center_y = center_monitor.y + center_monitor.height / 2
            case 13:

                right_monitor = monitors[1]
                center_x = right_monitor.x + right_monitor.width / 2
                center_y = right_monitor.y + right_monitor.height / 2
            case 2:
                center_monitor = monitors[0]
                center_x = center_monitor.x + center_monitor.width / 2
                center_y = center_monitor.y + center_monitor.height / 2
    except: raise ValueError("Неправильный код конфигурации экрана")

    pyautogui.moveTo(center_x + 50, center_y)
    pyautogui.moveTo(center_x - 50, center_y, 0.5)
#===================================================
def lclick():
    monitors = get_monitors()
    #print(monitors)
    try:
        match config.SCREEN_CONFIG:
            case 11:
                left_monitor = monitors[1]
                center_x = left_monitor.x + left_monitor.width / 2
                center_y = left_monitor.y + left_monitor.height / 2
            case 12:
                center_monitor = monitors[0]
                center_x = center_monitor.x + center_monitor.width / 2
                center_y = center_monitor.y + center_monitor.height / 2
            case 13:

                right_monitor = monitors[1]
                center_x = right_monitor.x + right_monitor.width / 2
                center_y = right_monitor.y + right_monitor.height / 2
            case 2:
                center_monitor = monitors[0]
                center_x = center_monitor.x + center_monitor.width / 2
                center_y = center_monitor.y + center_monitor.height / 2
    except: raise ValueError("Неправильный код конфигурации экрана")

    pyautogui.moveTo(center_x + 50, center_y)
    pyautogui.click()
    print('Left Click')
#===================================================
def skip_kinopoisk():
    #pyautogui.moveTo(-111, 888, duration=0.1)
    pyautogui.click(-111, 888)
#===================================================
def skip_jutsu():
    pyautogui.click(-1800, 1012)
#===================================================
def start():
    mb.showinfo("приятного пользования", "Удаленный ассистен телеграмм запущен!")
#===================================================
def change_to_speakers():
    subprocess.call("C:\\assistbot\\nircmd.exe setdefaultsounddevice \"2.1\" 1", creationflags=0x08000000)

def change_to_headset():
    subprocess.call("C:\\assistbot\\nircmd.exe setdefaultsounddevice \"наушники\" 1", creationflags=0x08000000)
def monitor_off():
    subprocess.call("C:\\assistbot\\nircmd.exe monitor off", creationflags=0x08000000)
def monitor_on():
    subprocess.call("C:\\assistbot\\nircmd.exe monitor on", creationflags=0x08000000)

def web_browser():
    webbrowser.open_new_tab("https://ntp.msn.com/edge/ntp")

def shutdown_timer(x):
    subprocess.call(f"shutdown /s /f /t {x*60}", creationflags=0x08000000)
