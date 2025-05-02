import os
import sys
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich import box
from time import sleep

console = Console()

API_KEY = "b798decaadb6533f24003044226f7bb9d069c8336ae2ba9181d1e89c1a8c3bef"
API_URL = "https://www.virustotal.com/api/v3/files"
HEADERS = {
    "x-apikey": API_KEY
}


BANNER = '''
███╗   ██╗███████╗██████╗  ██████╗      ███████╗ ██████╗  █████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔══██╗██╔═══██╗    ██╔════╝██╔════╝ ██╔══██╗████╗  ██║
██╔██╗ ██║█████╗  ██████╔╝██║   ██║    ███████╗██║      ███████║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║    ╚════██║██║      ██╔══██║██║╚██╗██║
██║ ╚████║███████╗██║  ██║╚██████╔╝    ███████║╚██████╗ ██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                      🛡️  NeroScan 🛡️
              Automated File Scanning Tool
'''

def ask_file_path():
    console.print("\n[bold green][>] Enter the path to the file you want to scan:[/bold green]", end=" ")
    return input("\n> ")

def scan_file(file_path):
    if not os.path.exists(file_path):
        console.print(f"[bold red][-] File not found: {file_path}[/bold red]")
        sys.exit(1)

    filename = os.path.basename(file_path)
    console.print(f"[cyan][*] Uploading:[/cyan] {filename}")

    with open(file_path, "rb") as f:
        files = {"file": (filename, f)}
        response = requests.post(API_URL, headers=HEADERS, files=files)

    if response.status_code != 200:
        console.print(f"[bold red][-] Error uploading file: {response.text}[/bold red]")
        sys.exit(1)

    file_id = response.json()["data"]["id"]
    console.print("[yellow][*] File uploaded. Fetching analysis...[/yellow]")

    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"

    with Progress() as progress:
        task = progress.add_task("[green]Waiting for analysis...", total=100)
        for _ in range(10):
            sleep(1)
            progress.update(task, advance=10)

    analysis_response = requests.get(analysis_url, headers=HEADERS)
    return analysis_response.json()

def display_results(results):
    attributes = results.get("data", {}).get("attributes", {})
    stats = attributes.get("stats", {})
    results = attributes.get("results", {})

    table = Table(title="Scan Report", box=box.SQUARE)
    table.add_column("Engine", style="bold white")
    table.add_column("Category", style="bold white")
    table.add_column("Result", style="bold white")

    for engine, data in results.items():
        category = data.get("category", "undetected")
        result = data.get("result", "-")

        if category == "undetected":
            category_style = "green"
        elif category == "suspicious":
            category_style = "yellow"
        elif category == "malicious":
            category_style = "red"
        else:
            category_style = "white"

        table.add_row(engine, f"[{category_style}]{category}[/{category_style}]", result)

    summary_json = {
        "✅ Undetected": stats.get("undetected", 0),
        "⚠️ Suspicious": stats.get("suspicious", 0),
        "🔴 Malicious": stats.get("malicious", 0),
        "❓ Timeout": stats.get("timeout", 0)
    }

    panel_content = "\n".join([f"[bold]{k}[/bold]: {v}" for k, v in summary_json.items()])
    console.print(Panel(panel_content, title="[bold blue]Scan Summary[/bold blue]", expand=False))

    console.print(table)

if __name__ == '__main__':
    console.print(BANNER, style="bold blue")
    file_path = ask_file_path()
    analysis = scan_file(file_path)
    display_results(analysis)
