def write_to_file(filename):
    # Initial write
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + "\n")
    print(f"Data successfully written to {filename}.")

    # Append mode
    more_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(more_input + "\n")
    print(f"Data successfully appended.")

    # Display final content
    print(f"\nFinal content of {filename}:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Main execution
if __name__ == "__main__":
    write_to_file("output.txt")