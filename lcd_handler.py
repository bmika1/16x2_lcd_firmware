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


    def display_time(self):
        self.lcd.set_cursor(0,0)
        self.lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        self.lcd.set_cursor(0,0) #Todo: check if this is needed


    #should be: top, bottom, scrolltop, scrollbottom, scrolinterval
    def display_rss(self, time_on_top):

        full_message = self.r_parser.refresh_reuters()
        while True:
            #message_buffer = ""
            visible_message = full_message[:16]
            self.lcd.clear()
            self.lcd.set_cursor(0,1)
            self.lcd.message(visible_message)
            time.sleep(0.2)
            for loc in range(len(full_message)):
                self.lcd.clear()
                if time_on_top is True:
                    self.display_time()
                self.lcd.set_cursor(0,1)
                visible_message = self.scroll_string(visible_message, full_message, loc)
                self.lcd.message(visible_message)
                self.lcd.set_cursor(0,0)
                time.sleep(0.2)

    def scroll_string(self, visible_message, full_message, loc, scrollby=1):
        visible_message = visible_message[scrollby:]+full_message[loc+16:scrollby+loc+16]
        return visible_message

    def load_buffer(self, buffer,  start, full_message):
        if len(buffer) >= 24:
	    buffer = buffer[8:]
        if start == 0:
            end = 16
        else:
            end = start + 8
        buffer = buffer + full_message[start:end]

        return buffer
