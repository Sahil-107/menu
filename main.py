#!/usr/bin/python3
from time import sleep
import os
import subprocess
import container
import awsmenu
import hadoop
import webserver
import yum_config

if __name__ == "__main__":
    text = '''
    Press 1 to run docker
    Press 2 to run AWS commands
    Press 3 to Hadoop complete configurations
    Press 4 to configure webserver
    Press 5 to configure yum repos
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
        elif toolOpt == "2":
            awsmenu.aws()
        elif toolOpt == "3":
            hadoop.hadoop()
        elif toolOpt == "4":
            webserver.webServer(sshIp)
        elif toolOpt == "5":
            yum_config.yum()
        else:
            continue

    os.system("tput clear")
