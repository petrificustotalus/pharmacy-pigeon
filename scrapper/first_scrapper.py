import requests


from pages.all_meds_pages import MadsPage
from database import database


def scrapp_meds():
    page_content = requests.get('https://www.lekinfo24.pl/lek/Ketoprofen%20LGO.html').content
    page = MadsPage(page_content)

    leki = page.lek  # leki is a list of MadsPage class elements [lek, lek, lek, ...]

    with open('mpstrony.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_line = line.split(',')
            page_content = requests.get(new_line[0]).content
            page = MadsPage(page_content)
            leki.extend(page.lek) # to samo co append akurat w tym przypadku?

    for lek in leki:
        #  database.add_med_to_the_table(lek['nazwa'], lek['postac'], lek['dawka'], lek['opakowanie'], lek['cena'])
        database.add_med_to_the_table(lek.nazwa, lek.postac, lek.dawka, lek.opakowanie, lek.cena)
        print(lek)
