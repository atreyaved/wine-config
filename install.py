import os
import time
a=input("do you have the necessary drivers from https://github.com/lutris/docs/blob/master/InstallingDrivers.md ? (y/n)")

if (a=="y"):
        b=input("do you have wine installed? (y/n)")
        if (b=="y"):
                print("installing dxvk in the default wine prefix")
                print("this will open up a wine configuration window, make sure to close it after it opens")
                time.sleep(3)
                os.system("wget https://github.com/doitsujin/dxvk/releases/download/v1.10.3/dxvk-1.10.3.tar.gz")
                os.system("tar -xf dxvk-1.10.3.tar.gz")
                os.system("winecfg")
                os.chdir("dxvk-1.10.3/")
                os.system("./setup_dxvk.sh install")
                c=input("do you have winetricks installed? (y/n)")
                if(c=="y"):
                        print("installing essentials")
                        os.system("winetricks wmp10 xact quartz d3dx9_24 mfc42 dotnet20 dsound quicktime dxfullsetup vcrun2010")
                        print("you're done! run a game and make sure it works fine")
                if(c=="n"):
                        print("install winetricks using your distro specific instructions")
        if(b=="n"):
                print("install wine using your distro specific instructions")



if (a=="n"):
        print("install drivers from https://github.com/lutris/docs/blob/master/InstallingDrivers.md first")
