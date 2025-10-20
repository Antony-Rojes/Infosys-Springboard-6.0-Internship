<h1>⚽ Football Player Market Value Prediction</h1>
<h2>📄 Abstract</h2>

This project develops a football player market value prediction system using structured data (performance, injury, market) and unstructured social media sentiment 💬. Data were collected from StatsBomb ⚽, Transfermarkt , and the Twitter API .

Built with Python , the system employs Pandas and NumPy for data processing, scikit-learn for preprocessing, and NLTK/TextBlob for sentiment analysis. The pipeline includes data collection, cleaning, feature engineering, and integration across key domains — performance, injury, market, and sentiment.

Two machine learning models were implemented:

🧠 Multivariate LSTM for capturing temporal dependencies

⚙️ XGBoost Regressor for non-sequential prediction

An optimized ensemble model combining both approaches achieved a normalized RMSE of 0.3334 and MAE of 1.74 📊.

Deployment was carried out using Joblib, with a Streamlit dashboard — TransferIQ 💻 providing real-time, interactive player valuation.

This project demonstrates the integration of data science, deep learning, and sentiment analytics to deliver actionable insights for football analytics, recruitment, and market evaluation 📈.

<h1>🧰 Tech Stack & Tools</h1>
<h2>🐍 Programming & Libraries</h2>

Python — Core language for data analysis and modeling

Pandas 📊 — Data manipulation and cleaning

NumPy 🔢 — Numerical computing and matrix operations

scikit-learn 🤖 — Preprocessing, feature scaling, and model evaluation

NLTK / TextBlob 💬 — Sentiment analysis from social media text

<h2>🧠 Machine Learning & Deep Learning</h2>

LSTM (Keras / TensorFlow) — Sequential model for performance time series

XGBoost ⚙️ — Gradient boosting for non-sequential regression

KerasTuner / RandomizedSearchCV 🎯 — Hyperparameter tuning

<h2>💾 Data Sources</h2>

StatsBomb Open Data ⚽ — Match event and player performance data

Transfermarkt 💸 — Player market and transfer valuations

Twitter API 🐦 — Social sentiment extraction

<h2>🚀 Deployment & Visualization</h2>

Joblib 🗂️ — Model persistence and storage

Streamlit 💻 — Interactive dashboard (TransferIQ) for real-time predictions

🧩 Development Tools

Jupyter Notebook 📓 — Prototyping and analysis

VS Code 🧑‍💻 — Project development environment

Git & GitHub 🌐 — Version control and project management
