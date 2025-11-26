# Contributing to PVE Utilities

Thank you for your interest in contributing to **PVE Utilities**!  
This project is maintained by:

- **Damian Bakker** (owner)

We welcome contributions of all kinds: code, ideas, tests, documentation, and feature requests.

---

## ⭐ How to Contribute

### 1. Fork the repository
Click the **Fork** button on GitHub to create your own copy.

### 2. Create a branch
Use clear branch names related to what you are working on:

git checkout -b feature/add-storage-info
git checkout -b fix/vm-list-crash


### 3. Make your changes
Keep changes small and focused.  
If you add a new function, please include:

- basic error handling  
- simple comments explaining what it does  

### 4. Commit guidelines
Use meaningful commit messages:

feat: add storage listing support
fix: correct cluster status crash
docs: improve readme


### 5. Push & create a Pull Request
Push your branch:

git push origin feature/add-storage-info


Then open a **Pull Request** on GitHub.

Explain:
- what you changed  
- why  
- how to test it  

---

## 🧪 Code Style Guidelines

- Python 3.x
- Keep functions short and readable
- Prefer clear naming (`list_nodes()`, `get_cluster_status()`, etc.)
- Avoid duplicating code — use helpers or modules when possible

---

## 📝 Reporting Issues

If you find a bug or want a new feature, open an **Issue** on GitHub.

Include:
- Proxmox version  
- API URL format used  
- Full error message if possible  
- Steps to reproduce  

---

## 🤝 Contributors

Thanks to everyone helping improve **PVE Utilities**!

- **Damian Bakker** – creator & maintainer 

---

## ❤️ Thank you

Every contribution helps the project grow.  
Feel free to propose anything — even small improvements are very welcome!
