import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from ubluk.items import Article


class UblSpider(scrapy.Spider):
    name = 'ubl'
    start_urls = ['https://www.ubluk.com/latest-news/?category=#blog-filter']

    def parse(self, response):
        links = response.xpath('//a[@class="btn btn-primary"]/@href').getall()
        yield from response.follow_all(links, self.parse_article)

        next_page = response.xpath('//a[@class="pagination-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get().strip()
        date = response.xpath('//div[@class="news-details text-right"]/p[1]').get().strip().split()[2]
        date = datetime.strptime(date, '%d/%m/%Y')
        date = date.strftime('%Y/%m/%d')
        content = response.xpath('//div[@class="content"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
