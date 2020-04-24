while(True):
    print("""Welcome to the interactive Calculator!
Please introduce two numbers.""")
    n1 = float(input("First Number: "))
    n2 = float(input("Second Number: "))
    print("What do you want to do? Select, '+', '-', '*', '/'. Or 'Exit' to leave the program." )
    operation = input("Choose match Operation: ")
    if operation == "+":
        print("The result is", n1 + n2)
    elif operation == "-":
        print("The result is", n1 - n2)
    elif operation == "*":
        print("The result is", n1 * n2)
    elif operation == "/":
        print("The resul is", n1 / n2)
    elif operation == "Exit or exit":
        print("Leaving the best calculator system of the World ..........")
        break
    else:
        print("Please select de correct mach operation")