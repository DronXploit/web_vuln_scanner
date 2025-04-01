import requests
from colorama import Fore, Style
from scanner.modules import xss, sqli, lfi

class VulnScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
        })

    def scan_all(self):
        print(f"\n{Fore.YELLOW}[+] Scanning {self.target_url}{Fore.RESET}")
        
        results = {
            'xss': xss.scan(self.target_url, self.session),
            'sqli': sqli.scan(self.target_url, self.session),
            'lfi': lfi.scan(self.target_url, self.session)
        }
        
        print(f"\n{Style.BRIGHT}=== Scan Summary ===")
        for test, result in results.items():
            status = f"{Fore.GREEN}SAFE{Fore.RESET}" if not result else f"{Fore.RED}VULNERABLE{Fore.RESET}"
            print(f"{test.upper():<8}: {status}")
        print(f"==================={Style.NORMAL}\n")
        
        return results