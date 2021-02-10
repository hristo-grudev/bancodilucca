import scrapy

from scrapy.loader import ItemLoader
from ..items import BancodiluccaItem
from itemloaders.processors import TakeFirst


class BancodiluccaSpider(scrapy.Spider):
	name = 'bancodilucca'
	start_urls = ['https://www.bancodilucca.it/ita/News']

	def parse(self, response):
		year_links = response.xpath('//ul[@class="left-menu list-unstyled"]//a/@href').getall()
		for link in year_links:
			yield response.follow(link, self.parse_year)

	def parse_year(self, response):
		post_links = response.xpath('//div[@class="testo"]//a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//article/h2/text()').get()
		description = response.xpath('//article/p/text()[normalize-space() and not(ancestor::p[@class="date"])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//article/p[@class="date"]/text()').get()

		item = ItemLoader(item=BancodiluccaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
