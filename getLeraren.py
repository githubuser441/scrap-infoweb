from bs4 import BeautifulSoup


def get_leraren(url, gebruikersnaam, wachtwoord, s):
    print("get_leraren is gestart")
    leraren = []
    # haal website met klassen op
    url += '/infoweb/index.php?ref=3'
    if gebruikersnaam == "":
        response = s.get(url).content
    else:
        response = s.get(url, auth=(gebruikersnaam, wachtwoord)).content
    html = BeautifulSoup(response)
    # filtert op leraren
    html_leraren = html.find_all("select")[1]
    html_leraren = html_leraren.find_all("option")
    # zet alle leraren in list
    for leraar in html_leraren:
        #print(html_groepen[x]['value'])
        leraren.append(leraar.text)
    print("get_leraren is voltooid")
    return leraren