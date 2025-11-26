#!/usr/bin/env python3
import argparse
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# load config
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        print("❌ Missing or invalid config.json")
        exit(1)


def api_get(cfg, endpoint):
    """
    Send GET request to Proxmox API
    """
    headers = {
        "Authorization": f"PVEAPIToken={cfg['token_id']}={cfg['token_secret']}"
    }
    url = f"{cfg['api_url']}/{endpoint}"

    try:
        response = requests.get(url, headers=headers, verify=False)
        return response.json()
    except Exception as e:
        print("API error:", e)
        exit(1)


def list_vms(cfg):
    """
    List real VMs on Proxmox
    """
    endpoint = f"nodes/{cfg['node']}/qemu"
    data = api_get(cfg, endpoint)

    if "data" not in data:
        print("❌ Error reading VMs list")
        return

    print("ID     Name               Status")
    print("----------------------------------")

    for vm in data["data"]:
        print(f"{vm['vmid']}    {vm.get('name','<no-name>'):15}  {vm['status']}")


def main():
    cfg = load_config()

    parser = argparse.ArgumentParser(description="PVE Utilities - Real Proxmox CLI Tool")
    parser.add_argument("command", help="Command (list-vms)")

    args = parser.parse_args()

    if args.command == "list-vms":
        list_vms(cfg)
    else:
        print("Unknown command:", args.command)
        print("Available commands: list-vms")


if __name__ == "__main__":
    main()
