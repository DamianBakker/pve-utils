# PVE Utilities – Real Proxmox CLI Tools

PVE Utilities (pve-utils) is an open-source collection of small command‑line tools that interact with a real Proxmox VE server through its API.

The goal is to provide lightweight CLI helpers for managing and monitoring Proxmox clusters.

## Features
### ✔ Available
- Real VM listing using the Proxmox API (`list-vms`)

### 🛠 In progress
- Storage usage
- Backup verification
- Cluster health

## Installation

pip install -r requirements.txt


## Setup

Create a file named `config.json`:

```json
{
    "api_url": "https://192.168.1.11:8006/api2/json",
    "token_id": "",
    "token_secret": "",
    "node": "pve"
}

Then run:

python3 pve_tool.py list-vms
