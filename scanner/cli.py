import argparse
from pyfiglet import Figlet
from colorama import Fore, Style, init
from .core import VulnScanner

init(autoreset=True)

def banner():
    f = Figlet(font='slant')
    print(Fore.RED + f.renderText('WEB VULN SCANNER'))
    print(f"{Style.DIM}Security Scanner v1.0{Style.NORMAL}\n")

def main():
    banner()
    parser = argparse.ArgumentParser(description='Web Vulnerability Scanner')
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed scan output")
    args = parser.parse_args()
    
    scanner = VulnScanner(args.url)
    results = scanner.scan_all()
    
    if args.verbose:
        print(f"\n{Style.BRIGHT}Detailed Results:")
        for test, result in results.items():
            print(f"{test.upper()}: {'Vulnerabilities found' if result else 'No issues detected'}")

if __name__ == "__main__":
    main()