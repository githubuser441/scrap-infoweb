from bs4 import BeautifulSoup
from datetime import *


def get_klassen(url, gebruikersnaam, wachtwoord, s):
    print("get_klassen is gestart")
    klassen = []
    # haal website met klassen op
    url += '/infoweb/index.php?ref=2'
    response = s.get(url, auth=(gebruikersnaam, wachtwoord)).content
    html = BeautifulSoup(response)
    # filtert op klassen
    html_groepen = html.find_all("select")[1]
    html_groepen = html_groepen.find_all("option")
    # zet alle klassen in list
    for x in range(3, len(html_groepen)):
        # print(html_groepen[x])
        klassen.append(html_groepen[x].text)
    print("get_klassen is voltooid")
    return klassen


def get_leerlingen(url, gebruikersnaam, wachtwoord, s, klas):
    print("get_leerlingen: "+klas)
    leerlingen = []
    today = datetime.today()
    week = (today.strftime("%U"))
    # haal website met leerlingen op
    url += '/infoweb/selectie.inc.php?wat=groep&weeknummer=%s&groep=%s' % (week, klas)
    if gebruikersnaam == "":
        response = s.get(url).content
    else:
        response = s.get(url, auth=(gebruikersnaam, wachtwoord)).content
    html = BeautifulSoup(response)
    # filtert op leerlingen
    html_leerlingen = html.find("select")
    html_leerlingen = html_leerlingen.find_all("option")
    for x in range(2, len(html_leerlingen)):
        #print(html_groepen[x]['value'])
        leerlingen.append(html_leerlingen[x].text)
    #print(leerlingen)
    return leerlingen


def checknummer(s):
    return any(i.isdigit() for i in s)
