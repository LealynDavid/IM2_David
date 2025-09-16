def convert_dollar(amount):
    """Convert USD to INR, GBP, and CNY"""

    inr_rate = 88.08
    gbp_rate = 0.73
    cny_rate = 7.12

    inr = amount * inr_rate
    gbp = amount * gbp_rate
    cny = amount * cny_rate

    return inr, gbp, cny

def main():
    print("Enter dollar ($) (* to exit): ", end="")
    user_input = input()

    while user_input != "*":
        try:
            dollar_values = list(map(int, user_input.split("@")))
            
            print(f"\n{'Dollar ($)':<12} {'Indian Rupee (₹)':<18} {'British Pound (£)':<20} {'Chinese Yuan (¥)'}")
            
            for amount in dollar_values:
                inr, gbp, cny = convert_dollar(amount)
                print(f"{amount:<12} {inr:<18.2f} {gbp:<20.2f} {cny:.2f}")

        except ValueError:
            print("Invalid input. Please enter values like 189@78@56@12")

        print("\nEnter dollar ($) (* to exit): ", end="")
        user_input = input()

    print("Bye")

if __name__ == "__main__":
    main()
