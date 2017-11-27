from Adafruit_CharLCD import Adafruit_CharLCD
import rss_parser
import time
from datetime import datetime

class LcdHandler:

    def __init__(self):
        self.lcd = Adafruit_CharLCD(rs=26, en=19,
                                    d4=13, d5=6, d6=5, d7=11,
                                    cols=16, lines=2)
        self.r_parser = rss_parser.RssParser()

    def get_time(self, time_format):
        return datetime.now().strftime(time_format)

    #should be: top, bottom, scrolltop, scrollbottom, scrolinterval
    def display_string(self, time_format, bottom_text, scroll_speed=9, repeats = 5):

        sleep_time = 1.1-(0.1*scroll_speed)

        for x in range(repeats):
            visible_message = "                "
            self.lcd.clear()
            self.lcd.set_cursor(0, 1)
            self.lcd.message(visible_message)
            time.sleep(sleep_time)
            for loc in range(len(bottom_text)):
                self.lcd.clear()
                self.lcd.set_cursor(0, 0)
                self.lcd.message(self.get_time(time_format))
                self.lcd.set_cursor(0, 1)
                visible_message = self.scroll_string(visible_message, bottom_text, loc)
                self.lcd.message(visible_message)
                self.lcd.set_cursor(0, 0)
                time.sleep(sleep_time)

    def scroll_string(self, visible_message, full_message, loc, scrollby=1):
        visible_message = visible_message[scrollby:]+full_message[loc:scrollby+loc]
        return visible_message
