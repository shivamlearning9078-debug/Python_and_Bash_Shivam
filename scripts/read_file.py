# Read Content from a File

file = open("student_data.txt", "r")

content = file.read()

print("Contents of the file:")
print(content)

file.close()
