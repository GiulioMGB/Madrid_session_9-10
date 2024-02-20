file_name = "x_files.txt"
fd = open(file_name, "a") # a is for append, w for write, r for read
fd.write("Hello, World!")
while True:
    line = input("Enter a line (or just press Enter to quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break



fd.close()