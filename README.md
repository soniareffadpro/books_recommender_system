# 📚 Book Recommender System

## 🧠 About

This **Book Recommender System** leverages **Python**, **Streamlit**, and **scikit-learn** to suggest similar books based on user input.  
Using a dataset from **[Kaggle](https://www.kaggle.com/datasets/ra4u12/bookrecommendation)**, the system analyzes book ratings and computes similarities with the **Nearest Neighbors** algorithm.  
It provides an interactive **Streamlit interface** where users can select a book and instantly get the **top 5 recommended titles** with their cover images.


## 💡 How It Works

1. **Dataset Loading**  
   The system uses a dataset from Kaggle containing three main CSV files:  
   - **BX-Books.csv** → book details such as title, author, and cover image  
   - **BX-Users.csv** → user demographic information  
   - **BX-Book-Ratings.csv** → ratings assigned by users to books  

2. **Data Preprocessing**  
   In the Jupyter notebook, the raw data is cleaned and merged to create a structured dataset suitable for recommendation.  
   Missing or inconsistent values are handled, and book titles are standardized for accurate matching.  

3. **Building the User–Item Matrix**  
   A **pivot table** is created using `Pandas`, where rows represent books and columns represent users.  
   Each cell corresponds to a rating given by a user to a specific book.  

4. **Sparse Matrix Conversion**  
   Since most users do not rate all books, the matrix is mostly empty.  
   It is therefore converted into a **sparse matrix** using `csr_matrix` from **SciPy** to optimize memory and computation.  

5. **Training the Recommendation Model**  
   The **Nearest Neighbors** algorithm from **scikit-learn** is applied to the sparse matrix.  
   This model computes **similarity distances** between books to identify the most similar ones.  

6. **Model Storage**  
   The trained model, along with processed data (`model.pkl`, `books_name.pkl`, `data.pkl`, `pivot_data.pkl`), is saved in the `artifacts/` folder for quick loading during app execution.  

7. **Streamlit Interface**  
   The **Streamlit app** (`app.py`) provides a simple interactive interface where users can:  
   - Select a book title from a dropdown menu  
   - Get the **top 5 similar book recommendations**  
   - View book titles and **cover images** directly on the web page  



## 🚀 Setup

1. Clone the repository:
```bash
git clone https://github.com/soniareffadpro/Book-Recommender-System.git
cd Book-Recommender-System
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Rebuild the model using the Jupyter notebook
If you want to train or explore the recommender from scratch, open the notebook in root directory and re-run all cells.

5. Run the Streamlit app:
```bash
streamlit run app.py
```

## 🖥️ Usage

1. Select a book from the dropdown menu.

2. Click "Show Recommendation".

3. The app displays 5 similar books along with their cover images.

## 📊 Example

Input: "The Hobbit"

Output:
-  The Lord of the Rings
- Harry Potter and the Philosopher’s Stone
- Eragon
- The Silmarillion
- The Chronicles of Narnia

## 📁 Project Structure
```text
Book-Recommender-System/
│
├── data/                     # Dataset files (from Kaggle)
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── artifacts/                # Pre-trained model and intermediate data
│   ├── model.pkl
│   ├── books_name.pkl
│   ├── data.pkl
│   └── pivot_data.pkl
│
├── recommender_system.ipynb  # Data cleaning & model building
│
├── app.py                    # Main Streamlit app
├── requirements.txt          # Project dependencies
└── README.md           

```
