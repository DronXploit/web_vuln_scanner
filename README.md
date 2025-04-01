# 🔍 Web Vulnerability Scanner - dronXPloit Edition

![Banner Preview](https://i.imgur.com/JQ7Gh3p.png)  
*"Powerful pentesting tool FOR LEGAL PURPOSE ONLY"*

## 🌟 Features
```python
- XSS Scanner       : Detect <script> injections
- SQLi Detector     : Find SQL injection flaws
- LFI Tester        : Check local file inclusion
- Interactive Mode  : User-friendly terminal UI
- Visual Analytics  : Color-coded results with ASCII art
- Animated Scans    : Real-time scanning effects

🚀 Quick Start

# Clone repo
git clone https://github.com/dronXPloit/web_vuln_scanner.git
cd web_vuln_scanner

# Setup environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run scanner
python quick_test.py

🎨 Interface Preview

╔═══════════════════════════════════════════════╗
║        WEB VULN SCANNER - BY: dronXPloit      ║
╚═══════════════════════════════════════════════╝

[ 🔍 🔍 🔍 ] Scanning target...

╔═══════════════════════════════════════════════╗
║                SCAN RESULTS                   ║
╠════════════╦══════════════════════════════════╣
║ XSS        ║ VULNERABLE⚠️                    ║
║ SQLi       ║ SAFE ✓                          ║
║ LFI        ║ VULNERABLE ⚠️                   ║
╚════════════╩══════════════════════════════════╝

## ![Hasil Detil](./images/SS(1), (2), (3))


📋 Test Cases

# Manual testing
python quick_test.py -u http://testphp.vulnweb.com

# Example vulnerable targets:
- http://testphp.vulnweb.com
- http://zero.webappsecurity.com
- http://demo.testfire.net


⚠️ Penting!
MIT License - © 2025 dronXPloit

DISCLAIMER: Use only on authorized systems.
Penetration testing without permission is illegal.
