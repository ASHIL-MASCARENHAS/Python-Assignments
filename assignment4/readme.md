```markdown
# Python File Handling Assignment

## Assignment 4 Solutions for Module 5

This repository contains two Python programs demonstrating file operations and error handling techniques.

### Program 1: File Reader with Error Handling
**Filename:** `assignment4_01.py`

This program safely reads and displays the contents of 'sample.txt' with:
- Line-by-line display with numbered output
- Automatic file closing using context manager
- Special handling for missing files
- Clean error messages

**How to Use:**
1. Create a 'sample.txt' file to test successful reading
2. Run the program to see either the file contents or a "file not found" message
3. No file modification occurs - read-only operation

### Program 2: File Writer with Append Functionality
**Filename:** `assignment4_02.py`

This interactive program handles file operations by:
1. Taking user input for initial file content
2. Writing content to 'output.txt' (creates new or overwrites existing)
3. Taking additional input to append to the file
4. Showing the final combined content

**Features:**
- Clear success messages after each operation
- Preserves existing content during append
- Demonstrates all three file modes: write, append, and read
- User-friendly output formatting

**Usage Notes:**
- Running multiple times will overwrite the initial content
- Appended text adds to existing content
- The program creates 'output.txt' if missing

**Testing Recommendations:**
1. Test with missing input file for Task 1
2. Verify append functionality by running Task 2 multiple times
3. Check special characters in input text
4. Verify empty input handling

Both programs follow Python best practices for file handling and include appropriate user feedback.
```