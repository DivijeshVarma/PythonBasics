# The input() function pauses your program and waits for the user to enter some text.
# Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

message = input("enter some text: ")
print(message)

name = input("Enter your name: ")
print(f"Hello {name}")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello {name}")


# Even numbers are always divisible by two, so if the modulo of a number and two is zero
# (here, if number % 2 == 0) the number is even. Otherwise, it’s odd.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is odd")
