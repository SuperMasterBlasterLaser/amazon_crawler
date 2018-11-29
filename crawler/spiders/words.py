# -*- coding: utf-8 -*-
import scrapy


class WordsSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    words_to_find = {
        "virtue": False,
        "signalling": False,
        "is": False,
        "society's": False,
        "version": False,
        "of": False,
        "proof": False,
        "stake": False
    }

    def parse(self, response):

        links = response.css('a::attr(href)').extract()

        body = str(response.body)

        for key, value in self.words_to_find.items():
            if not value:
                if key in body:
                    self.words_to_find[key] = True

        is_found = True
        for key, value in self.words_to_find.items():
            if not value:
                is_found = False

        if is_found:
            print('All words are found')
            return

        else:
            print(self.words_to_find)
            for link in links:
                if link.startswith('https://www.amazon.com'):
                    yield response.follow(link, self.parse)








