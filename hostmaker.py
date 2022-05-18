import os
import shutil
import time as t

t.sleep(2)
os.system("clear")
with open(".env", "r") as f:
    data = f.read()
print("Hostmaker by " + str(data))
servername = input("Server Name >> ")
ip = input("Your Server ip >> ")
print("\n")
print("Input Type File\nExample: exe, run, com, net, txt")
type_file = input("Type file >> ")

file = str(servername) + "." + str(type_file)

with open(file, "w") as x:
    x.write(str(ip) + " growtopia1.com\n" + str(ip) + " growtopia2.com")
    print(str(file) + " successfully created !")