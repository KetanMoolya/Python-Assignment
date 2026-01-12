#Calculate Factorial Using a Function 
x=int(input("Enter the Number: "))

def factorial_calc(x):
    if x==1:
        return 1
    else:
        factorial=x*factorial_calc(x-1)
        return factorial

output=factorial_calc(x)
        
print(f"Factorial of {x} is {output}")        
