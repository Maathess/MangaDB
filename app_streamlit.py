import streamlit as st
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["MangaDB"]
my_col_animes = my_db["new_animes_no_split"]
my_col_mangas = my_db["mangas_no_split"]


def request_animes(selected_number, selected_title, selected_type, selected_studio, selected_source, selected_status,
                   selected_genre):
    request_genre = {}
    request_type = {}
    request_title = {}
    request_studio = {}
    request_source = {}
    request_status = {}

    if selected_title != "":
        # search anime where title contains selected_title and ignore case
        request_title = {'Title': {'$regex': selected_title, '$options': 'i'}}

    if selected_type != " All":
        request_type = {'Type': selected_type}

    if selected_studio != " All":
        request_studio = {'Studio': {'$regex': selected_studio, '$options': 'i'}}

    if selected_genre != " All":
        request_genre = {'Genres': {'$regex': selected_genre, '$options': 'i'}}

    if selected_source != " All":
        request_source = {'Sources': selected_source}

    if selected_status != " All":
        request_status = {'Status': selected_status}

    if selected_number == "1 - 15":
        return {'$and': [request_title, request_type, request_studio, request_source, request_status, request_genre,
                         {'Episodes': {'$gt': 1}}, {'Episodes': {'$lt': 15}}]}
    elif selected_number == "15 - 50":
        return {'$and': [request_title, request_type, request_studio, request_source, request_status, request_genre,
                         {'Episodes': {'$gt': 15}}, {'Episodes': {'$lt': 50}}]}
    elif selected_number == "50 - 100":
        return {'$and': [request_title, request_type, request_studio, request_source, request_status, request_genre,
                         {'Episodes': {'$gt': 50}}, {'Episodes': {'$lt': 100}}]}
    elif selected_number == "> 1":
        return {'$and': [request_title, request_type, request_studio, request_source, request_status, request_genre,
                         {'Episodes': {'$gt': 1}}]}
    else:
        return {'$and': [request_title, request_type, request_studio, request_source, request_status, request_genre,
                         {'Episodes': {'$gt': 100}}]}


def request_mangas(selected_title, selected_genre, selected_type, selected_status):
    request_title = {}
    request_genre = {}
    request_type = {}
    request_status = {}

    if selected_type != " All":
        request_type = {'Type': selected_type}

    if selected_title != "":
        request_title = {'Title': {'$regex': selected_title, '$options': 'i'}}

    if selected_genre != " All":
        request_genre = {'Genres': {'$regex': selected_genre, '$options': 'i'}}

    if selected_status != " All":
        request_status = {'Status': selected_status}

    return {'$and': [request_title, request_genre, request_type, request_status]}


