# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on genres, cast, crew, and plot overview. This was my first machine learning project, built to learn the fundamentals of text vectorization, similarity scoring, and deploying an ML model as a web app.

🔗 **Live demo:** [movie-recommendation-system-shahariar.streamlit.app](https://movie-recommendation-system-shahariar.streamlit.app/)

## How it works

The recommender uses **content-based filtering** rather than collaborative filtering — it doesn't rely on user ratings or behavior, but instead compares movies based on their actual content:

1. **Data preprocessing** — combined each movie's overview, genres, cast, crew, and keywords into a single tag string, then cleaned and normalized the text (lowercasing, stemming, removing noisy short numeric tokens).
2. **Vectorization** — converted the tags into numerical vectors using **TF-IDF** (Term Frequency–Inverse Document Frequency), which weights distinctive words (like a specific director's name or a niche genre) more heavily than common ones.
3. **Similarity scoring** — computed **cosine similarity** between movie vectors to measure how closely related two movies are based on their content.
4. **Recommendation** — given a selected movie, the system returns the 5 most similar movies by similarity score.
5. **Posters** — movie posters are fetched live from the [TMDB API](https://www.themoviedb.org/documentation/api) for a more visual result.

## Dataset

Built on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), covering roughly 5,000 movies from 1916–2017, with a strong skew toward modern, U.S.-produced films.

## Tech stack

- **Python** — pandas, scikit-learn (TF-IDF, cosine similarity)
- **Streamlit** — web app frontend
- **TMDB API** — movie posters
- **Streamlit Community Cloud** — deployment

## Running locally

```bash
git clone https://github.com/<your-username>/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
```

Create a `.streamlit/secrets.toml` file with your own TMDB API key:

```toml
TMDB_API_KEY = "your_api_key_here"
```

Then run:

```bash
streamlit run app.py
```

## What I learned

This project was my introduction to:
- Text vectorization techniques (Bag of Words, TF-IDF) and when to use each
- Cosine similarity for measuring content-based similarity
- Building and deploying a full ML-powered web app end to end
- Managing API keys and secrets safely in a public repo
- Working within free-tier deployment constraints (file size limits, memory caps)

## Future improvements

- Add collaborative filtering using user ratings for hybrid recommendations
- Cache poster fetches to reduce redundant API calls
- Add filtering by genre, year, or rating alongside recommendations
