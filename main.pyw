from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import threading
import keyboard
# local
import sys
sys.path.insert(1, "E:\\my\\python\\assist20")
import config
import markups
import localfuncs
# SHIT!
storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

# KEYBOARDS!
power_keyboard = markups.power_keyboard
media_keyboard = markups.media_keyboard
volume_inline_keyboard = markups.volume_inline_keyboard
volume_keyboard = markups.volume_keyboard
cinema_keyboard = markups.cinema_keyboard
secret_various_keyboard = markups.secret_various_keyboard
exit_keyboard = markups.exit_keyboard
users = [1657230088, 778425555]

class UserState(StatesGroup):
    power = State()
    media = State()
    volume = State()
    cinema = State()
    secret = State()
    secret_various = State()
    secret_title = State()
    secret_label = State()
    text = State()
    power_timer = State()


@dp.callback_query_handler(lambda c: c.data == 'speakers')
async def audiodevice(callback_query: types.CallbackQuery):
    await callback_query.answer()
    localfuncs.change_to_speakers()
    await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'headset')
async def audiodevice(callback_query: types.CallbackQuery):
    await callback_query.answer()
    localfuncs.change_to_headset()
    await callback_query.answer()


@dp.message_handler(Text(equals='/monitor_off'), state='*')
async def monitor_off(message: types.Message):
    if message.from_user.id in users:
        localfuncs.monitor_off()
    else:
        await message.answer('u have no access')

@dp.message_handler(Text(equals='/browser'), state='*')
async def browser(message: types.Message):
    if message.from_user.id in users:
        localfuncs.web_browser()
    else:
        await message.answer('u have no access')

@dp.message_handler(Text(equals='/monitor_on'), state='*')
async def monitor_off(message: types.Message):
    if message.from_user.id in users:
        localfuncs.monitor_on()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='/kskip'), state='*')
async def kskip(message: types.Message):
    if message.from_user.id in users:
        localfuncs.skip_kinopoisk()
    else:
        await message.answer('u have no access')

@dp.message_handler(Text(equals='/jutskip'), state='*')
async def kskip(message: types.Message):
    if message.from_user.id in users:
        localfuncs.skip_jutsu()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='/speakers'), state='*')
async def speakersasshort(message: types.Message):
    if message.from_user.id in users:
        localfuncs.change_to_speakers()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='/headset'), state='*')
async def headsetshort(message: types.Message):
    if message.from_user.id in users:
        localfuncs.change_to_headset()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(startswith='/t'), state='*')
async def textwritershort(message: types.Message):
    if message.from_user.id in users:
        keyboard.write(message.text.replace('/t ', ''))
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals="❌"), state='*')
async def overrides(message: types.Message, state: FSMContext):
    await message.answer("===== MAIN MENU! =====", reply_markup=power_keyboard)
    await state.finish()


@dp.message_handler(Text(equals="/r"), state="*")
async def restart(message: types.Message, state: FSMContext):
    await message.answer("===== MAIN MENU! =====", reply_markup=power_keyboard)
    await state.finish()


@dp.message_handler(Text(equals="/secret"), state='*')
async def secret(message: types.Message):
    if message.from_user.id in users:
        await message.answer("""u come to secret menu!!
               select sign type""", reply_markup=secret_various_keyboard)
        await UserState.secret_various.set()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='🎬'), state='*')
async def cinema_menu(message: types.Message, state: FSMContext):
    if message.from_user.id in users:
        await state.finish()
        await message.answer("===== CINEMA MENU =====", reply_markup=cinema_keyboard)
        await UserState.cinema.set()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='🔋'), state='*')
async def power_menu(message: types.Message, state: FSMContext):
    if message.from_user.id in users:
        await state.finish()
        await message.answer("===== POWER MENU =====", reply_markup=power_keyboard)
        await UserState.power.set()
    else:
        await message.answer('u have no acces')

@dp.message_handler(Text(equals='🎹'), state='*')
async def media_menu(message: types.Message, state: FSMContext):
    if message.from_user.id in users:
        await state.finish()
        await message.answer("===== MEDIA MENU =====", reply_markup=media_keyboard)
        await UserState.media.set()
    else:
        await message.answer('u have no access')



@dp.message_handler(Text(equals='👂'), state='*')
async def volume_menu(message: types.Message, state: FSMContext):
    if message.from_user.id in users:
        await state.finish()
        await message.answer("===== VOLUME MENU =====", reply_markup=volume_keyboard)
        await message.answer("SELECT DEFAULT DEVICE!", reply_markup=volume_inline_keyboard)
        await UserState.volume.set()
    else:
        await message.answer('u have no access')



@dp.message_handler(state=UserState.cinema)
async def cinema_state(message: types.Message):
    if message.text == "⏯":
        localfuncs.lclick()
    elif message.text == "⏱":
        localfuncs.show_timer()
    elif message.text == '🌐':
        localfuncs.web_browser()

@dp.message_handler(state=UserState.power)
async def power_state(message: types.Message):
    if message.text == "🛑":
        localfuncs.shutdown()
    if message.text == "🔄":
        localfuncs.reboot()
    if message.text == "🕓":
        await UserState.power_timer.set()
        await message.answer("write the time after which the pc will turn off:")


@dp.message_handler(state=UserState.power_timer)
async def power_timer(message: types.Message, state: FSMContext):
    localfuncs.shutdown_timer(int(message.text))
    await message.answer("if u want to cancel timer write \'/cancel_timer\'")
    await state.finish()
    await UserState.power.set()
    await message.answer("===== MENU =====", reply_markup=power_keyboard)

@dp.message_handler(state=UserState.media)
async def media_state(message: types.Message):
    if message.text == "⏪":
        localfuncs.prev()
    elif message.text == "⏸":
        localfuncs.play()
    elif message.text == "⏩":
        localfuncs.next()


@dp.message_handler(state=UserState.volume)
async def volume_state(message: types.Message):
    if message.text == "➕":
        for i in range(config.volume_step):
            localfuncs.volume_up()
    elif message.text == "🔇":
        localfuncs.volumemute()
    elif message.text == "➖":
        for i in range(config.volume_step):
            localfuncs.volume_down()


@dp.message_handler(state=UserState.secret_various)
async def secret_various_selector(message: types.Message, state: FSMContext):
    if message.text == "🟥":
        await state.update_data(various="error")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup=exit_keyboard)
    elif message.text == "🟨":
        await state.update_data(various="warning")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup=exit_keyboard)
    elif message.text == "🟦":
        await state.update_data(various="info")
        await UserState.secret_label.set()
        await message.answer("then text sign label", reply_markup=exit_keyboard)
    else:
        await message.answer("ERROR!!!!! IQ????", reply_markup=power_keyboard)
        await state.finish()
        await UserState.power.set()


@dp.message_handler(state=UserState.secret_label)
async def secret_label(message: types.Message, state: FSMContext):
    await state.update_data(label=str(message.text))
    await message.answer("then text sign title", reply_markup=exit_keyboard)
    await UserState.secret_title.set()


@dp.message_handler(state=UserState.secret_title)
async def secret_title(message: types.Message, state: FSMContext):
    await state.update_data(title=str(message.text))
    data = await state.get_data()
    t = threading.Thread(target=localfuncs.show_secret, args=(data["various"], data["label"], data["title"]))
    t.start()
    await state.finish()
    await UserState.power.set()
    await message.answer("===== MENU =====", reply_markup=power_keyboard)


# ENTER POINT!
if __name__ == "__main__":
    thread = threading.Thread(target=localfuncs.start)
    thread.start()
    executor.start_polling(dp, skip_updates=True)

