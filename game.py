import pandas as pd
import os
import random
global UserStats
global i
global AttackIncrease
AttackIncrease = 0
global DefenceIncrease
DefenceIncrease = 0
i = 1
global User

#first thing you see when starting the game
def main_menu():
    flag = True
    while flag:
        os.system("cls")
        print("#####################")
        print(" Goonicle Adventures")
        print("#####################\n")
        print("#####################")
        print("1. New Game")
        print("2. Load Game")
        print("3. View High Scores")
        print("4. Close Game")
        print("#####################")
        choice = input("")
        #returns values for another function to use
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        elif choice == "4":
            return 4
        else:
            print("Invalid choice.")
            continue

#takes user choice for profession
def getprofession():
    flag = True
    while flag:
        print("What would you like your profession to be?")
        print("1. Knight")
        print("2. Archer")
        print("3. Magician\n")
        choice = input()
        #returns values based on user choice
        if choice == "1":
            return "Knight"
        elif choice == "2":
            return "Archer"
        elif choice == "3":
            return "Magician"
        else:
            print("Invalid choice.")
            continue

#creating a new game and everything that it entails.
def newgame():
    #global user as it is used in other functions
    global User
    global i
    os.system("cls")
    login_info = pd.read_csv("Logins.csv")
    flag = True
    #username perameters
    while flag:
        User = input("What would you like your username to be? ")
        if len(User) > 10:
            print("Username should be less than 10 characters long. ")
        else:
            #sees if username is in use
            df = login_info.loc[login_info['Username'] == User]
            if len(df) > 0:
                print("Username is in use!")
                continue
            flag = False
    os.system('cls')            
    
    #password perameters
    flag = True
    while flag:
        password = input("What would you like your password to be? ")
        if len(password) > 16:
            print("Password should be less than 16 characters long. ")
        else:
            flag = False
    os.system('cls')

    #saves login info in csv, removes index
    new_info = {"Username":User,"Password":password}

    login_info = pd.read_csv("Logins.csv")
    new_login_df = pd.DataFrame([new_info])
    updated_login_info = pd.concat([login_info, new_login_df])
    updated_login_info.to_csv("Logins.csv", index=False)

    #uses global variable to hold user stats as they ar ereferred to throughout the game
    global UserStats

    #gets profession and assigns values to a data frame
    proff = getprofession()

    #assigns all values for items and stats for a new account for each profession type
    if proff == "Knight":
        new_info = {"Username":User,"Profession":"Knight","Weapon":"Training Sword","Helmet":None,"Armor":None,"Shield":None,"Gloves":None,
                     "Boots":None, "Level":1, "Experience":0, "Health":200, "Defence":10, "Mana":100, "Attack":10, "Magic Attack":0, "Room":0}
        UserStats = {"Weapon":"Training Sword","Helmet":None,"Armor":None,"Shield":None,"Gloves":None, "Boots":None, "Level":1,
                      "Experience":0, "Health":200, "Defence":10, "Mana":100, "Attack":10, "Magic Attack":0, "Room":0}
    elif proff == "Archer":
        new_info = {"Username":User,"Profession":"Archer","Weapon":"Trainer Bow (10)","Helmet":None,"Armor":None,"Shield":None,"Gloves":None,
                     "Boots":None, "Level":1, "Experience":0, "Health":150, "Defence":10, "Mana":150, "Attack":10, "Magic Attack":10, "Room":0}
        UserStats = {"Weapon":"Trainer Bow (10)","Helmet":None,"Armor":None,"Shield":None,"Gloves":None, "Boots":None, "Level":1,
                      "Experience":0, "Health":150, "Defence":10, "Mana":150, "Attack":10, "Magic Attack":10, "Room":0}
    elif proff == "Magician":
        new_info = {"Username":User,"Profession":"Magician","Weapon":"Training Wand","Helmet":None,"Armor":None,"Shield":None,"Gloves":None,
                     "Boots":None, "Level":1, "Experience":0, "Health":100, "Defence":0, "Mana":200, "Attack":0, "Magic Attack":10, "Room":0}
        UserStats = {"Weapon":"Training Wand","Helmet":None,"Armor":None,"Shield":None,"Gloves":None, "Boots":None, "Level":1,
                      "Experience":0, "Health":100, "Defence":0, "Mana":200, "Attack":0, "Magic Attack":10, "Room":0}
    else:
        print("Fatal error!!!")
        exit()

    #saves user info   
 
    #makes new info a df, concats new data with old, rewrites to csv with correct indexebtvgfkshehgrjdgnu8o\liwesghdfo87weisuyhfiuwelsjhfo8ew
    userinfo = pd.read_csv("UserInfo.csv", index_col=[0])
    new_user_df = pd.DataFrame([new_info])
    if userinfo.empty == False:
        max_index = userinfo.index.max()
    else:
        max_index = 0
    new_user_df.index = [max_index + 1]
    updated_info = pd.concat([userinfo, new_user_df])
    updated_info.to_csv("UserInfo.csv")
    UserStats = pd.DataFrame(UserStats, index=[0])

    os.system('cls')
    print("###############################")
    print("Welcome to Goonicle Adventures!")
    print("###############################")
    print("#   Press ENTER to continue.  #")
    print("###############################")
    input()
    i = 0

