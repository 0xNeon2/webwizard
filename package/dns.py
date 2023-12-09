import subprocess

def dns_check():
    print("Enter Target website [ex: google.com ] :")
    domain = input("==> ")
    print("\n")
    print("===>> Wait ......this process may take some time ......")
    print("========================================================")
    print("\n")
    process = None
    try:
        # Start the dnsenum process and capture the output in real-time
        process = subprocess.Popen(["dnsenum", domain, "-noreverse"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Continuously read and print the output while the process is running
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
    except KeyboardInterrupt:
        if process:
            process.terminate()  # Terminate the dnsenum process on Ctrl+C
        print(".......Terminating...")
    except FileNotFoundError:
        print("The necessary tool is not found. Please make sure it is installed and in your system's PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

