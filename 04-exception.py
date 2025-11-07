x = input("Enter number1: ");
y = input("Enter number2: ");
try:
    z = int(x) / int(y);
    print("Result: ", z);
except ZeroDivisionError as e:
    print("Division by zero error ");
except TypeError as e:
    print("Type mismatch error");

print("Aman")