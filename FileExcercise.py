# Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned
# about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt
# in the same directory as your exercises from this chapter. Write a program that reads the file and
# prints what you wrote three times. Print the contents once by reading in the entire file,
# once by looping over the file object, and once by storing the lines in a list and then working
# with them outside the with block.

file = 'text_files/learning_python.txt'

print("--- Reading in the entire file:")
with open(file) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(file) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(file) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
print()
# Read in each line from the file you just created, learning_python.txt, and replace the word Python
# with the name of another language, such as C. Print each modified line to the screen.

file = 'text_files/learning_python.txt'

with open(file) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))

# Guest: Write a program that prompts the user for their name. When they respond,
# write their name to a file called guest.txt.

file = 'text_files/guest.txt'

with open(file, 'w') as guest:
    prompt = input("Enter your name: ")
    print(guest.write(prompt))

# Guest Book: Write a while loop that prompts users for their name. When they enter their name,
# print a greeting to the screen and add a line recording their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

file = 'text_files/guest.txt'

print("enter 'q' when finished")
while True:
    prompts = input("\nEnter your name: ")
    if prompts == 'q':
        break
    else:
        with open(file, 'a') as book:
            book.write(f"\n{prompts}\n")
            print(f"welcome {prompts}")

# Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason,
# add their reason to a file that stores all the responses.

file = 'text_files/guest.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(file, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")