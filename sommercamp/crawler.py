# Hier importieren wir die benötigten Softwarebibliotheken.
from resiliparse.extract.html2text import extract_plain_text
from scrapy import Spider, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http.response.html import HtmlResponse


class RemchingenSpider(Spider):
    name = "remchingencrawler"

    start_urls = [
        "https://www.remchingen.de/"

    ]

    link_extractor = LxmlLinkExtractor(
        allow_domains=[
            "remchingen.de",
            "www.remchingen.de"
            ]
    )

    custom_settings = {
        "USER_AGENT": "Sommercamp",
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS": 4,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        yield {
            "docno": str(hash(response.url)),
            "url": response.url,
            "title": response.css("title::text").get(),
            "text": extract_plain_text(response.text, main_content=True),
        }

        for link in self.link_extractor.extract_links(response):
            print(link)
            if link.text == "":
                continue
            yield Request(link.url, callback=self.parse)
