file_name = "x_files.txt"
fd = open(file_name) # r is implicit
print("here are the contents of the file: ")
print(fd.read())

for line in fd:
    print(line, end="")

fd.close()

with open(file_name) as fd:
    print("Here are the 3 letter words! ")
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3:
                print(word)

fd.close() 