import sys,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,requests 
import os
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 
_________________________________________________________
________________________##########_______________________
_______________________#############_____________________
______________________##############_____________________
_____________________#######______###____________________
_____________________######________##__##________________
_____________________######____________###_______________
_____________________#####_____________######____________
_____________________#####____________#######____________
_____________________#####___________#######_____________
_____________________#####____________######_____________
_____________________#####_____________######____________
_____________________######____________###_##____________
______________________######_______#___##________________
______________________#######____###_____________________
_______________________############______________________
________________________##########_______________________
__________________________######_________________________
@@@@@@  GECE' ve Wanders Tarafindan Kodlanmistir @@@@@@@@
______________ TurkHackTeam Saldiri Timleri _____________

                                                                                                                                                                                                                                                                                      
 1) GECE OtoExploit                     2) Zone-h Grabber  
             	  		  
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)


logo()


choice=raw_input('Sayi sec isinlan => ')
if choice=='1':
  print("""\n\033[91m Files/Tool1 klasorune gec ve list.txt olustur. Sonrasinda e tikla.

 e = evet 
 h = hayir\033[0m""")
  t=raw_input('~>')
  if t=='e':
   if system() == 'Linux':
    os.system("cd Files/Tool1 && chmod +x gece1.py && python gece1.py")
   if system() == 'Windows':
    os.system('cd Files/Tool1 && python gece1.py && list.txt')
   else:
    print('unknown error :| ')
  elif t=='h':
   main()
  else :
   print('unknown error :| ')

elif choice == '2':
    print("""\n\033[91m 
 e = evet 
 h = hayir\033[0m""")
    t = raw_input('~>')
    if t == 'e':
        if system() == 'Linux':
            os.system("cd Files/Tool15 && chmod +x zone.py && python zone.py")
        if system() == 'Windows':
            os.system('cd Files/Tool15 && python zone.py')
        else:
            print('unknown error :| ')
    elif t == 'h':
        main()
    else:
        print('unknown error :| ')   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
