def guessing():
    num_entered = 1
    random_number = 0
    entries = 0
    numbers_entered_list = list()
    while True:

        current_time = str(datetime.datetime.now()) + " "
        file = open("error.txt", "a+")
        try:
            random_number = random.randint(1, 100)
            while num_entered != random_number:
                num_entered = input("Enter a number: ")
                if num_entered.isdigit():
                    num_entered = int(num_entered)
                else:
                    raise TypeError("Type Error")
                    num_entered = input("Enter a number: ")
                if entries == 0 and num_entered == random_number:
                    print("WTF ARE YOU VANGA???")
                    numbers_entered_list.append(num_entered)
                if num_entered == random_number:
                    print("GOOD MAN!!!")
                    entries += 1
                    numbers_entered_list.append(num_entered)
                else:
                    if random_number > num_entered:
                        print("Enter a higher number")
                        entries += 1
                        numbers_entered_list.append(num_entered)
                    else:
                        print("enter a smaller number")
                        entries += 1
                        numbers_entered_list.append(num_entered)
            print(str(numbers_entered_list) + " It took " + str(entries) + " tries")
            numbers_entered_list = []
            entries = 0
            quest = input("do you want to continue? (yes/no): ")
            quest = quest.lower()
            if quest == "yes":
                num_entered = 0
                continue
            if quest == "no":
                quest = input("Do you want to continue another service? (yes/no): ")
                quest = quest.lower()
                if quest == "yes":
                    exec(open("main.py").read())
                    break
                if quest == "no":
                    quit()
                else:
                    raise Exception("input error")
                    continue
            else:
                raise Exception("input error")
        except TypeError as e:
            file.write(str(current_time) + str(e) + "\n")
            print(e)
        except Exception as e:
            file.write(str(current_time) + str(e) + "\n")
            print("error")
        finally:
            file.close()


guessing()
