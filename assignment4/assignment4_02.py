def write_to_file(filename):
    str = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(str + "\n")
    print(f"Data successfully written to {filename}.\n")

    str2 = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(str2 + "\n")
    print(f"Data successfully appended.")

    print(f"\nFinal content of {filename}:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

write_to_file("output.txt")