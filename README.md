<h1>Abstract</h1>
This project presents a comprehensive football player market value prediction system, leveraging 
structured performance, injury, and market data along with unstructured social media sentiment to 
produce accurate, data-driven valuations. Data sources included StatsBomb Open Data for granular 
match events, Transfermarkt for player transfer and market valuations, and Twitter API for public 
sentiment analysis. Python was the core programming language, with Pandas and NumPy employed 
for data processing, scikit-learn for preprocessing and scaling, and NLTK/TextBlob for sentiment 
analysis. 
The project followed a systematic data engineering pipeline, starting with data collection, cleaning, 
preprocessing, and feature engineering across four key domains: performance, injury, market, and 
sentiment. Sequential and non-sequential features were integrated into a unified dataset, standardized 
and imputed for completeness. Machine learning models included a Multivariate LSTM to capture 
temporal dependencies in player performance and an XGBoost Regressor as a non-sequential 
benchmark. Hyperparameter optimization was performed using KerasTuner and 
RandomizedSearchCV, resulting in an optimized ensemble model combining both approaches. 
Final model evaluation demonstrated a stable predictive framework, achieving a normalized RMSE of 
0.3334 and MAE of 1.74. Model persistence and deployment were handled using Joblib, with 
production-ready scripts and a Streamlit-based dashboard, TransferIQ, enabling interactive, real-time 
player market value predictions. This project demonstrates the effective fusion of multi-domain 
structured data, deep learning, ensemble methods, and sentiment analysis into a practical tool for 
football analytics, recruitment, and market evaluation.
