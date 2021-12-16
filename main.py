import datetime, random

result = 0
my_tuple = tuple()
my_list = list()


def mainmenu():
    # opening err.txt file and print realtime + string(error type) in it
    current_time = str(datetime.datetime.now()) + " "
    file = open("error.txt", "a+")
    try:
        print("1. calculator")
        print("2. guessing")
        print("3. exit")
        selection = input("enter the number: ")
        selection = selection.lower()
        if selection == "1":
            exec(open("calculator.py").read())
        if selection == "2":
            exec(open("guessing.py").read())
        if selection == "3":
            quit()
        if selection == "q":
            quit()
        if selection == "quit":
            quit()
        else:
            # adding an Exception
            raise Exception("input error")
    except Exception as e:
        file.write(str(current_time) + str(e) + "\n")
        print("error")
    finally:
        file.close()
    mainmenu()


mainmenu()
