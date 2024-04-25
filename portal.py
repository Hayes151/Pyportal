import time

print("PYTHON PORTAL")
time.sleep(3)

print("To play the Password Game, press 1. To play Crash the Terminal, press 2. To quit, press 3. For a description about the portal, press 4. To contact me, press 5. For news, press 6.")
print("WARNING: This software is in beta, so many things are subject to change, and some things may break.")
while True:
    choice = input("Choice: ")

    if choice == "1":
        while True:
            print("Loading Password Game...")
            time.sleep(3)
            code = input("Password: ")
            if code == "Coco":
                print("Password Correct!")
            else:
                print("Password Incorrect! To try again, press 1, or press 2 to return to the menu.")
                choice2 = input("Choice: ")
                if choice2 == "1":
                    code = input("Password: ")
                elif choice2 == "2": print("Returned to menu.")
                break

    elif choice == "2":
        text = input("Enter text to spam: ")
        while True:
            print(text)

    elif choice == "3":
        print("Exiting the program...")
        break
    elif choice == "4":
        print("PYTHON PORTAL Version 1.0 Programmed by Hayes Fryrear. Debugged by Visual Studio Code and ChatGPT. Copyright 2024 Htech Software LLC.")
    elif choice == "5":
        print("Loading contact info...")
        time.sleep(3)
        print("Info loaded!")
        print("Phone: 432-638-7426. Email: hayes151@icloud.com")

    elif choice == "6":
        print("Welcome! Here you will find the news section. This service is called Pynews. To access Pynews, press 1. To return to the menu, press 2.")
        while True:
            news = input("Choice: ")
            if news == "1":
                print("Big news Python Portal users! We have big plans to add more software to the portal, like a To-Do list, and a timer. Stay tuned! ")
            elif news == "2":
                print("Returning to menu.")
                break
            else:
                print("Invalid choice!")
