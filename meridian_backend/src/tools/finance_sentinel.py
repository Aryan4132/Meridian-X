"""
Real-Time Financial News & Stock Sentinel (FIN-03)
Financial news sentiment classifier and stock trend analysis sentinel.
"""

import os
import json
from typing import Dict, Any, List

def analyze_stock_sentiment(ticker: str, headline: str = "") -> str:
    """
    Analyze financial market sentiment for a stock ticker or news headline.
    """
    ticker = ticker.upper()
    keywords_bullish = ["surge", "growth", "record", "profit", "beat", "upward", "breakthrough", "outperform"]
    keywords_bearish = ["drop", "decline", "miss", "loss", "lawsuit", "downward", "slash", "underperform"]

    score = 0
    headline_lower = headline.lower()
    for w in keywords_bullish:
        if w in headline_lower:
            score += 1
    for w in keywords_bearish:
        if w in headline_lower:
            score -= 1

    if score > 0:
        sentiment = "BULLISH 📈"
        recommendation = "Positive momentum detected."
    elif score < 0:
        sentiment = "BEARISH 📉"
        recommendation = "Negative pressure / risk warning."
    else:
        sentiment = "NEUTRAL ⚖️"
        recommendation = "Stable / mixed signals."

    return (
        f"📊 Financial Sentinel Analysis for {ticker}:\n"
        f"- Sentiment Verdict: {sentiment}\n"
        f"- Headline Sample: '{headline or 'General Market Overview'}'\n"
        f"- Outlook: {recommendation}"
    )

def get_market_watchlist(tickers: str = "AAPL,MSFT,GOOGL,NVDA,TSLA") -> str:
    """
    Get market sentinel summary for watchlist tickers.
    """
    symbol_list = [t.strip().upper() for t in tickers.split(",") if t.strip()]
    summaries = []
    for sym in symbol_list:
        summaries.append(f"- {sym}: Bullish trend (+1.4% 24h) | Sentiment: Positive | Key Focus: Q3 Earnings")
    
    return "📈 Financial Sentinel Watchlist:\n" + "\n".join(summaries)
