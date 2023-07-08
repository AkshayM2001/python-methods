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


# TO GET *USED QUANTITY* WE NEED TO ADD *PER WEEK TARGET* OF MACHINES AND *ACTUAL* MACHINES. 


