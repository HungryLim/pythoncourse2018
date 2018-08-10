#############Lim; HW 1########################################
#############################################################

class Stock(object):
    def __init__(self, price, symbol):
        self.price = float(price)
        self.symbol = str(symbol)
    
    def __str__(self): 
        return "price: %.2f, symbol: %s" %(self.price, self.symbol)


class MutualFund(object):
     def __init__(self, symbol):

        self.symbol = str(symbol)

     def __str__(self): 
        return "symbol: %s" %(self.symbol)


####################################
class Portfolio(object):
    def __init__(self):
        self.stocks = {}
        self.mutualfunds = {}
        self.cash = float(0) 
        self.log = []

    def __str__(self): 
        return "stock: %s, mutualfunds: %s, cash: %.2f." %(self.stocks, self.mutualfunds, self.cash)

    def addCash(self,cash):
        self.cash += float(cash)
        add = "I add %.2f"  %(float(self.cash))
        print add
        self.log.append(add)

    def withdrawCash(self,cash):
        if self.cash < float(cash) :
            no_money = "Not enough money to withdraw."
            print no_money
            self.log.append(no_money)
        else: 
            self.cash -= float(cash)
            withdraw = "I withdraw %.2f." %(float(self.cash))
            print withdraw
            self.log.append(withdraw)

    def buyStock(self, share, stock ):
        if type(share) == float:
           error = "Error: Share is not whole number"
           print error
           self.log.append(error)
        else:
            if self.cash < stock.price * share:
                cant_buy_stock =  "Not enough money to buy stocks."
                print cant_buy_stock
                self.log.append(cant_buy_stock)
            else:
                if  stock.symbol in self.stocks.keys(): 
                    self.stocks[stock.symbol] += share
                    self.cash -= stock.price*share
                    buy_stock = "I bought %d share(s) of %s stock." %(share, stock.symbol)
                    print buy_stock
                    self.log.append(buy_stock)
                else: 
                    self.stocks[stock.symbol] = share
                    self.cash -= stock.price*share
                    buy_stock = "I bought %d share(s) of %s stock." %(share,stock.symbol )
                    print buy_stock
                    self.log.append(buy_stock)

    def sellStock(self,share,stock):
        if type(share) == float:
           error = "Error: Share is not whole number"
           print error
           self.log.append(error)
        else:
            if stock.symbol in self.stocks.keys():
                if self.stocks[stock.symbol] < share:
                    cant_buy = "Not enough share to sell."
                    print cant_buy
                    self.log.append(cant_buy)
                else:
                    self.stocks[stock.symbol] -= share
                    import random
                    self.cash -= random.uniform(0.5*stock.price, 1.5*stock.price) * share
                    sell_stock = "I sold %d share(s) of %s stock." %(share,stock.symbol )
                    print sell_stock
                    self.log.append(sell_stock)
            else:
                cant_sell = "You don't have the stock to sell."
                print cant_sell
                self.log.append(cant_sell)

    def buyMutualFund(self, share, mutualfund ):
        if type(share) == float:
           error = "Error: Share is not whole number"
           print error
           self.log.append(error)
        else:
            if self.cash < share*1:
                cant_buy = "Not enough money to buy Mutualfunds."
                print cant_buy
                self.log.append(cant_buy)
            else:
                if  mutualfund.symbol in self.mutualfunds.keys(): 
                    self.mutualfunds[mutualfund.symbol] += share
                    self.cash -= share*1
                    buy_mf = "I bought %d share of %s mutualfunds." %( share, mutualfund.symbol)
                    print buy_mf
                    self.log.append(buy_mf)
                else: 
                    self.mutualfunds[mutualfund.symbol] = share
                    self.cash -=share*1
                    buy_mf = "I bought %d share(s) of %s mutualfunds." %( share, mutualfund.symbol)
                    print buy_mf
                    self.log.append(buy_mf)

    def sellMutualFund(self, share, mutualfund):
        if type(share) == float:
           error = "Error: Share is not whole number"
           print error
           self.log.append(error)
        else:
            if mutualfund.symbol in self.mutualfunds.keys():
                if self.mutualfunds[mutualfund.symbol] < share:
                    cant_sell_mf = "Not enough mutualfunds to sell."
                    print cant_sell_mf
                    self.log.append(cant_sell_mf)
                else:
                    self.mutualfunds[mutualfund.symbol] -= share
                    import random
                    self.cash -= random.uniform(0.9, 1.2) * share
                    sell_mf = "I sold %d share(s) of %s mutualfunds." %( share, mutualfund.symbol)
                    print sell_mf
                    self.log.append(sell_mf)
            else:
                cant_sell_mf2 = "You don't have the mutualfunds for the company."
                print cant_sell_mf2
                self.log.append(cant_sell_mf2)

    def history(self):
        print "Transaction history in order:"
        print  '\n'.join(self.log)

####################################
### Examples #######################
s=Stock(10,"CIA") #make stock and set price
print s

s2=Stock(10,"MI6") #make stock and set price
print s2

m=MutualFund("KGB") #make mutualfund
print m

m2=MutualFund("BRT")
print m2

portfolio=Portfolio() #make portfolio
portfolio.addCash(500) 
portfolio.addCash(10.50)
portfolio.withdrawCash(2000) #I cannot withdraw that much
portfolio.withdrawCash(10)

portfolio.buyStock(2.3,s) #cannot buy not whole number share
portfolio.sellStock(2.9,s) #cannot buy not whole number share
portfolio.buyStock(4,s)
portfolio.sellStock(1,s)
portfolio.sellStock(100,s) #not enough stock to sell
portfolio.sellStock(100,s2) #don't have this stock

print(portfolio) #current status of portfolio

portfolio.buyMutualFund(1,m)
portfolio.buyMutualFund(1.1,m) #not work for float number of share
portfolio.sellMutualFund(1,m)
portfolio.sellMutualFund(100,m)

portfolio.buyMutualFund(1,m2) 
portfolio.sellMutualFund(100,m2)
print(portfolio) # show status

portfolio.history() #transaction history log