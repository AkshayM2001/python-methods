# From :- Akshay J. Matale.
# Batch :- Python 5:30 PM to 6:30 PM
# Date :- 05/07/2023


# GLOBAL VARIABLES/ITEMS

fruits = {"apple", "banana", "cherry"}
lang = {"html", "css", "banana"}

# Set of fruits

# Add Method
        # This method will add anything in set, but only one item at a time. 
        # not full list or set

def add_thoss_(set_name, value):
    try:
        print("Old list : ", set_name)
        set_name.add(value)
        print("Added to list", set_name)
    except Exception as e:
        print(e)

# It takes 2 areguments 1st for list/set name 2nd is item  or value in string format.

# add_thoss_(fruits, "lang")



# Remove Method

         # This method will remove anything in set, but only one item at a time. 
        # not full list or set

def kick_that(set_name, value):
    try:
        print("Given list :", set_name)
        set_name.remove(value)
        print("Updated list :", set_name)
    except Exception as e:
        print(e)

# It takes 2 areguments 1st for list/set name 2nd is item  or value in string format.

# kick_that(fruits, "apple")


# Union Method
        # The union() function returns the combined sets (i.e., all elements from both sets)

def all_in(set_name, set_name2):
    try:
        print("Given 1st list : ", set_name)
        print("Given 2st list : ", set_name2)
        ab = set_name.union(set_name2)
        print("Updated list :", ab)
    except Exception as e:
        print(e)

# It takes 2 areguments both are seperate sets.

# all_in(lang, fruits)


# Intersection Method
        # This method finds common in both set

def common_(set_name, set_name1):
    try:
        print("First set", set_name, "\nSecond set", set_name1)
        ac = set_name.intersection(set_name1)
        print("Common item is :", ac)
    except exception as e:
        print(e)

# It takes 2 areguments both are seperate sets.

# common_(lang, fruits)