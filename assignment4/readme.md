# Python File Operations Assignment

This repository contains two Python programs that demonstrate file operations and error handling as part of Assignment 4 for Module 5: Files, Exceptions, and Errors in Python.

## Programs

### Task 1: Read a File and Handle Errors

**File:** `assignment4_01.py`

This program:
1. Attempts to open and read a text file named `sample.txt`
2. Prints its content with line numbers if the file exists
3. Gracefully handles file not found errors and other exceptions

**Example Usage:**
```
python assignment4_01.py

# If file exists (sample.txt contains):
# Hello
# World
# Python

Reading file content:
Line 1: Hello
Line 2: World
Line 3: Python

# If file doesn't exist:
Error: The file 'sample.txt' does not exist.

### Task 2: Write and Append Data to a File

**File:** `assignment4_02.py`

This program:
1. Takes user input and writes it to `output.txt` (overwrites existing content)
2. Takes additional user input and appends it to the same file
3. Reads and displays the final content of the file

**Example Usage:**
```
python assignment4_02.py
Enter text to write to the file: Hello World
Enter additional text to append: This is additional text

Final content of output.txt:
Hello World
This is additional text
```

## Requirements

- Python 3.x
- No additional packages required

## How to Run

1. Clone this repository
2. Run each program separately:
   ```
   python assignment4_01.py
   python assignment4_02.py
   ```

## Notes

- For Task 1, you can create a `sample.txt` file to test the successful case
- For Task 2, the program will create `output.txt` if it doesn't exist

## Author
ASHIL MASCARENHAS

## License
This project is open source and available under the [MIT License](LICENSE).
```