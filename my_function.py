# def my_function():
#   print('Hello');
#   print("Hi");
#   print("Wassup")

# my_function();

# def sum():
#  num1 = int(input("enter num1: "));
#  num2 = int(input("enter num2: "))
#  return num1 + num2;


# print(sum())

# def sub(num1, num2):
#  result = num1 - num2;
 
 
#  num1 = int(input("enter num1: "));
#  num2 = int(input("enter num2: "));
#  result = sub(num1, num2)
#  print(result)
#  sub(num1, num2)


# def even_odd(num):
#   if num % 2 == 0:
#    return "even number";
#   else:
#    return "odd number";


# print(even_odd(10))

def even_odd(num):
    return num % 2 == 0

num = 1

while num <= 50:
    if even_odd(num):
        print(num)
    num = num + 1;

