def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i,line in enumerate(file,1):
                print(f"Line {i}: {line.strip()}")
                i+=1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    read_file("sample.txt")
    read_file("saample.txt")