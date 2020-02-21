
# moneyChamber V2
> Stock portfolio with clear performance graph.

## Why use moneyChamber ?
While most stock portfolios looks like this:
[![bad portfolio](https://i.ibb.co/t8bSQYY/Figure-2.png)]()
The always going up trend looks amazing, makes you feel like since you started you made loads of money, but all you see are (mostly) your deposits. 

Portfolios should look more like this:
[![good portfolio](https://i.ibb.co/5Lgvfkb/Figure-1.png)]()
Performance based only on price movement and received dividends.

That looks much more realistic, right ? 



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
- This statement can be recieved as monthly Trading212 email statement, or can be manually added/adjusted.

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
- If you have got any issues or ideas for this package, or just wanna say hello :), email me at hmelino.github@gmail.com

