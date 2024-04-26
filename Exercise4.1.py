employee_name=input("Enter the emplyee name :")

sick_list1=input("Enter the number of days missed "
                +"due to inlliness in each quarter,\n"
                +"'put a space between them' :").split()
try:
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
    
except IndexError as error:
    print(error.args[0])
except ValueError:
    print("That is not number !")