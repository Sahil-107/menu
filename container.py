#!/usr/bin/python3
'''
This is the file which allows contianer operations for the menu app
'''

# imports for menu
import os, subprocess

# imgname -> image name (required)
'''
command to be run ->
docker run -dit --name _cname_ --net {_netname_ || brigde} 
        -v _volname_:_volmount_ _imgname_:_imgv_
'''
def startContainer(sshIp=""):
    os.system("tput clear")
    imgname = input("enter docker image name (*req): ")
    imgv = input("enter docker image version (latest): ") or "latest"
    cname = input("enter docker container name (random): ") or None
    volname = input("enter docker volume name (none): ") or None
    volpath = input("enter docker volume path (none): ") or None
    netname = input("enter docker net name[brigde/host/null] (bridge):") or "bridge"

    volmnt = ""

    if (cname):
        cname = f"--name {cname}"
    else:
        cname = ""
    if (volname and volpath):
        volmnt = f"-v {volname}:{volpath}"
    
    return subprocess.getoutput(f'{sshIp} sudo podman run -dit --net {netname} {volmnt} {cname} {imgname}:{imgv}')

def pullImg(sshIp=""): 
    imgname = input("enter docker image name (*req): ")
    imgv = input("enter docker image version (latest): ") or "latest"
    
    return subprocess.getoutput(f'{sshIp} sudo podman pull {imgname}:{imgv}')


def status(resourceType, sshIp=""):
    return subprocess.getoutput(f'{sshIp} sudo podman {resourceType} ls')

if __name__ == '__main__':
    print("this code is not meant to be run.\nThis is a module")

