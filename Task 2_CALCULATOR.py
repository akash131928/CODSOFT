print("Enter two numbers to be calculated")

# taking the input numbers from user
first_num=float(input("Enter the 1st number "))
second_num=float(input("Enter the 2nd number "))

# taking the input choice from user
choice=int(input("enter the operation to be performed\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus\n\nNote: Enter the choice in the form of (1/2/3/4/5) "))

# arithematic oprations

if(choice==1):
    print("Sum=",first_num+second_num)

elif(choice==2):
    print("Sub=",first_num-second_num)

elif(choice==3):
    print("Mul=",first_num*second_num)

elif(choice==4):
    print("Div=",first_num/second_num)

elif(choice==5):
    print("modulus=",first_num%second_num)

else:
    print("invalid input")



