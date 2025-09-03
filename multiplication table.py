def print_table_with_highlight(rows, cols, search):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            value = i * j
            if value == search:
                print(f"[{value}]", end="\t")
            else:
                print(f"{value}", end="\t")
        print()  
while True:
    try:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if row <= 0 or col <= 0:
            break

        search = int(input("Search: "))
        print()  
        print_table_with_highlight(row, col, search)
        print() 

    except ValueError:
        print("Invalid input. Please enter integers only.\n")
