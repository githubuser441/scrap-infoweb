from bs4 import BeautifulSoup


def get_lokalen(url, gebruikersnaam, wachtwoord, s):
    print("get_lokalen is gestart")
    lokalen = []
    # haal website met lokalen op
    url += '/infoweb/index.php?ref=4'
    if gebruikersnaam == "":
        response = s.get(url).content
    else:
        response = s.get(url, auth=(gebruikersnaam, wachtwoord)).content
    html = BeautifulSoup(response)
    # filtert op leraren
    html_lokalen = html.find_all("select")[1]
    html_lokalen = html_lokalen.find_all("option")
    # zet alle leraren in list
    for lokaal in html_lokalen:
        #  print(html_groepen[x]['value'])
        if checknummer(lokaal.text):
            lokalen.append(lokaal.text)
    print("get_lokalen is voltooid")
    return lokalen


def checknummer(s):
    return any(i.isdigit() for i in s)
