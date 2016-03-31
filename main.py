from getLeerlingen import *
from getLeraren import *
from getLokalen import *
from json import dump
import requests
import re


def main(url, gebruikersnaam, wachtwoord):
    print("programma is gestart")
    # setup
    session = get_session(url, gebruikersnaam, wachtwoord)
    school = {}
    school["leerlingen"] = {}
    school["leraren"] = {}
    school["lokalen"] = {}
    school["statestieken"] = {}
    school["statestieken"]["leerlingen"] = {}
    school["statestieken"]["klassen"] = {}
    school["statestieken"]["leraren"] = {}
    school["statestieken"]["lokalen"] = {}
    school["statestieken"]["leerlingen"]["totaal"] = 0
    school["statestieken"]["klassen"]["totaal"] = 0
    school["statestieken"]["klassen"]["gemiddelt_aantal_leerlingen"] = 0
    school["statestieken"]["leraren"]["totaal"] = 0
    school["statestieken"]["lokalen"]["totaal"] = 0

    klassen = get_klassen(url, gebruikersnaam, wachtwoord, session)
    school["statestieken"]["klassen"]["totaal"] = len(klassen)

    # zoek leerlingen van alle klassen
    for klas in klassen:
        if re.search('[a-zA-Z]', klas):
            leerlingen = get_leerlingen(url, gebruikersnaam, wachtwoord, session, klas)
            school["statestieken"]["leerlingen"]["totaal"] += len(leerlingen)
            school["leerlingen"][klas] = leerlingen

    school["statestieken"]["klassen"]["gemiddelt_aantal_leerlingen"] = \
    round(school["statestieken"]["leerlingen"]["totaal"] / school["statestieken"]["klassen"]["totaal"], 1)

    leraren = get_leraren(url, gebruikersnaam, wachtwoord, session)
    school["leraren"] = leraren
    school["statestieken"]["leraren"]["totaal"] = len(leraren)

    lokalen = get_lokalen(url, gebruikersnaam, wachtwoord, session)
    school["lokalen"] = lokalen
    school["statestieken"]["lokalen"]["totaal"] = len(lokalen)

    print(school)
    export_to_json('school.json', school)
    print("programma is voltooid")


def export_to_json(path, data):
    with open(path, 'w') as outfile:
        dump(data, outfile, sort_keys=True, indent=4)


def get_session(url, gebruikersnaam, wachtwoord):
    s = requests.session()
    aanmelden = url+'/infoweb/index.php'
    if gebruikersnaam == "":
        s.get(aanmelden).content
    else:
        s.get(aanmelden, auth=(gebruikersnaam, wachtwoord))
    return s

url = input("url zonder infoweb/index.php \n")
gebruikersnaam = input("gebruikersnaam voor authentication(als dit niet noodig is laat leeg) \n")
if gebruikersnaam == "":
    wachtwoord = ""
else:
    wachtwoord = input("wachtwoord voor authentication \n")

main(url, gebruikersnaam, wachtwoord)
