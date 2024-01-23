from typing import Any, Iterator
from uuid import uuid5, NAMESPACE_URL

from resiliparse.extract.html2text import extract_plain_text
from scrapy import Spider, Request
from scrapy.linkextractors.lxmlhtml import \
    LxmlLinkExtractor, IGNORED_EXTENSIONS
from scrapy.http.response import Response
from scrapy.http.response.html import HtmlResponse


class SchoolSpider(Spider):
    name: str = "school"

    start_urls: list[str] = [
        "https://wilhelm-gym.de/",
    ]
    link_extractor = LxmlLinkExtractor(
        allow_domains=[
            "wilhelm-gym.de",
        ],
        deny_extensions=[
            *IGNORED_EXTENSIONS,
            "webp",
        ]
    )
    custom_settings = {
        "USER_AGENT": "Sommercamp (https://sommercamp.uni-jena.de)",
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS": 4,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1,
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response: Response) -> Iterator[dict[str, Any]]:
        if not isinstance(response, HtmlResponse):
            return

        yield {
            "docno": str(uuid5(NAMESPACE_URL, response.url)),
            "url": response.url,
            "title": response.css("title::text").get(),
            "text": extract_plain_text(response.text, main_content=True),
        }

        for link in self.link_extractor.extract_links(response):
            yield Request(link.url, callback=self.parse)
