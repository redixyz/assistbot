from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def inline_speaker():
    speaker_inline_buttons = [
        [InlineKeyboardButton(text='🔈', callback_data='change_to_speakers')],
        [InlineKeyboardButton(text='🎧', callback_data='change_to_headset')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=speaker_inline_buttons)

# reply keyboard buttons

button_power_menu = KeyboardButton(text="🔋")
button_power_of = KeyboardButton(text="🛑")
button_power_timer = KeyboardButton(text="🕓")
button_reboot = KeyboardButton(text="🔄")

button_media_menu = KeyboardButton(text="🎹")
button_previous = KeyboardButton(text="⏪")
button_pause = KeyboardButton(text="⏸")
button_next = KeyboardButton(text="⏩")

button_volume_menu = KeyboardButton(text="👂")
button_volume_plus = KeyboardButton(text="➕")
button_volume_mute = KeyboardButton(text="🔇")
button_volume_minus = KeyboardButton(text="➖")

button_cinema_menu = KeyboardButton(text="🎬")
button_show_timer = KeyboardButton(text="⏱")
button_click = KeyboardButton(text="⏯")
button_browser = KeyboardButton(text="🌐")

button_exit = KeyboardButton(text="❌")

row_buttons = [
    button_power_menu, button_media_menu, button_volume_menu, button_cinema_menu
]

# reply keyboard layouts
power_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[[button_power_of, button_power_timer, button_reboot], row_buttons])

media_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[[button_previous, button_pause, button_next], row_buttons])

volume_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[[button_volume_plus, button_volume_mute, button_volume_minus], row_buttons])

cinema_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[[button_show_timer, button_click, button_browser], row_buttons])
