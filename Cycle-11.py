# THIS PROJECT WILL FOR MATERIAL HANDLING AND RESOURCE MANAGEMENT FOR EARLY NOTIFICATIONS OF MATERIAL SHORATGE.
# IT WILL UPDATE BOTH SUPERVISER AND MATERIAL FEEDER TO FEED THOSE LOCATION

class quantity:
    def __init__ (self, ordered_quantity, mc_no, lsq):
        self.__order = ordered_quantity 
        self.used = mc_no
        self.lsq =lsq
        # self.mmq = mmq
    def plus(self, live_stock):
        self.ls = live_stock
        self.__order += self.ls
    def get_stock_quantity(self):
        print("Ordered_quantity :",  self.__order, "\nUsed_quantity :",  self.used *2, "\nStocks :", self.__order - (self.used *2))
        # print("\nMissmatched quantity :",(self.__order - (self.used *2) - ) )

        dz = self.__order - (self.used *2)

        # print(dz)
        
        if dz < 6:
            print("Need to order next batch")
        else:
            print("Still", dz, "quantites left")


ab = quantity(0, 0, 0)
# ab.plus(int(input("Enter recieved quantity : ")))
ab.plus(900)
ab.get_stock_quantity()

   