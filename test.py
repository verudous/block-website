import os

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

websites = ['www.roblox.com']

def block():
    try:
        with open(host_path, "a") as file:
            for web in websites:
                file.write(f"{redirect_ip} {web}\n")
    except Exception as e:
        print(e)
    os.system('ipconfig /flushdns >nul')

def unblock():
    try:
        with open(host_path, 'r') as file:
            content = file.readlines()
        with open(host_path, 'w') as file:
            for line in content:
                if not any(web in line for web in websites):
                    file.write(line)
    except Exception as e:
        print(e)
    os.system('ipconfig /flushdns >nul')

unblock()