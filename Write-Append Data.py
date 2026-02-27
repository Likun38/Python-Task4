filename = "output.txt"

# Taking input from user
text1 = input("Enter text to write to the file: ")

# Writing to file (this will overwrite if file already exists)
file = open(filename, "w")
file.write(text1 + "\n")
file.close()

print("Data successfully written to output.txt.\n")

# Taking additional input
text2 = input("Enter additional text to append: ")

# Appending to same file
file = open(filename, "a")
file.write(text2 + "\n")
file.close()

print("Data successfully appended.\n")

# Reading and displaying final content
print("Final content of output.txt:\n")

file = open(filename, "r")
content = file.read()
print(content)
file.close()