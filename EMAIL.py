def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For registering Type 1 and For login Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError

def getdetails():
    print("Please Provide")
    email = str(input("EMAIL: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    if email in info:
        return "Email Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +email + " " + password
    f.write(info)

def checkdetails():
    print("Please Provide")
    email = str(input("email: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(email) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + email
        else:
            return "Password entered is wrong"
    else:
        return "email not found. Please Sign Up."

print(choices())