my_tuple = ('hello', 1, 9, 1.5, "Python PCAP")

# Remove item by converting to list

my_list = list(my_tuple)

my_list.remove("hello")

my_tuple = tuple(my_list)

print("Remove item in tuple by converting to list:", my_tuple)

# Delete my_tuple

del my_tuple

# NameError: name 'my_tuple' is not defined

# print(my_tuple)