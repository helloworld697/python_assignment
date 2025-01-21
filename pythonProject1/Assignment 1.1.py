def tester(givenstring):
    if givenstring == "quit":
        return False
    elif len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)
    return True
    #return givenstring

def main():
    while True:
        givenstring = input("Writesomething(quit ends):")
        tester(givenstring)
        if not tester(givenstring):
            break


if __name__ == "__main__":
    main()
