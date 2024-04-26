import random

class Exercise2: 
    
    # the lengt of list
    lst_leng=0
    def __init__(self):
        # repeat until condition is met.
        while not self._getListLength():
            continue
        self.InitClass()
        
    #return true if length of list >=3 and <=10 and set the value to lst_leng
    def _getListLength(self):
        x = input("Enter the length of list :")
        if x.isnumeric() and int(x) >= 3 and int(x) <= 10:
            self.lst_leng = int(x)
            retresult=True
        return retresult

    def InitClass(self):
        #creat a new list
        my_lst = list()
        i=0
        while i < self.lst_leng:
            y = random.randint(0, 10)
            if y in my_lst:
                continue
            my_lst.append(y)
            i +=1
    
        #creat new list from old list
        newlist = list(my_lst)
        newlist.remove(min(my_lst))
        newlist.remove(max(my_lst))
        
        print(f"The old list is {my_lst}")
        print(f"The new list is {newlist}")
        
Exercise2()