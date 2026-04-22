def is_even(num):
    # if num % 2 ==0:
    #     return True
    # else:
    #     return False
            #OR
    return num % 2 == 0 #Because num % 2 == 0 already gives True/False.

num = int(input("Enter a number: "))
if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")