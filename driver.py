import lcd_handler
import rss_parser
from flask import Flask, request, render_template
app = Flask(__name__)

lcdh = lcd_handler.LcdHandler()
rssp = rss_parser.RssParser()
address = "http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk"


while True:
    rss_str = rssp.refresh_channel(address)
    #time_format = '%H:%M:%S.%f'`'`
    time_format =  '%b %d  %H:%M:%S'

    lcdh.display_string(time_format, rss_str, 1)


@app.route('/', methods=['POST'])
def update_rss():
    address = request.form['rss_address']

    ##return response

@app.route('/')
def display_template():
    return render_template('template.html')


