import getpass
import shutil
import os
import zipfile
import subprocess
import ctypes
import threading

#subprocess.call('python.exe -m pip install --upgrade pip', creationflags=0x08000000)
#subprocess.call('pip install -r requirements.txt', creationflags=0x08000000)
import requests
import dearpygui.dearpygui as dpg
import screeninfo


def config():
    dpg.create_context()
    with dpg.font_registry():
        default_font = dpg.add_font(r"data\Kanit-SemiBold.ttf", 20)
        second_font = dpg.add_font(r"data\Kanit-Black.ttf", 26)

    def confirm_handler():
        dpg.stop_dearpygui()

    def save_callback(sender):
        dpg.configure_item('main_window', show=False)
        dpg.configure_item('confirm_window', show=True)
        dpg.set_primary_window('main_window', False)
        dpg.set_primary_window('confirm_window', True)

        display_count = dpg.get_value('display_count')
        first_m, second_m, third_m = dpg.get_value('first_m'), dpg.get_value('second_m'), dpg.get_value('third_m')
        first_d, second_d, third_d = dpg.get_value('first_d'), dpg.get_value('second_d'), dpg.get_value('third_d')

        moncfg = 1 if display_count == 1 else (
            211 if first_m and first_d else 212 if display_count == 2 else (
                311 if first_m and first_d else 312 if first_m and second_d else 313 if first_m else (
                    321 if second_m and first_d else 322 if second_m and second_d else 323 if second_m else (
                        331 if third_m and first_d else 332 if third_m and second_d else 333
                    ))))

        global parametrs
        parametrs = [dpg.get_value('token'), dpg.get_value('user_id'), dpg.get_value('volume_step'), moncfg]

        dpg.set_value('second_window_text', f"""BOT TOKEN: {parametrs[0]}
USER ID: {parametrs[1]}
VOLUME STEP: {parametrs[2]}
MONITOR CONFIG: {parametrs[3]}""")

    def back_btn_handler():
        dpg.configure_item('main_window', show=True)
        dpg.configure_item('confirm_window', show=False)
        dpg.set_primary_window('main_window', True)
        dpg.set_primary_window('confirm_window', False)

    def callback_error():
        if not (dpg.get_value('volume_step')) == '':
            if int(dpg.get_value('volume_step')) % 2 != 0:
                dpg.set_value('even_text', 'ONLY EVEN NUMBERS!')
                dpg.configure_item("save_button", enabled=False)
            else:
                dpg.set_value('even_text', '')
                dpg.configure_item("save_button", enabled=True)

    def checkbox_handler():
        display_count = dpg.get_value('display_count')

        items_to_configure = {
            1: [('select_display', False), ('second_m', False), ('third_m', False),
                ('first_d', False), ('second_d', False), ('third_d', False)],
            2: [('select_display', True), ('first_d', True), ('second_m', True),
                ('third_m', False), ('second_d', True), ('third_d', False)],
            3: [('select_display', True), ('first_d', True), ('second_m', True),
                ('third_m', True), ('second_d', True), ('third_d', True)]
        }

        for item, state in items_to_configure.get(display_count, []):
            dpg.configure_item(item, show=state)

        first_m, second_m, third_m = dpg.get_value('first_m'), dpg.get_value('second_m'), dpg.get_value('third_m')
        dpg.configure_item('first_m', enabled=not second_m and not third_m)
        dpg.configure_item('second_m', enabled=not first_m and not third_m)
        dpg.configure_item('third_m', enabled=not first_m and not second_m)

        first_d, second_d, third_d = dpg.get_value('first_d'), dpg.get_value('second_d'), dpg.get_value('third_d')
        dpg.configure_item('first_d', enabled=not second_d and not third_d)
        dpg.configure_item('second_d', enabled=not first_d and not third_d)
        dpg.configure_item('third_d', enabled=not first_d and not second_d)

    with dpg.window(tag='main_window', no_collapse=True, no_resize=True, no_close=True,
                    no_move=True):

        token_input = dpg.add_input_text(label='BOT TOKEN', height=40, no_spaces=True,
                                         tag="token")
        user_id_input = dpg.add_input_text(label='USER ID', height=40, no_spaces=True,
                                           tag='user_id')
        volume_step_input = dpg.add_input_text(label='VOLUME STEP', callback=callback_error, height=40, no_spaces=True,
                                               tag='volume_step', default_value='2')
        monitor_count_input = dpg.add_slider_int(label='DISPLAY COUNT', height=40,
                                                 tag='display_count', callback=checkbox_handler,
                                                 min_value=1, max_value=3, default_value=1, no_input=True)

        dpg.add_text('', tag='even_text')
        dpg.add_text('select primary display')
        with dpg.group(horizontal=True):
            dpg.add_checkbox(label='1', show=True, tag='first_m', callback=checkbox_handler)
            dpg.add_checkbox(label='2', show=False, tag='second_m', callback=checkbox_handler)
            dpg.add_checkbox(label='3', show=False, tag='third_m', callback=checkbox_handler)
        dpg.add_text('select a display for watching movies', tag='select_display', show=False)
        with dpg.group(horizontal=True):
            dpg.add_checkbox(label='1', show=False, tag='first_d', callback=checkbox_handler)
            dpg.add_checkbox(label='2', show=False, tag='second_d', callback=checkbox_handler)
            dpg.add_checkbox(label='3', show=False, tag='third_d', callback=checkbox_handler)
        dpg.add_button(label='SAVE', callback=save_callback, width=200, height=40, pos=[150, 300], tag='save_button')
        dpg.bind_font(default_font)
        dpg.bind_item_font('save_button', second_font)

    with dpg.window(tag='confirm_window', width=500, height=400, no_collapse=True, no_resize=True, no_close=True,
                    no_move=True, show=False):
        dpg.add_text('', tag='second_window_text')
        dpg.add_button(label='CONFIRM', callback=confirm_handler, width=100, height=40, pos=[290, 300],
                       tag='confirm_btn')
        dpg.add_button(label='BACK', callback=back_btn_handler, width=100, height=40, pos=[150, 300],
                       tag='back_btn')
        dpg.bind_font(default_font)
        dpg.bind_item_font('confirm_btn', second_font)
        dpg.bind_item_font('back_btn', second_font)
    mon_x, mon_y = next((monitor.width, monitor.height) for monitor in screeninfo.get_monitors() if monitor.is_primary)
    with dpg.theme() as global_theme:

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 6, 6, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 20, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 20, 2, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 20, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 6, 6, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 20, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 20, 2, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 20, category=dpg.mvThemeCat_Core)

    dpg.bind_theme(global_theme)

    # dpg.show_style_editor()

    dpg.create_viewport(title='AssistBot Setup', width=540, height=400, resizable=False, x_pos=mon_x // 2 - 270,
                        y_pos=mon_y // 2 - 200, large_icon='data/ico.ico', small_icon='data/ico.ico')
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('main_window', True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def nircmd_setup(dest):
    link = 'https://www.nirsoft.net/utils/nircmd-x64.zip'
    with open('nircmd.zip', 'wb') as f:
        f.write(requests.get(link).content)

    with zipfile.ZipFile('nircmd.zip', 'r') as archive:
        archive.extract('nircmd.exe', dest)

    os.remove('nircmd.zip')


def main():
    source = ['localfuncs.py', 'markups.py', 'utilcommands.py']
    dest = 'C://assistbot'

    shutil.rmtree(dest, ignore_errors=True)
    os.makedirs(dest)

    config()
    user, volume_step, moncfg = map(int, parametrs[1:4])
    token = str(parametrs[0])

    nircmd_setup(dest)

    for file in source:
        shutil.copy(os.path.join(os.getcwd(), 'bot', file), dest)

    shutil.copy(
        os.path.join(os.getcwd(), 'bot', 'main.py'),
        os.path.join(
            'C:\\Users', getpass.getuser(),
            'AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\main.pyw'
        )
    )

    config_content = f"""
SCREEN_CONFIG = {moncfg}
volume_step = {volume_step // 2}
BOT_TOKEN = '{token}'
user = {user}"""

    with open('config.py', 'w') as cfg:
        cfg.write(config_content)
    shutil.move('config.py', dest)


def cwindow():
    ctypes.windll.user32.MessageBoxW(None, 'just wait few seconds\nrequirements are downloading', 'notification', 0)


if __name__ == '__main__':
    thread = threading.Thread(target=cwindow)
    thread.start()
    config()