#interface for login menu
def logininterface():
    print("#############################")
    print("#           Login           #")
    print("#############################")

#loads stored user data using username / password
def loadgame():
    os.system('cls')
    global User
    global UserStats
    j = 0
    flag = True
    while flag:
        os.system('cls')
        #prints display
        logininterface()
        #j is used to see if there has been an invalid attempt
        if j == 1:
            print("-----Username not found!-----")
        User = str(input("-----Enter your username-----\n"))
        logins = pd.read_csv("Logins.csv")
        #reads login csv and sees if there is a user with the name
        UserData = logins.loc[logins["Username"] == User]
        if len(UserData) == 0:
            j = 1
        else:
            #counts how many login attempts
            attempts = 0
            j = 0
            while flag:
                os.system('cls')
                #prints display
                logininterface()
                #j is used to see if there has been an invalid attempt
                if j == 1:
                    #5 wrong attempts will close the program
                    if attempts == 5:
                        print("-- Too many wrong attempts --") 
                        print("-----  Closing program. -----")
                        exit()
                    #informs the user when a wrong password is used
                    print(f"--Incorrect password! ({attempts}/5)--")
                PassWord = input("-----Enter your password-----\n")
                #rereads csv for security
                logins = pd.read_csv("Logins.csv")
                UserData = logins.loc[logins["Username"] == User]
                #gets value of password from csv, from userdata value
                ExpPassword = UserData["Password"].values
                #adds 1 to attemps if its wrong, breaks from loop if its right
                if PassWord != ExpPassword:
                    attempts += 1
                    j = 1
                    continue
                else:
                    flag = False
    #assigns user data to the whole of the users stored data
    UserInfo = pd.read_csv("UserInfo.csv", index_col=[0])
    UserData = UserInfo.loc[UserInfo["Username"] == User]
    #assigns user stats to all except the username and profession, as these will never change
    UserStats = UserData.iloc[:,2:]
    global i 
    i = 0
    prefaces(0)
    deeper()

#displays the high scores of all users saved.
def highscores():
    os.system("cls")
    print("###########################")
    print("#       High Scores       #")
    print("###########################")
    #opens high scores file
    scores = pd.read_csv("HighScores.csv")
    #sorts them by highest level
    scores = scores.sort_values("_Level_", ascending=False)
    #prints the top 10
    print(scores.head(10).to_string(index=False))
    print("###########################")
    print("#  Press ENTER to return  #\n#      to main menu.      #")
    print("###########################")
    global i
    i = 1
    input()

#main menu interface and handles all starting functions
def before_game():
    global i
    while i == 1:
        #opens main menu, allowing to start a new game, load a game, display highscores or quit
        mmchoice = main_menu()
        global z
        z = 2 if mmchoice == 2 else False
        newgame() if mmchoice == 1 else loadgame() if mmchoice == 2 else highscores() if mmchoice == 3 else exit()

#prints off current / updated stats
def prefaces(x):
    #calls upon global variable to get up to date info
    global UserStats
    UserStatsDF = pd.DataFrame(UserStats, index=[0])
    os.system("cls")
    if x == 1:
        stats = "#  These are your updated Stats.  #"
    else:
        stats = "#  These are your current Stats.  #"
    print("###################################")
    print(stats)
    print("###################################")
    #makes a dataframe of current user stats and transposes it to make it visually appealing
    print(UserStatsDF.T.rename(columns={0: ""}))
    print("###################################")
    print("#     Press ENTER to continue.    #")
    print("###################################")
    input()

