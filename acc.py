def new_acc(username, passw):
    DB = open("DB", "a")
    DB.write(username+":"+passw+":"+"\n")
    DB.close()
def connection(username, passw):
    DB = open("DB", "r")
    test = 0
    for line in DB.readlines():
        if line.split(":")[0] == username:
            if line.split(":")[1] == passw:
                print("Loged as {}".format(username))
                test = 1
    if test == 0:
        print("[!]Password or user is Wrong")
    DB.close()
while True:
    cmd = input(">>")
    if cmd.lower()=="new":
        user = input("username: ")
        pas = input("password: ")
        new_acc(user, pas)
        print("Registred!")
    if cmd.lower() == "connect":
        userC = input("Username Or Email: ")
        pasC = input("Password: ")
        connection(userC, pasC)
    if cmd.lower() == "exit":
        break
