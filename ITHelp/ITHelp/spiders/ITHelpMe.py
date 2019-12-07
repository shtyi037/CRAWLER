# -*- coding: utf-8 -*-
import scrapy
from ..items import IthelpItem


class IthelpmeSpider(scrapy.Spider):
    name = 'ITHelpMe'
    # allowed_domains = ['https://ithelp.ithome.com.tw']
    #入口的URLS
    start_urls = ['https://ithelp.ithome.com.tw/users/20040221/ironman/2236']
    
    def parse(self, response):
        day = ''
        for each in response.xpath('//div[@class="qa-list profile-list ir-profile-list"]'):
            item = IthelpItem()
            item['series'] = (each.xpath('//h3[@class="qa-list__title qa-list__title--ironman"]/text()').extract()[0]).strip()
            #處理取出的值
            day = each.xpath('./div/div/span/text()').extract()[0]
            item['day'] = (day.lstrip('DAY\n')).strip()
            item['positionName'] = (each.xpath('./div/h3/a/text()').extract()[0]).strip()
            item['positionLink'] = (each.xpath('./div/h3/a/@href').extract()[0]).strip()

            yield item
        # 用待爬的URL再次發起請求
        nextUrl = response.xpath('//*[@rel="next"]/@href').extract()[0]
        # #print(nextUrl)
        yield scrapy.Request(nextUrl, callback=self.parse)