#saves the game
def saving():
    #calls upon global variables
    global UserStats
    global User
    #opens csv and locates where the username is saved.
    UserInfo = pd.read_csv("UserInfo.csv", index_col=[0])
    UserData = UserInfo.loc[UserInfo["Username"] == User]
    #gets the username and profession (as these will never change)
    KeptUserData = UserData.iloc[:,:2]
    #resets index for concatonation
    KeptUserDataDF = pd.DataFrame(KeptUserData).reset_index(drop=True)
    #makes user stats dictionary a dataframe, sets index to 0. This is the same as keptuserdatadf,
    #making concatonation easy
    UserStatsDF = pd.DataFrame(UserStats).reset_index(drop=True)
    #adds the two dataframes together, from top to bottom.
    NewUserData = pd.concat([KeptUserDataDF, UserStatsDF], axis=1).reset_index(drop=True) 
    #gets indef to replace in the csv
    UserDataIndex = UserInfo.loc[UserInfo["Username"] == User].index
    #replaces the data from the index in the main dataframe and replaces the csv
    UserInfo.iloc[UserDataIndex] = NewUserData.values[0]
    UserInfo.to_csv("UserInfo.csv", index=True)
    
    #also saves user level in high scores csv
    level_up()

#saves the level of the user in the high scores csv
def level_up():
    #calls upon global variables for up to date info
    global User
    global UserStats
    HighScores = pd.read_csv("HighScores.csv")
    Level = int(UserStats["Level"])
    #if there is no user with the same username as the current player saved in the high scores csv,
    #it will add the user to the list. This is unsorted as the list is sorted in the program rather than hard coded.
    if len(HighScores.loc[HighScores["___Username___"] == User]) == 0:
        UserLevel = pd.DataFrame({"___Username___": [User], "_Level_": [Level]})
        HighScores = pd.concat([HighScores, UserLevel], axis=0, ignore_index=True)
    else:
        #if there is a user with the same username, get index of user in file and replace it with current high score.
        UserLevel = pd.DataFrame({"___Username___": [User], "_Level_": [Level]})
        UserLevelIndex = HighScores.loc[HighScores["___Username___"] == User].index
        HighScores.loc[UserLevelIndex, "_Level_"] = Level
    #replaces csv with saved dataframe instead
    HighScores.to_csv("HighScores.csv", index=False)
    os.system("cls")

#menu to allow the user to save, exit, view a guide, view their stats
def in_game_menu():
    flag = True
    j = 0
    while flag == True:
        #main menu
        os.system("cls")
        if j == 1:
            print("##########################")
            print("- Invalid option choice! -")
        print("##########################")
        print("#          Menu          #")
        print("##########################")
        print("1. View Stats ")
        print("2. View Handbook")
        print("3. Save Game")
        print("4. Save and Quit")
        print("5. Quit WITHOUT saving")
        print("6. Exit Menu")
        print("##########################")
        choice = input()
        if choice == "1": 
            #calls upon the function showing all current user stats held in a variable
            prefaces(0)
            j = 0
        elif choice == "2":
            #tutorial in case the user forgets anything
            os.system("cls")
            print("#############################")
            print("#       User Handbook       #")
            print("#############################\n")
            print("You may save the game at any")
            print("point, however fight progress")
            print("and the rooms around you will")
            print("NOT be saved.")
            print("\n######### Movement #########\n")
            print("User movement is dictated by")
            print("using a letter-movement")
            print("system (a for left, d for")
            print("right, w for ahead). There")
            print("is no backtracking due to")
            print("the constant room shifting")
            print("in this trial.")
            print("\n######### Fighting #########\n")
            print("Fighting in the game uses the")
            print("number keys on your keyboard")
            print("for the designated attacks")
            print("associated with them. These")
            print("attacks will be stated at the")
            print("start of every fight.")
            print("\n#############################")
            print("# press ENTER to go back to #")
            print("#         main menu         #")
            print("#############################")
            input()
            flag = True
        elif choice == "3":
            #calls upon saving function to write data to csv
            os.system("cls")
            saving()
            print("#############################")
            print("#        Data saved         #")
            print("#  Press ENTER to continue  #")
            print("#############################")
            input()
            flag = True
            j = 0
        elif choice == "4":
            #calls upon saving function to write data to csv and quits game
            saving()
            os.system("cls")
            print("##############################")
            print("#         Data saved         #")
            print("##############################")
            print("#   Thank you for playing!   #")
            print("#  Press ENTER to exit game  #")
            print("##############################")
            input()
            exit()
        elif choice == "5":
            #exits game without saving, makes sure the user wants to.
            flag1 = True
            j1 = 0
            while flag1:
                os.system("cls")
                if j1 == 1:
                    print("###############################")
                    print("--- Invalid option choice!  ---")
                print("###############################")
                print("# Are you sure you would like #")
                print("#   to exit without saving?   #")
                print("###############################")
                print("1. Yes (all data since last\n   save will be lost!)")
                print("2. No")
                choice2 = input()
                if choice2 == "1":
                    os.system("cls")
                    exit()
                elif choice2 == "2":
                    flag1 = False
                else:
                    j1 = 1
        elif choice == "6":
            flag = False
        else:
            j = 1

