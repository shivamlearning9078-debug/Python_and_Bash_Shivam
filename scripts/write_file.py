# Write Content to a File

file = open("student_data.txt", "w")

file.write("Python and Bash Assignment\n")
file.write("Name: Shivam\n")
file.write("Topic: File Handling in Python\n")
file.write("This file was created using Python.\n")

file.close()

print("Content written to student_data.txt successfully!")
