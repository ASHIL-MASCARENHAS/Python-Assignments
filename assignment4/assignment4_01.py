def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            i=1
            for line in file:
                print(f"Line {i}: {line.strip()}")
                i+=1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

read_file("sample.txt")