#function used for both starting a new game and continuing one.
def deeper():
    os.system("cls")
    print("#########################################")
    print("# You can hear echos coming from deeper #")
    print("#    within the dungeon. You shiver.    #")
    print("#########################################")
    input()
    while True:
        room_generation()

#function to introduce the game and begin the loop of gameplay.
def first_room():
    #textual "backstory"
    global UserStats
    os.system("cls")
    print("##################################")
    print("#          Goony McGoon          #")
    print("#--------------------------------#")
    print("#      Here begins a trial,      #\n#    challenged by many souls    #")
    print("#      but survived by few.      #\n#                                #\n#    Which side will you join    #")
    print("#       fabled traveller..       #")
    print("#--------------------------------#")
    print("##################################")
    print("#    Press ENTER to continue.    #")
    print("##################################")
    input()
    os.system("cls")
    print("##################################")
    print("#    You start to feel sleepy    #")
    print("##################################")
    print("#     Was there something in     #")
    print("#          the drink he          #")
    print("#          gave to you?          #")
    print("##################################")
    print("#    Press ENTER to continue.    #")
    print("##################################")
    input()
    os.system("cls")
    print("##################################")
    print("#          Goony McGoon          #")
    print("#--------------------------------#")
    print("#  Good luck, brave adventurer. ##")
    print("##################################")
    input()
    os.system("cls")
    print("##################################")
    print("#          You pass out          #")
    print("##################################")
    input()
    os.system("cls")
    print("##################################")
    print("# You awaken in a dimly lit room #")
    print("#    This is where it begins.    #")
    print("##################################")
    input()
    #increases user room count to 1, as this is the first room.
    UserStats["Room"] += 1
    flag = True
    while flag:
        os.system("cls")
        print("######################################")
        print("# There is only a room ahead of you. #")
        print("######################################\n")
        print("######################################")
        print("#         Enter W to proceed.        #")
        print("######################################")
        print("#      For future reference -a-      #")
        print("#    goes left and -d- goes right    #")
        print("#------------------------------------#")
        print("#      The menu can be used via      #")
        print("#     inputting -m- at any time!     #")
        print("######################################")
        dir = input()
        if dir.upper() == "W":
            deeper()
            flag = False
        elif dir.upper() == "M":
            in_game_menu()
            flag = True
        else:
            flag = True

#determines how many rooms are around you, and goes through the event of the next room.
def room_generation():

    #function just for printing the text
    def txt_format(room_txt):
        os.system("cls")
        print("########################################")
        print(room_txt)
        print("########################################")
        print("# What direction would you like to go? #")
        print("########################################")
        return input() 
    #contains all varieties of rooms
    room_combos = ["#  There is only a room ahead of you.  #",
                   "#      There is a room ahead, and      #\n#            to your right.            #", 
                   "#      There is a room ahead, and      #\n#             to your left             #",
                   "#      There is a room ahead, and      #\n#          either side of you          #",
                   "#  There is only a room to your left.  #",
                   "#  There is only a room to your right  #",
                   "#    There is a room on either side    #"]
    #contains accepted inputs for all varieties of rooms
    room_combos_inputs = [["w", "W", "m", "M"], ["w", "W", "d", "D", "m", "M"],
                          ["w", "W", "a", "A", "m", "M"], 
                          ["w", "W", "a", "A", "d", "D", "m", "M"],
                          ["a", "A", "m", "M"], ["d", "D", "m", "M"], 
                          ["a", "A", "d", "D", "m", "M"]]
    #determines what room(s) will be avaliable for the player, and inputs accepted for them.
    room = random.randint(0,6)
    room_txt = room_combos[room]
    room_accepted_input = room_combos_inputs[room]
    #takes user input, validates, calls upon menu or continues with game
    user_input_boolean = True
    while user_input_boolean == True:
        flag = True
        while flag:
            choice = txt_format(room_txt)
            flag = False if choice in room_accepted_input else True
            if choice not in ["m", "M"]:
                user_input_boolean = False
            else:
                in_game_menu()
                flag = True
    #increases room count 
    UserStats["Room"] += 1
    #encounter in the next room.
    event_number = random.randint(1,100)
    if event_number in range(1,46):
        empty_room()
    elif event_number in range(46,66):
        mob_room()
    else:
        loot_room()        
        input()

