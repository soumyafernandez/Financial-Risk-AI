import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import numpy as np

st.set_page_config(page_title="FinRisk AI", layout="wide")

st.title("📊 FinRisk AI — Financial Risk Dashboard")

# Sidebar
st.sidebar.markdown("## 📊 FinRisk AI")
st.sidebar.markdown("Analyze stocks & portfolio risk")

ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Download stock data
with st.spinner("Downloading stock data..."):
    data = yf.download(ticker, start=start_date, end=end_date)

if len(data) == 0:
    st.warning("No data found. Try another ticker.")

else:
    # Fix multi-index issue
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    st.subheader("Stock Price Data")
    st.dataframe(data.tail())

    # ==========================
    # 📈 Price Chart
    # ==========================
    st.subheader("📈 Closing Price Trend")

    fig = px.line(data, x=data.index, y="Close", title=f"{ticker} Closing Price")
    st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # 📊 Returns
    # ==========================
    data["Returns"] = data["Close"].pct_change().dropna()

    st.subheader("📊 Daily Returns")

    fig2 = px.line(data, x=data.index, y="Returns")
    st.plotly_chart(fig2, use_container_width=True)

    # ==========================
    # 📉 Risk Metrics
    # ==========================
    volatility = np.std(data["Returns"]) * np.sqrt(252)

    st.subheader("📉 Risk Metrics")

    col1, col2 = st.columns(2)

    col1.metric("Annual Volatility", round(volatility, 4))
    col2.metric("Average Daily Return", round(data["Returns"].mean(), 4))

    st.subheader("Returns Distribution")

    fig3 = px.histogram(data, x="Returns", nbins=50)
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # ==========================
    # 📊 Portfolio Analysis
    # ==========================
    st.subheader("📊 Portfolio Risk Analysis")

    portfolio = st.text_input(
        "Enter portfolio tickers (comma separated)",
        "AAPL,MSFT,TSLA"
    )

    tickers = [t.strip() for t in portfolio.split(",")]

    portfolio_data = yf.download(tickers, start=start_date, end=end_date)["Close"]

    # Handle single ticker case
    if isinstance(portfolio_data, pd.Series):
        portfolio_data = portfolio_data.to_frame()

    returns = portfolio_data.pct_change().dropna()

    # Equal weights
    weights = np.ones(len(tickers)) / len(tickers)

    portfolio_returns = returns.dot(weights)

    # Portfolio metrics
    portfolio_volatility = np.std(portfolio_returns) * np.sqrt(252)
    portfolio_return = np.mean(portfolio_returns) * 252

    risk_free_rate = 0.02

    if portfolio_volatility != 0:
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    else:
        sharpe_ratio = 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Portfolio Return", round(portfolio_return, 4))
    col2.metric("Portfolio Volatility", round(portfolio_volatility, 4))
    col3.metric("Sharpe Ratio", round(sharpe_ratio, 4))

    st.subheader("Portfolio Returns Over Time")

    fig4 = px.line(portfolio_returns, title="Portfolio Returns")
    st.plotly_chart(fig4, use_container_width=True)

    # ==========================
    # 📊 Correlation
    # ==========================
    st.subheader("📊 Correlation Heatmap")

    correlation_matrix = returns.corr()

    fig5 = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Stock Correlation Matrix"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("---")

    # ==========================
    # 🎯 Monte Carlo Simulation
    # ==========================
    st.subheader("🎯 Monte Carlo Simulation")

    num_simulations = 100
    num_days = 252

    simulation_results = np.zeros((num_days, num_simulations))

    for i in range(num_simulations):
        simulated_returns = np.random.normal(
            portfolio_returns.mean(),
            portfolio_returns.std(),
            num_days
        )

        simulation = np.cumprod(1 + simulated_returns)
        simulation_results[:, i] = simulation

    sim_df = pd.DataFrame(simulation_results)

    fig6 = px.line(sim_df, title="Monte Carlo Simulation")
    st.plotly_chart(fig6, use_container_width=True)

    final_values = sim_df.iloc[-1]

    st.subheader("📊 Simulation Insights")

    col1, col2, col3 = st.columns(3)

    col1.metric("Best Case", round(final_values.max(), 2))
    col2.metric("Worst Case", round(final_values.min(), 2))
    col3.metric("Average Outcome", round(final_values.mean(), 2))

    # ==========================
    # 📉 VaR
    # ==========================
    st.subheader("📉 Value at Risk (VaR)")

    VaR = portfolio_returns.quantile(0.05)

    st.metric("95% VaR", round(VaR, 4))

    fig7 = px.histogram(portfolio_returns, nbins=50)

    fig7.add_vline(
        x=VaR,
        line_dash="dash",
        annotation_text="VaR"
    )

    st.plotly_chart(fig7, use_container_width=True)

    # ==========================
    # 📉 CVaR
    # ==========================
    st.subheader("📉 Conditional VaR (CVaR)")

    CVaR = portfolio_returns[portfolio_returns <= VaR].mean()

    st.metric("CVaR", round(CVaR, 4))

    # ==========================
    # ⚠️ Risk Level
    # ==========================
    st.subheader("⚠️ Risk Level")

    if portfolio_volatility < 0.15:
        risk_level = "Low Risk 🟢"
    elif portfolio_volatility < 0.30:
        risk_level = "Moderate Risk 🟡"
    else:
        risk_level = "High Risk 🔴"

    st.metric("Portfolio Risk Level", risk_level)

    # ==========================
    # 🧠 AI Insights
    # ==========================
    st.subheader("🧠 AI Insights")

    if sharpe_ratio > 1:
        st.success("Strong risk-adjusted returns")
    else:
        st.warning("Improve risk-return balance")

    if portfolio_volatility > 0.25:
        st.warning("High volatility detected")

    avg_corr = correlation_matrix.mean().mean()

    if avg_corr > 0.7:
        st.warning("Poor diversification")
    else:
        st.success("Well diversified portfolio")

    if final_values.min() < 0.5:
        st.error("High downside risk in worst case")