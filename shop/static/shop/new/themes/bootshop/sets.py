# # import math
# # def greet(n):
# #     '''This function prints out a greeting'''
    
# #     print(f"Good morning {n}")


# # greet("mercy")



# def salary(rate, hours):
#     ans = rate * hours
#     return f"Your salary is {ans}"

# print(salary(rate=5, hours=8))
# numbers  = [2, 4, 6, 8]
# sq = []

# def squares(num):
#     return num * num

# for num in numbers:
#     a = squares(num)
#     sq.append(a)


# print(sq)



# def maximum(num1, num2, num3):
#     return max(num1, num2, num3)


# print(maximum(2,311,40, 67))

# def country(country="Nigeria"):
#     return f"You are from {country}"

# print(country())

# def greet(*names):
#     return f"Good day {names[0]}"

# print(greet("Prosper", "Edward", "Emmanuel", "Lizzy"))



# numbers = input("Enter numbers separated by spaces")
# numbers_list = numbers.split()
# print(numbers_list)


# my_numbers = [2, 6, 15, 14, 12, 13, 84, 17]
# ans = []

# def even():
#     for num in my_numbers:
#         if num % 2 == 0:
#             ans.append(num)
#     return ans

# print(even())

# num1 = int(input("Enter the first number: "))
# num2= int(input("Enter the second number: "))
# operator = input("Enter an operator: ")


# def calculator(num1, num2, operator):
#     if operator == "+":
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return("Invalid operator")
    

# print(calculator(num1, num2, operator))


def checker(name):
    small_letters = 0
    capital_letters = 0
    for letter in name:
        if letter.islower():
            small_letters += 1
        else:
            capital_letters += 1
    return [small_letters, capital_letters]
    

print(checker("Prosper"))






