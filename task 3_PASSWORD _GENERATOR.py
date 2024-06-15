import random
import string

print("Hello!Welcome to the password Generator")

# charcters to use in the password
a=string.ascii_lowercase
b=string.ascii_uppercase

# numbers to use in the password
c=string.digits

# symbols to be use in the password
d=string.punctuation

# combination of above elements to form mix password
combination=a+d+c+b

# desired length of the password
length=int(input("\nEnter the length of the password to be generated "))
if(length<=0):
    print("\nplease do not enter Negative or zero value \nTry again:")


# generating password using random elements
Password=''.join(random.sample(combination,length))

# Display of password
print("The Generated Password is:",Password)