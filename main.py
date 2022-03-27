#    ____            _                         
#   |  _ \ __ _  ___| | ____ _  __ _  ___  ___ 
#   | |_) / _` |/ __| |/ / _` |/ _` |/ _ \/ __|
#   |  __/ (_| | (__|   < (_| | (_| |  __/\__ \
#   |_|   \__,_|\___|_|\_\__,_|\__, |\___||___/
#                              |___/           

from replit import clear as cls
from termcolor import cprint
import random, cursor
from getkey import getkey
from switch import Switch as ss

#     ____             __ _                       _   _             
#    / ___|___  _ __  / _(_) __ _ _   _ _ __ __ _| |_(_) ___  _ __  
#   | |   / _ \| '_ \| |_| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
#   | |__| (_) | | | |  _| | (_| | |_| | | | (_| | |_| | (_) | | | |
#    \____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                           |___/                                   

cursor.hide()
prefix = "." # command prefix

#    ____            _                 _   _                 
#   |  _ \  ___  ___| | __ _ _ __ __ _| |_(_) ___  _ __  ___ 
#   | | | |/ _ \/ __| |/ _` | '__/ _` | __| |/ _ \| '_ \/ __|
#   | |_| |  __/ (__| | (_| | | | (_| | |_| | (_) | | | \__ \
#   |____/ \___|\___|_|\__,_|_|  \__,_|\__|_|\___/|_| |_|___/
#                                                            

name = "Chat Test"
veraw = 7 # raw variable for the version; 
version = "Build Version " + str(float(veraw))
vwarn = f"(as of {version})"
maintenance = False # restricts chat (DEPRECATED)
debug = False # shows extra info
talking = "u1"

#    _____                 _   _                 
#   |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
#   | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#   |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
#   |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                                                

def brk(): # standalone line break
  print("")

def ctag(args,c): # appends a unique tag to text with matching properties
  cprint(str.upper(args),"white","on_" + c)

def msg(name,tag,color,text): # sends a message with special parameters
  cprint(name,color,attrs = ["bold"],end = " ")
  ctag(tag,color)
  print(text + "\n")

def dmsg(args): # sends a vibrant message when debug is enabled
  if debug and not maintenance:
    cprint(args,"magenta",end = " ")
    ctag("dmsg","magenta")
    print("")

def rpline(): # gets rid of previous line
  print("\033[A                             \033[A")

def ujoin(user): # adds a user to a specific location
  ran = random.randint(1,5)
  with ss(ran) as case:
    if case(1):
      lms = "Are you rrready to rrrumble?!?!"
    if case(2):
      lms = "You're finally here."
    if case(3):
      lms = "How 'ya doin'?"
    if case(4):
      lms = "...You should probably say something now."
    if case(5):
      lms = "By any chance, do you happen to know who Joe is?"
    if case(6):
      lms = "Allow me to introduce yourself. Wait a minute..."
  msg("Welcomer","bot","green",f"Welcome, {user}! {lms}")

def clog(change,category): # adds an item to the changelog
  print(change,end = " ")
  ctag(category,"yellow")

def cserver(name,desc): # creates a server
  cprint("          " + name + "          \n","white", attrs = ["bold","underline"])
  cprint(f"Description: {desc}\nMembers: Default\n","white", attrs = ["bold","dark"])

def cmdl(cmd,args,prp): # logs a command and what it does
  cprint(prefix + cmd,"red",end = " ")
  cprint(args,"green",end = " ")
  print("-",end = " ")
  cprint(prp,"cyan")

def ctitle(txt): # creates a bold title
  cprint(txt,"white",attrs = ["reverse"])

#    _____ _ _   _      
#   |_   _(_) |_| | ___ 
#     | | | | __| |/ _ \
#     | | | | |_| |  __/
#     |_| |_|\__|_|\___|
#                       

ctitle(name)
print(version + "\n")

#    __  __                  
#   |  \/  | ___ _ __  _   _ 
#   | |\/| |/ _ \ '_ \| | | |
#   | |  | |  __/ | | | |_| |
#   |_|  |_|\___|_| |_|\__,_|
#                            

print("Select an option from below to get started.\n")

print("1 - Start the program")
print("2 - View changelog")
print("3 - Start the program in debug mode")
print("4 - View statistics")
print("5 - View commands")

brk()

print("Awaiting input...")

mselection = getkey()

#     ____ _                            _             
#    / ___| |__   __ _ _ __   __ _  ___| | ___   __ _ 
#   | |   | '_ \ / _` | '_ \ / _` |/ _ \ |/ _ \ / _` |
#   | |___| | | | (_| | | | | (_| |  __/ | (_) | (_| |
#    \____|_| |_|\__,_|_| |_|\__, |\___|_|\___/ \__, |
#                            |___/              |___/ 

if mselection == "2" or mselection == "3":
  cls()
  if mselection == "3":
    debug = True
  ctitle(name + " Changelog")
  print(vwarn)

  dmsg("Debug mode is enabled!")
  
  clog("Added a rock-paper-scissors command. Check the commands list!","feature")
  clog("Fixed some crashes; more crash fixes to come, too","patch")

  input("\nEnter anything to continue\n")

