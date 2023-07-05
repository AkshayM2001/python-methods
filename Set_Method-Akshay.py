# From :- Akshay J. Matale.
# Batch :- Python 5:30 PM to 6:30 PM
# Date :- 05/07/2023


# GLOBAL VARIABLES/ITEMS

fruits = {"apple", "banana", "cherry"}
lang = {"html", "css"}

# Set of fruits

# Add Method
        # This method will add anything is not set

def add_thoss_(set_name, *value):
    try:
        print("Old list : ", set_name)
        print("Added to list", set_name.add(value))
    except Exception as e:
        print(e)

add_thoss_(fruits, lang)

