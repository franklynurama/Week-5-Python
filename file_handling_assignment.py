# file_handling_assignment.py

# File Creation and Writing
try:
    # Creating a new file and writing to it
    with open('my_file.txt', 'w') as file:
        file.write("Line 1: Hello, this is a sample text file.\n")
        file.write("Line 2: The number 42 is the answer to everything.\n")
        file.write("Line 3: Python is fun!\n")
    print("File 'my_file.txt' created and initial content written.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file creation: {e}")

# File Reading and Display
try:
    # Reading the contents of the file
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt' after initial write:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    # Appending additional lines to the file
    with open('my_file.txt', 'a') as file:
        file.write("Line 4: Appending more text.\n")
        file.write("Line 5: The universe is vast and mysterious.\n")
        file.write("Line 6: Keep coding and learning!\n")
    print("\nAppended more lines to 'my_file.txt'.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")

# Final File Reading to Display Updated Content
try:
    # Reading the updated file content
    with open('my_file.txt', 'r') as file:
        updated_content = file.read()
        print("\nContents of 'my_file.txt' after appending:")
        print(updated_content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

# Ensure that resources are closed properly
finally:
    print("\nFile handling operation completed.")
