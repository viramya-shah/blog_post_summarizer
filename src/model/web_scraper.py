from trafilatura import fetch_url, extract
from uuid import uuid4
from .data_model import Document

class WebScraper:
    def __init__(self):
        """
        Init class attributes
        """
        self.content = {}

    def _scrape(self, url: str) -> str:
        """
        Internal function for scraping
        :param url: URL of the page
        :return: Fetched and parsed content
        """
        doc = fetch_url(url=url)
        content = extract(doc)
        return content

    def scrape(self, urls: list | str, nested: bool = False) -> list[Document]:
        """
        Scrapes the given list of URLs
        :param urls: Either a list of URLs or a single URL
        :param nested: Whether to fetch and parse the URLs inside the given URLs page
        :return: A list of Document object
        """
        if nested:
            raise NotImplementedError("Not a feature yet!")

        if isinstance(urls, str):
            url_list = [urls]
        else:
            url_list = urls

        return [Document(id=str(uuid4()), url=url, content=self._scrape(url)) for url in url_list]
