from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
from api import APIKEY, SECRETKEY

client = Client(APIKEY, SECRETKEY)