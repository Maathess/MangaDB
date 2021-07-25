import streamlit as st
import pymongo
import altair as alt
import pandas as p

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["MangaDB"]
# my_col = my_db["animes"]
# my_col = my_db["new_animes"]
my_col = my_db["new_animes_no_split"]


def request(selected_number, selected_title):
    genres = []
    request_format = {}
    request_title = {}

    if selected_title != "":
        # search anime where title contains selected_title and ignore case
        request_title = {'Title': {'$regex': selected_title, '$options': 'i'}}

    # if selected_format != "All":
    #     request_format = {'Type': selected_format}

    if selected_number == "1 - 15":
        return {'$and': [request_title, request_format, {'Episodes': {'$gt': 1}}, {'Episodes': {'$lt': 15}}]}
    elif selected_number == "15 - 50":
        return {'$and': [request_title, request_format, {'Episodes': {'$gt': 15}}, {'Episodes': {'$lt': 50}}]}
    elif selected_number == "50 - 100":
        return {'$and': [request_title, request_format, {'Episodes': {'$gt': 50}}, {'Episodes': {'$lt': 100}}]}
    elif selected_number == "> 1":
        return {'$and': [request_title, request_format, {'Episodes': {'$gt': 1}}]}
    else:
        return {'$and': [request_title, request_format, {'Episodes': {'$gt': 100}}]}


