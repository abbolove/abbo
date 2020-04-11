import requests
import json

def memberIDver(istenen):
    r = requests.get("https://www.kap.org.tr/tr/api/kapmembers/IGS/A")
    text = '{"data":' + r.text + '}'
    data = json.loads(text)
    for hisse in data["data"]:
        semboller = hisse["stockCode"].split(", ")
        for sembol in semboller:
            if sembol == istenen.upper():
                return hisse["mkkMemberOid"]

bu = ""   
print(memberIDver(bu))
