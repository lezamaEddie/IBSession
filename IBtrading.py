#pip install ibapi
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

#realtime 
from ibapi.contract import Contract
import threading
import time


#for orders
from ibapi.order import *




class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self) #initializes the client
    
    

class ibConnect:
    ib = None
    def __init__(self):
        #connect to IB TWS
        self.ib = IBApi()    #see the class
        self.ib.connect("127.0.0.1", 7497, 1) #Local IP used, 7497 port used, 1 because suggested value

        ib_thread = threading.Thread(target=self.run_loop, daemon=True) #placing IBapi on separate thread and updates IB actions
        ib_thread.start()
        time.sleep(1) #making IBSession take a break between actions


    def buy_order(self, symbol, amount):

        #CREATING ORDER, determines the type, buy/sell, and amount
        order = Order()
        order.orderType = "MKT" #order type is on a market
        order.action = "BUY" 
        order.totalQuantity = amount

        #CONTRACT FOR ORDER, determines what stock, if it is a stock, what exchange to use, currency, and backup exchange
        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK" #other types such as futures available
        contract.exchange = "SMART" #automatically determines best exchange
        contract.currency = "USD" 
        contract.primaryExchange = "ISLAND" #backup exchange
        
        
        #PLACE THE ORDER
        self.ib.placeOrder(int(round(time.time())), contract, order) #ID MUST BE UNIQUE (uses time)
        time.sleep(1) #ensures uniqueness of every time ID
        

    def sell_order(self, symbol, amount):
        #CREATING ORDER, determines the type, buy/sell, and amount
        order = Order()
        order.orderType = "MKT"
        order.action = "SELL"
        order.totalQuantity = amount

        #CONTRACT FOR ORDER, determines what stock, if it is a stock, what exchange to use, currency, and backup exchange
        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK" #other types such as futures available
        contract.exchange = "SMART" #automatically determines best exchange
        contract.currency = "USD" 
        contract.primaryExchange = "ISLAND" #backup exchange
        
       
        #PLACE THE ORDER
        self.ib.placeOrder(int(round(time.time())), contract, order) #ID MUST BE UNIQUE (uses time)
        time.sleep(1) #ensures uniqueness of every time ID


    def run_loop(self):
        self.ib.run()

    
    


ibSession = ibConnect() #initations IB session
ibSession.buy_order("AAPL", 54)
ibSession.sell_order("AAPL", 34)

ibSession.buy_order("GOOGL", 5)
ibSession.sell_order("GOOGL", 1)