def main():
    icon = "https://i.skyrock.net/4993/75904993/pics/2954055433_1_7_EKbbFdP7.png"
    end_request_animes = {'Title': 1, 'Rating': 1, 'Genres': 1, 'Studio': 1, 'Sources': 1, 'Status': 1, 'Type': 1,
                          'Synopsis': 1, 'Episodes': 1, 'Date': 1, 'Duration': 1, 'Img_Url': 1, '_id': 0}

    end_request_mangas = {'Title': 1, 'Rating': 1, 'Genres': 1, 'Volumes': 1, 'Chapters': 1, 'Status': 1, 'Authors': 1,
                          'Type': 1, 'Synopsis': 1, 'Published': 1, 'Img_Url': 1, '_id': 0}
    number_anime = 1
    number_manga = 1

    # Page details
    st.set_page_config(page_title="MangaDB", page_icon=icon, layout="wide")
    st.title("MangaDB", )
    st.text("The manga database")
    st.markdown("""---""")

    sidebar = st.sidebar.selectbox("What page ?", ("Animes", "Mangas", "Stats"))

    if sidebar == "Animes":
        st.header("Animes :")

        form = st.form(key="animes")
        a_selected_title = form.text_input("Enter an anime name")

        details_expander = form.beta_expander("More details")
        with details_expander:
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                a_selected_type = st.selectbox("Format",
                                               (" All", " TV", " OVA", " Movie", " Special", " ONA", " Music"))

                a_selected_studio = st.selectbox("Studio",
                                                 (" All", " Toei Animation", " Madhouse", " Studio Deen",
                                                  " Studio Pierrot", " Bones", " Mappa", " Ufotable",
                                                  " Wit Studio", " Studio Ghibli", " Square Enix"))

                a_selected_genre = st.selectbox("Genre",
                                                (" All", " Action", " Adventure", " Comedy", " Fantasy", " Horror",
                                                 " Romance", " Shojo", " Shounen", " Seinen"))
            with col2:
                nb_episode = st.selectbox("Number of episodes",
                                          ("> 1", "1 - 15", "15 - 50", "50 - 100", "100+"))

                a_selected_source = st.selectbox("Source",
                                                 (" All", " Manga", " Light novel", " Visual novel", " Original"))
            with col3:
                a_selected_sorting = st.selectbox("Sorting",
                                                  ("By rating", "By name"))

                a_selected_status = st.selectbox("Status",
                                                 (" All", " Currently Airing", " Finished Airing"))

        button = form.form_submit_button(label="Submit")

        if button:
            if a_selected_sorting == "By rating":
                animes = my_col_animes.find(
                    request_animes(nb_episode, a_selected_title, a_selected_type, a_selected_studio, a_selected_source,
                                   a_selected_status, a_selected_genre),
                    end_request_animes).sort("Rating", pymongo.DESCENDING)
            else:
                animes = my_col_animes.find(
                    request_animes(nb_episode, a_selected_title, a_selected_type, a_selected_studio, a_selected_source,
                                   a_selected_status, a_selected_genre),
                    end_request_animes).sort("Title", pymongo.ASCENDING)

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
                            st.write("**Number of episodes :**", str(anime["Episodes"]))  # nb tome
                            st.write("**Status :**", anime["Status"])
                            st.write("**Synopsis :**", anime["Synopsis"])
                            st.write("**Format :**", anime["Type"])  #
                            st.write("**Date :**", anime["Date"])
                            st.write("**Duration :**", anime["Duration"])  #
                            st.write("**Studio :**", anime["Studio"])  #
                            st.write("**Source :**", anime["Sources"])  #
                    number_anime += 1
                    st.markdown("---")
            else:
                st.text("Sorry, no result for your search...")

    elif sidebar == "Mangas":
        st.header("Mangas :")

        form = st.form(key="mangas")
        m_selected_title = form.text_input("Enter a manga name")
        details_expander = form.beta_expander("More details")
        with details_expander:
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                m_selected_genre = st.selectbox("Genre",
                                                (" All", " Action", " Adventure", " Comedy", " Fantasy", " Horror",
                                                 " Romance", " Shojo", " Shounen", " Seinen"))
                m_selected_type = st.selectbox("Type", (" All", " Manga", " Manhua",  " Manhwa", " Novel", " Light Novel"))
            with col2:
                m_selected_status = st.selectbox("Status",
                                                 (" All", " Publishing", " Finished", " On Hiatus"))
            with col3:
                m_selected_sorting = st.selectbox("Sorting",
                                                  ("By rating", "By name"))

        button = form.form_submit_button(label="Submit")

        if button:
            if m_selected_sorting == "By rating":
                mangas = my_col_mangas.find(request_mangas(m_selected_title, m_selected_genre, m_selected_type, m_selected_status),
                                            end_request_mangas).sort("Rating", pymongo.DESCENDING)
            else:
                mangas = my_col_mangas.find(request_mangas(m_selected_title, m_selected_genre, m_selected_type, m_selected_status),
                                            end_request_mangas).sort("Title", pymongo.ASCENDING)

            if mangas.count() != 0:
                st.write("Result(s) :", str(mangas.count()), " anime(s)")
                st.markdown("---")
                for manga in mangas:
                    image, details = st.beta_columns([1, 4])
                    with image:
                        st.image(str(manga["Img_Url"]), width=100)
                    with details:
                        st.write(str(number_manga), " -", manga["Title"])
                        st.write("**Rating :**", manga["Rating"])
                        st.write("**Genres :**", manga["Genres"])
                        details = st.beta_expander("More details")
                        with details:
                            st.write("**Authors :**", manga["Authors"])
                            st.write("**Status :**", manga["Status"])
                            if str(manga["Volumes"]) == "nan":
                                st.write("**Volumes :** Unknown")
                            else:
                                st.write("**Volumes :**", str(manga["Volumes"]), "(", str(manga["Chapters"]), "chapters)")
                            st.write("**Synopsis :**", manga["Synopsis"])
                            st.write("**Type :**", manga["Type"])
                            st.write("**Published :**", manga["Published"])

                    number_manga += 1
                    st.markdown("---")
            else:
                st.text("Sorry, no result for your search...")
    else:
        st.header("Stats :")


if __name__ == '__main__':
    main()
