import re
import pyautogui as pt
import pyperclip as pc
from pynput.keyboard import Controller, Key
from time import sleep

keyboard = Controller()


# this programm only works when whatsapp web is on the Main window in full screen mode
# TODO: remove all repetitions
class WhatsApp:
    def __init__(self, speed=-0.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        self.response = 'test'
        self.reciever_name = ''

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_circle.png', confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.click()
        except Exception as e:
            print('Exception (nav_green_dot)', e)

    def nav_text_box(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.click()
        except Exception as e:
            print('Exception (nav_text_box)', e)

    def nav_message(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence=0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(120, -40, duration=self.speed)
        except Exception as e:
            print('Exception (nav_message)', e)

    def get_message(self):
        try:
            pt.tripleClick(interval=self.click_speed)
            pt.click(button='RIGHT')
            pt.moveRel(10, 10, duration=self.speed)
            pt.click()
            self.message = pc.paste().lower()
            print('User says: ' + self.message)
        except Exception as e:
            print('Exception (get_message)', e)

    def process_message(self):
        try:
            x = re.search("hausaufgaben", self.message.lower()) or re.search("helf", self.message.lower())
            if x:
                self.response = 'Nein, geh schlafen'
            else:
                self.response = 'test'
        except Exception as e:
            print('Exception (process_message)', e)

    def respond(self):
        try:
            pc.copy(self.response)
            pt.hotkey('ctrl', 'v')
        except Exception as e:
            print('Exception (respond)', e)

    def send_message(self):
        try:
            self.move_relative_to_image(image='paper_plane.png', x=10, y=10)
            pt.click()
        except Exception as e:
            print('Exception(send_message)', e)

    def open_contact_tab(self):
        try:
            position = pt.locateOnScreen('lupe.png')
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(50, 40, duration=self.speed)
            pt.click()
            pt.moveRel(0, 40, duration=self.speed)
            pt.click()
        except Exception as e:
            print('Exception(open_contact_tab)', e)

    def get_reciever_name(self):
        try:
            self.move_relative_to_image(image='call_icon.png', x=80, y=-70)
            pt.tripleClick()
            pt.hotkey('ctrl', 'c')
            self.move_relative_to_image(image='cross.png', x=20, y=10)
            pt.click()
            self.reciever_name = pc.paste()
            print('The Receiver is: ' + self.reciever_name)
        except Exception as e:
            print('Exception(open_contact_tab)', e)

    def move_relative_to_image(self, image, x, y):
        position = pt.locateOnScreen(image, confidence=0.6)
        pt.moveTo(position[0:2], duration=self.speed)
        pt.moveRel(x, y, duration=self.speed)

    def search_contact(self, contact_name):
        self.move_relative_to_image(image='dots.png', x=-40, y=70)
        pt.click()
        self.insert_text(contact_name)
        pt.moveRel(0, 100, duration=self.speed)
        pt.click()
        self.move_relative_to_image(image='cross.png', x=20, y=10)
        pt.click()

    def insert_text(self, contact_name):
        pc.copy(contact_name)
        pt.hotkey('ctrl', 'v')
        keyboard.release(Key.ctrl.value)



def spam_user(name, message, times):
    wa_bot.search_contact(contact_name= name)
    wa_bot.nav_text_box()
    wa_bot.response = message
    for x in range(times):
        wa_bot.respond()
        pt.hotkey('enter')


wa_bot = WhatsApp(speed=.5, click_speed=.3)
sleep(2)

# this part of code spamms a specified user
# spam_user(name='Joseph Stalin', message='komm csgo', times=20)

#wa_bot.send_message()

# gets reciever name
wa_bot.open_contact_tab()
sleep(1)
wa_bot.get_reciever_name()

# responds to new incomign message
# wa_bot.nav_green_dot()
# wa_bot.nav_message()
# wa_bot.get_message()
# wa_bot.process_message()
# wa_bot.nav_text_box()
# wa_bot.respond()
# wa_bot.send_message()
