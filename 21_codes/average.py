high_score=95

test1=int(input("enter the score for test1 : "))
test2=int(input("enter the score for test2 : "))
test3=int(input("enter the score for test3 : "))

average= (test1+test2+test3)/3
print("the average score is",average)

if average>=high_score:
    print("congratulations!")
    print("that is a great average!")
