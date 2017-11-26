import feedparser


class RssParser:

    def refresh_reuters(self):

        reuters_topnews = feedparser.parse("http://feeds.reuters.com/reuters/topNews")['entries']

        reuters_string = ''

        for entry in reuters_topnews:
            reuters_string = reuters_string + entry['title'] + ' | '


        #print reuters_string

        return reuters_string

