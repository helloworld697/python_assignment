def tester(givenstring):
    if givenstring == "quit":
        break
    elif len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)
    return givenstring

def main():
    givenstring = input("Writesomething(quit ends):")
    tester(givenstring)
   # if givenstring == "quit":


if __name__ == "__main__":
    main()
