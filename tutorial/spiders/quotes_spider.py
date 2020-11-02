import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls =[]
    def parse(self, response):
        try:
            yield {
            'stt': self.start_urls.index(response.url),
            'sim': response.url.split("*")[-1].split("?")[0],
            # 'sim so sanh': response.xpath('//*[@class="table-cell--left"]//text()').extract(),
            'sim so sanh': response.css('a.sim-number::attr(href)')[0].get().split("com/")[1],
            'gia': response.css('div.sim-price::text')[0].get()
            }
            
        except Exception:
            yield {
                'stt': self.start_urls.index(response.url),
                'sim': response.url.split("*")[-1].split("?")[0],
                'sim so sanh': 'n/a',
                'gia': 'n/a'
            }



        # try:
        #     yield {
        #         'stt': self.start_urls.index(response.url),
        #         'sim': response.url.split('*')[-1].split('&')[0],
        #         'gia': response.css('table.tab-sim tr td::text')[2].get()
        #         }    
        # except Exception:
        #     yield {
        #         'stt': self.start_urls.index(response.url),
        #         'sim': response.url.split('*')[-1].split('&')[0],
        #         'gia': 'n/a'
        #         }  
 

