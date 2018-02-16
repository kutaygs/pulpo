'''
Imports
'''
import sys
import argparse
import os
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep

'''
Common Functions
'''


class color:
    RED = '\033[91m'
    END = '\033[0m'


def clearScr():
    os.system('clear')


def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)


'''
Variables
'''

toolDir = "tools/"
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = ['yes', 'y', 'ye', 'Y']

pulpologo = color.END + """
              .______    __    __   __      .______     ______
              |   _  \  |  |  |  | |  |     |   _  \   /  __  |
              |  |_)  | |  |  |  | |  |     |  |_)  | |  |  |  |
              |   ___/  |  |  |  | |  |     |   ___/  |  |  |  |
              |  |      |  `--'  | |  `----.|  |      |  `--'  |
              | _|       \______/  |_______|| _|       \______/

"""
alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"


'''
Starts Menu Classes
'''


class pulpo:
    def __init__(self):
        clearScr()
        print (pulpologo + color.RED + '''
                     }-----{+} Made with LOVE by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
   }-----{+} Program python dilinde ingilizce ve Turkce yapilmistir. {+}-----{
    }-----{+} This program made with python in English and Turkish. {+}-----{


  ''' + color.END + '''
             {1}--Wireless Testing // Wi-Fi testleri
             {9}-Exit\n
             ''')
        choice = raw_input("pulpo~# ")
        clearScr()
        if choice == "1":
            wirelessTestingMenu()
        elif choice == "9":
            sys.exit()
        else:
            print("Incorrect entry // Hatali Giris")
            self.__init__()
        self.completed()

    def completed(self):
        print("Completed, click return to go back // Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()


'''
Wireless Testing Tools Classes
'''


class wirelessTestingMenu:
    def __init__(self):
        clearScr()
        print (pulpologo)
        print("   {1}--wifite")
        print("   {2}--fern")
        print("   {3}--kismet")
        print("   {4}--LazyScript")
        print("   {9}-Back To The Main Menu // Ana Menuye Git\n")
        choice4 = raw_input("pulpo~# ")
        clearScr()
        if choice4 == "1":
            wifite()
        elif choice4 == "2":
            fern()
        elif choice4 == "3":
            kismet()
        elif choice4 == "4":
            Lazy()
        elif choice4 == "9":
            pulpo()
        elif choice4 == "99":
                admin()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        print("Completed, click return to go back // Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()


        def fern():
            if yesOrNo():
                os.system("sudo python /usr/share/Fern-Wifi-Cracker/execute.py")

def Lazy():
    if yesOrNo():
        os.system("cd")
        os.system("git clone https://github.com/arismelachroinos/lscript.git")
        os.system("cd")
        os.system("cd lscript")
        os.system("chmod +x install.sh")
        os.system("./install.sh")
        os.system("")

def kismet():
    if yesOrNo():
        os.system("kismet")
        os.system("")


def wifite():
    if yesOrNo():
        os.system("wget https://raw.github.com/derv82/wifite/master/wifite.py")
        os.system("chmod +x wifite.py")
        os.system("./wifite.py")
        os.system("")


def admin():
    if yesOrNo():
            print (pulpologo + color.RED + '''

       }-----{+} Now you are on my Admin Panel {+}-----{


      '''


if __name__ == "__main__":
    try:
        pulpo()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
