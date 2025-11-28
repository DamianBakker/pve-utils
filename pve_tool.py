#!/usr/bin/env python3
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# -------------------------------------------------------
# LOAD CONFIG
# -------------------------------------------------------
def load_config():
    """Load configuration from config.json"""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading config.json: {e}")
        exit(1)


# -------------------------------------------------------
# API SESSION
# -------------------------------------------------------
class ProxmoxAPI:
    def __init__(self, cfg):
        self.cfg = cfg
        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"PVEAPIToken={cfg['token_id']}={cfg['token_secret']}",
            "User-Agent": "pve-utils/1.0"
        })

    def get(self, endpoint):
        """Send GET request to Proxmox API"""
        url = f"{self.cfg['api_url']}/{endpoint}"

        try:
            response = self.session.get(url, verify=False, timeout=10)
            response.raise_for_status()

            try:
                return response.json()
            except json.JSONDecodeError:
                print("❌ API returned non-JSON response")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ API Request failed: {e}")
            return None


# -------------------------------------------------------
# COMMANDS
# -------------------------------------------------------
def list_nodes(api):
    data = api.get("nodes")
    if not data or "data" not in data:
        print("❌ Unable to list nodes")
        return

    print("\nNodes in cluster:")
    for node in data["data"]:
        status = node.get("status", "unknown")
        print(f"- {node['node']} ({status})")
    print()


def get_version(api):
    data = api.get("version")
    if not data or "data" not in data:
        print("❌ Unable to get version")
        return

    v = data["data"]
    print("\nProxmox Version:")
    print(f"{v['version']} (release: {v['release']})\n")


def list_storages(api, cfg):
    data = api.get(f"nodes/{cfg['node']}/storage")
    if not data or "data" not in data:
        print("❌ Unable to list storages")
        return

    print(f"\nStorages on node: {cfg['node']}")
    for storage in data["data"]:
        stype = storage.get("type", "?")
        print(f"- {storage['storage']} (Type: {stype})")
    print()


def list_vms(api, cfg):
    data = api.get(f"nodes/{cfg['node']}/qemu")
    if not data or "data" not in data:
        print("❌ Unable to list VMs")
        return

    vms = data["data"]
    if len(vms) == 0:
        print(f"\nNo VMs on node: {cfg['node']}\n")
        return

    print("\nID     Name               Status")
    print("----------------------------------")
    for vm in vms:
        name = vm.get("name", "<no-name>")
        print(f"{vm['vmid']}    {name:15}  {vm['status']}")
    print()


def cluster_status(api):
    data = api.get("cluster/status")
    if not data or "data" not in data:
        print("❌ Unable to read cluster status")
        return

    print("\nCluster status:")
    for node in data["data"]:
        name = node.get("name", "<unknown>")
        status = node.get("status", "unknown")
        print(f"- {name}: {status}")
    print()


# -------------------------------------------------------
# MAIN MENU
# -------------------------------------------------------
def main():
    cfg = load_config()
    api = ProxmoxAPI(cfg)

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
            list_nodes(api)
        elif choice == "2":
            get_version(api)
        elif choice == "3":
            list_storages(api, cfg)
        elif choice == "4":
            list_vms(api, cfg)
        elif choice == "5":
            cluster_status(api)
        elif choice == "6":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
