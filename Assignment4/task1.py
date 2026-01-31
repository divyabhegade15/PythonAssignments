#writing into the file
with open("sample.txt", "w") as fh:
    fh.write("This is a sample text file.\n")
    fh.write("It contains multiple lines.")

#reading the file
try:
    with open("sample.txt", "r") as fh:
        print("Reading file content:")

        line_no = 1
        for line in fh:
            print("Line", line_no, ":", line.strip())
            line_no += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
