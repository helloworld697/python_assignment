def print_menu():
    print("\nWould you like to")
    print("(1) Add")
    print("(2) Remove items")
    print("(3) Quit?")

def add_item(shopping_list):
    item = input("What will be added?: ")
    shopping_list.append(item)

def remove_item(shopping_list):
    print(f"There are {len(shopping_list)} items in the list.")
    try:
        index = int(input("Which item is deleted?: "))
        if 0 <= index < len(shopping_list):
            shopping_list.pop(index)
        else:
            print("Incorrect selection.")
    except ValueError:
        print("Incorrect selection.")

def main():
    shopping_list = []
    while True:
        print_menu()
        choice = input("Select an option: ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            if shopping_list:
                remove_item(shopping_list)
            else:
                print("There are no items to remove.")
        elif choice == '3':
            break
        else:
            print("Incorrect selection.")

    print("\nThe following items remain in the list:")
    for item in shopping_list:
        print(item)

if __name__ == "__main__":
    main()
