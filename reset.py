import os
import time
from getpass import getpass
os.system('clear')
def banner():
	print("\033[91m   ____________________________________\033[0m")
	print("")
	print("\033[92m     Reset your username & password \033[0m")
	print("\033[91m   ____________________________________\033[0m")
	print("")
	print("")
banner()
user=str(input("\033[96mEnter Your new Username :- \033[0m"))
print("")
password=getpass("\033[96mEnter Your new Password :- \033[0m")
f=open("/data/data/com.termux/files/usr/lib/user.txt","w")
f.write(f"{user}\n")
f.write(password)
f.close()
print("")
print("")
print("\033[1;34m[\033[1;92m+\033[1;34m]creating...........")
time.sleep(1)
print("")
print("\033[1;34m[\033[1;92m+\033[1;34m]\033[1;91mReset Successfully.......\033[0m")
def backup():
    print("")
    print("\033[1;34m[\033[1;92m+\033[1;34m]\033[1;34mUpdating backup.....\033[0m")
    print("")
    os.system('cp /data/data/com.termux/files/usr/lib/user.txt /sdcard')
    time.sleep(1)
    print("\033[1;34m[\033[1;92m+\033[1;34m]\033[1;96mBackup updated......\033[0m")
backup()