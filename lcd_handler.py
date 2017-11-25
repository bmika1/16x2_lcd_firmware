from Adafruit_CharLCD import Adafruit_CharLCD
import rss_parser
import time

class LcdHanlder:

    def __init__(self):
        self.lcd = Adafruit_CharLCD(rs=26, en=19,
                               d4=13, d5=6, d6=5, d7=11,
                               cols=16, lines=2)
        self.r_parser = rss_parser.RssParser()


    def display_rss(self):

        to_display = self.r_parser.refresh_reuters()
        self.lcd.clear()
        self.lcd.message(to_display)
        for x in range(len(to_display)):
            self.lcd.move_left()
            time.sleep(1)




