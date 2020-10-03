import re
from locators.meds_locators import MedsLocators


class MedsParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Lek {self.nazwa}, postac {self.postac}, dawka {self.dawka}, opakowanie {self.opakowanie}, cena {self.cena}'

    @property
    def nazwa(self):
        locator = MedsLocators.NAZWA
        nazwa_leku = self.parent.select_one(locator).string
        return nazwa_leku

    @property
    def postac(self):
        locator = MedsLocators.POSTAC
        postac_leku = self.parent.select_one(locator).string
        return postac_leku

    @property
    def dawka(self):
        locator = MedsLocators.DAWKA
        dawka_leku = self.parent.select_one(locator).string
        return dawka_leku

    @property
    def opakowanie(self):
        locator = MedsLocators.OPAKOWANIE
        opakowanie_leku = self.parent.select_one(locator).string
        return opakowanie_leku

    @property
    def cena(self):
        locator = MedsLocators.CENA
        cena_leku = str(self.parent.select_one(locator))
        pattern = '.*<span.*span>(.*)</td>'
        mather = re.search(pattern, cena_leku)

        return mather.group(1)
