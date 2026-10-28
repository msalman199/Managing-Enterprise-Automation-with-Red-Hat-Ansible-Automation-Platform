<div align="center">

# 🤖 Automating Automation Controller with the REST API

### Idempotent Playbooks, Token Authentication, and Automated Maintenance Reporting

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![AWX](https://img.shields.io/badge/AWX-Automation%20Controller-1F1F1F?style=for-the-badge&logo=redhat&logoColor=EE0000)
![REST API](https://img.shields.io/badge/REST-API-blue?style=for-the-badge)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [📋 Lab Summary](#-lab-summary)
- [🛠️ Key Skills Practiced](#️-key-skills-practiced)
- [🧠 Key Concepts](#-key-concepts)
- [🚀 Next Steps](#-next-steps)
- [🏁 Conclusion](#-conclusion)

---

## 📋 Lab Summary

In this lab, you automated the configuration of an Ansible Automation Controller environment **entirely through its documented REST API**, using idempotent Ansible playbooks instead of manual clicks or unsupported file edits.

| # | What You Built | Description |
|---|----------------|-------------|
| 1️⃣ | **Organization** | Created an organization in Automation Controller through the API |
| 2️⃣ | **Project** | Registered and synced an external Git repository as a project |
| 3️⃣ | **Maintenance Playbook** | Queried Controller health, recent job activity, and project sync status to generate a timestamped report |

> 🎯 **Focus:** Treating Automation Controller itself as code — configured through its API rather than its web interface.

---

## 🛠️ Key Skills Practiced

Along the way you practiced core **Infrastructure as Code** patterns:

| Pattern | Description |
|---------|-------------|
| 🔑 **Token-Based Authentication** | Authenticating API requests with tokens |
| ♻️ **Idempotent Create-or-Lookup Logic** | Safely re-running playbooks without creating duplicates |
| ⏳ **Waiting on Asynchronous Operations** | Waiting for long-running operations, such as project syncs, to complete |
| 📄 **Jinja2 Report Templates** | Using Jinja2 templates to produce operational reports |

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **Controller REST API** | The documented interface used to configure Automation Controller without manual clicks |
| **Idempotency** | Running the same playbook repeatedly yields the same end state |
| **Create-or-Lookup** | Reuse an existing resource if present; create it only if missing |
| **Asynchronous Operations** | Operations such as project sync that finish after the request returns |
| **Jinja2 Templates** | Templating used to turn queried data into a timestamped report |
| **Infrastructure as Code** | Managing platform configuration through version-controlled, repeatable automation |

---

## 🚀 Next Steps

From here, consider:

- 🚨 Extending the maintenance playbook to **alert on failed job or project statuses**
- ⏰ Integrating it into a **scheduled job template** inside the Controller itself
- 🔁 Applying the same API-driven approach to automate **credential, inventory, and job template management**

---

## 🏁 Conclusion

You automated an Automation Controller environment through its REST API using idempotent playbooks, building an organization, a synced Git project, and a timestamped maintenance report — the same API-driven approach can now be extended across the rest of your Controller configuration.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Education-0A66C2?style=for-the-badge)

**Happy Automating! 🤖**

</div>
