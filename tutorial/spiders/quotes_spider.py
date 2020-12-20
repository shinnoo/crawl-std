import scrapy


class QuotesSpider(scrapy.Spider):
    start_urls = [
        "https://simthanglong.vn/tim-sim/091*113848.html?m10so_filter=0&price_filter=0&telco_filter=0&giaban_filter=1&tragop_filter=0"]
    name = "quotes"

    # TongKhoSim
    # def parse(self, response):
    #     try:
    #         yield {
    #         'stt': self.start_urls.index(response.url),
    #         'sim': response.url.split("*")[-1].split("?")[0],
    #         # 'sim so sanh': response.xpath('//*[@class="table-cell--left"]//text()').extract(),
    #         'sim so sanh': response.css('a.sim-number::attr(href)')[0].get().split("com/")[1],
    #         'gia': response.css('div.sim-price::text')[0].get()
    #         }
    #
    #     except Exception:
    #         yield {
    #             'stt': self.start_urls.index(response.url),
    #             'sim': response.url.split("*")[-1].split("?")[0],
    #             'sim so sanh': 'n/a',
    #             'gia': 'n/a'
    #         }

    # Sim ami
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

    # SimThangLong
    def parse(self, response):
        row = response.xpath('//*[@class="tblsim-res2"]//tr')
        try:
            yield {
                'stt': self.start_urls.index(response.url),
                'sim': response.url.split("*")[-1].split(".html")[0],
                'sim so sanh': row.xpath('td[2]//@href').extract_first(),
                'gia': row.xpath('td[3]//text()').extract_first(),
            }
        except Exception:
            yield {
                'stt': self.start_urls.index(response.url),
                'sim': response.url.split("*")[-1].split(".html")[0],
                'sim so sanh': 'n/a',
                'gia': 'n/a'
            }
