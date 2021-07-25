# MangaDB

MangaDB est la plateforme qui va t'aider à choisir le prochain anime à matter !

## Arborescence (dossiers/fichiers importants)
```bash
├── Database transformation.ipynb (MongoDB collection transformation)
├── README.md
├── anime_no_split.csv (data without splitting "Genres" & "Studios")
├── anime_splitted.csv (split "Genres" & "Studios")
├── app_streamlit.py
└── mangaDbSpider.ipynb (scrapper & ETL)
``` 
## Les technologies :
```
Python 2.7 (selenium, pymongo, flask, flask-pymongo, pandas, request)
MongoDB
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

Sur collection scrappée aller sur onglet "Aggregate"
1- select $addFields
2- {
      episodesInt: { $toInt: "$episodes" }
   }
3- Save
4- Créer view "animes"
```

### Lancer application en local

Dans le terminal "flask run" puis ouvrir navigateur et aller sur http://127.0.0.1:5000/ 

### Utilisation du formulaire :
Deux listes déroulantes une pour le type de programme et l'autre pour le nombres d'épisodes souhaités et bouton de soumission du formulaire
## Usage :
Renseigner dans le formulaire vos critères et soumettre le formulaire.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributeurs

[B.Rafaël](https://github.com/RBonilauri) & [K.Maathess](https://github.com/Maathess)

