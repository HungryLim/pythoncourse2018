
class Stock(object):
    def __init__(self, price, symbol):
        self.price = price 
        self.symbol = str(symbol)
    
    def __str__(self): 
        return "price: %d, symbol: %s" %(self.price, self.symbol)

s=Stock(20,"BRT")
print s


class MutualFund(object):
     def __init__(self, symbol):

        self.symbol = str(symbol)

     def __str__(self): 
        return "symbol: %s" %(self.symbol)

m=MutualFund("APP")
print m

####################################
print s.price
portfolio=Portfolio()
portfolio.addCash(500)
portfolio.withdrawCash(2000)

portfolio.buyStock(2,s)
portfolio.sellStock(1,s)
print portfolio

portfolio.buyMutualFund(1,m)




####################################
class Portfolio(object):
    def __init__(self):
        self.stocks = {}
        self.mutualfunds = {}
        self.cash = 0 
        self.log = []

    def __str__(self): 
        return "stock: %s, mutualfunds: %s, cash: %d" %(self.stocks, self.mutualfunds, self.cash)

    def addCash(self,cash):
        self.cash += cash
        add = "I add %d" %(self.cash)
        print add
        self.log.append(add)

    def withdrawCash(self,cash):
        if self.cash < cash :
            print "Not enough money"
        else: 
            self.cash -= cash
            print self.cash

    def buyStock(self, share, stock ):
        if self.cash < stock.price * share:
                print "Not enough money"
        else:
            if  stock.symbol in self.stocks.keys(): 
                self.stocks[stock.symbol] += share
                self.cash -= stock.price*share
                print self.stocks
            else: 
                self.stocks[stock.symbol] = share
                self.cash -= stock.price*share
                print self.stocks

    def sellStock(self,share,stock):
        if stock.symbol in self.stocks.keys():
             if self.stocks[stock.symbol] < share:
                 print "Not enough share"
             else:
                self.stocks[stock.symbol] -= share
                import random
                self.cash - random.uniform(0.5*stock.price, 1.5*stock.price) * share
                print self.stocks
        else: 
             print "You don't have the stocks for the company."
   
    def buyMutualFund(self, share, mutualfund ):
        if self.cash < share*1:
                print "Not enough money"
        else:
            if  mutualfund.symbol in self.mutualfunds.keys(): 
                self.mutualfunds[mutualfund.symbol] += share
                self.cash -= share*1
                print self.mutualfunds
            else: 
                self.mutualfunds[mutualfund.symbol] = share
                self.cash -=share*1
                print self.mutualfunds

    def sellMutualFund(self,symbol, share):
         if  (stock.mutualfunds in self.mutualfunds.symbol) :
             if self.mutualfunds.share < share:
                 print "Not enough share"
             else:
                self.stocks.mutualfunds.update -= share
                self.cash - uniform(0.9,1.2) * share
         else: 
             print "You don't have that stocks."

Portfolio.buyStock(1,s)