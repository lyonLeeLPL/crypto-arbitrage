from gdax.order_book import OrderBook
import sys
import time
import datetime as dt

from gdax.public_client import PublicClient

if __name__ == '__main__':
	
	
	class Spread(OrderBook):

		def __init__(self, product_id = ''):
			super(Spread, self).__init__(product_id=product_id)

			self._bid = None
			self._ask = None
			self._bidDepth = None
			self._askDepth = None

		def on_message(self, message):
			super(Spread, self).on_message(message)
			
			bid = self.get_bid()
			bidDepth = sum([b['size'] for b in self.get_bids(bid)])
			ask = self.get_ask()
			askDepth = sum([a['size'] for a in self.get_asks(ask)])

			if self._bid == bid and self._ask == ask and self._bidDepth == bidDepth and self._askDepth == askDepth:
                		# If there are no changes to the bid-ask spread since the last update, no need to print
                		pass
            		else:
                		# If there are differences, update the cache
                		self._bid = bid
                		self._ask = ask
                		self._bidDepth = bidDepth
                		self._askDepth = askDepth
                		print('{} {} bid: {:.3f} @ {:.2f}\task: {:.3f} @ {:.2f}'.format(
                    			dt.datetime.now(), self.product_id, bidDepth, bid, askDepth, ask))
	
	# will add support for other pairs
	#first version will be designed for buying ETH/USD to BTC/USD only
	ethusd = Spread('ETH-USD')
	#ethusd.start()
	# wait 4 seconds due to websocket rate limit
	ethbtc = Spread('ETH-BTC')
	#ethbtc.start()
	btcusd = Spread('BTC-USD')
	#btcusd.start()
	ethusd.start()
	ethbtc.start()
	btcusd.start()

	
	#arbitrage logic to buy ETHUSD
	'''
	if ethusd.bid/ethbtc.bid == x:
		if 	
	'''
	
	try:
        	while True:
            		time.sleep(10)
    	except KeyboardInterrupt:
        	ethusd.close()
		ethbtc.close()
		btcusd.close()

    	if ethusd.error or ethbtc.error or btcusd.error:
        	sys.exit(1)
    	else:
        	sys.exit(0)
	
