import pandas as pd
import numpy as np
import re

cols = ["Date", "Open", "High", "Low", "Close", "Volume", "Name"]
name = [
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

# TODO Create seperate folder for Volume correlation network analysis
# TODO Repeat workflow and compute graph similarity between networks.


def preproc():
    # read the csv file in a dataframe
    df = pd.read_csv("all_stocks_2006-01-01_to_2018-01-01.csv")

    # convert 'Date' column to a datetime object
    df["Date"] = pd.to_datetime(df["Date"])

    # preprocess data for time series analysis
    df = df.pivot(index="Date", columns="Name", values="Close")

    return df


if __name__ == "__main__":
    preproc()
