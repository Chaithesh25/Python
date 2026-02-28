correc_user = "anish"
correct_pass = "1233"
attemp = 3
while attemp > 0:
    username = input("enter user name: ")
    password = input("enter your password: ")

    if username == correc_user and password == correct_pass:
        print("login succesfull>>")
        break
    else:
        print("invalid username or password")
        attemp = attemp -1

if attemp == 0:
    print("your account is blocked")
        