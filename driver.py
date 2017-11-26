import lcd_handler
import rss_parser


lcdh = lcd_handler.LcdHandler()
rssp = rss_parser.RssParser()

reuters_str = rssp.refresh_reuters()
time_format = '%H:%M:%S.%f'
# '%b %d  %H:%M:%S'

lcdh.display_string(time_format, reuters_str)
