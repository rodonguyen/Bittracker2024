# BitTracker

A trading bot utilising SuperTrend Algorithm.

At its core, the Supertrend calculates an upperbound and lower bound and use them as threshold to buy/sell. Due to the trending nature of cryptocurrency, trailing stop for orders is analysed (by me) and proved to be suitable and bring great profit (great enough to cancel out multiple lost trades).

However, it's not efficient during sideway + volatile period. Therefore, you can consider to turn the bot off for time like this.

Here is a demo screenshot of Supertrend Indicator in TradingView. `Buy` is placed at the end of red line and `Sell` is placed at the end of green line.  
![tradingview-supertrend](/media/tradingview-supertrend.png)

Code modified from youtube. com/ watch?v=1PEyddA1y5E

## [Analysis code 🔗](experiment/2_analyse_backtest_result/analyse_backtest_result_2023.ipynb)

[View here](experiment/2_analyse_backtest_result/analyse_backtest_result_2023.ipynb)  
Go to these sections:  
- Analyse backtest result distribution, pick top configs with highest risk-adjusted returns
- Backtest result and analysis

## Blogs 🔗

I'm in the process of writing blogs to share about BitTracker, you can read it here: [A Trading Bot for Cryptocurrency - BitTracker (P.1)](https://rodonguyen.medium.com/a-trading-bot-for-cryptocurrency-bittracker-p-1-f0c211134c47)

<p align="center">
<a href='https://rodonguyen.medium.com/a-trading-bot-for-cryptocurrency-bittracker-p-1-f0c211134c47'><img src="media/blog-screenshot.png" alt="drawing" width="360" /></a>
</p>

## Dependencies

-   Pandas
-   CCXT

## Instruction

Class SupertrendBot (`supertrend.py`) is used to initiate bot's configuration and has necessary functions to run your bot and trade with the Exchanges. Quickly read through the `__init__` of this class to get an idea on what to include in its object initiation.

An example of a bot is [`bot_matic.py`](/bot_matic.py).

## Workflow

-   Get CoinApi API
    -   https://docs.coinapi.io/market-data/rest-api/ohlcv/ohlcv-list-all-periods
    -   https://docs.coinapi.io/market-data/rest-api/metadata/list-all-exchanges
    -   Bitcoin, oldest data in bitstamp
    -   Eth, oldest data in bitfinex
-   Download historical data: `0_get_historical_data.py`
-   Replace `;` with `,` in downloaded csv
-   Run `1_backtest/backtest.py`
-
