import socket

def dcon():
    print("Enter Target website [www.domain_name] :")
    domain = input("==> ")

    try:
        ip_address = socket.gethostbyname(domain)
        print("===========================================")
        print(f"The IP address of {domain} is {ip_address}")
        print("===========================================")
    except socket.gaierror:
        print("Could not resolve the domain.")
