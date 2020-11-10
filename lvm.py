import os

lvm_part="""
Enter 1 to check storage devices is attached to the OS
Enter 2 to create Physical Volume
Enter 3 to display Physical Volume
Enter 4 to manage Volume Group
Enter 5 to display Volume Groups
Enter 6 to manage Logical Volume
Enter 7 to display Logical Volumes
Enter b to go back to main menu
"""

def lvm():
    while True:
        os.system("clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Logical Volume Management".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        x = input(lvm_part)

        if x == '1':
            os.system("fdisk -l")

        elif x == '2':
            while True:
                pv1 = input("Enter the name of storage: ")
                os.system(f"pvcreate {pv1}")
                another = input("Do you want to create another LV [Y/N]: ").upper()
                if another == 'Y':
                    pass
                else:
                    exit()

        elif x == '3':
            pv = input("Enter the name of storage: ")
            os.system(f"pvdisplay {pv}")

        elif x == '4':
            print("""
            Enter 1 to create new Volume Group
            Enter 2 extend Volume Group
            """)
            vg = int(input())
            if vg == 1:
                vgn = input("Give name to the VG: ")
                pvn = input("Enter the name of PV: ")
                os.system(f"vgcreate {vgn} {pvn}")

            elif vg == 2:
                vgn = input("Enter the name of existing VG: ")
                pvn = input("Enter the name of the PV: ")
                os.system(f"vgextend {vgn} {pvn}")

        elif x == '5':
            vgn = input("Enter the name of VG: ")
            os.system(f"vgdisplay {vgn}")

        elif x == '6':
            print("""
            Enter 1 to create new Logical Volume
            Enter 2 extend Logical Volume
            Enter 3 to format the Logical Volume
            Enter 4 to mount the Logical Volume
            """)
            lv = int(input())

            if lv == 1:
                size = input("Enter size for your LV: ")
                lvn = input("Give name to your LV: ")
                vgn = input("Enter name of the VG: ")
                os.system(f"lvcreate --size {size} --name{lvn} {vgn}")

            elif lv == 2:
                lvn = input("Give name to your LV: ")
                vgn = input("Enter name of the VG: ")
                os.system(f"lvextend --size {size} /dev/{vgn}/{lvn}")

            elif lv == 3:
                vgn = input("Enter the name of VG:")
                lvn = input("Enter the name of LV:")
                os.system(f"mkfs.ext4  /dev/{vgn}/{lvn}")
                print("Partiton formatted....\n")
                mout = input("Do you want to mount LV [Y/N]: ").upper()

                if mout == "Y":
                    path = input("Enter path of folder where you want to mount : ")
                    print("Creating directory")
                    os.system(f'mkdir {path}')
                    print("\nMounting Now ....\n")
                    mntout = os.system(f"mount /dev/{vgn}/{lvn} {path}")
                else:
                    exit()

        elif x == '7':
            os.system("lvdisplay")

        elif x == 'b':
            exit()

        else:
            print("Not Supported")
        input("Press enter to contiue....")