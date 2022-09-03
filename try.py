try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    div=a/b
    print("Divison is: "+str(div))
except ZeroDivisionError :
    print("Denominator can't be zero") 
