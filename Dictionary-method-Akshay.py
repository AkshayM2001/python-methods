# From :- Akshay J. Matale.
# Batch :- Python 5:30 PM to 6:30 PM
# Date :- 03/07/2023


# Global Variables

list1 = { "name":"Akshay", "age":22, "address":"Uruli"}
list2 = {"name": "Samir", "age":29, "address":"Pune"}
ada = {}
# Get Method
        # This method provide keys value.

try:
    def check_value(dict_name, value):
        try:
            print(value, "is", dict_name.get(value) )

        except Exception as e:
            print(e)
except Exception as e:
            print(e)



# It take 2 arguments 1st is dictionary name and 2nd key not values
           
# check_value(list2, "address")



# Keys Method
            # This method prints all keys not values

try:
    def check_keys(dict_name):
        try:
            print(dict_name.keys())
        except Exception as e:
            print(e)
except Exception as e:
            print(e)


# This take 1 aregument that is dictionary name

# check_keys(list1)



# Values Method
            # This method prints all values

try:
    def check_all_values(c):
        try:
            print(c.values())
        except Exception as e:
            print(e)
except Exception as e:
            print(e)

# This take 1 aregument that is dictionary name
           
# check_all_values(list1)



# Items Method
            # This method give all data from dictionary in tuple() format.

try:
    def check_all(dict_name):
        try:
            print(dict_name.items())
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
# This take 1 aregument that is dictionary name

# check_all(list1)



# Update Method
        # This method will update keys values form 1 list to another list.

try:
    def add_new(f, ac):
        try:
            print("Given dictionary is: ", f)
            f.update(ac)
            print("updated dictionary is :", f)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# It take 2 arguments both dictionary name 1st will be selected and 2nd dictionary's values will be added in 1st dictionary.

# add_new(list1, list2)


# POP Method
            # This method removes any key with it's value.

try:
    def kick(dict_name ,key_name):
        try:
           ae = dict_name.pop(key_name)
           print(key_name, "&", ae, "removed.")
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# It take 2 areguments 1st dictionary name & 2nd key which user wants to remove.

# kick(list2, "name")



# Popitem Method
            # This method removes last key with it's value and it prints key and value in tuple().

try:
    def kick_show(dict_name):
        try:
           af = dict_name.popitem()
           print("Last key and value of dictionary is :", af)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# This take 1 aregument that is dictionary name


# kick_show(list2)



# Clear Method
            # This method removes all keys and values in dictionary and shows none.

try:
    def del_all(dict_name):
        try:
            print("Given dictionary is :", dict_name)
            af = dict_name.clear()
            print("dictionary Deleted :", af)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# This take 1 aregument that is dictionary name

# del_all(list2)



# Setdefault Method
            # This method will give output which developer wanted to show.
            # when user wants click on big data but it will give only one output.

try:
    def dev_show(dict_name, key):
        try:
            ag = dict_name.setdefault(key)
            print(ag) 
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# It take 2 areguments 1st dictionary name & 2nd key which user wants to watch.

# dev_show(list1, "name")



# Copy Method 
            # it will copy dictionary simple. it will remove all old dictionary data.

try:
    def xerox(dict_name1, dict_name2):
        try:
            print("Given dictionary : ", dict_name1)
            dict_name2 = dict_name1.copy()
            print("Copied dictionary :", dict_name2)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# It take 2 areguments both dictionary name, 1st dictionary will be copied & in 2nd dictionary will be pasted.

# xerox(list1, list2)
             