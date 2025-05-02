#!/bin/bash
clear

echo "███╗   ██╗███████╗██████╗  ██████╗      ███████╗ ██████╗  █████╗ ███╗   ██╗"
echo "████╗  ██║██╔════╝██╔══██╗██╔═══██╗    ██╔════╝██╔════╝ ██╔══██╗████╗  ██║"
echo "██╔██╗ ██║█████╗  ██████╔╝██║   ██║    ███████╗██║      ███████║██╔██╗ ██║"
echo "██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║    ╚════██║██║      ██╔══██║██║╚██╗██║"
echo "██║ ╚████║███████╗██║  ██║╚██████╔╝    ███████║╚██████╗ ██║  ██║██║ ╚████║"
echo "╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝"
echo "                          🛡️  NeroScan 🛡️"
echo "                  Automated File Scanning Tool"
echo ""

# Check if Python3 is installed
echo "[+] Checking for Python3..."
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is not installed."; exit 1; }
echo "[✓] Python3 is installed."

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    echo "[+] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[✓] Virtual environment already exists."
fi

echo "[+] Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "[+] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check if everything is installed
if ! python3 -c "import requests, tqdm" >/dev/null 2>&1; then
    echo "[✗] Some packages failed to install."
    exit 1
fi

# Create necessary directories
echo "[+] Setting up project directories..."
mkdir -p reports scanned_files

# Complete installation message
echo "[✓] Installation completed successfully!"

# Launch NeroScan
echo "[>] Launching NeroScan..."
python3 neroscan.py

