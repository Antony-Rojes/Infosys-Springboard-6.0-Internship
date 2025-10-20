import streamlit as st
import pandas as pd
data_path = r"C:\Users\M.ANTONY ROJES\Downloads\Infosys\Deployment\Player_Market_Value_Prediction_Dataset.csv"
df = pd.read_csv(data_path)
df.fillna("Unknown", inplace=True)
if 'Player Name' in df.columns:
    df.rename(columns={'Player Name': 'player'}, inplace=True)
st.set_page_config(
    page_title="TransferIQ: Market Value Predictor",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.header("🔍 Player Explorer")
st.sidebar.markdown("Select a player to view predictions, valuation, and profile insights.")
players_list = sorted(df['player'].dropna().unique())
selected_player = st.sidebar.selectbox("🎯 Choose a player", players_list)
st.title("Football Player Market Value Prediction Dashboard")
st.markdown("""
Welcome to **TransferIQ**, your intelligent football analytics companion.  
Explore player valuation powered by advanced machine learning models and enriched sentiment analysis.
""")
if selected_player:
    player_row = df[df['player'] == selected_player].iloc[0]
    usd_value = player_row.get('Market Value (M)', 0)
    exchange_rate = 88.73
    inr_value = usd_value * 1_000_000 * exchange_rate
    st.markdown(f"## 📊 Market Value for **{selected_player}**")
    col1, col2 = st.columns([1, 2])
    col1.metric("💵 USD Value", f"${usd_value:.2f} M")
    col2.metric("🇮🇳 INR Value", f"₹{inr_value:,.0f}")
    st.divider()
    st.markdown("### 🧠 Player Profile")
    profile_fields = ['Age', 'Injury Status', 'Sentiment Label']
    profile_cols = st.columns(len(profile_fields))
    for i, field in enumerate(profile_fields):
        value = player_row.get(field, "Unknown")
        profile_cols[i].markdown(f"**{field}:** {value}")
    st.divider()
    st.markdown("### 📈 Prediction Metrics")
    pred_fields = ['y_test', 'lstm_preds', 'ensemble_preds', 'lstm_market_value', 'ensemble_market_value']
    pred_cols = st.columns(2)
    for i, field in enumerate(pred_fields):
        value = player_row.get(field, "Unknown")
        if isinstance(value, (int, float)):
            pred_cols[i % 2].markdown(f"**{field}:** `{value:.4f}`")
        else:
            pred_cols[i % 2].markdown(f"**{field}:** `{value}`")
    st.divider()
    st.markdown("📌 *All predictions are generated using TransferIQ's LSTM and ensemble modeling pipeline.*")