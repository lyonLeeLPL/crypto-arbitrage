### crypto-arbitrage
Uses the GDAX websocket feed to automate triangle arbitrage between ETHUSD, BTCUSD, ETHBTC pairs

Example:

	BTC-USD bid: 7170.56
	ETH-BTC bid: 0.09894
	ETH-USD ask: 708.25

	Start $708.25
	Buy 1 ETH @ 708.25 = 1 ETH
	Sell 1 ETH for BTC at 0.09894 = 0.09894 BTC
	Sell 0.09894 BTC for USD at 7170.56 = $709.45
	Profit = 709.45 - 708.25 = $1.20


Run on AWS us-east1 region for best performance

Use at your own risk
