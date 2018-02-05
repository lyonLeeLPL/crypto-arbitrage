from websocket import WebSocketApp
from json import dumps, loads
import logging
logging.basicConfig(filename='ticks2.log', level=logging.DEBUG)
URL = "wss://ws-feed.gdax.com"

def on_message(_, message):
    
    #pprint(loads(message))
    m = loads(message)
    logging.info(m)
    #print m
    #print m
    #if m['type'] == 'ticker':
    	#logging.info(str(','.join(list(m['open_24h'],m['product_id'],m['price'],m['best_ask'],m['best_bid'],m['high_24h'],m['volume_24h'],m['last_size'],m['time'],m['volume_30d'],m['side'],m['low_24h']))))
    

def on_open(socket):
   
    params = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
    }
    socket.send(dumps(params))

def main():
   
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == '__main__':
    main()

