a = {"Alice":80,"Oliver":74,"Chris":91}  # Create an empty dictionary to store student marks

while True:  # Loop to continuously ask for input
    b= input("Enter a student's name: ")
    if b in a:
        print(b + "'s marks:", a[b])
    else:
        print("Student not found.")