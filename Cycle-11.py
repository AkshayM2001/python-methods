class quantity():
    
    def __init__ (self, ordered_quantity, mc_no, lsq):
        self.__order = ordered_quantity 
        self.used = mc_no
        self.lsq =lsq
        self.lsq = self.__order - self.used

    def plus(self, live_stock):
        self.ls = live_stock
        self.__order += self.ls

    def minus(self, live_stock):
        self.ls = live_stock
        self.__order += self.ls

    def get_stock_quantity(self):

        print("Ordered_quantity :",  self.__order, "\nUsed_quantity :",  self.used, "\nStocks :", self.lsq)



ab = quantity(0, 0, 0)
ab.plus(900)
ab.used = int(input("Machine number : "))
ab.get_stock_quantity()
