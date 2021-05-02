import webbrowser

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["school"]
mycol = mydb["students"]

stud = []

tbl = "<tr><td>Name</td><td>Age</td><td>Section</td></tr>"
stud.append(tbl)

for y in mycol.find():
    a = "<tr><td>%s</td>"%y['name']
    stud.append(a)
    b = "<td>%s</td>"%y['age']
    stud.append(b)
    c = "<td>%s</td></tr>"%y['section']
    stud.append(c)

contents = '''<html>
    <head>
            <meta charset="utf-8" />
            <title>MANGA DB</title>

            <style>
                h1{
                    color: black;
                    text-align: center;
                    font-family: Arial, Helvetica, sans-serif;
                }
            </style>

    </head>

        <body>
            <img src="https://preview.redd.it/99nxlz8pte031.png?width=1920&format=png&auto=webp&s=7e0158219d0c96ccec30b35d9e58c346c45e7f88"/>
            <h1>MangaDB</h1>

            <form name="search" action="./form.py" method="get">
                Type: <SELECT name="Type" size="1">
                    <OPTION>TV<OPTION>Anime<OPTION>Manga</OPTION></SELECT>
                Nombre d'episodes : <SELECT name="NbEp" size="1">
                    <OPTION>1-10<OPTION>10-50<OPTION>50-10<OPTION>+100</SELECT>
                Note : <input type="text" name="note">
            <input type="submit" value="Valider">
            </form>
<table>
%s
</table>
</body>
</html>
'''%(stud)

filename = 'webbrowser.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)
webbrowser.open(filename)