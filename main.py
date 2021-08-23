#!/usr/bin/python3
from time import sleep
import os
import subprocess
import container
import awsmenu
import hadoop
import webserver
import yum_config
import partition_2
import lvm
import cron

if __name__ == "__main__":
    text = '''
    Press 1 for Docker
    Press 2 for AWS commands
    Press 3 for Hadoop complete configurations
    Press 4 for configure webserver
    Press 5 for configure yum repos
    Press 6 for Partitions
    Press 7 for Logical volume Management
    Press 8 for Crontab
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
        elif toolOpt == "6":
            partition_2.part()
        elif toolOpt == "7":
            lvm.lvm()
        elif toolOpt == "8":
            cron.crontab()
        else:
            continue

    os.system("tput clear")
