# From :- Akshay J. Matale.
# Batch :- Python 5:30 PM to 6:30 PM
# Date :- 02/07/2023


# GLOBAL VARIABLES/ITEMS

list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 24, 46, 67, 687, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 24, 46, 67, 687, 4, 5, 8]
list1 = ["ram", "ddr4", "cl", "22ms", "cap", "8gb"]
list2 = [["gtx", "1650ti"], ["ryzen", "5500h", "3.2ghz"], ["ssd", "256gb", "1tb"]]
new = [1, 2, 3, 4, 5, 6, 7, 8]
shuffled = [5, 6, 7, 1, 2, 11, 18, 16, 19]

# LIST METHODS


# Append Method

try:
    def add_this(*a):
        try:
            print("Given-list: ", list1)
            list1.append(*a)
            print("Updated-list: ", list1)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Clear Method

try:
    def delete_all(*b):
        try:
            print("Given-list: ", b)
            b.clear()
            print("List Deleted!!!!")
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Copy Method

try:
    def copy_all(c):
        try:
            print("Given-list: ", c)
            c.copy()
            new = tuple(c)
            print("List Copied :", new)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Count Method


try:
    def count_all(d):
        try:
            print("Given-list: ", list_num)
            ab = (list_num.count(d))
            print("Total count is : ", ab)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Extend Method


try:
    def extend_all(*f):
        try:
            print("Given-list: ", new)
            new.extend(*f)
            print("Extend list : ", new)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Index Method


try:
    def index_of(g):
        try:
            print("Given-list: ", new)
            print("Index number is : ", new.index(g))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Insert method


try:
    def insert_this(*h):
        try:
            print("Given-list: ", new)
            new.insert(*h)
            print("Inserted list is : ", new)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# POP Method


try:
    def remove_last(i):
        try:
            print("Given-list: ", i)
            i.pop()
            print("Extend list : ", i)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Remove Method


try:
    def remove_match(j):
        try:
            print("Given-list: ", new)
            new.remove(j)
            print("Removed first matching number : ", j)
            print("Updated  list : ", new)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)


# Reverse  Method


try:
    def reverse_all(k):
        try:
            print("Given-list: ", k)
            k.reverse()
            print("Reversed  list : ", k)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# Sort Method

try:
    def rearrenge_it(l):
        try:
            print("Given-list: ", l)
            l.sort()
            print("Reversed  list : ", l)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)



# Give input

#1] add_this("32gb", "ddr5")
#2] delete_all(list1)
#3] copy_all(list_num)
#4] count_all(5)
#5] extend_all([11, 132, 74])
#6] index_of(4)
#7] insert_this(6, 1111)
#8] remove_last(list1)
#9] remove_match(5)
#10] reverse_all(list1)
#11] rearrenge_it(shuffled)