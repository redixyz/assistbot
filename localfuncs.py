import pyautogui
import os
import random
import config
import tkinter.messagebox as mb
import webbrowser
import keyboard
pyautogui.FAILSAFE = False

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
    os.system("shutdown /s /f /t 0 ")
#===================================================
def reboot():
    os.system("shutdown /r /f /t 0 ")
#===================================================
def show_timer():
    SCREEN_X = random.randint(500, 525)
    SCREEN_Y = random.randint(400, 420)
    SCREEN_13X = SCREEN_X + 600
    if config.SCREEN_CONFIG == 11:
        pyautogui.moveTo(-SCREEN_X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 12:
        pyautogui.moveTo(SCREEN_X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 13:
        pyautogui.moveTo(SCREEN_13X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 2:
        pyautogui.moveTo(SCREEN_X, SCREEN_Y , duration=0.5)
#===================================================
def lclick():
    SCREEN_X = random.randint(500, 525)
    SCREEN_Y = random.randint(400, 420)
    SCREEN_13X = SCREEN_X + 600
    if config.SCREEN_CONFIG == 11:
        pyautogui.moveTo(-SCREEN_X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 12:
        pyautogui.moveTo(SCREEN_X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 13:
        pyautogui.moveTo(SCREEN_13X, SCREEN_Y, duration=0.5)
    elif config.SCREEN_CONFIG == 2:
        pyautogui.moveTo(SCREEN_X, SCREEN_Y, duration=0.5)
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
# def show_secret(various, label, title):
#     if various == "error":
#         mb.showerror(label, title)
#     elif various == "warning":
#         mb.showwarning(label, title)
#     elif various == "info":
#         mb.showinfo(label, title)
#===================================================
def start():
    mb.showinfo("приятного пользования", "Удаленный ассистен телеграмм запущен!")
#===================================================
def change_to_speakers():
    os.system("C:\\assistbot\\nircmd.exe setdefaultsounddevice \"2.1\" 1")
def change_to_headset():
    os.system("C:\\assistbot\\nircmd.exe setdefaultsounddevice \"Динамики\" 1")
def monitor_off():
    os.system("C:\\assistbot\\nircmd.exe monitor off")
def monitor_on():
    os.system("C:\\assistbot\\nircmd.exe monitor on")

def web_browser():
    webbrowser.open('google.com')

def shutdown_timer(x):
    os.system(f"shutdown /s /f /t {x*60}")
