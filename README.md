# MangaDB

MangaDB est la plateforme qui va t'aider à choisir le prochain anime/manga à matter !

## Arborescence (dossiers/fichiers importants)
```bash
├── Database transformation.ipynb (MongoDB collection transformation)
├── README.md
├── anime_no_split.csv (data without splitting "Genres" & "Studios")
├── anime_splitted.csv (split "Genres" & "Studios")
├── app_streamlit.py
├── MangaDB_scrapper.ipynb (scrapper & ETL)
└── manga_no_split.csv (data without splitting )
``` 
## Les technologies :
```
Python 3.8 (selenium, pymongo, streamlit, pandas, request, numpy, csv)
MongoDB
chromedriver
```
## Installation
### Scrapping :
```
Accéder au notebook mangaDbSpider.ipynb :
- exécuter les cellules dans l'ordre
- modofier le path pour la création du csv
```
### Création collection
```bash
Version CSV :
1 - Créer une nouvelle collection dans votre BDD
2 - Charger le fochier csv
3 - renseigner le type des colonnes et terminer le chargement

Si le changement de type n'a pas été réaliser (pour les int)
Dans la collection créée, aller sur onglet "Aggregate"
1- select $addFields
2- {
      episodesInt: { $toInt: "$le_nom_de_la_colonne" }
   }
3- Save
4- Créer view "animes"
```

### Lancer application en local

Dans le terminal "Streamlit run app_streamlit.py" et se rendre à l'url indiquer dans la console

### Utilisation du formulaire :
Plusieurs options de filtres !!! Amusez vous :D 

## Usage :
Renseigner dans le formulaire vos critères et soumettre le formulaire.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributeurs

[B.Rafaël](https://github.com/RBonilauri) & [K.Maathess](https://github.com/Maathess)

