<div align="center">

# 🚀 Deploying AWX & Orchestrating Workflows

### AWX Controller • Inventories • Job Templates • Workflow Templates • Scheduled Operations

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![AWX](https://img.shields.io/badge/AWX-Controller-1B1B1B?style=for-the-badge&logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Containers-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

---

## 📑 Table of Contents

- [📋 Lab Summary](#-lab-summary)
- [🛠️ Key Skills Practiced](#️-key-skills-practiced)
- [📚 Key Concepts](#-key-concepts)
- [🌍 Real-World Applications](#-real-world-applications)
- [🚀 Next Steps](#-next-steps)

---

## 📋 Lab Summary

In this lab, you deployed a working **AWX automation controller** using containers, built a multi-group Ansible inventory, and wrote playbooks that provision a web server and a PostgreSQL database server. You then configured AWX projects, credentials, job templates, and a workflow template to orchestrate the deployment through a web interface, and implemented operational playbooks for scheduled configuration updates and backups with retention cleanup.

---

## 🛠️ Key Skills Practiced

| # | Skill | Details |
|---|-------|---------|
| 1 | 📦 **Controller Deployment** | Deployed a working AWX automation controller using containers |
| 2 | 🗂️ **Inventory Design** | Built a multi-group Ansible inventory |
| 3 | 📝 **Provisioning Playbooks** | Wrote playbooks that provision a web server and a PostgreSQL database server |
| 4 | ⚙️ **AWX Configuration** | Configured projects, credentials, and job templates |
| 5 | 🔗 **Workflow Orchestration** | Built a workflow template to orchestrate the deployment through the web interface |
| 6 | 💾 **Operational Playbooks** | Implemented scheduled configuration updates and backups with retention cleanup |

---

## 📚 Key Concepts

| Concept | Description |
|---------|-------------|
| **AWX Controller** | Web-based automation controller for running and managing Ansible content |
| **Inventory** | Multi-group listing of managed hosts targeted by playbooks |
| **Privilege Escalation** | Running tasks with elevated rights on managed hosts |
| **Project** | Source of playbooks used by job templates |
| **Credential** | Stored authentication data used when running jobs |
| **Job Template** | Reusable definition combining inventory, project, credentials, and playbook |
| **Workflow Template** | Orchestrates multiple job templates into one deployment flow |
| **Retention Cleanup** | Removing old backups according to a retention policy |

---

## 🌍 Real-World Applications

These Ansible Automation Platform concepts, including inventories, privilege escalation, job templates, and workflow orchestration, are directly applicable to enterprise infrastructure automation.

---

## 🚀 Next Steps

- ✅ Extend the workflow with **approval nodes**
- 🔗 Integrate a **real source control backend** for the project
- 🔐 Add **Ansible Vault** to encrypt the database password variable instead of using a plaintext default

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Education-0A66C2?style=for-the-badge)

**Created for Al Nafi Training Labs**

</div>
