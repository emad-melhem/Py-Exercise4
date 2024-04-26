letter= input("Enter your Text :")
my_list=list(letter)

x=""
if len(my_list) > 0:
    x= " not"
print(f"This list is{x} empty!")
print(my_list)