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
# TODO: options from 9
    docker = '''
    [1] create container
    [2] pull image
    [3] list running contianers
    [4] list all containers
    [5] list images
    [6] start container
    [7] stop container
    [8] terminate or delete contianer
    [9] execute commands in the container
    [10] copy file from container to host
    [11] copy file from host to container
    [12] search for images
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
                out=container.operate("container", "ls", sshIp)
            elif subOpt == "4":
                out=container.operate("container", "ls -a", sshIp)
            elif subOpt == "5":
                out=container.operate("image", "ls", sshIp)
            elif subOpt == "6":
                cnameId = input("Enter container name or id: ")
                out=container.operate("container", "start", cnameId, sshIp)
            elif subOpt == "7":
                cnameId = input("Enter container name or id: ")
                out=container.operate("container", "stop", cnameId, sshIp)
            elif subOpt == "8":
                cnameId = input("Enter container name or id: ")
                out=container.operate("container", "rm -f", cnameId, sshIp)
            elif subOpt == "9":
                cnameId = input("Enter container name or id: ")
                cmd = input("Enter the command you want to run: ")
                cnameId = f"{cnameId} {cmd}"
                out=container.operate("container", "exec -it", cnameId, sshIp)
            else: 
                continue
            print(out)
            input("press any key to go back to menu")
        else:
            continue

    os.system("tput clear")
