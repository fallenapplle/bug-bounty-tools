import subprocess
import os
import time

# ANSI color codes for colorful output
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
END = '\033[0m'

# Paths for Go and Pip binaries
GO_BIN_PATH = os.path.expanduser("/home/apple/go/bin")
PIP_BIN_PATH = os.path.expanduser("/home/apple/.local/bin")

def run_command(command):
    """Run a command using subprocess and return the output."""
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode('utf-8').strip() if e.stderr else str(e)
        raise RuntimeError(f"Error occurred while executing command: {' '.join(command)}\n{error_message}")

def is_tool_installed(tool_name):
    """Check if a tool is installed."""
    try:
        subprocess.run(["which", tool_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_snap_tools():
    """Install tools using Snap."""
    snap_tools = [
        ["go", "--classic"],
        ["xmind", "--classic"],
        ["httpx"]
    ]
    for tool in snap_tools:
        tool_name = tool[0]
        if not is_tool_installed(tool_name):
            try:
                run_command(["sudo", "snap", "install"] + tool)
                print(f"{GREEN}Installed: {tool_name}{END}")
            except RuntimeError as e:
                print(f"{RED}Error: {e}{END}")
        else:
            print(f"{YELLOW}Already installed: {tool_name}{END}")

def install_apt_tools():
    """Install tools using APT."""
    apt_tools = [
        "john",
        "python3-pip",
        "nmap",
        "sqlmap",
        "gobuster",
        "dirb",
        "wireshark",
        "aircrack-ng",
        "nikto",
        "hydra"
    ]
    for tool in apt_tools:
        if not is_tool_installed(tool):
            try:
                run_command(["sudo", "apt", "install", "-y", tool])
                print(f"{GREEN}Installed: {tool}{END}")
            except RuntimeError as e:
                print(f"{RED}Error: {e}{END}")
        else:
            print(f"{YELLOW}Already installed: {tool}{END}")

def install_additional_tools():
    """Install additional tools using Go."""
    additional_tools = [
        
        "github.com/OJ/gobuster/v3@latest",
        "github.com/tomnomnom/waybackurls@latest",
        "github.com/ffuf/ffuf/v2@latest",
        "github.com/tomnomnom/httprobe@latest",
        "github.com/tomnomnom/anew@latest",
        "github.com/tomnomnom/unfurl@latest",
        "github.com/tomnomnom/fff@latest",
        "github.com/tomnomnom/meg@latest",
        "github.com/tomnomnom/qsreplace@latest"
    ]
    for tool in additional_tools:
        tool_name = tool.split("/")[-1].split("@")[0]
        if not is_tool_installed(tool_name):
            try:
                run_command(["go", "install", "-v", tool])
                print(f"{GREEN}Installed: {tool_name}{END}")
            except RuntimeError as e:
                print(f"{RED}Error: {e}{END}")
        else:
            print(f"{YELLOW}Already installed: {tool_name}{END}")

def install_pip_and_go_tools():
    """Install tools using Pip and Go."""
    go_tools = [
        "github.com/owasp-amass/amass/v4/...",
        "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
        "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "github.com/tomnomnom/assetfinder@latest"
    ]
    pip_tools = [
        "knockpy",
        "py-altdns==1.0.2",
        "arjun"
    ]
    for tool in go_tools:
        tool_name = tool.split("/")[-1]
        if not is_tool_installed(tool_name):
            try:
                run_command(["go", "install", "-v", tool])
                print(f"{GREEN}Installed: {tool_name}{END}")
            except RuntimeError as e:
                print(f"{RED}Error: {e}{END}")
        else:
            print(f"{YELLOW}Already installed: {tool_name}{END}")

    for tool in pip_tools:
        tool_name = tool.split("==")[0]
        if not is_tool_installed(tool_name):
            try:
                run_command(["pip3", "install", tool])
                print(f"{GREEN}Installed: {tool_name}{END}")
            except RuntimeError as e:
                print(f"{RED}Error: {e}{END}")
        else:
            print(f"{YELLOW}Already installed: {tool_name}{END}")

def install_bug_hunting_tools():
    """Install all bug hunting tools."""
    print(f"{YELLOW}=== Installing Bug Hunting Tools ==={END}")

    print(f"\n{YELLOW}[Step 1/4] Installing Snap tools...{END}")
    install_snap_tools()
    time.sleep(2)

    print(f"\n{YELLOW}[Step 2/4] Installing APT tools...{END}")
    install_apt_tools()
    time.sleep(2)

    print(f"\n{YELLOW}[Step 3/4] Installing additional tools...{END}")
    install_additional_tools()
    time.sleep(2)

    print(f"\n{YELLOW}[Step 4/4] Installing Pip and Go tools...{END}")
    install_pip_and_go_tools()
    time.sleep(2)

    print(f"\n{GREEN}=== Installation complete! ==={END}")
    print("You're all set to start bug hunting!")

if __name__ == "__main__":
    try:
        install_bug_hunting_tools()
    except Exception as e:
        print(f"{RED}Critical Error occurred: {e}{END}")
