while True:
    ans = input("Yes or No: ").strip().lower()
    if ans == "break":
        print("cheater")
        break
    elif ans == "yes":
        print("Do again")
    else:
        print("You've escaped")
        break