# About

Hedgecraft is an open-source portfolio selection algorithm that address many of the shortcomings of the efficient frontier model of modern portfolio theory (MPT). The algorithm is designed to handle historical time series of unequal dimensions, enabling optimization across asset classes with sparse data. For a comprehensive walkthrough of the project please see the [Hedgecraft notebook](https://nbviewer.jupyter.org/github/mayabenowitz/Hedgecraft/blob/master/notebooks/Hedgecraft.ipynb).

## Installation

First clone the repository in a local folder

```html
git clone https://github.com/mayabenowitz/Hedgecraft.git
```

then run the scripts from the terminal with

```html
python {filename}.py
```
or

```html
python3 {filename}.py
```

E.g., typing

```html
python plt_corr_nx.py
```

in the terminal will plot a time series correlation network using the the data in the repository.

## Dependencies

A comprehensive list of current dependencies include the following libraries

```html
Pandas (data manipulation)
Numpy (scientific computing)
Scipy (statistical computing)
dcor (energy statistics)
NetworkX (graph analytics)
Matplotlib (plotting)
Seaborn (plotting)
pypfopt (portfolio optimization)
datetime (dates & times)
```
