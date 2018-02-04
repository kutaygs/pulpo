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
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


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
              |   _  \  |  |  |  | |  |     |   _  \   /  __  \  
              |  |_)  | |  |  |  | |  |     |  |_)  | |  |  |  | 
              |   ___/  |  |  |  | |  |     |   ___/  |  |  |  | 
              |  |      |  `--'  | |  `----.|  |      |  `--'                   | 
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
        print (pulpologo + color.RED + """
                     }-----{+} CODED by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
   }-----{+} Program python dilinde ingilizce ve Turkce yapilmistir. {+}-----{
    }-----{+} This program made with python in English and Turkish. {+}-----{

   
     
             {1}--Wireless Testing // Wi-Fi testleri
             {9}-Exit\n
             """)
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
        print("   {1}--pixiewps")
        print("   {2}--program")
        print("   {3}--program")
        print("   {9}-Back To The Main Menu // Ana Menuye Git\n")
        choice4 = raw_input("pulpo~# ")
        clearScr()
        if choice4 == "1":
            pixiewps()
        elif choice4 == "2":
            pixiewps()
        elif choice4 == "3":
            pixiewps()
        elif choice4 == "9":
            pulpo()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        print("Completed, click return to go back // Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()



def pixiewps():
    if yesOrNo():
        os.system("git clone  https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps & make ")
        os.system("sudo make install")



if __name__ == "__main__":
    try:
        pulpo()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
