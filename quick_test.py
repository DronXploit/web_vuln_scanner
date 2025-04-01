#!/usr/bin/env python3
from scanner.core import VulnScanner
from colorama import init, Fore, Style
from pyfiglet import Figlet
import sys
import time
import random

init(autoreset=True)

def animate_text(text, width=45, delay=0.05):
    print(f"{Fore.YELLOW}╔{'═'*width}╗")
    sys.stdout.write(f"{Fore.YELLOW}║ {Fore.YELLOW}")
    
    for char in text.center(width-2):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))  
    
    print(f" {Fore.YELLOW}║\n╚{'═'*width}╝")

def show_banner():
    # Animasi garis atas
    print(f"\n{Fore.YELLOW}", end="")
    for _ in range(45):
        print("═", end="", flush=True)
        time.sleep(0.01)
    print()
    animate_text("Web Vuln Scanner | by: dronXploit")
    
    print(f"""{Fore.BLUE}                                          
                            :            
                            @@=  @-@=      
                            :@*%%@*       
                             -@@%@@%      
                             *@@@@@@@@:    
                            :%@@*#        
                    *@@@@@@@@@@@%*        
                  %@@@@@@@@@@@%:%@        
                :@@@@%%@@@*@=*:=##         
               :@@@@@@@@%*;; @@**%:         
               -@@@@@@@@@;; :%* ;:         
               *@@@@@@@@@;; @@ #;          
               %@@%@%@@@*@*@*:            
     :*=      :@@@   *@%  :@%:            
    -@*:    :*@@*    =@*  :@@:           
     :*@@@@@@*:      *@%  :@@@@@@@@%:    
                     :@@@@@@@:    :::      
                           :::                                            
    {Fore.RESET}""")
    
    animate_text("PENTEST TOOL v2.0 | UPDATE AT 01-04-2025")
def animated_scan():
    print(f"\n{Fore.YELLOW}[ ", end="")
    for i in range(5):
        print(f"🔍", end=" ", flush=True)
        time.sleep(0.3)
    print(f"{Fore.YELLOW}]")

def scan_target(target_url):
    try:
        animate_text("MEMULAI SCAN")
        
        animated_scan()
        
        scanner = VulnScanner(target_url)
        results = scanner.scan_all()
        
        print(f"\n{Fore.YELLOW}╔{'═'*45}╗")
        print(f"{Fore.YELLOW}║{Fore.YELLOW}{'HASIL SCAN':^45}║")
        print(f"{Fore.YELLOW}╠{Fore.YELLOW}{'═'*19}={'═'*25}╣")
        print(f"{Fore.YELLOW}║ {Fore.YELLOW}VULNERABILITY{Fore.YELLOW} ║ {Fore.YELLOW}STATUS{Fore.YELLOW}{' '*22}║")
        print(f"{Fore.YELLOW}╠{Fore.YELLOW}{'═'*19}={'═'*25}╣")
        
        for test_name, is_vulnerable in results.items():
            status = f"{Fore.RED}VULNERABLE ⚠️" if is_vulnerable else f"{Fore.YELLOW}AMAN ✓"
            print(f"{Fore.YELLOW}║ {test_name.upper():<13} ║ {status:<32} ║")
        
        print(f"{Fore.YELLOW}╚{'═'*45}╝\n")
        
    except Exception as e:
        print(f"\n{Fore.RED}╔{'═'*45}╗")
        print(f"║{'ERROR':^45}║")
        print(f"╠{'═'*45}╣")
        print(f"║ {str(e):<58} ║")
        print(f"╚{'═'*45}╝")

def show_examples():
    examples = [
        "http://testphp.vulnweb.com",
        "http://zero.webappsecurity.com",
        "http://demo.testfire.net"
    ]
    
    animate_text("CONTOH TARGET VULNERABLE")
    print(f"\n{Fore.YELLOW}╔{'═'*45}╗")
    
    for i, example in enumerate(examples, 1):
        print(f"{Fore.YELLOW}║ {Fore.WHITE}{i}. {example:<40}{Fore.YELLOW} ║")
    print(f"{Fore.YELLOW}╚{'═'*45}╝\n")

def interactive_mode():
    show_banner()
    
    while True:
        print(f"\n{Fore.YELLOW}┌───────────────────────────────┐")
        print(f"{Fore.YELLOW}│{Fore.WHITE}  MENU UTAMA:{Fore.YELLOW}{' '*18}│")
        print(f"{Fore.YELLOW}├───────────────────────────────┤")
        print(f"{Fore.YELLOW}│ {Fore.WHITE}1.{Fore.WHITE} Scan URL Target            {Fore.YELLOW}│")
        print(f"{Fore.YELLOW}│ {Fore.WHITE}2.{Fore.WHITE} Lihat Contoh Target        {Fore.YELLOW}│")
        print(f"{Fore.YELLOW}│ {Fore.WHITE}3.{Fore.WHITE} Keluar                     {Fore.YELLOW}│")
        print(f"{Fore.YELLOW}└───────────────────────────────┘\n")
        
        choice = input(f"\n{Fore.BLUE}Pilih opsi {Fore.YELLOW}[1-3]{Fore.YELLOW}: ").strip()
        
        if choice == '1':
            animate_text("MASUKKAN URL TARGET")
            target = input(f"{Fore.BLUE}\nURL Target http atau https (contoh: http://target.com): {Fore.RESET}").strip()
            
            if not target:
                print(f"\n{Fore.RED}❌ URL tidak boleh kosong!")
                continue
                
            if not target.startswith(('http://', 'https://')):
                target = 'https://' + target
                
            scan_target(target)
            
        elif choice == '2':
            show_examples()
            
        elif choice == '3':
            animate_text("SAMPAI JUMPA LAGI")
            break
            
        else:
            animate_text("PILIHAN TIDAK VALID!")

if __name__ == "__main__":
    try:
        interactive_mode()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\n⚠️ Program dihentikan oleh pengguna")
        sys.exit(0)