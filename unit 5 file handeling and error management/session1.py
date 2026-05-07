# greetings = open("hello.txt","r")
# print(greetings)
# greetings.close




# f = open("hello.txt","r")
# print("Filename:",f.name)
# print("File mode:",f.mode)
# print("Is file closed:",f.close)
# f.close()
# print("Is File closed?:",f.close)

# f = open("hello.txt","r")
# content = f.read()
# print(content)
# f.close

newFile = open("newFile.txt","w")
print(newFile)
newFile.write("This is the new file created by the python.")
newFile.close

FileOverwrite = open("newFile.txt","w")
newFile.write("The content of the new file is changed")
FileOverwrite.close()

appendFile = open("hello.txt","a")
appendFile.write("\n\nDon't Forget to Smile Today")
appendFile.close()

with open("hello.txt","r")as f:
    contents = f.read()
    print(contents)

