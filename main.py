#!/usr/bin/python3
from time import sleep
import os, subprocess
import container
import webserver

if __name__ == "__main__":
    text = '''
    Press 1 to run docker
    Press 2 to run hadoop
    Press 3 to configure webserver
    Press q to quit the Program
    Enter your option: '''

    sshIp = ""
    isSsh = input('do you want to do ssh? (yes/no)-no: ') or "no"
    isSsh.lower()

    while True:
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Welcome to the menu".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        if isSsh == "yes":
            sshIp = input('Enter the ssh IP or domain: ')
            sshIp = f"ssh {sshIp} "
     
        toolOpt = input(text)

        if toolOpt == "q":
            print("exiting..")
            sleep(1)
            break
        elif toolOpt == "1":
            container.dockerMenu(sshIp)
        elif toolOpt == "3":
            webserver.webServer(sshIp)
        else:
            continue

    os.system("tput clear")
