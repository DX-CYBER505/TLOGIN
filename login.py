import os
import os.path
from getpass import getpass
os.system("clear")
def function():
    pass
    print("")
    os.system("clear")
    print("\033[91m    _________________________________________\033[0m")
    print("\033[92m")
    print("     ██╗      ██████╗  ██████╗ ██╗███╗   ██╗")
    print("     ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")
    print("     ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")
    print("     ██║     ██║   ██║██║   ██║██║██║╚██╗██║")
    print("     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")
    print("     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝")
    print("\033[91m    _________________________________________\033[0m")
    print("")
function()
while(1):
		try:
			f=open("/data/data/com.termux/files/usr/lib/user.txt","r")
			username=f.readline()
			username=username.strip()
			password=f.readline()
			password=password.strip()
			f.close()
			usr=input("\033[92mEnter username -: \033[0m")
			print("")
			pas=getpass("\033[92mEnter password -: \033[0m")
			if usr==username:
				if pas==password:
					os.system("clear")
					print("\033[1;92m                 Access Granted\033[0m")
					print("\033[96m          <------------------------>")
					print("\033[1;91m                  welcome \033[0m" +usr+ "" )
					print("")
					break
				else :
					print("")
					print("")
					print("")
					print("")
					print("\033[1;91m Access Denied\033[0m")
					print("")
					print("")
					print("")
					print("")
			else:
				print("")
				print("")
				print("")
				print("")
				print("")
				print("\033[91m Incorrect username\033[0m")
				print("")
				print("")
				print("")
				print("")
		except Exception:
			print("")
			print("")
			print("")
			print("")
			print("\033[91m Try again\033[0m")
			print("")
			print("")
			print("")
			print("")
		except KeyboardInterrupt:
			print("")
			print("")
			print("")
			print("\033[96mExit.......\033[0m")
			os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
			print("")
			print("")
			print("")