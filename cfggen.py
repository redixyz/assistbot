import getpass
import shutil

language = int(input("""CHOOSE LANGUAGE / ВЫБЕРИТЕ ЯЗЫК

        EN = 1 / RU = 2
               """))
if language == 2:
    monitor_count = int(input("Сколько мониторов вы используете? (число от 1 до 3):"))
    if monitor_count == 2:
        cinemapos = int(input("""\n какой монитор вы бы использовали для просмотра фильма?
        
                левый - 1 // правый - 2
                          """))

    if monitor_count == 1:
        cinemapos = 1

    if monitor_count == 3:
        cinemapos = int(input("""\n какой монитор вы бы использовали для просмотра фильма?
        
     левый - 1 // центральный - 2 // правый - 3
                                  """))

    volume_step = int(int(input('\n количество прибавляемой/убавляемой громкости с помощью бота за 1 нажатие. (только четные числа!. рекомендуется 2): '))/2)
    if volume_step % 2 == 0:
        print('ТОЛЬКО ЧЕТНЫЕ ЧИСЛА!!!!')
        input('хорошо?')
    else:
        token = input("Токен телеграм бота: ")
        user = int(input('ваш id в телеграмме (getmyid_bot): '))

if language == 1:
    monitor_count = int(input("How many monitors are you using? (a number from 1 to 3):"))
    if monitor_count == 2:
        cinemapos = int(input("""\n Which monitor would you use for watching movies?

        Left - 1 // Right - 2
        """))

    if monitor_count == 1:
        cinemapos = 1

    if monitor_count == 3:
        cinemapos = int(input("""\n Which monitor would you use for watching movies?

        Left - 1 // Center - 2 // Right - 3
        """))

    volume_step = int(int(input('\nVolume increment/decrement with the bot for 1 press. (only even numbers!. recommended 2): ')) / 2)
    if volume_step % 2 == 0:
        print('ONLY EVEN NUMBERS!!!!')
        input('k?')
    else:
        token = input("Telegram bot token: ")
        user = int(input('your tg id (getmyid_bot): '))

if monitor_count != 1:
    if cinemapos <= monitor_count:
        a = cinemapos
    moncfg = int('1' + str(a))
else:
    moncfg = 2

config = open('config.py', 'x')
with open('config.py', 'w') as cfg:
    cfg.write(f"""SCREEN_CONFIG = {moncfg}
volume_step = {volume_step}
BOT_TOKEN = \'{token}\'
user = {user}""")

if language == 1:
    x = int(input("""
do you want to add this bot to startup?
1 - yes
0 - no 
"""))

if language == 2:
    x = int(input("""
Желаете ли вы добавить этого бота в автозагрузку?
1 - да
0 - нет
"""))

if x == 1:
    shutil.copy('main.pyw', rf'C:\Users\{getpass.getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.pyw')
else: pass
