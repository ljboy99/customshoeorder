import json, os


userchoice = ''
def currentorderlist():
    global userchoice
    #print(str(os.listdir("current_orders/")))
    print(str(os.listdir("current_orders/")).replace(", ", "\n")
                                            .replace("[", "")
                                            .replace("]", "")
                                            .replace("'", "")
                                            .replace(".json", "")
                                            .replace("_", " "))
    userchoice = input("""You may view an active order by 
typing a name and style number, 
as formatted above.
""")
    for i in os.listdir("current_orders/"):
        if userchoice[0:10] == i[0:10]:
            order = open("current_orders/"+i)
            print(json.load(order))
        #else:
        #    print("no match")

def viewagain():
    viewanother = input('Would you like to view another order? ')
    if viewanother[0].upper() == "Y":
        view()
#    else:
#        with open("customordermenu.py") as f:
#            exec(f.read())

def view():
    currentorderlist()
    viewagain()

view()