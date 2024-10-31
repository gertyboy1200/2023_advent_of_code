with open('day_1_input.txt', 'r') as file:
    lines = file.readlines()  # Reads all lines into a list

output = []
for line in lines:

# Extract the first and last digit only
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:  # Store the first digit
                first_digit = int(char)
            last_digit = int(char)  # Continuously update the last digit
    output.append(((first_digit * 10) + last_digit))

print(sum(output))
