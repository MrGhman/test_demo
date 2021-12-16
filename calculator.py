def calculator():
    def addition(x, y):
        return x + y

    # subtract
    def subtraction(x, y):
        return x - y

    # multiple
    def multiplication(x, y):
        return x * y

    # divide
    def division(x, y):
        return x / y

    # add

    while True:
        # opening err.txt file and print realtime + string(error type) in it
        current_time = str(datetime.datetime.now()) + " "
        file = open("error.txt", "a+")
        try:
            # input action
            choice = input("enter the action(+;-;*;/): ")
            if choice in ('+', '-', '*', '/'):
                # input numbers
                num1 = input("enter first number: ")
                num2 = input("enter second number: ")
                if num1.isdigit() != True or num2.isdigit() != True:
                    raise Exception("input error")
                    continue

                if choice == '+':
                    result = addition(float(num1), float(num2))

                elif choice == '-':
                    result = subtraction(float(num1), float(num2))

                elif choice == '*':
                    result = multiplication(float(num1), float(num2))

                elif choice == '/' and float(num2) != 0:
                    result = division(float(num1), float(num2))
                if float(num2) == 0:
                    # adding Zero Division Error Exception
                    raise ZeroDivisionError("Zero Division Error")
                    continue
                print(str(num1) + choice + str(num2) + " = " + str(result))
                my_tuple = (str(num1) + choice + str(num2) + " = " + str(result))
                my_list.append(my_tuple)
                print(my_list)

                # ask about continue
                # Stop while loop - if answer is no
                quest = input("do you want to continue? (yes/no): ")
                quest = quest.lower()
                if quest == "no":
                    exec(open("main.py").read())
                    break
                if quest == "yes":
                    continue
                else:
                    raise Exception("input error")

            else:
                raise Exception("invalid operation")
            # adding Exceptions
        except ValueError as e:
            file.write(str(current_time) + str(e) + "\n")
            print(e)
        except ZeroDivisionError as e:
            file.write(str(current_time) + str(e) + "\n")
            print(e)
        except Exception as e:
            file.write(str(current_time) + str(e) + "\n")
            print("error")
        finally:
            file.close()


calculator()
