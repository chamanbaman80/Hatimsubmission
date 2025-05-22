
file1=open("output.txt","w")
writing_file=file1.write("Hello, python!")
print(writing_file)
file1.close()


file3=open("output.txt","a")
appending_file=file3.write("\nLearning file handling in python.")
print(appending_file)
file3.close()

