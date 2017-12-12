from gdax.order_book import OrderBook
import sys
import time
import datetime as dt

from gdax.public_client import PublicClient

if __name__ == '__main__':
	
	'''
	class ArbitrageTrader(EthUsdOrderBook, EthBtcOrderBook, BtcUsdOrderBook):

		def __init__(self, product_id = ''):
			super(ArbitrageTrader, self).__init__(product_id=product_id)

			self._EthUsd = {"bid" : None, "bidDepth" : None, "ask" : None, "askDepth": None}
			self._EthBtc = {"bid" : None, "bidDepth" : None, "ask" : None, "askDepth": None}
			self._BtcUsdBid = {"bid" : None, "bidDepth" : None, "ask" : None, "askDepth": None}

		def on_message(self, message):
			super(ArbitrageTrader, self).on_message(message)
	'''
	# will add support for other pairs
	#first version will be designed for buying ETH/USD to BTC/USD only
	ethusd = OrderBook('ETH-USD')
	ethusd.start()
	ethbtc = OrderBook('ETH-BTC')
	ethbtc.start()
	btcusd = OrderBook('BTC-USD')
	btcusd.start()


	#arbitrage logic to buy ETHUSD
	'''
	if ethusd.bid/ethbtc.bid == x:
		if 	
	'''
	'''
	try:
        	while True:
            		time.sleep(10)
    	except KeyboardInterrupt:
        	order_book.close()

    	if order_book.error:
        	sys.exit(1)
    	else:
        	sys.exit(0)
	'''
