Events = [
    {"Name": "battle of stockholm", "Location": "Vallentuna","ID": "953214949", "Type": "Bjj", "Capacity": [400, 400]},
    {"Name": "bjj open", "Location": "London","ID": "953214971", "Type": "Bjj", "Capacity": [640, 650]},
    {"Name": "battle of sandviken", "Location": "Spain","ID": "0903214971", "Type": "Boxing", "Capacity": [250, 250]},
    {"Name": "bjj open", "Location": "Ohio","ID": "0904949696", "Type": "muay thai", "Capacity": [100, 250]}
]
choice = input("Welcome To The Event managment system, what would you like to do today?\n[0] - Quit\n[1] - Register to event\n[2] - Add Event\n[3] - Remove Event(Requires host ID)\n[4] - Check capacity\n[5] - modify Event(requires login)\nEnter: ")
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
def Modify_event():
    mod = input("ID Required\nEnter: ")
    if mod == Events[0]["ID"]:
        kok = input("\nWhat would you like to modify for battle of stockholm\n[1] - Name\n[2] - Location\n[3] - Type\nEnter: ")
        if kok == "1":
            nmn = input("What Would you like the new name to be?\nEnter: ")
            new_Event_2 = {
                "Name": nmn,
                "Location": Events[0]["Location"],
                "ID": Events[0]["ID"],
                "Type": Events[0]["Type"],
                "Capacity": Events[0]["Capacity"]
            }
            print(new_Event_2)
        else:
            if kok == "2":
                nmnn = input("What Would you like the new location to be?\nEnter: ")
                new_Event_2n = {
                    "Name": Events[0]["Name"],
                    "Location": nmnn,
                    "ID": Events[0]["ID"],
                    "Type": Events[0]["Type"],
                    "Capacity": Events[0]["Capacity"]
                }
                print(new_Event_2n)
            else:
                if kok == "3":
                    nmnnn = input("What Would you like the new Type to be?\nEnter: ")
                    new_Event_2nn = {
                        "Name": Events[0]["Name"],
                        "Location": Events[0]["Location"],
                        "ID": Events[0]["ID"],
                        "Type": nmnnn,
                        "Capacity": Events[0]["Capacity"]
                    }
                    print(new_Event_2nn)
    else:
        if mod == Events[1]["ID"]:
            kok = input("\nWhat would you like to modify for bjj open\n[1] - Name\n[2] - Location\n[3] - Type\nEnter: ")
            if kok == "1":
                nmn = input("What Would you like the new name to be?\nEnter: ")
                new_Event_2 = {
                    "Name": nmn,
                    "Location": Events[1]["Location"],
                    "ID": Events[1]["ID"],
                    "Type": Events[1]["Type"],
                    "Capacity": Events[1]["Capacity"]
                }
                print(new_Event_2)
            else:
                if kok == "2":
                    nmnn = input("What Would you like the new location to be?\nEnter: ")
                    new_Event_2n = {
                        "Name": Events[1]["Name"],
                        "Location": nmnn,
                        "ID": Events[1]["ID"],
                        "Type": Events[1]["Type"],
                        "Capacity": Events[1]["Capacity"]
                    }
                    print(new_Event_2n)
                else:
                    if kok == "3":
                        nmnnn = input("What Would you like the new Type to be?\nEnter: ")
                        new_Event_2nn = {
                            "Name": Events[1]["Name"],
                            "Location": Events[1]["Location"],
                            "ID": Events[1]["ID"],
                            "Type": nmnnn,
                            "Capacity": Events[1]["Capacity"]
                        }
                        print(new_Event_2nn)
        else:
            if mod == Events[2]["ID"]:
                kok = input("\nWhat would you like to modify for battle of sandviken\n[1] - Name\n[2] - Location\n[3] - Type\nEnter: ")
                if kok == "1":
                    nmn = input("What Would you like the new name to be?\nEnter: ")
                    new_Event_2 = {
                        "Name": nmn,
                        "Location": Events[2]["Location"],
                        "ID": Events[2]["ID"],
                        "Type": Events[2]["Type"],
                        "Capacity": Events[2]["Capacity"]
                    }
                    print(new_Event_2)
                else:
                    if kok == "2":
                        nmnn = input("What Would you like the new location to be?\nEnter: ")
                        new_Event_2n = {
                            "Name": Events[2]["Name"],
                            "Location": nmnn,
                            "ID": Events[2]["ID"],
                            "Type": Events[2]["Type"],
                            "Capacity": Events[2]["Capacity"]
                        }
                        print(new_Event_2n)
                    else:
                        if kok == "3":
                            nmnnn = input("What Would you like the new Type to be?\nEnter: ")
                            new_Event_2nn = {
                                "Name": Events[2]["Name"],
                                "Location": Events[2]["Location"],
                                "ID": Events[2]["ID"],
                                "Type": nmnnn,
                                "Capacity": Events[2]["Capacity"]
                            }
                            print(new_Event_2nn)
            else:
                if mod == Events[3]["ID"]:
                    kok = input("\nWhat would you like to modify for battle of sandviken\n[1] - Name\n[2] - Location\n[3] - Type\nEnter: ")
                    if kok == "1":
                        nmn = input("What Would you like the new name to be?\nEnter: ")
                        new_Event_2 = {
                            "Name": nmn,
                            "Location": Events[3]["Location"],
                            "ID": Events[3]["ID"],
                            "Type": Events[3]["Type"],
                            "Capacity": Events[3]["Capacity"]
                        }
                        print(new_Event_2)
                    else:
                        if kok == "2":
                            nmnn = input("What Would you like the new location to be?\nEnter: ")
                            new_Event_2n = {
                                "Name": Events[3]["Name"],
                                "Location": nmnn,
                                "ID": Events[3]["ID"],
                                "Type": Events[3]["Type"],
                                "Capacity": Events[3]["Capacity"]
                            }
                            print(new_Event_2n)
                        else:
                            if kok == "3":
                                nmnnn = input("What Would you like the new Type to be?\nEnter: ")
                                new_Event_2nn = {
                                    "Name": Events[3]["Name"],
                                    "Location": Events[3]["Location"],
                                    "ID": Events[3]["ID"],
                                    "Type": nmnnn,
                                    "Capacity": Events[3]["Capacity"]
                                }
                                print(new_Event_2nn)



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
                else:
                    if choice == "5":
                        Modify_event()
