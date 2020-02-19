
# moneyChamber V2
> Stock portfolio with clear performance graph.

## Why use moneyChamber ?
With moneyChamber you will get clear view on portfolio performance which is based entirely on stock price changes and dividends payments. It doesnt include deposits as most portfolios does, which is usually confusing. 

## Installation
### Clone

- Clone this repo to your local machine using ' git clone https://github.com/hmelino/moneyChamber.git'
### API key 
- moneyChamber require worldtradingdata api key to download and process history stock prices.
- FREE api key can be obtained on [worldtradingdata.com](https://www.worldtradingdata.com/)
- once you have received your API key, please create new file called `sensData.py` and save it inside
> moneyChamber/sensData.py
```Python
apiKey='your_worldtradingdata_api_key'
```
### Statement
- All stock data are being imported from file  statement.txt which looks like :
```Python
1	POS123456789	2019.04.29 12:36	Buy	69	VUKE	32.4349				32.17	-18.28	0
2	POS123456788	2018.10.26 10:02	Buy	1	VMID	29.435				33.305	3.87	0
3	POS123456787	2018.12.10 10:00	Buy	5	PSN	2213.6				3054	42.02	0
```
- You can usually get statement like from Trading212 monthly email statement, or you can manually adjust/add values from this example statement.

## Use

> Import the package 

```Python
import moneyChamber
```

> Initialize new object with CreatePortfolio() function and run the code.

```Python
retirementPortfolio = moneyChamber.Portfolio()
```
>Output will be performance graph of your portfolio.


## Contact

- Website at <a href="https://github.com/hmelino" target="_blank">`https://github.com/hmelino`</a>