def main():
    icon = "https://i.skyrock.net/4993/75904993/pics/2954055433_1_7_EKbbFdP7.png"
    end_request = {'Title': 1, 'Rating': 1, 'Genres': 1, 'Studio': 1, 'Sources': 1, 'Status': 1, 'Type': 1,
                   'Synopsis': 1, 'Episodes': 1, 'Date': 1, 'Duration': 1, 'Img_Url': 1, '_id': 0}
    number_anime = 1

    # Page details
    st.set_page_config(page_title="MangaDB", page_icon=icon, layout="wide")
    st.title("MangaDB", )
    st.text("The manga database")
    st.markdown("""---""")

    # Sidebar
    sidebar = st.sidebar.selectbox("What page ?",
                                   ("Search", "Stats"))

    if sidebar == "Search":
        st.header("Search :")

        # Search a manga
        form = st.form(key="search")
        selected_title = form.text_input("Enter manga name")
        # genre_expander = form.beta_expander("Genres")
        # with genre_expander:
        #     col1, col2, col3, col4, col5 = st.beta_columns(5)
        #     with col1:
        #         st.checkbox(" Action")
        #         st.checkbox(" Demons")
        #         st.checkbox(" Harem")
        #         st.checkbox(" Kids")
        #         st.checkbox(" Music")
        #         st.checkbox(" Romance")
        #         st.checkbox(" Shoujo")
        #         st.checkbox(" Space")
        #         st.checkbox(" Vampire")
        #     with col2:
        #         st.checkbox(" Adventure")
        #         st.checkbox(" Drama")
        #         st.checkbox(" Hentai")
        #         st.checkbox(" Magic")
        #         st.checkbox(" Mystery")
        #         st.checkbox(" Samurai")
        #         st.checkbox(" Shoujoo Ai")
        #         st.checkbox(" Sports")
        #         st.checkbox(" Yaoi")
        #     with col3:
        #         st.checkbox(" Cars")
        #         st.checkbox(" Ecchi")
        #         st.checkbox(" Historical")
        #         st.checkbox(" Martial Arts")
        #         st.checkbox(" Parody")
        #         st.checkbox(" School")
        #         st.checkbox(" Shounen")
        #         st.checkbox(" Super Power")
        #         st.checkbox(" Yuri")
        #     with col4:
        #         st.checkbox(" Comedy")
        #         st.checkbox(" Fantasy")
        #         st.checkbox(" Horror")
        #         st.checkbox(" Mecha")
        #         st.checkbox(" Police")
        #         st.checkbox(" Sci-Fi")
        #         st.checkbox(" Shounen Ai")
        #         st.checkbox(" Supernatural")
        #     with col5:
        #         st.checkbox(" Dementia")
        #         st.checkbox(" Game")
        #         st.checkbox(" Josei")
        #         st.checkbox(" Military")
        #         st.checkbox(" Psychological")
        #         st.checkbox(" Seinen")
        #         st.checkbox(" Slice of Life")
        #         st.checkbox(" Thriller")

        details_expander = form.beta_expander("More details")
        with details_expander:
            col1, col2 = st.beta_columns(2)
            with col1:
                nb_episode = st.selectbox("Number of episodes",
                                          ("> 1", "1 - 15", "15 - 50", "50 - 100", "100+"))
            with col2:
                selected_sorting = st.selectbox("Sorting",
                                                ("None", "By name", "By rating"))
            # col1, col2, col3 = st.beta_columns(3)
            # with col1:
            #     selected_format = st.selectbox("Format",
            #                                    (" All", " TV", " OVA", " Movie", " Special", " ONA", " Music"))
            #
            #     # selected_studio = st.selectbox("Studio",
            #     #                                (" Toei Animation", " Madhouse", " Studio Deen", " Studio Pierrot", " Bones",
            #     #                                 " Mappa", " Ufotable", " Wit Studio", " Studio Ghibli", " Square Enix"))
            # with col2:
            #     nb_episode = st.selectbox("Number of episodes",
            #                               ("> 1", "1 - 15", "15 - 50", "50 - 100", "100+"))
            # with col3:
            #     selected_sorting = st.selectbox("Sorting",
            #                                     ("None", "By name", "By rating"))
            #
            #     # selected_source = st.selectbox("Source",
            #     #                                ("Manga", "Light novel", "Other"))

        button = form.form_submit_button(label="Submit")

        if button:

            if selected_sorting == "None":
                # animes = my_col.find({'Title': {'$regex': selected_title, '$options': 'i'}}, end_request)
                animes = my_col.find(request(nb_episode, selected_title), end_request)
            elif selected_sorting == "By name":
                animes = my_col.find(request(nb_episode, selected_title),
                                     end_request).sort("Title", pymongo.ASCENDING)
            else:
                animes = my_col.find(request(nb_episode, selected_title),
                                     end_request).sort("Rating", pymongo.DESCENDING)

            if animes.count() != 0:
                st.write("Result(s) :", str(animes.count()), " anime(s)")
                st.markdown("---")
                for anime in animes:
                    image, details = st.beta_columns([1, 4])
                    with image:
                        st.image(str(anime["Img_Url"]), width=100)
                    with details:
                        st.write(str(number_anime), " -", anime["Title"])
                        st.write("**Rating :**", anime["Rating"])
                        st.write("**Genres :**", anime["Genres"])
                        details_expander = st.beta_expander("More details")
                        with details_expander:
                            st.write("**Number of episodes :**", str(anime["Episodes"]))
                            st.write("**Status :**", anime["Status"])
                            st.write("**Synopsis :**", anime["Synopsis"])
                            st.write("**Format :**", anime["Type"])
                            st.write("**Date :**", anime["Date"])
                            st.write("**Duration :**", anime["Duration"])
                            st.write("**Studio :**", anime["Studio"])
                            st.write("**Source :**", anime["Sources"])


                    number_anime += 1
                    st.markdown("---")
            else:
                st.text("Sorry, no result for your search...")

    else:
        st.header("Stats")
        st.write("Total of animes : 947")

        selected_stat = st.sidebar.selectbox("What stat ?",
                                             ("Genre", "Score", "Studio"))

        if selected_stat == "Score":
            st.subheader("By score")
        elif selected_stat == "Genre":
            st.subheader("By genre")
        else:
            st.subheader("By studio")


if __name__ == '__main__':
    main()
