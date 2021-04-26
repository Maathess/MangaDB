import string
import scrapy
from scrapy import Request


class MangaDbSpider(scrapy.Spider):
    name = 'Manga'
    start_urls = ["https://myanimelist.net/manga.php", ]

    def parse(self, response):
        xp = "//div[@id='horiznav_nav']//li/a/@href"
        return (Request(url, callback=self.parse_manga_list_page) for url in response.xpath(xp).extract())

    def parse_manga_list_page(self, response):
        for tr_sel in response.css('div.js-categories-seasonal tr ~ tr'):
            yield {
                "title": tr_sel.css('a[id] strong::text').extract_first().strip(),
                "synopsis": tr_sel.css("div.pt4::text").extract_first(),
                "type_": tr_sel.css('td:nth-child(3)::text').extract_first().strip(),
                "episodes": tr_sel.css('td:nth-child(4)::text').extract_first().strip(),
                "rating": tr_sel.css('td:nth-child(5)::text').extract_first().strip()
            }

        next_urls = response.xpath("//div[@class='spaceit']//a/@href").extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)
            
#class MongoPipeline(object):
#
#    collection_name = 'manga_items'
#
#    def open_spider(self, spider):
#        self.client = pymongo.MongoClient()
#        self.db = self.client["MangaDB"]
#
#    def close_spider(self, spider):
#        self.client.close()
#
#    def process_item(self, item, spider):
#        self.db[self.collection_name].insert_one(dict(item))
#        return item