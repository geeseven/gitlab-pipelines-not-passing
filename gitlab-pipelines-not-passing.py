from requests import get
from xmltodict import parse

# (repo, branch)
repos = [
    ("https://gitlab.gnome.org/GNOME/mutter", "wip/carlosg/input-thread"),
    ("https://gitlab.gnome.org/GNOME/glib", "master"),
    ("https://gitlab.com/encode21/jakrevo", "iuts"),
]

not_passed = []

for repo in repos:
    url = "{}/badges/{}/pipeline.svg".format(repo[0], repo[1])
    text = get(url).text
    svg = parse(text)
    if svg["svg"]["g"][1]["g"]["text"][2]["#text"] != "passed":
        not_passed.append(url.split("/")[-4])

if not_passed:
    print(*not_passed, sep=", ")
else:
    print("None")
