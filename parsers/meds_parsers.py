from locators.meds_locators import MedsLocators


class MedsParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Lek {self.nazwa}, opakowanie, dawka, cena'

    @property
    def nazwa(self):
        locator =MedsLocators.NAZWA
        nazwa_leku = self.parent.select_one(locator).string
        return nazwa_leku