import streamlit as st
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["MangaDB"]
my_col = my_db["animes"]


def get_number_of_episodes():
    number_of_episodes = 0
    return number_of_episodes


def main():
    icon = "https://i.skyrock.net/4993/75904993/pics/2954055433_1_7_EKbbFdP7.png"
    test = "https://us.123rf.com/450wm/sabelskaya/sabelskaya1603/sabelskaya160300156/54119905-carr%C3%A9-neon-lumi%C3%A8re-bleue-au-n%C3%A9on-.jpg?ver=6"
    end_request = {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0}
    number_anime = 1

    # Page details
    st.set_page_config(page_title="MangaDB", page_icon=icon, layout="wide")
    st.title("MangaDB", )
    st.text("The manga database")
    st.markdown("""---""")

    # Sidebar
    sidebar = st.sidebar.selectbox("What page ?", ("Search", "Stats"))

    if sidebar == "Search":
        st.header("Search :")

        # Search a manga
        form = st.form(key="search")
        title_input = form.text_input("Enter manga name")
        genre_expander = form.beta_expander("Genres")
        with genre_expander:
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            with col1:
                st.checkbox("Action")
                st.checkbox("Demons")
                st.checkbox("Harem")
                st.checkbox("Kids")
                st.checkbox("Music")
                st.checkbox("Romance")
                st.checkbox("Shoujo")
                st.checkbox("Space")
                st.checkbox("Vampire")
            with col2:
                st.checkbox("Adventure")
                st.checkbox("Drama")
                st.checkbox("Hentai")
                st.checkbox("Magic")
                st.checkbox("Mystery")
                st.checkbox("Samurai")
                st.checkbox("Shoujoo Ai")
                st.checkbox("Sports")
                st.checkbox("Yaoi")
            with col3:
                st.checkbox("Cars")
                st.checkbox("Ecchi")
                st.checkbox("Historical")
                st.checkbox("Martial Arts")
                st.checkbox("Parody")
                st.checkbox("School")
                st.checkbox("Shounen")
                st.checkbox("Super Power")
                st.checkbox("Yuri")
            with col4:
                st.checkbox("Comedy")
                st.checkbox("Fantasy")
                st.checkbox("Horror")
                st.checkbox("Mecha")
                st.checkbox("Police")
                st.checkbox("Sci-Fi")
                st.checkbox("Shounen Ai")
                st.checkbox("Supernatural")
            with col5:
                st.checkbox("Dementia")
                st.checkbox("Game")
                st.checkbox("Josei")
                st.checkbox("Military")
                st.checkbox("Psychological")
                st.checkbox("Seinen")
                st.checkbox("Slice of Life")
                st.checkbox("Thriller")

        details_expander = form.beta_expander("More details")
        with details_expander:
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                format = st.selectbox("Format",
                                      ("All", "TV", "OVA", "Movie", "Special", "ONA"))
                studio = st.selectbox("Studio", ("truc", "machin", "bidule"))
            with col2:
                nb_episode = st.selectbox("Number of episodes",
                                          ("> 1", "1 - 15", "15 - 50", "50 - 100", "100+"))
            with col3:
                source = st.selectbox("Source", ("Manga", "Light novel", "Other"))

        button = form.form_submit_button(label="Submit")

        if button:
            st.write("format -->", format, " ; episodes -->", nb_episode, " ; genre -->", studio, " ; studio -->", studio, " ; source -->", source)
            st.header("Result(s) : ")
            if nb_episode == "1 - 15":
                animes = my_col.find({'$and': [
                    {'episodesInt': {'$gt': 1}},
                    {'episodesInt': {'$lt': 15}}]}, end_request)
            elif nb_episode == "15 - 50":
                animes = my_col.find({'$and': [
                    {'episodesInt': {'$gt': 15}},
                    {'episodesInt': {'$lt': 50}}]}, end_request)
            elif nb_episode == "50 - 100":
                animes = my_col.find({'$and': [
                    {'episodesInt': {'$gt': 50}},
                    {'episodesInt': {'$lt': 100}}]}, end_request)
            elif nb_episode == "> 1":
                animes = my_col.find(
                    {'episodesInt': {'$gt': 1}},
                    end_request)
            else:
                animes = my_col.find({'$and': [
                    {'episodesInt': {'$gt': 100}}]}, end_request)

            if len(animes) == 0:
                st.write("Sorry, no anime found for your search...")
            else:
                for anime in animes:
                    image, details = st.beta_columns([1, 4])
                    with image:
                        st.image(test, width=100)
                    with details:
                        st.write(number_anime, " -", anime["title"])
                        st.write("number of episodes :", anime["episodesInt"])
                    number_anime += 1
                    st.markdown("---")

    else:
        st.header("Stats")
        st.write("Total of animes : 947")

        selected_stat = st.sidebar.selectbox("What stat ?", ("Genre", "Score", "Studio"))

        if selected_stat == "Score":
            st.subheader("By score")
        elif selected_stat == "Genre":
            st.subheader("By genre")
        else:
            st.subheader("By studio")


        # note & type


if __name__ == '__main__':
    main()
