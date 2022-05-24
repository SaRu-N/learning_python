# Reading  a file
example_file=open("example.txt","r") #opening file in read mode
# checking if file is readable or not
print(example_file.readable())
print(example_file.read())
# prints file line by line
print(example_file.readline())
# print the data inside an array
print(example_file.readlines()[2])
# using for loop to read the file
for lines in example_file.readlines():
     print(lines)
example_file.close()
# writng in a file use w (this will override)
# for append use a
example_file=open("example.txt","a")
example_file.write("\nI am writing this file externally")
example_file.close()
example_file=open("example.txt","r")
for lines in example_file.readlines():
    print(lines)
example_file.close()
example2_file=open("example2.html","w")
example2_file.write("\n<p>This is my first paragraph</p>")
example2_file.close()
