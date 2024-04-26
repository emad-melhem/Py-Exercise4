employee_name=input("Enter the emplyee name :")
try:
    sick_list1=input("Enter the number of days missed "
                    +"due to inlliness in each quarter,\n"
                    +"'put a space between them' :").split()
    if len(sick_list1) == 4:
        if int(sick_list1[0]) + int(sick_list1[1]) + int(sick_list1[2]) + int(sick_list1[3]) > 365:
            raise IndexError("This list doesn’t have the right size")
        
        sum_sick_days = 0
        for quart in sick_list1:
            if int(quart) < 0:
                raise IndexError(f"{employee_name} can’t be sick for {quart} days!")
            sum_sick_days += int(quart)
            
        print(f"{employee_name} was sick for {sum_sick_days} days.")
        print(f"He went dancing for {365 - sum_sick_days} days")
            
    else:
        raise IndexError("This list doesn’t have the right size")
    
    
    #creat the sick days for new year 
    
    sick_list2=input("Enter the number of days missed "
                    +"due to inlliness in each quarter in new year,\n"
                    +"'put a space between them' :").split()
    if len(sick_list2) == 4:
        if int(sick_list2[0]) + int(sick_list2[1]) + int(sick_list2[2]) + int(sick_list2[3]) > 365:
            raise IndexError("This list doesn’t have the right size")   
        for quart2 in sick_list2:
            if int(quart2) < 0:
                raise IndexError(f"{employee_name} can’t be sick for {quart2} days!") 
        
        sick_list=sick_list1 + sick_list2   # concated all lists
        sick_list = list(map(int, sick_list))    #change list member from str to int.
        
        max_day=max(sick_list) # get max number from list.
        qn_list = [] # list for index of max number.
        counter=1
        for dq in sick_list:
            if dq == max_day:
                qn_list.append(counter)  # append index of max number to new list.
            counter += 1
                
        print(f"The full list of {employee_name} sick days is: {sick_list}")
        first_str = ""
        second_str= ""
        for index1 in qn_list:
            if index1 < 4:
                if first_str != "":
                    first_str +=", "
                first_str += str(index1)
        if first_str != "":
            first_str += " of the first year."
            
        for index1 in qn_list:
            if index1 > 3:
                if second_str != "":
                    second_str +=", "
                second_str += str(index1)
        if second_str != "":
            second_str += " of the second year."
            
        print(f"{employee_name} was sick the most in quarter {first_str} {second_str}")
        # the end of new year codes.
        
    else:
        raise IndexError("This list doesn’t have the right size")
    
    
except IndexError as error:
    print(error.args[0])
except ValueError:
    print("That is not number !")
    
