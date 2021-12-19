import re
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

mouse = Controller()


#this programm only works when whatsapp web is on the Main window in full screen mode
class WhatsApp:
    def __init__(self, speed=-0.5, click_speed = .3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        self.response = 'test'

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_circle.png', confidence= 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration =self.speed)
            pt.click()
        except Exception as e:
            print('Exception (nav_green_dot)', e)

    def nav_text_box(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence= 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration =self.speed)
            pt.click()
        except Exception as e:
            print('Exception (nav_text_box)', e)
    def nav_message(self):
        try:
            position = pt.locateOnScreen('paper_clip.png', confidence= 0.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(120, -40, duration =self.speed)
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
            print('Exception (get_message)',e)

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
            pt.click(button='RIGHT')
            pt.moveRel(10, -100, duration=self.speed)
            pt.click()
        except Exception as e:
            print('Exception respond)', e)

    def send_message(self):
        try:
           position = pt.locateOnScreen('paper_plane.png')
           pt.moveTo(position[0:2], duration = self.speed)
           pt.moveRel(10, 10, duration = self.speed)
           pt.click()
        except Exception as e:
            print('Exception(send_message)', e)







wa_bot = WhatsApp(speed=.5,click_speed=.3)
sleep(2)
wa_bot.nav_green_dot()
wa_bot.nav_message()
wa_bot.get_message()
wa_bot.process_message()
wa_bot.nav_text_box()
wa_bot.respond()
wa_bot.send_message()



