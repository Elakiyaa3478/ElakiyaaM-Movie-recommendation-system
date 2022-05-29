# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pickle
import pandas as pd
import requests
import sklearn
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(page_title='Movie Recommendation Engine',page_icon=":shark:")
hide_menu_style="""
<style>
footer {visibility:hidden;}
</style>
"""


st.snow()
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title('MOVIE RECOMMENDATION SYSTEM')

def fetch_poster(movie_id):
	response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4598347883cd2c7cfa21b58fcf3d60cc&language=en-US'.format(movie_id))
	data=response.json()
	return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):

	movie_index = movies[movies['title'] == movie].index[0]
	distances = similarity[movie_index]
	movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
	recommended_movies=[]
	recommended_movies_posters=[]
	for i in movies_list:
		movie_id=movies.iloc[i[0]].movie_id
		recommended_movies.append(movies.iloc[i[0]].title)
		recommended_movies_posters.append(fetch_poster(movie_id))
	return recommended_movies,recommended_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.subheader("I RECOMMEND MOVIES BASED ON YOUR INTEREST!!")

selected_movie_name=st.selectbox("ENTER YOUR FAVOURITE MOVIE",movies['title'].values)
if st.button('Recommend'):
	st.subheader("Recommending best movies for you..")
	names,posters=recommend(selected_movie_name)
	col1,col2,col3,col4,col5=st.columns(5)
	with col1:
		st.caption(names[0])
		st.image(posters[0])
	with col2:
		st.caption(names[1])
		st.image(posters[1])

	with col3:
		st.caption(names[2])
		st.image(posters[2])
	with col4:
		st.caption(names[3])
		st.image(posters[3])
	with col5:
		st.caption(names[4])
		st.image(posters[4])











