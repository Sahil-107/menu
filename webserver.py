import os

webserverval = '''
Press 1 to install HTTPD
Press 2 to start Webserver
Press 2 to start Webserver
Press b to go back to main menu
enter your choice: '''

def webServer(sshIp):
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Docker Operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        print('''
        Press 1 to install HTTPD
        Press 2 to start Webserver
        Press 3 to restart Webserver
        Press b to go back to main menu
        enter your choice: ''')
        x = input(webserverval)

        if x == "1":
            os.system("{sshIp} dnf install httpd")
        elif x == "2":
            os.system("{sshIp} systemctl enable --now httpd")
            print("Web server started")
        elif x == "3":
            os.system("{sshIp} systemctl restart httpd")
            print("Web server restarted")
        elif x == "b":
            return
