# THIS PROJECT WILL FOR MATERIAL HANDLING AND RESOURCE MANAGEMENT FOR EARLY NOTIFICATIONS OF MATERIAL SHORATGE.
# IT WILL UPDATE BOTH SUPERVISER AND MATERIAL FEEDER TO FEED THOSE LOCATION


# TO GET STOCK QUANTITY FIRST WE NEED PART NUMBER AND ORDERD QUANTITY -- USED QUANTITY == LIVE QUANTITY

def get_stock_quantity(ordered_quantity, used_quantity):
    try: 
        live_quantity = ordered_quantity - used_quantity
        print("Ordered_quantity :", ordered_quantity, "\nUsed_quantity :", used_quantity, "\nStocks :", live_quantity)
    except Exception as e:
        print(e)


# HERE 1st AREGUEMENT **ORDERED QUANTITY** AND 2nd **USED QUANTITY**

# get_stock_quantity(350, 150)


# TO GET *USED QUANTITY* WE NEED TO ADD *TARGET* OF MACHINES AND *ACTUAL* MACHINES. 

def used_quantity(actual):
    try:
        total = target - actual
        print("Yearly machines target :", target, "\nToday confirmed machine :",actual, "\nRemaining machines : ", total)

        #### GETTING WEEK NUMBER ASSUMING PER WEEK 5 MACHINES TARGET
        ## 40/5 = 8,  41/5 = 8.2, 42/5 = 8.4 then 8 is week that obtained by ROUND function
        tar = int(actual)
        week = round(tar / 5)

        ### NOW MACHINE NUMBER IN WEEK BETWEEN 1 TO 5
        ## for that 8.2-8 = 0.2 using if else assigining 0.2 = 1, 0.4 = 2 and rest
        
        per_week = tar / 5
        per_week = per_week - week

        if per_week == 0.2:
            first = "1"
            print(first)
        elif per_week == 0.4:
            second = "2"
            print(second)
        elif per_week == 0.6:
            third = "3"
            print(third)
        elif per_week == 0.8:
            forth = "4"
            print(forth)
        elif per_week == 0:
            fifth = "5"
            print(fifth)
        else:
            print("Restart")
            

        #### NOW ADDIND WEEK NUMER + MACHINE NO
        print(week, "week and ", )
        
        # if used == 0:
        #     pass
        # elif used > 0 :
        #     print("WE have backlog of :", used)
        # else:
        #     print(" Please check your detalis")
    except Exception as e:
        print(e)


target = 215 # int(input("Week Target : "))

used_quantity(int(input("Enter Machine no :")))

# 43 weeks and 215 mc
# 40 no mc
# 40/5 = 8
# 41/5 = 8.2

