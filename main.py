#!/usr/bin/python3
from time import sleep
import os, subprocess
import container

if __name__ == "__main__":
    text = '''
    [1] run docker
    [2] run hadoop
    [q] quit
    Enter your option: '''
# TODO: options from 5
    docker = '''
    [1] create container
    [2] pull image
    [3] list running contianers
    [4] list images
    [5] start container
    [6] stop container
    [7] terminate or delete contianer
    [8] search for images
    [b] back to main menu
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
            sshIp = f"ssh {sshIp} "
     
        toolOpt = input(text)

        if toolOpt == "q":
            print("exiting..")
            sleep(1)
            break
        elif toolOpt == "1":
            os.system("tput clear")
            subOpt = input(docker)
            out=""
            os.system("tput reset")
            if subOpt == "1":
                out=container.startContainer(sshIp)
            elif subOpt == "2":
                out=container.pullImg(sshIp)
            elif subOpt == "3":
                out=container.status("container", sshIp)
            elif subOpt == "4":
                out=container.status("image", sshIp)
            else: 
                continue
            print(out)
            input("press any key to exit")
        else:
            continue

    os.system("tput clear")
