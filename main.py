from time import sleep
import os, subprocess
import container

if __name__ == "__main__":
    text = '''
    [1] run docker
    [2] run hadoop
    [q] quit
    Enter your option: '''
    docker = '''
    [1] create container
    [2] pull image
    [3] create volume
    [4] create network
    [5] check status
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
     
        toolOpt = input(text)

        if toolOpt == "q":
            print("exiting..")
            sleep(1)
            break
        elif toolOpt == "1":
            os.system("tput clear")
            subOpt = input(docker)
            if subOpt == "1":
                container.start_container()
            else: 
                continue
        else:
            continue

    os.system("tput clear")
