import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import sys
#sys.path.insert(1, "C:\\assistbot")
import config
import markups
import localfuncs
from utilcommands import misc

TOKEN = config.BOT_TOKEN
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


class UserState(StatesGroup):
    power = State()
    media = State()
    volume = State()
    cinema = State()
    secret = State()
    text = State()
    power_timer = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    if message.from_user.id == config.user:
        await message.answer("===== MAIN MENU! =====", reply_markup=markups.power_keyboard)
        await state.clear()
    else:
        await message.answer('u have no access')

@dp.message(F.text == '🎬')
async def cinema_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("===== CINEMA MENU =====", reply_markup=markups.cinema_keyboard)
    await state.set_state(UserState.cinema)



@dp.message(F.text == '🔋')
async def power_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("===== POWER MENU =====", reply_markup=markups.power_keyboard)
    await state.set_state(UserState.power)



@dp.message(F.text == '🎹')
async def media_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("===== MEDIA MENU =====", reply_markup=markups.media_keyboard)
    await state.set_state(UserState.media)


@dp.message(F.text == '👂')
async def volume_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("===== VOLUME MENU =====", reply_markup=markups.volume_keyboard)
    await message.answer('====CHOOSE SPEAKERS====',reply_markup=markups.inline_speaker())
    await state.set_state(UserState.volume)


@dp.message(UserState.cinema)
async def cinema_state(message: Message):
    if message.text == "⏯":
        localfuncs.lclick()
    elif message.text == "⏱":
        localfuncs.show_timer()
    elif message.text == '🌐':
        localfuncs.web_browser()


@dp.message(UserState.power)
async def power_state(message: Message, state: FSMContext):
    if message.text == "🛑":
        localfuncs.shutdown()
    if message.text == "🔄":
        localfuncs.reboot()
    if message.text == "🕓":
        await state.set_state(UserState.power_timer)
        await message.answer("write the time after which the pc will turn off:")


@dp.message(UserState.power_timer)
async def power_timer(message: Message, state: FSMContext):
    localfuncs.shutdown_timer(int(message.text))
    await message.answer("if u want to cancel timer write \'/cancel_timer\'")
    await state.clear()
    await state.set_state(UserState.power)
    await message.answer("===== MENU =====", reply_markup=markups.power_keyboard)


@dp.message(UserState.media)
async def media_state(message: Message):
    if message.text == "⏪":
        localfuncs.prev()
    elif message.text == "⏸":
        localfuncs.play()
    elif message.text == "⏩":
        localfuncs.next()

@dp.message(UserState.volume)
async def volume_state(message: Message):
    if message.text == "➕":
        for i in range(config.volume_step):
            localfuncs.volume_up()
    elif message.text == "🔇":
        localfuncs.volumemute()
    elif message.text == "➖":
        for i in range(config.volume_step):
            localfuncs.volume_down()


async def main():
    dp.include_router(misc)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
