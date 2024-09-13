
# import streamlit as st
import pickle
import pandas as pd
movie_list=pickle.load(open('movies.pkl','rb'))
mov=pickle.load(open('mov.pkl','rb'))
movie_list1=movie_list['title'].values
# movie_list=pd.DataFrame(movie_list)
similarity=pickle.load(open('similarity.pkl','rb'))
import streamlit as st
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movie_list1)

def recommend (movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    movie_link=[]
    for i in movies_list:
        # poster fetch
        id=movie_list.iloc[i[0]].movie_id
        movie_link.append(mov[mov['id']==id].homepage)
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies,movie_link

if st.button('Recommend'):
    recommendations,recom_link=recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(i)
    for i in recommendations:
        st.write(i)


