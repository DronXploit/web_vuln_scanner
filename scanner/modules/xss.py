from urllib.parse import urljoin
from bs4 import BeautifulSoup
from colorama import Fore, Style

def scan(url, session):
    print(f"\n{Fore.CYAN}[+] Testing for XSS vulnerabilities...{Fore.RESET}")
    test_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "'\"><script>alert(1)</script>"
    ]
    vuln_found = False
    
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for form in soup.find_all('form'):
            form_action = form.get('action', '')
            form_method = form.get('method', 'get').lower()
            
            inputs = {}
            for input_tag in form.find_all('input'):
                name = input_tag.get('name')
                if name:
                    inputs[name] = test_payloads[0] 
            
            target_url = urljoin(url, form_action)
            
            for payload in test_payloads:
                data = {k: payload for k in inputs.keys()}
                
                if form_method == 'post':
                    res = session.post(target_url, data=data)
                else:
                    res = session.get(target_url, params=data)
                
                if payload in res.text:
                    print(f"{Fore.RED}[!] XSS Vulnerability found at {target_url}")
                    print(f"    Payload: {Style.BRIGHT}{payload}{Style.NORMAL}")
                    vuln_found = True
                    break
    
    except Exception as e:
        print(f"{Fore.YELLOW}[!] XSS Scan Error: {e}{Fore.RESET}")
    
    if not vuln_found:
        print(f"{Fore.GREEN}[✓] No XSS vulnerabilities found{Fore.RESET}")
    
    return vuln_found