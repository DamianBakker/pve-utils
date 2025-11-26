#!/usr/bin/env python3
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ------------------ CONFIG ------------------
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        print("❌ Missing or invalid config.json")
        exit(1)

# ------------------ API WRAPPER ------------------
def api_get(cfg, endpoint):
    """Send GET request to Proxmox API"""
    headers = {
        "Authorization": f"PVEAPIToken={cfg['token_id']}={cfg['token_secret']}"
    }
    url = f"{cfg['api_url']}/{endpoint}"
    try:
        response = requests.get(url, headers=headers, verify=False)
        return response.json()
    except Exception as e:
        print("API error:", e)
        return None

# ------------------ COMMANDS ------------------
def list_nodes(cfg):
    data = api_get(cfg, "nodes")
    if not data or "data" not in data:
        print("❌ Error reading nodes")
        return
    print("\nNodes in cluster:")
    for node in data["data"]:
        print(f"- {node['node']} ({node['status']})")
    print()

def get_version(cfg):
    data = api_get(cfg, "version")
    if not data or "data" not in data:
        print("❌ Error getting version")
        return
    print("\nProxmox Version:")
    print(f"{data['data']['version']} ({data['data']['release']})\n")

def list_storages(cfg):
    endpoint = f"nodes/{cfg['node']}/storage"
    data = api_get(cfg, endpoint)
    if not data or "data" not in data:
        print("❌ Error reading storages")
        return
    print("\nStorages on node:", cfg['node'])
    for storage in data["data"]:
        print(f"- {storage['storage']} (Type: {storage['type']})")
    print()

def list_vms(cfg):
    endpoint = f"nodes/{cfg['node']}/qemu"
    data = api_get(cfg, endpoint)
    if not data or "data" not in data:
        print("❌ Error reading VMs list")
        return
    if len(data["data"]) == 0:
        print("\nNo VMs found on node:", cfg['node'], "\n")
        return
    print("\nID     Name               Status")
    print("----------------------------------")
    for vm in data["data"]:
        print(f"{vm['vmid']}    {vm.get('name','<no-name>'):15}  {vm['status']}")
    print()

def cluster_status(cfg):
    data = api_get(cfg, "cluster/status")
    if not data or "data" not in data:
        print("❌ Error reading cluster status")
        return
    print("\nCluster status:")
    for node in data["data"]:
        name = node.get("name", "<no-name>")
        status = node.get("status", "online")  # fallback si clé manquante
        print(f"- {name}: {status}")
    print()

# ------------------ MAIN MENU ------------------
def main():
    cfg = load_config()

    while True:
        print("\n=== Proxmox CLI Tool ===")
        print("1. List Nodes")
        print("2. Proxmox Version")
        print("3. List Storages")
        print("4. List VMs")
        print("5. Cluster Status")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            list_nodes(cfg)
        elif choice == "2":
            get_version(cfg)
        elif choice == "3":
            list_storages(cfg)
        elif choice == "4":
            list_vms(cfg)
        elif choice == "5":
            cluster_status(cfg)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
