def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return"Error! Division zero not allowed"
    return a/b

def calculator():
    print("----WELCOME TO CALCULATOR----")
    while True:
        print("Select an operation")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=int(input("Enter your choice(1-5):"))
        if choice==5:
            return "EXIT!..................."
            break
        try:
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))

        except ValueError:
            print("Value Error!Try again.")
            continue
        if choice==1:
            result=addition(num1,num2)
            print(f"Result:{num1}+{num2}={result}")
        elif choice==2:
            result=subtraction(num1,num2)
            print(f"Result:{num1}-{num2}={result}")
        elif choice==3:
            result=multiplication(num1,num2)
            print(f"Result:{num1}*{num2}={result}")
        elif choice==4:
            result=division(num1,num2)
            print(f"Result:{num1}/{num2}={result}")
        else:
            print("Invalid Choice!.Try again.")

if __name__=="__main__":
    calculator()