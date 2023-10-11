from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#===================================================
button_power_menu = KeyboardButton("🔋")
button_power_of = KeyboardButton("🛑")
button_power_timer = KeyboardButton("🕓")
button_reboot = KeyboardButton("🔄")
#===================================================
button_media_menu = KeyboardButton("🎹")
button_previous = KeyboardButton("⏪")
button_pause = KeyboardButton("⏸")
button_next = KeyboardButton("⏩")
#===================================================
button_volume_menu = KeyboardButton("👂")
button_volume_plus = KeyboardButton("➕")
button_volume_mute = KeyboardButton("🔇")
button_volume_minus = KeyboardButton("➖")
#===================================================
button_cinema_menu = KeyboardButton("🎬")
button_show_timer = KeyboardButton("⏱")
button_click = KeyboardButton("⏯")
button_browser = KeyboardButton("🌐")
#===================================================
# button_error = KeyboardButton("🟥")
# button_warning = KeyboardButton("🟨")
# button_info = KeyboardButton("🟦")
button_exit = KeyboardButton("❌")
#===================================================
row_buttons = [button_power_menu,button_media_menu,button_volume_menu,button_cinema_menu]

power_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_power_of, button_power_timer, button_reboot).row(*row_buttons)
media_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_previous, button_pause, button_next).row(*row_buttons)
volume_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_volume_plus, button_volume_mute, button_volume_minus).row(*row_buttons)
cinema_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_show_timer, button_click,button_browser).row(*row_buttons)
#secret_various_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_error, button_warning, button_info).row(button_exit)
exit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_exit)
power_timer_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_exit)
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# button_volume_headset = InlineKeyboardButton(text ="🎧", callback_data = 'headset')
# button_volume_speakers = InlineKeyboardButton(text="🔈", callback_data = 'speakers')
# volume_inline_keyboard = InlineKeyboardMarkup(row_width=2).add(button_volume_headset, button_volume_speakers)