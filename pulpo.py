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

fsocietylogo = color.END + """
              .______    __    __   __      .______     ______   
              |   _  \  |  |  |  | |  |     |   _  \   /  __  \  
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


class fsociety:
    def __init__(self):
        clearScr()
        print (fsocietylogo + color.RED + """
                }-----{+} With LOVE by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
   }-----{+} Program python dilinde ingilizce ve Turkce yapilmistir. {+}-----{
    }-----{+} This program made with python in English and Turkish. {+}-----{


    """ + color.END + """
       {1}--Wireless Testing // Wi-Fi testleri
       {9}-Exit\n
     """)
        choice = raw_input("fsociety~# ")
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
        print(fsocietylogo)
        print("   {1}--reaver // reaver")
        print("   {2}--pixiewps // pixiewps")
        print("   {3}--Bluetooth Honeypot GUI Framework // Bluetooth Honeypot GUI Framework\n")
        print("   {99}-Back To The Main Menu // Ana Menuye Git\n")
        choice4 = raw_input("fsociety~# ")
        clearScr()
        if choice4 == "1":
            reaver()
        elif choice4 == "2":
            pixiewps()
        elif choice4 == "3":
            bluepot()
        elif choice4 == "99":
            fsociety()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        print("Completed, click return to go back // Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()


def reaver():
    if yesOrNo():
        os.system(
            "apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone --depth=1 https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ & ./configure")
        os.system("cd reaver-wps-fork-t6x/src/ & make")


def pixiewps():
    if yesOrNo():
        os.system("git clone --depth=1 https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps & make ")
        os.system("sudo make install")


def bluepot():
    print("You need to have at least 1 bluetooh receiver // En az 1 bluetooth aliciniz olmasi gerekmekte")
    if yesOrNo():
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")







def reaver():
    print """
      Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup
      WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a
      wide variety of access points and WPS implementations
      1 to accept / 0 to decline
        """
    if yesOrNo():
        os.system(
            "apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone --depth=1 https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ & ./configure")
os.system("cd reaver-wps-fork-t6x/src/ & make")








def pixiewps():
    print"""Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some Access Points, the so-called "pixie dust attack" discovered by Dominique Bongard in summer 2014. It is meant for educational purposes only
    """
    if yesOrNo():
        os.system("git clone --depth=1 https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps & make ")
os.system("sudo make install")





def bluepot():
    print("you need to have at least 1 bluetooh receiver (if you have many it will work wiht those, too). You must install / libbluetooth-dev on Ubuntu / bluez-libs-devel on Fedora/bluez-devel on openSUSE ")
    if yesOrNo():
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")







if __name__ == "__main__":
    try:
        fsociety()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
