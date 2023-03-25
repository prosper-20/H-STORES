# input_string = input('Enter elements of a list separated by space ')

# user_list = input_string.split("a")
# print(type(user_list))

# print(user_list)

# for i in range(0, 5):
#     print("prosper")


# def counter(string_s):
#     new =  [letter for letter in string_s if letter not in ("a", "e", "i", "o", "u")]
#     return len(new)
    # cons = 0
    # for letter in string_s:
    #     if letter not in ["a", "e", "i", "o", "u"]:
    #         cons += 1

    # return cons





# number_list = []
# n = int(input("Enter the list size "))


# for i in range(0, n):
#     item = int(input("Enter a number:"))
#     number_list.append(item)

# print("User list is ", number_list)


# n = int(input("Enter the size of the list "))
# num_list = [int(num) for num in input("Enter the list items separated by space ").strip().split()]

# print("User list: ", num_list)

# a = []
# b = list()

# print(type(b))

# numList = list(map(int, input("Enter the list numbers separated by space ").strip().split()))
# print("User List: ", numList)


# def checker(word):
#     new = word.split("-")
#     new.sort()
#     return "-".join(new)


# print(checker("green-yellow-red-black"))


def prime_checker(num):
    if num == 1:
        return True
    elif num == 2:
        return False
    else:
        for i in range(2, num):
            if(num % i ==0):
                return False
        return True   
    
print(prime_checker(4))
    


# def calculation(num1, num2):
#     addition = num1 + num2
#     subtraction = num1 - num2
#     return(addition, subtraction)

# print(calculation(50, 10))






