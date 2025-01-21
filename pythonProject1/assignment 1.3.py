def main():
    products = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    totalsum = 0

    print("Supermarket")
    print("===========")

    while True:
        choice = int(input("Please select product (1-10) 0 to Quit: "))
        if choice == 0:
            break
        elif 1 <= choice <= 10:
            price = products[choice - 1]
            totalsum += price
            print(f"Product: {choice} Price: {price}")
        else:
            print("Incorrect selection.")

    print(f"Total: {totalsum}")

    payment = int(input("Payment: "))
    print(f"Change: {payment - totalsum}")

if __name__ == "__main__":
    main()