#    ____  _        _   _     _   _          
#   / ___|| |_ __ _| |_(_)___| |_(_) ___ ___ 
#   \___ \| __/ _` | __| / __| __| |/ __/ __|
#    ___) | || (_| | |_| \__ \ |_| | (__\__ \
#   |____/ \__\__,_|\__|_|___/\__|_|\___|___/
#                                            

elif mselection == "4":
  cls()
  print(name + " Miscellaneous Stats")
  print(vwarn)
  
  print(f"name: {str(name)}")
  print("veraw:" + str(veraw))
  print("version:" + str(version))
  print("debug:" + str(debug))
  print("talking:" + str(talking))
  print("prefix:" + str(prefix))

  input("\nEnter anything to continue\n")

#     ____                                          _     
#    / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
#   | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
#   | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#    \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
#                                                         

elif mselection == "5":
  cls()
  ctitle(name + " Command List")
  print(vwarn)

  print("NOTE: You can send a period to switch users.\n")

  cmdl("nick","(new nickname)","Changes your chat nickname")
  cmdl("flip","(no arguments)","Flips a coin")
  cmdl("roll","(min) (max)","Rolls a random number between MIN and MAX")
  cmdl("ver","(no arguments)","Returns the current " + name + " build version")
  cmdl("rps","(object)","Play rock-paper-scissors with a bot")

  input("\nEnter anything to continue\n")

#    ____       _               
#   / ___|  ___| |_ _   _ _ __  
#   \___ \ / _ \ __| | | | '_ \ 
#    ___) |  __/ |_| |_| | |_) |
#   |____/ \___|\__|\__,_| .__/ 
#                        |_|    

cls()

ctitle("Room Creation Menu\n")
room = input("ROOM NAME: ")
desc = input("ROOM DESCRIPTION: ")

cls()

ctitle("Add Visitors Menu\n")
u1 = input("USER 1 NAME: ")
u1 = u1.replace(" ","")
u2 = input("USER 2 NAME: ")
u2 = u2.replace(" ","")
cls()

cserver(room,desc)

ujoin(u1)
ujoin(u2)

#     ____ _           _                             
#    / ___| |__   __ _| |_ _ __ ___   ___  _ __ ___  
#   | |   | '_ \ / _` | __| '__/ _ \ / _ \| '_ ` _ \ 
#   | |___| | | | (_| | |_| | | (_) | (_) | | | | | |
#    \____|_| |_|\__,_|\__|_|  \___/ \___/|_| |_| |_|
#                                                    

while True:
  if talking == "u1":
    u1m = input("> ")
    rpline()
  elif talking == "u2":
    u2m = input("> ")
    rpline()
  if maintenance:
    cprint(f"The application is currently undergoing maintenance ({name} {version})","red")
  else:
    pass
  
  # commands
  cmd = globals()[talking + "m"]

  # anti-log
  if not cmd == "." and not cmd.startswith(prefix + "nick") and not maintenance:
    msg(globals()[talking],"user","cyan",globals()[talking + "m"])

  if cmd.startswith(prefix + "nick"):
    new = globals()[talking + "m"].split(" ")
    old = globals()[talking]
    globals()[talking] = new[1]
    msg("System","bot","red",old + ' changed their nickname to "' + globals()[talking] + '"')
  
  if cmd == prefix:
    if talking == "u1":
      talking = "u2"
      dmsg("Talking set to User2")
    elif talking == "u2":
      talking = "u1"
      dmsg("Talking set to User1")
  
  if cmd.startswith(prefix + "roll"):
    r1 = globals()[talking + "m"].split(" ")
    msg("System","bot","red","You rolled " + str(random.randint(int(r1[1]),int(r1[2]))) + "!")
  
  if cmd == prefix + "flip":
    coinstring = ""
    rng = random.randint(1,3)
    if rng == 1:
      coinstring = "Whoa! You flipped heads. Swick!"
    elif rng == 2:
      coinstring = "Damn it! You flipped tails. Maybe next time..."
    elif rng == 3:
      coinstring = "...What?! You managed to land it on its side..."
    msg("System","bot","red",coinstring)

  if cmd == prefix + "ver":
    msg("Updater","bot","blue",f"You are currently running {version}.")

  if cmd.startswith(prefix + "rps"):
    obj = globals()[talking + "m"].split(" ")
    robj = random.randint(1,3)
    rvar = "placeholder"
    if robj == 1:
      rvar = "rock"
    elif robj == 2:
      rvar = "paper"
    elif robj == 3:
      rvar = "scissors"
    rmsg = f"I choose {rvar}...!"
    if "rock".lower() in obj[1].lower() or "paper".lower() in obj[1].lower() or "scissors".lower() in obj[1].lower():
      msg("RPS","bot","yellow",rmsg)
    else:
      msg("RPS","bot","yellow","Uh, I don't recognize that object...")