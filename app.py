import pickle
import streamlit as st
import numpy as np

# import data
st.header('Book Recommender System')
model = pickle.load(open('artifacts/model.pkl','rb'))
books_name = pickle.load(open('artifacts/books_name.pkl','rb'))
data = pickle.load(open('artifacts/data.pkl','rb'))
pivot_data = pickle.load(open('artifacts/pivot_data.pkl','rb'))


def fetch_poster(suggestion):
    poster_url = []

    # suggestion is an array of shape (1, n_neighbors)
    for book_indices in suggestion:
        for book_id in book_indices:
            book_name = pivot_data.index[book_id]
            ids = np.where(data['title'] == book_name)[0][0]
            url = data.iloc[ids]['img_url']
            poster_url.append(url)
    
    return poster_url




def recommend_book(book_name):
    books_list = []
    book_id = np.where(pivot_data.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(
        pivot_data.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6
    )

    poster_url = fetch_poster(suggestion)
    
    for book_indices in suggestion:
        for idx in book_indices:
            books_list.append(pivot_data.index[idx])
    
    return books_list, poster_url
      



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    books_name
)


if st.button('Show Recommendation', key='show_recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    
    cols = st.columns(len(recommended_books)-1)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_books[i+1])
            st.image(poster_url[i+1])
            # Example button (if any) inside the loop
            # st.button("Add to Cart", key=f"add_{i}")
