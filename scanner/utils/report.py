from datetime import datetime
from colorama import Fore

def generate_html_report(vulnerabilities, filename="report.html"):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vulnerability Report</title>
        <style>
            body {{ font-family: Arial; }}
            .vuln {{ color: red; }}
            .timestamp {{ color: gray; }}
        </style>
    </head>
    <body>
        <h1>Web Vulnerability Report</h1>
        <p class="timestamp">Generated at {datetime.now()}</p>
        <ul>
    """
    
    for vuln in vulnerabilities:
        html += f'<li class="vuln">{vuln}</li>'
    
    html += """
        </ul>
    </body>
    </html>
    """
    
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f"{Fore.GREEN}[+] Report saved as {filename}{Fore.RESET}")