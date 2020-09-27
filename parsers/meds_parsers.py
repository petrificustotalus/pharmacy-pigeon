from locators.meds_locators import MedsLocators


class MedsParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Lek {self.nazwa}, postac {self.postac}, dawka {self.dawka}, opakowanie, cena {self.cena}'

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
    def cena(self):
        locator = MedsLocators.CENA
        cena_leku = self.parent.select_one(locator).string
        return cena_leku
