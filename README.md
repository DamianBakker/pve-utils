[![Contributors](https://img.shields.io/github/contributors/DamianBakker/pve-utils)](https://github.com/DamianBakker/pve-utils/graphs/contributors)
# PVE Utilities – Real Proxmox CLI Tools

PVE Utilities (pve-utils) is an open-source collection of lightweight command-line tools that interact with a real Proxmox VE server using its official API.

The goal is to provide simple, reliable CLI helpers for managing and monitoring your Proxmox nodes and clusters — without needing the web interface.

---

## 🚀 Features

### ✔ Available
- Interactive CLI menu
- List cluster nodes
- Get Proxmox version
- List storage on a node
- List VMs on a node
- Show cluster status

### 🛠 In Progress
- Storage usage & free space
- Backup verification
- VM lifecycle actions (start/stop/reboot)
- Create VM from template
- ISO & backup management
- Cluster metrics

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/DamianBakker/pve-utils.git
cd pve-utils

Install the required Python packages:

pip install -r requirements.txt

⚙️ Setup

Create a config.json file in the project directory:

{
    "api_url": "https://YOUR-PVE-IP:8006/api2/json",
    "token_id": "root@pam!mytoken",
    "token_secret": "your-secret-here",
    "node": "pve"
}

🔐 How to create an API Token in Proxmox

    Go to Datacenter → Permissions → API Tokens

    Select your user (ex: root@pam)

    Click Add

    Create a token (ex: name: pveutils)

    Copy the Token ID and Secret

Paste them into config.json.
🖥️ Usage

Run the interactive CLI tool:

python pve_tool.py

You will see:

=== Proxmox CLI Tool ===
1. List Nodes
2. Proxmox Version
3. List Storages
4. List VMs
5. Cluster Status
6. Exit
Choose an option:

📌 Example Commands (non-interactive)

List VMs directly:

python pve_tool.py list-vms

List storages:

python pve_tool.py list-storages

Get version:

python pve_tool.py version