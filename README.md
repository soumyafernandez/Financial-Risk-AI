# 📊 FinRisk AI – Financial Risk Analysis Dashboard

FinRisk AI is an interactive financial analytics dashboard that allows users to analyze stock market performance and evaluate financial risk using real-time market data.

This project demonstrates how **data science, financial analytics, and visualization** can be combined to build a **FinTech-style risk analysis tool**.

The dashboard fetches stock market data, calculates financial metrics, and visualizes insights through an interactive web application.

---

## 🚀 Features

- 📈 Stock Price Trend Visualization
- 📊 Historical Market Data Analysis
- 📉 Daily Returns Calculation
- ⚠️ Volatility (Risk Measurement)
- 📊 Returns Distribution Visualization
- 🎛 Interactive Stock Ticker Input
- 📅 Custom Date Range Selection

---
## 📸 Dashboard Preview

![Dashboard]("Output pictures/Financial Risk Dashboard.png")

## 🧠 Technologies Used

### Streamlit
Streamlit is used to create the interactive dashboard interface.  
It allows developers to build web applications directly using Python.

Features used:
- Interactive dashboard layout
- Sidebar inputs
- Data tables and charts
- Financial metrics display

---

### Pandas
Pandas is used for data manipulation and analysis.

It helps to:
- Store stock data in DataFrames
- Perform time-series analysis
- Calculate daily returns and volatility

Example:

```python
data["Returns"] = data["Close"].pct_change()
```

---

### yfinance

yfinance is used to download historical stock market data from Yahoo Finance.

It retrieves:
- Open price
- Close price
- High and low prices
- Trading volume

Example:

```python
data = yf.download(ticker, start=start_date, end=end_date)
```

---

### Plotly Express

Plotly Express is used to create interactive financial charts.

Advantages:
- Interactive graphs
- Zoom and hover functionality
- Professional financial visualizations

Example:

```python
fig = px.line(data, x=data.index, y="Close")
```

---

## 🏷 What is a Stock Ticker?

A **stock ticker** is a unique symbol used to identify publicly traded companies in stock markets.

Examples:

| Company | Ticker |
|--------|--------|
| Apple | AAPL |
| Tesla | TSLA |
| Microsoft | MSFT |
| Reliance Industries | RELIANCE.NS |

Users can enter a ticker symbol in the dashboard to analyze that company's stock performance.

---

## 📉 Financial Metrics Used

### Daily Returns

Daily return measures the percentage change in stock price between trading days.

Formula:

```
Daily Return = (Today's Price − Yesterday's Price) / Yesterday's Price
```

---

### Volatility

Volatility measures how much a stock price fluctuates over time and is used as a key indicator of financial risk.

Formula used in this project:

```
Volatility = Standard Deviation of Returns × √252
```

Where **252 represents the number of trading days in a year**.

---

## ⚙️ How the Project Works

### 1️⃣ User Input

The user enters:
- Stock ticker symbol
- Start date
- End date

---

### 2️⃣ Data Collection

The application downloads stock data using **yfinance**.

---

### 3️⃣ Data Processing

Using **Pandas**, the system calculates:
- Daily returns
- Average returns
- Volatility

---

### 4️⃣ Data Visualization

Using **Plotly Express**, the dashboard generates charts such as:
- Stock price trend
- Daily returns
- Returns distribution

---

### 5️⃣ Dashboard Display

Using **Streamlit**, all results are displayed in an interactive dashboard.

---

## 💻 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/FinRiskAI.git
cd FinRiskAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Purpose of the Project

The goal of this project is to demonstrate:

- Financial risk analysis
- Data-driven investment insights
- FinTech dashboard development
- Real-world financial data processing

This project serves as a **portfolio project for Financial Analyst, Risk Analyst, and FinTech roles**.

---

## 🚀 Future Improvements

- Portfolio optimization (weight allocation)
- AI-based stock recommendations
- News sentiment analysis
- Deployment on cloud (Streamlit Cloud / AWS)

---

## 👩‍💻 Author

**Soumya Fernandez**