#prints text based on the room being empty
def empty_room():
    os.system("cls")
    print("###########################################")
    print("# The room you find yourself in is devoid #")
    print("# of anything. It is an empty, dark abyss #")
    print("###########################################")
    input()
    room_generation()

#prints text based on emcountering an enemy
def mob_room():
    df = pd.read_csv("UserInfo.csv")
    user_data = df.loc[df['Username'] == User]
    profession = user_data.iloc[0]['Profession']
    os.system("cls")
    def possible_attacks():
        global UserStats
        attacks = []
        if profession == "Knight":
            attacks.append("1. Basic Attack: {0} max dmg".format(UserStats["Attack"]))
            attacks.append("2. Infused Attack: {0} max dmg [{1}]".format(UserStats["Magic Attack"], "Uses 20 mana."))
            return attacks
        elif profession == "Magician":
            attacks.append("1. Basic Attack: {0} max dmg".format(UserStats["Attack"]))
            attacks.append("2. Infused Attack: {0} max dmg [{1}]".format(UserStats["Magic Attack"], "Uses 10 mana."))
            return attacks
        else:
            attacks.append("1. Basic Attack: {0} max dmg [Uses 1 Arrow]".format(UserStats["Attack"]))
            attacks.append("2. Infused Attack: {0} max dmg [Uses 2 Arrows, {1}]".format(UserStats["Magic Attack"], "Uses 10 mana."))
            return attacks
    print("###########################################")
    print("#         You encounter an enemy!         #")
    print("###########################################")
    #input()
    mob = mob_choice()
    arrows = 10
    engaged_UserStats = pd.DataFrame(UserStats, index=[0]).iloc[:,[8,9,11,12]]
    while mob["HP"] > 0:
        os.system("cls")
        print("###########################################")
        print("#               Enemy Stats               #")
        print("###########################################")
        print(mob.to_string())
        print("###########################################")
        print("#        What would you like to do        #")
        print("###########################################\n")
        attack_list = possible_attacks()
        print(attack_list[0])
        print(attack_list[1])
        print(f"Current arrow count: {arrows}") if profession == "Archer" else 10
        print("3. View current stats")
        print("\n###########################################")
        choice = input()
        if choice == "1":
            highest_attack = int(engaged_UserStats["Attack"].iloc[0])
            rolled_multiplier = random.randint(70,101)
            if rolled_multiplier == 101:
                attack = highest_attack * 1.5
                print("Crit attack!")
            else:
                attack = round(highest_attack * (rolled_multiplier / 100))
            print(attack)
            input()
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("###########################################")
            print("#              Current Stats              #")
            print("###########################################")
            print(engaged_UserStats.T.rename(columns={0:""}))
            print("\n###########################################")
            input()
        else:
            ()

    #lvl 1 = attack below 40, lvl 2 above 70, lvl 3 above 90
    room_generation()

#prints text based on finding loot
def loot_room():
    os.system("cls")
    print("###########################################")
    print("#          You've found a chest!          #")
    print("###########################################")
    input()
    #lvl proportionate to user lvl
    loot_varient = random.randint(1,101)
    if loot_varient <= 15:
        potion_loot()
    else:
        equipment_loot()
    room_generation()

