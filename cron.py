import os

cron="""
Enter 1 to List all the Jobs
Enter 2 to create Physical Volume
Enter 3 to display Physical Volume
Enter 4 to manage Volume Group

"""

def crontab():
    while True:
        os.system("clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("CronTab".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        x = input(cron)

        if x == '1':
            os.system("crontab -l")

        elif x == 'b':
            exit()

        else:
            print("Not Supported")
        input("Press enter to contiue....")