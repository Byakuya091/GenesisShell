from click_shell import shell
import os
from datetime import datetime
import subprocess
from time import sleep


@shell(prompt='GenesisShell > ', intro="""
       
  ______                                           __             ______   __                  __  __ 
 /      \                                         |  \           /      \ |  \                |  \|  
|  $$$$$$\  ______   _______    ______    _______  \$$  _______ |  $$$$$$\| $$____    ______  | $$| $$
| $$ __\$$ /      \ |       \  /      \  /       \|  \ /       \| $$___\$$| $$    \  /      \ | $$| $$
| $$|    \|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$$| $$|  $$$$$$$ \$$    \ | $$$$$$$\|  $$$$$$\| $$| $$
| $$ \$$$$| $$    $$| $$  | $$| $$    $$ \$$    \ | $$ \$$    \  _\$$$$$$\| $$  | $$| $$    $$| $$| $$
| $$__| $$| $$$$$$$$| $$  | $$| $$$$$$$$ _\$$$$$$\| $$ _\$$$$$$\|  \__| $$| $$  | $$| $$$$$$$$| $$| $$
 \$$    $$ \$$     \| $$  | $$ \$$     \|       $$| $$|       $$ \$$    $$| $$  | $$ \$$     \| $$| $$
  \$$$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$ \$$$$$$$  \$$ \$$$$$$$   \$$$$$$  \$$   \$$  \$$$$$$$ \$$ \$$
                                                                                                                                                                                                          
       Welcome to GenesisShell v1.0!
Enter "help" for a list of all commands.
""")
def my_app():
    pass


@my_app.command()
def clear():
    os.system("cls")


@my_app.command()
def help():
    print("""
    Here is a list of all additional commands:

    help: show this list
    sine: display a sine representation ascii art
    cosine: display a cosine representation ascii art
    notes: create and edit a raw file
    """)


@my_app.command()
def sine():
    print("""
 1 -|         ,-'''-.
    |      ,-'       `-.           *Not so accurate scale*
    |    ,'             `.
    |  ,'                 `.
    | /                     
    |/                       
----+-------------------------\--------------------------
    |          __           __ \          __           /  __
    |          ||/2         ||  \        3||/2        /  2||
    |                            `.                 ,'
    |                              `.             ,'
    |                                `-.       ,-'
-1 -|                                   `-,,,-'


    """)


@my_app.command()
def cosine():
    print("""
                 | 1
              ,--|--.
           ,-'   |   `-.           *Not so accurate scale*
         ,'      |      `.
       ,'        |        `.
      /          |          
     /           |           \                           /
----+------------+------------\------------+------------/---
   __            |0         __ \          __           /  __
   ||            |          ||  \         ||          /  3||  
 - ---           |          ---  `.                 ,'   --- 
    2            |           2     `.             ,'      2
                 |                   `-.       ,-'
                 | -1                   `--,--'


    """)


@my_app.command()
def notes():
    file_name = input("Enter the file name: ")
    content = input("Write here: ")

    with open(file_name, "w") as f:
        f.write(content)


@my_app.command()
def notes_openr(): # opens an existing note on the GenesisShell directory, in read mode
    file_name = input("Which file do you want to open ? : ")

    with open(file_name, "r") as f:
        f_contents = f.read()
        print(f_contents)


@my_app.command()
def notes_openw(): # opens an existing note on the GenesisShell directory, in write mode
    file_name = input("Which file do you want to open ? : ")
    content = input("Write here: ")

    with open(file_name, "w") as f:
        f.write(content)



@my_app.command()
def time():
    print("Current computer datetime is: ", datetime.now())
    

@my_app.command()
def fetch():
    
    print("OS: ")
    print(subprocess.Popen(["powershell", "Get-WmiObject Win32_OperatingSystem"]))
    print("_-"*20)

    print("CPU: ")
    print(subprocess.Popen(["powershell", "Get-WmiObject Win32_Processor"]))
    print("_-"*20)

    print("DISK: ")
    print(subprocess.Popen(["powershell", "Get-WmiObject Win32_LogicalDisk"]))
    print("_-"*20)

    sleep(2)

    print("""
 

              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$  %:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /  $XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++ +/:-.


""")


if __name__ == "__main__":
    my_app()
