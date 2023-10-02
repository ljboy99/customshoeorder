

command = input("""Welcome to the custom order menu
What would you like to do?
    1. Create custom order
    2. View custom order
    3. Delete custom order
    4. Update custom order
    5. Fulfill custom order
    """)

if command[0] == "1":
    with open("write.py") as f:
        exec(f.read())
elif command[0] == "2":
    with open("view.py") as f:
        exec(f.read())
elif command[0] == "3":
    with open() as f:
        exec(f.read())
elif command[0] == "4":
    with open() as f:
        exec(f.read())
elif command[0] == "5":
    with open() as f:
        exec(f.read())
