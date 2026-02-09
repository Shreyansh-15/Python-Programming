def is_multiple_of_5(num):
    return num % 5 == 0
num = int(input("Enter a number: "))

if is_multiple_of_5(num):
    print("True")
else:
    print("False")