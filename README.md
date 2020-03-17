
  

# moneyChamber V2

> Stock portfolio with clear performance graph.

  

## Why use moneyChamber ?

Most of stock portfolios will look like example below.

[![bad portfolio](https://i.ibb.co/t8bSQYY/Figure-2.png)]()



Portfolio seems to be growing, but at this case, all the growth you can see are mostly deposits. 

That's why I have designed and coded this Python stock portfolio, that excludes deposits and profit is based purely on stock price movement and paid dividends.

[![good portfolio](https://i.ibb.co/5Lgvfkb/Figure-1.png)]()

With moneyChamber you will receive much clearer overview on performance of your portfolio.

  
  
  



## How to clone moneyChamber
  >- Clone this repository to your local machine using
 ```Python
git clone https://github.com/hmelino/moneyChamber.git
```


## API key

>- moneyChamber require worldtradingdata api key to download and process history stock prices.
>
>- FREE api key can be obtained on [worldtradingdata.com](https://www.worldtradingdata.com/)


## Statement

>- All stock data are being imported from file statement.txt which looks like :

```Python

1 POS123456789 2019.04.29 12:36 Buy 69 VUKE 32.4349  32.17 -18.28  0

2 POS123456788 2018.10.26 10:02 Buy 1 VMID 29.435  33.305  3.87  0

3 POS123456787 2018.12.10 10:00 Buy 5 PSN 2213.6  3054  42.02  0

```

>- This statement can be recieved as monthly Trading212 email statement, or can be manually added/adjusted.

  

## How to use 
>Import the package
```Python
from moneyChamber import Porfolio
```
> Initialize new object with Portfolio() function and use path to your .txt [statement](#statement) as argument
  ```Python
retirementPortfolio = moneyChamber.Portfolio('statement.txt')
```
>Add your World Trading Data [api key](#api-key)

```Python
retirementPortfolio.apiKey='your_own_world_trading_data_api_key'
```
> **Optionally** you can load your paid [dividends](#dividends-file) file.
> ![Dividends](https://i.ibb.co/WH3mYPG/ezgif-7-5d4ddc7ad5ef.gif)]
```Python
retirementPortfolio.loadDividends('dividends.txt')
```
> When all files are loaded, you can plot graph using showGraph() function
```Python
retirement.showGraph()
```

## Dividends file
>To import details about paid dividends into moneyChamber, please save them in JSON style as seen below.
>
>{"name_of_stock":{"date_when_dividend_was_recieved":total_amount_recieved}
```JSON
{"VUKE": {"2019-06-29": 5.32, "2019-10-16": 9.23, "2020-01-02": 14.36},
 "VMID": {"2018-12-26": 0.22, "2019-03-27": 0.15}}
```
>MoneyChamber will automatically calculate dividend yeld and payment received per individual stock.
  
## Contact
>  - My github portfolio <a  href="https://github.com/hmelino"  target="_blank">`https://github.com/hmelino`</a>
>
>- If you have got any issues or ideas for this package, or just wanna say hello :), email me at hmelino.github@gmail.com