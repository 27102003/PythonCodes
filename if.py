state=input("Enter either add or subtract: ")
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if state.lower() == 'add':
        print("Addition is: "+str(a+b))
elif state.lower() == 'sub':
        print("Subtraction is: "+str(a-b))
else:
     print("Invalid choice")
    
