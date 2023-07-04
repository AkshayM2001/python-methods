# From :- Akshay J. Matale.
# Batch :- Python 5:30 PM to 6:30 PM
# Date :- 03/07/2023


# GLOBAL VARIABLES/ITEMS
list0 = "HP laptops are best with Ryzen cpu"
list1 = " ram", "-ddr4", " cl", "-22ms", " cap", "-8gb"
list2 = "1, 1, 2, 3, 4, 5, 6, 7, 4, 3, 6, 7"
new = "1, 2, 3, 4, 5, 6, 7, 8"
space = "              hello world    "
cap_list = "RAM, DDR4, CL, 22MS, CAP, 8GB"


# STRING METHODS

# Upper Method

try:
    def capital(a):
        try:
            print("Given List : ", a)
            b = ", ".join(a)

            print("Capitalised list : ", b.upper())
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Lower Method

try:
    def small_letter(b):
        try:
            print("Given List : ", b)
            z = "".join(b)

            print("Small Letters list : ", z.lower())
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

 # Strip Method

try:
    def del_space_(c):
        try:
            print("Given List : ", c)
            z = "".join(c)
            print("Removed spaces  : ", z.strip())
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Split Method

try:
    def seperate_with(d):
        try:
            print("Given List : ", d)
            z = "".join(d)
            print("splitted list : ", z.split(" "))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)



# Join Method

try:
    def combine_all(f):
        try:
            print("Given List : ", f)
            z = "".join(f)
            print("joined list : ", z)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Replace Method

try:
    def change_item(*g):
        try:
            print("Given List : ", list0)
            z = "".join(list0)
            print("Changed list : ", z.replace(*g))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Startwith Method

try:
    def first_word(h):
        try:
            print("Given List : ", list0)
            z = "".join(list0)
            print("Your Guess : ", z.startswith(h))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Endswith Method

try:
    def last_word(i):
        try:
            print("Given List : ", list0)
            z = "".join(list0)
            print("Your Guess : ", z.endswith(i))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Find Method

try:
    def index_num(*j):
        try:
            print("Given List : ", list0)
            z = "".join(list0)
            print("Changed list : ", z.find(*j))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Count Method

try:
    def count_all(k):
        try:
            print("Given-list: ", list2)
            ab = (list2.count(k))
            print("Total count is : ", ab)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)






# Input
# capital(list1)
# small_letter(cap_list)
# del_space_(space)
# seperate_with(list0)
# combine_all(list1)
# change_item("Ryzen", "Intel")
# first_word("HP")
# last_word("cpu")
# index_num("best")
# count_all("1")