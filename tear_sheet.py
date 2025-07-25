import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def generate_tear_sheet(ticker):
    stock = yf.Ticker(ticker)

    # Basic Info
    info = stock.info
    print(f"\n--- {info.get('longName')} ({ticker.upper()}) ---")
    print(f"Sector: {info.get('sector')}")
    print(f"Market Cap: ${info.get('marketCap'):,}")
    print(f"Forward P/E: {info.get('forwardPE')}")
    print(f"ROE: {info.get('returnOnEquity')}")
    print(f"Debt/Equity: {info.get('debtToEquity')}")

    # Historical Price Chart
    hist = stock.history(period="1y")
    hist['Close'].plot(title=f"{ticker.upper()} 1-Year Price Chart")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.tight_layout()
    plt.savefig(f"{ticker}_price_chart.png")
    plt.close()
    print(f"Chart saved as {ticker}_price_chart.png")

if __name__ == "__main__":
    ticker = input("Enter a stock ticker (e.g., AAPL): ")
    generate_tear_sheet(ticker)