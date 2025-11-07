name = "aman";
i = 0;
for element in name:
    print(i, ". ",element);
    i = i+1;
print("Length of the string is: ", len(name));
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
else:
    print("No, 'free' is not present.")

print('aman' not in txt);


# String Slicing
b = "Hello, World!"
print(b[2:5])  # prints characters from index 2 to 4
print(b[:5])  # prints characters from the beginning to index 4

print(b[2:])  # prints characters from index 2 to the end

print(b[-5:-2])  # prints characters from index -5 to -3


# modifying strings
a = "  Hello, World! "   
print(a.upper());
print(a.strip().upper().lower())
print(a.replace("H", "J"))

print(a.split(","))  # returns ['  Hello', ' horld! ']

# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt) gives error because age is integer and we are trying to concatenate string with integer.

age = 36
txt = f"My name is John, I am {age}"
print(txt);

import math_utils;
print("Sum  from math_utils module:", math_utils.add(12,3));