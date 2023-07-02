Events = [
    {"Name": "battle of stockholm", "Registrations": 300, "Location": "Vallentuna","ID": "953214949", "Type": "Bjj", "Capacity": [400, 400]},
    {"Name": "bjj open", "Registrations": 250,"Location": "London","ID": "953214971", "Type": "Bjj", "Capacity": [640, 650]},
    {"Name": "battle of sandviken", "Registrations": 450, "Location": "Spain","ID": "0903214971", "Type": "Boxing", "Capacity": [250    , 250]},
    {"Name": "bjj open", "Registrations": 450, "Location": "Ohio","ID": "0904949696", "Type": "muay thai", "Capacity": [100, 250]}
]
choice = input("Welcome To The Event managment system, what would you like to do today?\n[0] - Quit\n[1] - Register to event\n[2] - Add Event\n[3] - Remove Event(Requires host ID)\n[4] - Check capacity\nEnter: ")
def pick_event():
    print(Events[0]["Name"], Events[0]["Location"])
    print(Events[1]["Name"], Events[1]["Location"])
    print(Events[2]["Name"], Events[1]["Location"])
    print(Events[3]["Name"], Events[3]["Location"])
    Mano = input("Which Event would you like to Register to?\nEnter: ")
    if Mano == Events[0]["Name"]:
        Reg = input("Name: ")
        Beg = input("Age: ")
        Heg = input("Belt: ")
        Leg = input("ID: ")

        Regis = {
            "Name:": Reg,
            "Age:": Beg,
            "Belt:": Heg,
            "ID": Leg,
            "Event:": Events[0]["Name"]
        }
        print(Regis)


    else:
        if Mano == Events[1]["Name"]:
            Regr = input("Name: ")
            Begr = input("Age: ")
            Hegr = input("Belt: ")
            Legr = input("ID: ")

            Regisr = {
                "Name:": Regr,
                "Age:": Begr,
                "Belt:": Hegr,
                "ID": Legr,
                "Event:": Events[1]["Name"]
            }
            print(Regisr)
        else:
            if Mano == Events[2]["Name"]:
                Regrr = input("Name: ")
                Begrr = input("Age: ")
                Hegrr = input("Belt: ")
                Legrr = input("ID: ")

                Regisrr = {
                    "Name:": Regrr,
                    "Age:": Begrr,
                    "Belt:": Hegrr,
                    "ID": Legrr,
                    "Event:": Events[2]["Name"]
                }
                print(Regisrr)
            else:
                if Mano == Events[3]["Name"]:
                    Regrrr = input("Name: ")
                    Begrrr = input("Age: ")
                    Hegrrr = input("Belt: ")
                    Legrrr = input("ID: ")

                    Regisrrr = {
                        "Name:": Regrrr,
                        "Age:": Begrrr,
                        "Belt:": Hegrrr,
                        "ID": Legrrr,
                        "Event:": Events[3]["Name"]
                    }
                    print(Regisrrr)
def Add_event():
    name = input("What will the name of the event be:")
    IDR = input("What is you're ID:")
    Location = input("What is the location:")
    Type = input("What is the type of Event example (Bjj, Boxing, Muay thai): ")


    Event_2 = {
        "name": name,
        "Registrations": "0",
        "Location": Location,
        "ID": IDR,
        "Type": Type
    }

    Events.append(Event_2)
    for Ev in Events:
        print(Ev)

def Remove_Event():
    IRS = input("Enter The ID of the Event: ")
    if IRS == Events[0]["ID"]:
        IRS_2 = input("Are You Sure you want to delete " + Events[0]["Name"] + " enter Yes or no\nEnter: ")
        if IRS_2 == "yes" or "Yes":
            del(Events[0])
            for i in Events:
                print(i)
        else:
            print("")
    else:
        if IRS == Events[1]["ID"]:
            IRS_2 = input("Are You Sure you want to delete " + Events[1]["Name"] + " enter Yes or no\nEnter: ")
            if IRS_2 == "yes" or "Yes":
                del(Events[1])
                for i in Events:
                    print(i)
            else:
                print("")
        else:
            if IRS == Events[2]["ID"]:
                IRS_2 = input("Are You Sure you want to delete " + Events[2]["Name"] + " enter Yes or no\nEnter: ")
                if IRS_2 == "yes" or "Yes":
                    del(Events[2])
                    for i in Events:
                        print(i)
                else:
                    print("")
            else:
                if IRS == Events[3]["ID"]:
                    IRS_2 = input("Are You Sure you want to delete " + Events[3]["Name"] + " enter Yes or no\nEnter: ")
                    if IRS_2 == "yes" or "Yes":
                        del(Events[3])
                        for i in Events:
                            print(i)
                    else:
                        print("")
def Check_capacity():
    check = input("Which Event would you like to check?\n[1] - " + Events[0]["Name"] + "\n[2] - " + Events[1]["Name"] + "\n[3] - " + Events[2]["Name"] + "\n[4] - " + Events[3]["Name"] + "\nEnter: ")
    if check == "1":
        if Events[0]["Capacity"][0] == Events[0]["Capacity"][1]:
            print("Full")
        else:
            if Events[0]["Capacity"][0] < Events[0]["Capacity"][1]:
                print("Open")
    else:
        if check == "2":
            if Events[1]["Capacity"][0] == Events[1]["Capacity"][1]:
                print("Full")
            else:
                if Events[1]["Capacity"][0] < Events[1]["Capacity"][1]:
                    print("Open")
        else:
            if check == "3":
                if Events[2]["Capacity"][0] == Events[2]["Capacity"][1]:
                    print("Full")
                else:
                    if Events[2]["Capacity"][0] < Events[2]["Capacity"][1]:
                        print("Open")
            else:
                if check == "4":
                    if Events[3]["Capacity"][0] == Events[3]["Capacity"][1]:
                        print("Full")
                    else:
                        if Events[3]["Capacity"][0] < Events[3]["Capacity"][1]:
                            print("Open")
                
        


        

if choice == "0":
    print("")
else:
    if choice == "1":
        pick_event()
    else:
        if choice == "2":
            Add_event()
        else:
            if choice == "3":
                Remove_Event()
            else:
                if choice == "4":
                    Check_capacity()