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
def start_container(imgname, imgv=None, cname=None, volname=None, netname=None, volpath=None):
    volmnt = ""
    netname = netname or "bridge"
    imgv = imgv or "latest"
    if (cname):
        cname = f"--name {cname}"
    else:
        cname = ""
    if (volname and volpath):
        volmnt = f"-v {volname}:{volpath}"
    
    return f'sudo docker run -dit --net {netname} {volmnt} {cname} {imgname}:{imgv}'

if __name__ == '__main__':
    print("this code is not meant to be run.\nThis code will be imported")
