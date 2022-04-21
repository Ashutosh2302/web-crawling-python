import scrapy

class WhiskyScraper(scrapy.Spider):
    name = 'whisky_spider'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            name = products.css('a.product-item-link::text').get()
            link = products.css('a.product-item-link').attrib['href']
            try:
                price = products.css('span.price::text').get().replace('£', '')
            except:
                price = 'sold out'
            yield {
                'name': name,
                'price': price,
                'link': link,
            }
       