# 🛡️ NeroScan
![Tool Preview](https://i.postimg.cc/YqVWwntg/Screenshot-From-2025-05-02-11-15-39.png)

A powerful automated file scanning tool designed for cybersecurity research.  
Helps quickly analyze suspicious files and generate detailed reports with a clean, color-coded interface.

---

## 📦 Features

- Beautiful CLI interface with Rich formatting.
- Upload any file and automatically fetch a full scan report.
- Categorized results with color-coded severity:
  - 🟩 Green → Safe
  - 🟨 Yellow → Suspicious
  - 🟥 Red → Malicious
- Displays summary statistics.
- Fast and easy to use.

---

## ⚙️ Requirements

- Python 3.8+
- Internet connection (for uploading and scanning files)

---

## 🧪 Installation

Clone the repository:

```bash
git clone https://github.com/MaestroNero/NeroScan.git
cd NeroScan
```

Install The tool:

```bash
chmod +x install.sh
./install.sh
```

Run the tool:

```bash
python3 neroscan.py
```

## 📁 Supported File Types

The following file types are supported by NeroScan through the VirusTotal API:

### 🧩 1. Executables
- `.exe` — Windows Executables  
- `.dll` — Dynamic-Link Libraries  
- `.msi` — Microsoft Installer  
- `.com`, `.bat`, `.cmd`, `.scr`, `.pif` — Scriptable Executables

### 🧾 2. Documents
- `.doc`, `.docx` — Microsoft Word  
- `.xls`, `.xlsx` — Microsoft Excel  
- `.ppt`, `.pptx` — Microsoft PowerPoint  
- `.rtf`, `.csv` — Rich Text Format and Comma-Separated Values  
- `.pdf` — PDF documents (potentially with embedded scripts/macros)

### 📦 3. Archive Files
- `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`  
> Archives should not be password-protected unless you provide the password in advance.

### 🐧 4. Linux/Unix Files
- `.elf` — Linux Executable and Linkable Format  
- `.sh` — Shell Scripts  
- `.bin`, `.run` — Binary Executables

### 💻 5. macOS Files
- `.dmg`, `.pkg`, `.app`, `.osx` — Apple Installers and Apps

### 📱 6. Android Files
- `.apk` — Android Package Files  
- `.dex` — Dalvik Executable Files

### 🍏 7. iOS Files
- `.ipa` — iOS App Archive  
- `.mobileconfig`, `.plist` — Configuration and Property Files

### 🧬 8. Scripting and Source Code
- `.js` — JavaScript  
- `.vbs` — Visual Basic Script  
- `.ps1` — PowerShell  
- `.py`, `.rb` — Python and Ruby  
- `.jar`, `.class` — Java Files  
- `.html`, `.htm`, `.xml` — Web Files

### 🔧 9. System and Driver Files
- `.sys` — Windows System Drivers  
- `.drv`, `.cpl` — Control Panel and Driver Files

---

**Note:**  
Maximum file size via the public VirusTotal API is generally around **650MB**.  
Some encrypted, protected, or nested files may not be fully analyzed.


---

## 🚀 Usage

You will be prompted to enter the path of the file you want to scan.

The tool will:

1. Upload the file.
2. Wait for the analysis.
3. Display the result in a color-coded table showing the severity of the scan results.

[>] Enter the path to the file you want to scan: 
/home/nero/[namefile]

---

## 📜 License & Credits

This project is open-source and maintained by:

👤 The Maestro Nero  
🔗 [Telegram Channel](https://t.me/CYBER_Nero)
