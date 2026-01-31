text=input("Enter text to write to the file:")
with open("output.txt","w") as fh:
    fh.write(text)
print("Data successfully written to output.txt.")


additional_text=input("Enter additional text to append:")
with open("output.txt","a") as fh:
    fh.write("\n"+additional_text)
print("Data successfully appended.")

print("Final content of output.txt:")
with open("output.txt","r") as fh:
    for line in fh:
        print(line.strip())
