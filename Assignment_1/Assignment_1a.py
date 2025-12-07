### Perform Basic Mathematical Operations

first_num = int(input("Enter a first number: "))
second_num = int(input("Enter a second number: "))

print(f"First number: {first_num}")
print(f"Second number: {second_num}")

add = first_num + second_num
sub = first_num - second_num
multi = first_num * second_num

# Error handling for division by zero
if second_num != 0:
    div = first_num / second_num
else:
    div = "undefined (cannot divide by zero)"

print(f"Addition: {add}")
print(f" Subtraction: {sub}")
print(f"Multiplication: {multi}")
print(f"Division: {div}")