# About

Hedgecraft is an open-source portfolio selection algorithm that address many of the shortcomings of the efficient frontier model of modern portfolio theory (MPT). The algorithm is designed to handle historical time series of unequal dimensions and detect non-linear associations between assets, enabling optimization across asset classes with sparse data. For a comprehensive walkthrough of the project please see the [Hedgecraft notebook](https://nbviewer.jupyter.org/github/mayabenowitz/Hedgecraft/blob/master/notebooks/Hedgecraft.ipynb).

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
# Motivation

## Wrestling with Imperfect Data

Hedgecraft, like MPT, is built on the theory of diversification: by selecting assets whose pairwise correlations are minimal, in theory, an optimal allocation that yields superior risk-adjusted returns can be obtained. The difficulty of this approach is that the correlations are non-stationary (e.g., see the [Financial 15 Index of South Africa](http://www.turingfinance.com/wp-content/uploads/2014/09/financial-fifteen-correlations.png)) and are known to harbor non-linear effects ([Haluszczynski, 2017](https://arxiv.org/pdf/1712.02661.pdf); [Hsieh, 1995](https://faculty.fuqua.duke.edu/~dah7/faj1995.pdf)). To make matters worse financial data is incredibly sparse. While there's plenty of historical data for stocks, the same can't be said for fixed income or alternative assets, for example. In practice, and more often than not, quantitative analysts face the problem of estimating correlations between time series of unequal dimension.

There are two types of missing data in financial time series: periodically missing values and entirely missing trajectories (I.e., time series that abruptly end). Depicted in the above diagram is the case where most of the assets have missing trajectories, and hence replacing their missing values becomes a problem of forecasting. Pearson's correlation coefficient is of no help here since it (1) only captures linear associations in the data and (2) only works for time series of equal dimension.

## A Network-based Approach

There's been accumulating evidence that asset correlation networks follow a power-law degree distribution, which roughly means only a few nodes are weakly correlated with the rest of the network ([Tse, et al. 2010](http://cktse.eie.polyu.edu.hk/pdf-paper/JoEF-1009.pdf); [Boginski, et al. 2005](https://www.sciencedirect.com/science/article/pii/S0167947304000258)). An asset correlation network is a graph whose nodes are assets and whose edges are the pairwise correlations between the assets' historical time series (usually taken as the daily closing prices or logarithmic returns). The emergence of complex networks and the study of their fundamental organizing principles have garnered significant attention from the scientific community, large in part from the seminal works of [Albert Barabasi](https://www.barabasilab.com/) that show most of these networks are governed by simple "scale-free" laws. Forecasting financial time series is known to be [notoriously difficult](https://towardsdatascience.com/3-facts-about-time-series-forecasting-that-surprise-experienced-machine-learning-practitioners-69c18ee89387), but perhaps forecasting the evolution of asset correlation networks isn't? If asset correlation networks are driven by simple laws, then it's reasonable to assume these laws can be learned by a single ML algorithm (as opposed to learning a model for each time series). What's more, these observations suggest the degree distribution of asset correlation networks are stationary, further suggesting the selected ML model need only be trained once (as opposed to continuously).

## Communicability of Complex Networks

How do rumors or ideas spread from person to person? How do computer viruses jump from email to email? What can be done to amplify the communication of ideas or to prevent a computer from getting a virus via email? These are all questions of the communicability of complex networks: how things spread and which nodes have the greatest influence in the process ([Estrada & Hatano, 2008](https://arxiv.org/pdf/0707.0756.pdf)). In the case of an asset correlation network, we're interested in how volatility spreads between assets and how we can act on such insights to optimize our portfolio. For example, suppose Apple suddenly loses 40% of its value, wiping out, say, two years of explosive gains. How would this highly volatile event ripple throughout our portfolio? Which of our assets would bear the brunt of the impact? Which would parry it unscathed? To this end, we aim to build a portfolio selection algorithm that can ingest imperfect data, anticipate changes in an asset correlation network, and predict how volatility propagates asset to asset.
