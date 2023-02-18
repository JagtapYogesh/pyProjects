from bs4 import BeautifulSoup
import lxml
import requests
LINK_PREFIX = "https://www.nobroker.in"

class Property:
    def __init__(self):
        self.URL = "https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41MzMwMzIzLCJsb24iOjczLjkzMzAwMywicGxhY2VJZCI6IkNoSUpkV0tvSDRIQndqc1JrUUNnYUtOYnB6VSIsInBsYWNlTmFtZSI6Ik11bmRod2EifSx7ImxhdCI6MTguNTUzODI0MSwibG9uIjo3My45NDc2Njg5LCJwbGFjZUlkIjoiQ2hJSmxhU0xLTVBEd2pzUlNnQmpPbUV6NkRnIiwicGxhY2VOYW1lIjoiS2hhcmFkaSJ9XQ==&radius=2.0&sharedAccomodation=0&type=BHK2&availability=within_30_days&city=pune&locality=Mundhwa,&locality=Kharadi"
        self.listings = []

    def fetch_listings(self):
        response = requests.get(self.URL)
        site_html = response.text
        soup = BeautifulSoup(site_html, "lxml")

        locations_divs = soup.select("section div div div")
        name_headings = soup.select(".group .flex .capitalize .heading-6")
        for item in range(0, len(name_headings)):
            location = locations_divs[item+1].get_text()
            name = name_headings[item].get_text()
            link = name_headings[item].select_one("a").get_attribute_list("href")
            item = {
                "name": name,
                "location": location,
                "link": f"{LINK_PREFIX}{link[0]}"
            }
            self.listings.append(item)

    def get_properties(self):
        return self.listings
