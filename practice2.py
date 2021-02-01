# # [3, 5, 6, 7, 8]
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [2, 4, 1]
# res = list(set(a) ^ set(b))
# print(res)
#
# # Original list [1, 1, 1, 1, 4, 4, 4, 4]
# # New list [1, 4]
# nums = [1, 1, 1, 1, 4, 4, 4, 4]
# print(f'Original list {nums}')
#
# new = []
#
# # for list in nums:
# #     if list not in new:
# #         new.append(list)
# #     else:
# #         pass
#
# [new.append(list) for list in nums if list not in new]
# print(f"New list {new}")
#
#
# places = {}
#
# vacation = True
#
# while vacation:
#     poll0 = input("Enter your name: ")
#     poll = input("If you could visit one place in the world, where would you go? ")
#     poll2 = input("is any one want to take poll yes/no: ")
#
#     places[poll0] = poll
#
#     if poll2 == 'no':
#         vacation = False
#
# print("\n--Poll results--")
# for key, value in places.items():
#     print(f"{key.title()} would visit {value.title()}")

# import random
#
#
# def pick_num():
#     low = int(input("Enter low num: "))
#     high = int(input("Enter high num: "))
#     rand_num = random.randint(low, high)
#     return rand_num
#
#
# def first_guess():
#     guess = int(input("Guess the number: "))
#     return guess
#
#
# def check_answer(rand_num, guess):
#     while True:
#         if rand_num == guess:
#             print(f"Correct!{rand_num}")
#             break
#         elif rand_num > guess:
#             guess = int(input("Too low, guess again: "))
#         else:
#             guess = int(input("Too high, guess again: "))
#
#
# def main():
#     rand_num = pick_num()  # why do I assign the returned variable back to the function?
#     guess = first_guess()  # why do I assign the returned variable back to the function?
#     check_answer(rand_num, guess)
#
#
# main()

def print_shape():
    for i in range(3):
        print('***')


print_shape()
