from bs4 import BeautifulSoup

from locators.meds_pages_locators import MpMedsPageLocators
from parsers.meds_parsers import MedsParser


class MadsPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def lek(self):
        locator = MpMedsPageLocators.MEDICAMENT
        leki = [MedsParser(e) for e in self.soup.select(locator)]
        return leki
