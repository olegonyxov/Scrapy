

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        filename2 = "saved8.txt"
        with open(filename, 'wb') as f:
            f.write(response.body)
            with open(filename2, 'a') as f1:
                for quote in response.css("div.quote"):
                    text1 = quote.css("span.text::text").get()
                    print("11111111111", text1)
                    f1.write(text1+"\n")





