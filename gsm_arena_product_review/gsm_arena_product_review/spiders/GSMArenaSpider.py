import scrapy
from ..items import GsmArenaProductReviewItem
import logging

class GSMArenaSpider(scrapy.Spider):
    name = 'gsm_arena_product_review'
    
    def __init__(self, start_url='', *args, **kwargs):
        super(GSMArenaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
    
    def parse(self, response):
        logging.info('Processing..' + response.url)
        all_div_review = response.css('div.user-thread')
        for quote in all_div_review:
            item =  GsmArenaProductReviewItem()
            item['review'] = quote.css('p.uopin::text').extract_first()
            yield item
        next_page = self.__get_next_page(response)
        logging.info(f"next page: {next_page}")
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
            
    def __get_next_page(self, response):
        nav_page_html = response.css('div.nav-pages').get()
        nav_page = scrapy.Selector(text=nav_page_html)
        all_a_tags = nav_page.css('a').getall()
        if scrapy.Selector(text=all_a_tags[-1]).css('a::attr(title)').get() == 'Next page':
            return scrapy.Selector(text=all_a_tags[-1]).css('a::attr(href)').get()
        return None