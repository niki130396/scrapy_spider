import scrapy
import re
from parliment_spider.items import ParlimentSpiderItem

date_pattern = re.compile("\d{2}/\d{2}/\d{4}")
email_pattern = re.compile("[\w\.-]+@[\w\.-]+(\.[\w]+)+")


class ParlimentSpider(scrapy.Spider):
    name = 'parliment_spider'
    start_urls = ["https://www.parliament.bg/bg/MP"]

    def parse(self, response):
        items = response.xpath("//div[@class='MPinfo']/a/@href").extract()
        for item in items:
            url = f"https://www.parliament.bg{item}"
            yield scrapy.Request(url, callback=self.parse_mp)

    def parse_mp(self, response):
        item = ParlimentSpiderItem()

        first_name, middle_name, last_name = response.xpath("//div[@class='MProwD']//text()").extract()
        mail = list(filter(email_pattern.match, response.xpath("//div[@class='MPinfo']//li/a/text()").extract()))[0]
        list_items = response.xpath("//div[@class='MPinfo']//li/text()").extract()
        birth_date = re.search(date_pattern, list_items[0])
        birth_place = list_items[0][birth_date.span()[-1]+1:list_items[0].index(',')]
        profession = list_items[1].split(': ')[-1]
        languages = list_items[2].split(': ')[-1]
        political_party = list_items[3][list_items[3].index(':')+2:re.search('\d', list_items[3]).start()-1]

        item['first_name'] = first_name
        item['middle_name'] = middle_name
        item['last_name'] = last_name
        item['birth_date'] = list_items[0][birth_date.span()[0]:birth_date.span()[1]]
        item['birth_place'] = birth_place
        item['profession'] = profession
        item['languages'] = languages
        item['political_party'] = political_party
        item['email_address'] = mail

        yield item
