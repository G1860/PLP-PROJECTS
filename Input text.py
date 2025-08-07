# Step 1: Create input.txt and write 5 lines of text into it
with open('input.txt', 'w') as input_file:
    input_file.write("Python is a powerful programming language.\n")
    input_file.write("It is widely used in web development.\n")
    input_file.write("Data science relies heavily on Python.\n")
    input_file.write("It is also popular in automation.\n")
    input_file.write("Learning Python opens many doors.\n")

# Step 2: Read from input.txt
with open('input.txt', 'r') as file:
    content = file.read()

# Step 3: Count the number of words
word_count = len(content.split())

# Step 4: Convert content to uppercase
uppercase_content = content.upper()

# Step 5: Write to output.txt
with open('output.txt', 'w') as output_file:
    output_file.write("=== UPPERCASE CONTENT ===\n")
    output_file.write(uppercase_content + "\n")
    output_file.write(f"Total word count: {word_count}\n")

# Step 6: Print success message
print("✅ The output.txt file was created successfully with processed content!")
