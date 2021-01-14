from tkinter import *

root = Tk()
root.title("TornValue by TornTrader")
root.geometry("500x500")

def check_answer(question, answers):
    answer = " "
    while answer not in answers:
        answer = input(question).lower()
    return answer


def script():
    Value = input("\nPaste the Raw total Trade value as numbers only...")
    value = float(Value)
    eighty = value * 0.8
    ninety = value * 0.9
    ninety_one = value * 0.91
    ninety_five = value * 0.95
    ninety_eight = value * 0.98

    choice = check_answer("\nWhat percentage Would you like to Profit?\n(1) 20%\n(2) 10%\n(3) 9%\n(4) 5%\n"
                          "(5) 2%\n\n>>> ", ["1", "2", "3", "4", "5"])
    if choice == "1":
        expression = int(eighty)
        print("\nTotal Worth: ", Value)
        print("Trade Value: ", int(expression))
        print("Total Profit: ", int(int(Value) - expression))

    elif choice == "2":
        expression = int(ninety)
        print("\nTotal Worth: ", Value)
        print("Trade Value: ", int(expression))
        print("Total Profit: ", int(int(Value) - expression))

    elif choice == "3":
        expression = int(ninety_one)
        print("\nTotal Worth: ", Value)
        print("Trade Value: ", int(expression))
        print("Total Profit: ", int(int(Value) - expression))

    elif choice == "4":
        expression = int(ninety_five)
        print("\nTotal Worth: ", Value)
        print("Trade Value: ", int(expression))
        print("Total Profit: ", int(int(Value) - expression))

    else:
        expression = int(ninety_eight)
        print("\nTotal Worth: ", Value)
        print("Trade Value: ", int(expression))
        print("Total Profit: ", int(int(Value) - expression))

    restart = check_answer("\nStart Over?\n(1) Yes\n(2) No\n\n>>> ", ["1", "2"])
    if restart == "1":
        script()
    else:
        quit()


script()
mainloop()