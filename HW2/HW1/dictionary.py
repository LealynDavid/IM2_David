def main():
    # Create dictionary with initial shopping items
    mydict = {}
    mydict[0] = "underwear"
    mydict[1] = "tank top"
    mydict[2] = "jacket"

    print("You have", len(mydict), "items in the cart")

    while True:
        choice = input("\nWhat would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").strip().upper()

        if choice == "D":  # Display items
            print("\nDisplaying Values")
            print("Key      Value")
            for k, v in mydict.items():
                print(f"{k:<8} {v}")

        elif choice == "S":  # Search items
            search_value = input("\nEnter item to search: ").strip()
            found = False

            # First try searching by value
            for k, v in mydict.items():
                if v.lower() == search_value.lower():
                    print(f"Found {v} item")
                    found = True
                    break

            # If not found, try searching by key
            if not found:
                try:
                    key = int(search_value)
                    val = mydict.get(key)
                    if val:
                        print(f"Found {val} item")
                    else:
                        print("Im sorry, not in the cart")
                except ValueError:
                    print("Im sorry, not in the cart")

        elif choice == "R":  # Remove item
            key_input = input("\nEnter key to search: ")
            try:
                key = int(key_input)
                if key in mydict:
                    removed_value = mydict.pop(key)
                    print(f"The key {key} with value {removed_value} has been deleted")
                else:
                    print("Key not found")
            except ValueError:
                print("Key not found")

        elif choice == "C":  # Change item
            key_input = input("\nEnter key to search: ")
            try:
                key = int(key_input)
                if key in mydict:
                    print(f"Found {mydict[key]} item")
                    new_value = input("Enter value: ")
                    mydict[key] = new_value
                else:
                    print("Im sorry, not in the cart")
            except ValueError:
                print("Im sorry, not in the cart")

        elif choice == "*":  # Exit
            print("Bye")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
else:
    print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

