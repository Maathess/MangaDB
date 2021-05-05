from pymongo import MongoClient

client = MongoClient()


#%%

print(client.database_names())

#%%

db_manga = client.MangaDB

#%%

collection_anime = db_manga['anime_items']

#%%

db_manga.collection_names()

#%%

result = collection_anime.delete_many({"episodes": "-"})
result

#%%

result_last = collection_anime.delete_many({"rating":'N/A'})
result_last
