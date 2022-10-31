from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import pyautogui
import tkinter.messagebox as mb
import config
import win32api, win32con
import time
import os
import random
import threading

#SHIT!
storage = MemoryStorage()
bot = Bot(token = config.MAIN_BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

#BUTTONS!
#===================================================
button_power_menu = KeyboardButton("🔋")
button_power_of = KeyboardButton("🛑")
button_reboot = KeyboardButton("🔄")
#===================================================
button_media_menu = KeyboardButton("🎹")
button_previous = KeyboardButton("⏪")
button_pause = KeyboardButton("⏸")
button_next = KeyboardButton("⏩")
#===================================================
button_volume_menu = KeyboardButton("🔉")
button_volume_plus = KeyboardButton("➕")
button_volume_mute = KeyboardButton("🔇")
button_volume_minus = KeyboardButton("➖")
#===================================================
button_cinema_menu = KeyboardButton("🎬")
button_show_timer = KeyboardButton("⏱")
button_click = KeyboardButton("⏯")
#===================================================
button_error = KeyboardButton("🟥")
button_warning = KeyboardButton("🟨")
button_info = KeyboardButton("🟦")
button_exit = KeyboardButton("❌")

#KEYBOARDS!
#===================================================
power_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_power_of, button_reboot).row(button_power_menu,button_media_menu,button_volume_menu,button_cinema_menu )
media_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_previous, button_pause, button_next).row(button_power_menu,button_media_menu,button_volume_menu,button_cinema_menu )
volume_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_volume_plus, button_volume_mute, button_volume_minus).row(button_power_menu,button_media_menu,button_volume_menu,button_cinema_menu )
cinema_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_show_timer, button_click).row(button_power_menu,button_media_menu,button_volume_menu,button_cinema_menu )
secret_various_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_error, button_warning, button_info).row(button_exit)
exit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_exit)
#===================================================

#FSM!
class UserState(StatesGroup):
    power = State()
    media = State()
    volume = State()
    cinema = State()
    secret = State()
    secret_various = State()
    secret_title = State()
    secret_label = State()

#BOT FUNCTIONS!
#===================================================
@dp.message_handler(Text(equals="/r"), state= "*")
async def restart(message: types.Message, state: FSMContext):
    await message.answer("==== BOT RESTARTED! =====",reply_markup=power_keyboard)
    await state.finish()
