
num1 = int(input("enter the first number: "));
op = input("Enter the operation you want to perform: (+,-,/,*): ");
num2 = int(input("enter the second number: "))


match op:
    case "+":
        result = num1+num2
        print(f"num1 + num2 = {result}")
    case "-":
        result = num1 - num2
        print(f"num1 - num2 = {result}")

    case "*":
        result = num1 * num2
        print(f"num1 * num2 = {result}")

    case "/":
        if(num2 == 0):
            print("zeroDivisionError")
        else:
            result = num1 / num2
            print(f"num1 / num2 = {result}")