#gives player the choice to use a found potion
def potion_loot():
    global AttackIncrease
    global DefenceIncrease
    global UserStats
    #opens potions csv, takes a random index from it and gives it to the user to make a choice
    potions = pd.read_csv("potions.csv")
    potion_choice = random.randint(0,len(potions)-1)
    Potion_DF = potions.iloc[potion_choice]
    flag = True
    while flag:
        #textual input and prints what potion and the stat boosts
        os.system("cls")
        print("###########################################")
        print("#         It contains a potion...         #")
        print("###########################################")
        print(Potion_DF.to_string())
        print("###########################################")
        print("#      Would you like to use it? Y/N      #")
        print("###########################################")
        choice = input()
        if choice.upper() == "Y":
            #if it is used, gets val of stat effect and its value increase, adds it to user stats
            stat_increase = Potion_DF.loc["Stat Effect"]
            effect_increase = Potion_DF.loc["Effect Increase"]
            if Potion_DF.loc["Stat Effect"] == "Attack":
                AttackIncrease += effect_increase
            if Potion_DF.loc["Stat Effect"] == "Defence":
                DefenceIncrease += effect_increase
            UserStats[stat_increase] += effect_increase
            prefaces(1)
            flag = False
        elif choice.upper() == "N":
            #if not used, breaks out of loop
            flag = False
        else:
            #handles invalid inputs
            flag = True

#picks equipment that is found
def equipment_loot():
    global UserStats
    global User
    #read csv to get user profession,equipment and makes equipment levels numerical to wokr with
    df = pd.read_csv("UserInfo.csv")
    user_data = df.loc[df['Username'] == User]
    profession = user_data.iloc[0]['Profession']
    equipment = pd.read_csv("equipments.csv")
    equipment["Level"] = pd.to_numeric(equipment["Level"])
    avaliable_equipment = equipment.loc[equipment["Level"] <= int(UserStats["Level"])] 
    avaliable_equipment = avaliable_equipment.loc[avaliable_equipment["Class"] == profession]
    #picks random equipment avaliable to user and selects it
    equipment_choice = random.randint(0, len(avaliable_equipment) - 1)
    Raw_Equipment_DF = avaliable_equipment.iloc[equipment_choice]
    #removes lvl and class from datafamrae
    Equipment_DF = Raw_Equipment_DF[:4] 
    #makes userstats a df
    UserStatsDF = pd.DataFrame(UserStats, index=[0])
    #copies userstats for an updateable version, only taking needed collumns
    Current_Equipment = UserStatsDF.iloc[:, [0, 1, 2, 3, 4, 5, 9, 11]]
    displayed_user_stats = UserStatsDF.iloc[:, [0, 1, 2, 3, 4, 5, 9, 11]]
    #copies displayed stats t oshow alongside new stats
    new_user_stats = displayed_user_stats.copy()
    equipment_item = Equipment_DF
    #assigns base def depending on proff.
    base_defence = 10 if profession == "Knight" else 0 if profession == "Magician" else 10
    #updates stat s based on each type of equipmet
    #if it is their first item, no subtraction from the defence as it will make def go into negative.
    #repeated for all defence adding equipment
    if equipment_item["Type"] == "Weapon":
        new_user_stats["Attack"] += (equipment_item["Attack"] + AttackIncrease - Current_Equipment["Attack"])
        new_user_stats["Weapon"] = equipment_item["Name"]
        Current_Equipment["Attack"] = equipment_item["Attack"]
        Current_Equipment["Weapon"] = equipment_item["Name"]
    elif equipment_item["Type"] == "Armor":
        new_user_stats["Defence"] += (equipment_item["Defense"] + DefenceIncrease - (Current_Equipment["Defence"] if pd.notna(Current_Equipment["Armor"].values[0]) else 0))
        new_user_stats["Armor"] = equipment_item["Name"]
        Current_Equipment["Armor"] = equipment_item["Name"]
    elif equipment_item["Type"] == "Boots":
        new_user_stats["Defence"] += (equipment_item["Defense"] + DefenceIncrease - (Current_Equipment["Defence"] if pd.notna(Current_Equipment["Boots"].values[0]) else 0))
        new_user_stats["Boots"] = equipment_item["Name"]
        Current_Equipment["Boots"] = equipment_item["Name"]
    elif equipment_item["Type"] == "Gloves":
        new_user_stats["Defence"] += (equipment_item["Defense"] + DefenceIncrease - (Current_Equipment["Defence"] if pd.notna(Current_Equipment["Gloves"].values[0]) else 0))
        new_user_stats["Gloves"] = equipment_item["Name"]
        Current_Equipment["Gloves"] = equipment_item["Name"]
    elif equipment_item["Type"] == "Shield":
        new_user_stats["Defence"] += (equipment_item["Defense"] + DefenceIncrease - (Current_Equipment["Defence"] if pd.notna(Current_Equipment["Shield"].values[0]) else 0))
        new_user_stats["Shield"] = equipment_item["Name"]
        Current_Equipment["Shield"] = equipment_item["Name"]
    else:
        new_user_stats["Defence"] += (equipment_item["Defense"] + DefenceIncrease - (Current_Equipment["Defence"] if pd.notna(Current_Equipment["Helmet"].values[0]) else 0))
        new_user_stats["Helmet"] = equipment_item["Name"]
        Current_Equipment["Helmet"] = equipment_item["Name"]
    #turns into a df
    new_user_stats = pd.DataFrame(new_user_stats, index=[0])
    #checks if there is just one value in one of the equipment slots as this means base def needs to be added
    equipment_columns = ["Helmet", "Armor", "Shield", "Gloves", "Boots"]
    non_none_count = new_user_stats[equipment_columns].notna().sum(axis=1).iloc[0]  
    #adds base def if it is not a weapon
    if non_none_count == 1:
        if equipment_item["Type"] != "Weapon":
            new_user_stats.loc[0, "Defence"] += base_defence
    #concat to display old stats vs new stats
    stat_comparison = pd.concat([displayed_user_stats, new_user_stats], axis=0, ignore_index=False)
    stat_comparison.index = ["Old Stats", "New Stats"]
    flag = True
    while flag:
        #visualisaiton
        os.system("cls")
        print("###########################################")
        print("#   It contains a piece of equipment...   #")
        print("###########################################")
        print(Equipment_DF.to_string())
        print("###########################################")
        print(stat_comparison.T)
        print("###########################################")
        print("#     Would you like to equip it? Y/N     #")
        print("###########################################")
        choice = input()

        if choice.upper() == "Y":
            #overwrites only the changed stats from UserStats
            for stat in ["Weapon", "Armor", "Boots", "Gloves", "Shield", "Helmet", "Attack", "Defence"]:
                if new_user_stats[stat].item() != UserStats[stat].item():
                    UserStats[stat] = new_user_stats[stat].item()
            #prints updated full stats
            prefaces(1)
            flag = False
        elif choice.upper() == "N":
            #breaks out of loop, changes no data
            flag = False
        else:
            #input validation
            flag = True

