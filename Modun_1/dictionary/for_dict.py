import numbers

my_dict = {
    "name" : "Thach Minh Quan",
    "age"  : 20,
    "class" : "cs1",
    "class_2" : "it1",
    "toan": 10,
    "van":10,
    "ly":4.5,
    "anh":3.5

}
for i in my_dict:
    if my_dict[i]==10:
        print("key:", i, "-", "value:", my_dict[i])

print("----------------------------------")
for i in my_dict:
    if type(my_dict[i]) != str:
        if my_dict[i] < 5:
            print("key:", i, "-", "value:", my_dict[i])
        else:
            print(" no value err")