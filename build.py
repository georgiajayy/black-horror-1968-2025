import csv, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
LED = {"Night of the Living Dead","Get Out","Us","Ma","His House","Candyman","Nope","The Blackening","Sinners"}
films = list(csv.DictReader(open(root/"data/films.csv")))
for f in films:
    f["all_black"] = f["film"] in LED and not (f["film"]=="Candyman" and f["year"]=="1992")
chars = list(csv.DictReader(open(root/"data/black_characters.csv")))
WIKI = {"Jada Pinkett":"Jada Pinkett Smith","Chris Owen":"Chris Owen (actor)"}
NOWIKI = {"Dante Brown","Tanyell Waivers","Malaika Abigaba","Evan Alex","Peter Maloney"}
def wiki(a): return None if (not a or a in NOWIKI) else WIKI.get(a,a)
for f in films: f["wiki"] = wiki(f["first_victim_actor"])
for c in chars: c["wiki"] = wiki(c["actor"])
html = (root/"src/template.html").read_text()
html = html.replace("__FILMS__", json.dumps(films)).replace("__CHARS__", json.dumps(chars))
(root/"index.html").write_text(html)
print("built index.html")