#===================================================
@dp.message_handler()
async def selector(message: types.Message, state: FSMContext):
    if message.text == "🎬":
        await state.finish()
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()

    elif message.text == "🔋":
        await state.finish()
        await message.answer("===== POWER MENU =====", reply_markup= power_keyboard)
        await UserState.power.set()
    elif message.text == "🎹":
        await state.finish()
        await message.answer("===== MEDIA MENU =====", reply_markup= media_keyboard)
        await UserState.media.set()
    elif message.text == "/secret":
        await message.answer("""u come to secret menu!!
            select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    elif message.text == "🔉":
        await state.finish()
        await message.answer("===== VOLUME MENU ====", reply_markup= volume_keyboard)
        await UserState.volume.set()
#===================================================
@dp.message_handler(state=UserState.cinema)
async def cinema_state(message: types.Message):
    if message.text == "⏯":
        lclick()
    elif message.text == "⏱":
        show_timer()

    elif message.text == "🎬":
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()
    elif message.text == "🔋":
        await message.answer("===== POWER MENU =====", reply_markup= power_keyboard)
        await UserState.power.set()
    elif message.text == "🎹":
        await message.answer("===== MEDIA MENU =====", reply_markup= media_keyboard)
        await UserState.media.set()
    elif message.text == "🔉":
        await message.answer("===== VOLUME MENU ====", reply_markup= volume_keyboard)
        await UserState.volume.set()
    elif message.text == "/secret":
        await message.answer("""u come to secret menu!!
            select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    else:
        await message.answer("ERROR! iq?")
#===================================================
@dp.message_handler(state=UserState.power)
async def power_state(message: types.Message):
    if message.text == "🛑":
        shutdown()
    elif message.text == "🔄":
        reboot()

    elif message.text == "🎬":
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()
    elif message.text == "🔋":
        await message.answer("===== POWER MENU =====", reply_markup= power_keyboard)
        await UserState.power.set()
    elif message.text == "🎹":
        await message.answer("===== MEDIA MENU =====", reply_markup= media_keyboard)
        await UserState.media.set()
    elif message.text == "🔉":
        await message.answer("===== VOLUME MENU ====", reply_markup= volume_keyboard)
        await UserState.volume.set()
    elif message.text == "/secret":
        await message.answer("""u come to secret menu!!
            select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    else:
        await message.answer("ERROR! iq?")
#===================================================
@dp.message_handler(state=UserState.media)
async def media_state(message: types.Message):
    if message.text == "⏪":
        prev()
    elif message.text == "⏸":
        play()
    elif message.text == "⏩":
        next()


    elif message.text == "🎬":
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()
    elif message.text == "🔋":
        await message.answer("===== POWER MENU =====", reply_markup= power_keyboard)
        await UserState.power.set()
    elif message.text == "🎹":
        await message.answer("===== MEDIA MENU =====", reply_markup= media_keyboard)
        await UserState.media.set()
    elif message.text == "🔉":
        await message.answer("===== VOLUME MENU ====", reply_markup= volume_keyboard)
        await UserState.volume.set()
    elif message.text == "/secret":
        await message.answer("""u come to secret menu!!
            select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    else:
        await message.answer("ERROR! iq?")
@dp.message_handler(state=UserState.volume)
async def volume_state(message: types.Message):
    if message.text == "➕":
        for i in range(config.volume_step):
            volume_up()
    elif message.text == "🔇":
        volumemute()
    elif message.text == "➖":
        for i in range(config.volume_step):
            volume_down()


    elif message.text == "🎬":
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()
    elif message.text == "🔋":
        await message.answer("===== POWER MENU =====", reply_markup= power_keyboard)
        await UserState.power.set()
    elif message.text == "🎹":
        await message.answer("===== MEDIA MENU =====", reply_markup= media_keyboard)
        await UserState.media.set()
    elif message.text == "🔉":
        await message.answer("===== VOLUME MENU ====", reply_markup= volume_keyboard)
        await UserState.volume.set()
    elif message.text == "/secret":
        await message.answer("""u come to secret menu!!
            select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    else:
        await message.answer("ERROR! iq?")
@dp.message_handler(Text(equals="/secret"))
async def secret_set(message: types.Message):
    await message.answer("""u come to secret menu!!
    select sign type""", reply_markup= secret_various_keyboard)
    await UserState.secret_various.set()
@dp.message_handler(state=UserState.secret_various)
async def secret_various_selector(message: types.Message, state: FSMContext):
    if message.text == "🟥":
        await state.update_data(various = "error")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup= exit_keyboard)
    elif message.text == "🟨":
        await state.update_data(various = "warning")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup= exit_keyboard)
    elif message.text == "🟦":
        await state.update_data(various = "info")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup= exit_keyboard)
    elif message.text == "❌":
        await state.finish()
        await UserState.power.set()
    else:
        await message.answer("ERROR!!!!! IQ????", reply_markup = power_keyboard)
        await state.finish()
        await UserState.power.set()
@dp.message_handler(state=UserState.secret_label)
async def secret_label(message: types.Message, state: FSMContext):
    if message.text == "❌":
        await state.finish()
        await UserState.power.set()
    else:
        await state.update_data(label=str(message.text))
        await message.answer("then text sign title", reply_markup= exit_keyboard)
        await UserState.secret_title.set()
@dp.message_handler(state = UserState.secret_title)
async def secret_title(message: types.Message, state: FSMContext):
    if message.text == "❌":
        await state.finish()
        await UserState.power.set()
        await message.answer("===== MENU =====", reply_markup=power_keyboard)
    else:
        await state.update_data(title=str(message.text))
        data = await state.get_data()
        t = threading.Thread(target=show_secret, args=(data["various"], data["label"], data["title"]))
        t.start()
        await state.finish()
        await UserState.power.set()
        await message.answer("===== MENU =====", reply_markup= power_keyboard)

#EXTRA FUNCTIONS!
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
    os.system("shutdown /s /t 0 ")
#===================================================
def reboot():
    os.system("shutdown /r /t 0 ")
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
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('Left Click')
#===================================================
def show_secret(various, label, title):
    if various == "error":
        mb.showerror(label, title)
    elif various == "warning":
        mb.showwarning(label, title)
    elif various == "info":
        mb.showinfo(label, title)
#===================================================
def start():
    mb.showinfo("ВСЕ ЗАЕБИСЬ (НЕТ)", "Удаленный ассистен телеграмм запущен!")
#===================================================


#ENTER POINT!
if __name__ == "__main__":
    thread = threading.Thread(target=start)
    thread.start()
    executor.start_polling(dp, skip_updates=True)

