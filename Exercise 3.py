my_list1=['h', 'e', 'l', 'l', 'o']
my_list2=['h', 'e', 'y']

my_list3=[my_list1, my_list2]
for x in my_list3:
    if len(x) == 5:
        print(f"The string is: {''.join(x)}")
    else:
        print("This list doesn’t have the right size")