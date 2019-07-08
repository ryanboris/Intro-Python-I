# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
num = input("Enter a number: ")
num = int(num)


def is_even(num):
    return num % 2 == 0


print(is_even(num))
# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def is_input_even(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")


is_input_even(num)
