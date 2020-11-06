from time import sleep
import os, subprocess
import container

if __name__ == "__main__":
    text = '''
    [1] run docker
    [2] run hadoop
    [b] back to main menu
    [q] quit
    Enter your option: '''
    sshIp = ""

    while True:
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Welcome to the menu".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        isSsh = input('do you want to do ssh? (yes/no)-no: ') or "no"

        isSsh.lower()

        if isSsh == "yes":
            sshIp = input('Enter the ssh IP or domain: ')
     
        toolOpt = input(text)

        if toolOpt == "q":
            print("exiting..")
            sleep(1)
            break
        elif toolOpt == "b":
            continue 
        else:
            continue

    os.system("tput clear")
