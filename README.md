# MangaDB

MangaDB est la plateforme qui va t'aider à choisir le prochain anime à matter !

## Arborescence (dossiers/fichiers importants)
```bash
├── MangaDbSpider
|   ├── spiders
|   |   |── mangaDbSpider.ipynb (notebook explicatif)
|   |   └── mangaDbSpider.py
|   |── pipelines.py
|   └── settings.py
|
|   ├── templates
|       |── base.html
|       |── home.html
|       └── list.html
|
├── Database transformation.ipynb
├── README.md
├── app.py
├── run
└── scrapy.cfg
``` 
## Les technologies :
```
Python 2.7 (scrapy, pymongo, flask, flask-pymongo, pandas)
MongoDB
```
## Installation
### Scrapping :
```
Créer environnement python 3.8
Se rendre dans le dossier "spiders" et écrire la commande suivante : 
1- scrapy runspider mangaDBSpider.py
2- scrapy crawl Manga
```
### Création collection
```bash
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

