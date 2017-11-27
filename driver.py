import lcd_handler
import rss_parser
from flask import Flask, request, render_template
import thread

app = Flask(__name__)

lcdh = lcd_handler.LcdHandler()
rssp = rss_parser.RssParser()
address = "http://feeds.bbci.co.uk/news/uk/rss.xml?edition=uk"
_update_request = False

def display_on_screen():
    rss_str = rssp.refresh_channel(address)
    #time_format = '%H:%M:%S.%f'`'`
    time_format =  '%b %d  %H:%M:%S'
    lcdh.display_string(time_format, rss_str, 9, 1)

@app.route('/', methods=['POST'])
def update_rss():
    address = request.form['rss_address']

    ##return response

@app.route('/')
def display_template():
    return render_template('template.html')


if __name__ == '__main__':
    thread.start_new_thread(display_on_screen())
    app.run(debug=True, host='0.0.0.0')
   

