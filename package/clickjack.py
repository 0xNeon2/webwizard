from urllib.request import urlopen

def check_clickjacking_vulnerability(url):
    try:
        if "http" not in url:
            url = "http://www." + url

        data = urlopen(url)
        headers = data.info()

        if "X-Frame-Options" in headers:
            return False  # Not vulnerable to clickjacking
        else:
            return True  # Vulnerable to clickjacking
    except:
        return False  # An error occurred or the site is not accessible

def clickjacking():
    print("Enter Target website [http://www.domain_name] :")
    url = input("==> ")
    is_vulnerable = check_clickjacking_vulnerability(url)

    if is_vulnerable:
        print("==============================================")
        print("Website is vulnerable to clickjacking!")
        print("==============================================")
    else:
        print("==============================================")
        print("Website is not vulnerable to clickjacking.")
        print("==============================================")

