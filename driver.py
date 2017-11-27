import lcd_handler
import rss_parser


lcdh = lcd_handler.LcdHandler()
rssp = rss_parser.RssParser()


while True:
    rss_str = rssp.refresh_channel("http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk")
    #time_format = '%H:%M:%S.%f'`'`
    time_format =  '%b %d  %H:%M:%S'

    lcdh.display_string(time_format, rss_str, 8)
