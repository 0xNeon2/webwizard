import subprocess

def recon():
    print("Enter Target website [ex: google.com ] :")
    domain = input("==> ")
    print("Searching for the details..........")
    try:
        output = subprocess.check_output(["whois", domain], universal_newlines=True, stderr=subprocess.STDOUT)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error running whois: {e.output}")
    except FileNotFoundError:
        print("The necessary tool is not found. Please make sure it is installed and in your system's PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")