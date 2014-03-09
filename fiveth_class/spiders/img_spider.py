from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from fiveth_class.items import FivethClassItem

class catch_img(Spider):
    name = 'catchimg'
    allowed_domains = ['5-y.2-d.jp']
    # start page
    start_urls = ["http://5-y.2-d.jp/pict.html"]

    def parse(self, response):
        sel = Selector(response)
        # next page to scrapy
        next_link = sel.xpath('//a/@href').re('/pict\d{2}.html')
        # all image link in the page
        pic_link = sel.xpath('//img').re('/pict/\d{4}-\d{2}-\d{2}.jpg')

        # build up item object
        item = FivethClassItem()
        item['image_urls'] = []

        #store all image link to image_urls list
        for link in pic_link:
            # turn relative link to absoluate link then add to list
            item['image_urls'].append("http://5-y.2-d.jp" + link)
        # return link list
        yield item

        # return next link to scrapy
        for link in next_link:
            yield Request("http://5-y.2-d.jp" + link, callback=self.parse)