#picks mobs avaliavle to fight based on user lvl, and handles sfighting mechanics
def mob_choice():
    global UserStats
    monsters = pd.read_csv("monsters.csv")
    user_lvl = int(UserStats["Level"]) 
    monsters["Level"] = pd.to_numeric(monsters["Level"])
    #user lvl gives what mobs are avaliable t ofight
    if user_lvl in range(1,10):
        valid_mobs = monsters.loc[monsters["Level"] == 1]
        index = random.randint(0,len(valid_mobs)-1)
        mob = valid_mobs.iloc[index]
        return mob

    elif user_lvl in range(10,30):
        valid_mobs = monsters.loc[monsters["Level"].isin([1, 2])]
        index = random.randint(0,len(valid_mobs)-1)
        mob = valid_mobs.iloc[index]
        return mob

    #if user is lvl 30+, access to fight all mobs
    elif user_lvl in range(30,40):
        valid_mobs = monsters.loc[monsters["Level"].isin([1, 2, 3])]
        index = random.randint(0,len(valid_mobs)-1)
        mob = valid_mobs.iloc[index]
        return mob

    elif user_lvl in range (40,60):
        valid_mobs = monsters.loc[monsters["Level"].isin([2, 3])]
        index = random.randint(0,len(valid_mobs)-1)
        mob = valid_mobs.iloc[index]
        return mob

    else:
        valid_mobs = monsters.loc[monsters["Level"] == 3]
        index = random.randint(0,len(valid_mobs)-1)
        mob = valid_mobs.iloc[index]
        return mob

#testing

User = "test"
UserStats = {"Weapon":"Training Sword","Helmet":None,"Armor":None,"Shield":None,"Gloves":None, "Boots":None, "Level":100,
                "Experience":0, "Health":200, "Defence":10, "Mana":100, "Attack":10, "Magic Attack":0, "Room":0}
mob_room()

#equipment_loot()

#first_room()
#loadgame()
#saving()
#actual game

before_game()
if z == 2:
    prefaces(0)
    deeper()
else:
    prefaces(0)
    first_room()



#you have cleared room x!
#attack implementation
#beat mob, random equipment / potion item