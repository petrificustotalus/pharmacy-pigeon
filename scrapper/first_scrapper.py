import requests


from pages.all_meds_pages import MadsPage


def scrapp_meds():
    page_content = requests.get('https://www.lekinfo24.pl/lek/Ketoprofen%20LGO.html').content
    page = MadsPage(page_content)

    leki = page.lek

    with open('mpstrony.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_line = line.split(',')
            page_content = requests.get(new_line[0]).content
            page = MadsPage(page_content)
            leki.extend(page.lek)

    for e in leki:
        lek = e
        print(e)