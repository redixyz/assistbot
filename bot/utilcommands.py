import keyboard
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import CallbackQuery
import localfuncs
import markups
from aiogram.filters import Command, StateFilter
import pyautogui

misc = Router(name=__name__)


@misc.callback_query(F.data == 'change_to_headset')
async def change_to_headset(call: CallbackQuery):
    try:
        localfuncs.change_to_headset()
        await call.answer()
    except:
        await call.answer(
            text="не ворк даун",
            show_alert=True
        )


@misc.callback_query(F.data == 'change_to_speakers')
async def change_to_speakers(call: CallbackQuery):
    try:
        localfuncs.change_to_speakers()
        await call.answer()
    except:
        await call.answer(
            text="не ворк даун",
            show_alert=True
        )


@misc.message(Command('monitor_off'), StateFilter(None))
async def monitor_off(message: Message):
    localfuncs.monitor_off()


@misc.message(F=="⏱",StateFilter(None))
async def show_timer(message:Message):
    localfuncs.show_timer()


@misc.message(F=="⏯",StateFilter(None))
async def pause_film(message: Message):
    localfuncs.lclick()

@misc.message(Command('monitor_on'), StateFilter(None))
async def monitor_off(message: Message):
    localfuncs.monitor_on()


@misc.message(Command('browser'), StateFilter(None))
async def browser(message: Message):
    localfuncs.web_browser()


@misc.message(Command('kskip'), StateFilter(None))
async def kskip():
    localfuncs.skip_kinopoisk()


@misc.message(Command('jutskip'), StateFilter(None))
async def kskip(message: Message):
    localfuncs.skip_jutsu()


@misc.message(F.text.startswith('/t'), StateFilter(None))
async def textwritershort(message: Message):
    pyautogui.write(message.text.replace('/t ', '', 1))


@misc.message(F == "❌", StateFilter(None))
async def overrides(message: Message, state: FSMContext):
    await message.answer("===== MAIN MENU! =====", reply_markup=markups.power_keyboard)
    await state.clear()


@misc.message(Command("start"), StateFilter(None))
async def restart(message: Message, state: FSMContext):
    await message.answer("===== MAIN MENU! =====", reply_markup=markups.power_keyboard)
    await state.clear()
