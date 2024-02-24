# Get the size of the array from the user
array_size = int(input("Enter the size of the array: "))

# Initialize an empty array
user_array = []

# Loop to get input from the user and store it in the array
for i in range(array_size):
    element = int(input("Enter element {} of the array: ".format(i+1)))
    user_array.append(element)

# Print the array
print("Array entered by the user:", user_array)

# Sort the array
user_array.sort()

result = set()

for i in range(len(user_array)-2):
    left = i + 1
    right = len(user_array) - 1
    while left < right:
        current_sum = user_array[i] + user_array[left] + user_array[right]
        if current_sum == 0:
            result.add((user_array[i], user_array[left], user_array[right]))
            left += 1
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1

print("Result:", result)
