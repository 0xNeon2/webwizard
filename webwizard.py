import os
import sys
import platform
import subprocess
import time
from package.dork import read
from package.sub_package import spider
from package.do2ip import dcon
from package.Recon import recon
from package.dns import dns_check
from package.clickjack import clickjacking
from package.xss import xss
from package.sqli import sql

banner=("""
█████   ███   █████ ██████████ ███████████  █████   ███   █████ █████ ███████████   █████████   ███████████   ██████████  
░░███   ░███  ░░███ ░░███░░░░░█░░███░░░░░███░░███   ░███  ░░███ ░░███ ░█░░░░░░███   ███░░░░░███ ░░███░░░░░███ ░░███░░░░███ 
 ░███   ░███   ░███  ░███  █ ░  ░███    ░███ ░███   ░███   ░███  ░███ ░     ███░   ░███    ░███  ░███    ░███  ░███   ░░███
 ░███   ░███   ░███  ░██████    ░██████████  ░███   ░███   ░███  ░███      ███     ░███████████  ░██████████   ░███    ░███
 ░░███  █████  ███   ░███░░█    ░███░░░░░███ ░░███  █████  ███   ░███     ███      ░███░░░░░███  ░███░░░░░███  ░███    ░███
  ░░░█████░█████░    ░███ ░   █ ░███    ░███  ░░░█████░█████░    ░███   ████     █ ░███    ░███  ░███    ░███  ░███    ███ 
    ░░███ ░░███      ██████████ ███████████     ░░███ ░░███      █████ ███████████ █████   █████ █████   █████ ██████████  
     ░░░   ░░░      ░░░░░░░░░░ ░░░░░░░░░░░       ░░░   ░░░      ░░░░░ ░░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░   
                                                                                                                project_N"""
)

for col in banner:
        print(col, end="")
        sys.stdout.flush()
        time.sleep(0.0025)

def os_info():
    uname_info = platform.uname()
    print("||------------------------------------------||")
    print("|| System Name: ", uname_info.system)
    print("|| Release: ", uname_info.release)
    print("|| Machine: ", uname_info.machine)
    print("||------------------------------------------||")

def main_check():
    os_info()

def root_check():
    return os.geteuid() == 0

def target_search():
    print("---------------------------------------------------------------- ")
    print("##-- Copy your desired dork and paste it on the Spider --##")
    print("---------------------------------------------------------------- ")
    read.dorkshow() 
    print("---------------------------------------------------------------- ")
    spider.spider()

def Domain_to_ip():
    dcon()  

def Recon():
    recon()  

def dns_t():
    dns_check()

def click():
    clickjacking()

def check_xss():
    xss()

def Sqli_check():
    sql()

def Exit():
    print("Exiting the program.")
    sys.exit()

def menu_and_crawler():
    print("---------------------------------------------------------------- ")
    print("##-- Copy your desired dork and paste it on the Spider --##")
    print("---------------------------------------------------------------- ")
    read.dorkshow()
    print("---------------------------------------------------------------- ")
    spider.spider()  
    show_menu()

# dictionary of choice
menu_options = {
    '1': menu_and_crawler,
    '2': Domain_to_ip,
    '3': Recon,
    '4': dns_check,
    '5': click,
    '6': check_xss,
    '7': Sqli_check,
    '8': Exit,
}

# menu of fucntions
def show_menu():
    while True:
        print("Select an option:")
        print("1. Web Scraper")
        print("2. Domain to IP")
        print("3. Recon")
        print("4. Dns Enumeration")
        print("5. Clickjaking Test")
        print("6. XSS test")
        print("7. SQLi test")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '8':
            Exit()
        elif choice in menu_options:
            function = menu_options[choice]
            function()
        else:
            print("Invalid choice. Please try again.")

def main():
    if root_check():
        print("\n|| Root permission is enabled---------------||")
        main_check()
        command = "./check_tools.sh"
        subprocess.run(command,check = True , shell= True)
        print("||------------------------------------------||")
        print("||-------Explore the world of hacking-------||")
        print("||------------------------------------------||")
        show_menu()
    else:
        print("\n## You must have root permission to run this program")
        sys.exit(1)

if __name__ == "__main__":
    main()
