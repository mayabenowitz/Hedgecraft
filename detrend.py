import pandas as pd
import numpy as np
import preproc as pre

cols = ["Date", "Open", "High", "Low", "Close", "Volume", "Name"]
names = [
    "MMM",
    "AXP",
    "AAPL",
    "BA",
    "CAT",
    "CVX",
    "CSCO",
    "KO",
    "DIS",
    "XOM",
    "GE",
    "GS",
    "HD",
    "IBM",
    "INTC",
    "JNJ",
    "JPM",
    "MCD",
    "MRK",
    "MSFT",
    "NKE",
    "PFE",
    "PG",
    "TRV",
    "UTX",
    "UNH",
    "VZ",
    "WMT",
    "GOOGL",
    "AMZN",
    "AABA"
]


def detrend():
    df = pre.preproc()

    # detrends each stock time series using the difference method
    for n in names:
        df[n] = df[n].diff()

    return df


if __name__ == "__main__":
    detrend()
