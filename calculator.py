first_number=input("Enter first number : ")
operator=input("+,-,*,/,%")
second_number=input("Enter second numeber : ")
first_number=int(first_number)
second_number=int(second_number)
if operator=='+':
    print(first_number + second_number)
elif operator=='-':
    print(first_number - second_number)
elif operator=='*':
    print(first_number * second_number)
elif operator=='/':
    print(first_number / second_number)
elif operator=='%':
    print(first_numeber % second_number)
else :
    print("Invalid")                   