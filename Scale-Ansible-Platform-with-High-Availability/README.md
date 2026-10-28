<div align="center">

# 🔁 Ansible Automation Platform High Availability

### Shared PostgreSQL, HAProxy Health Checks, and Failure Monitoring

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![HAProxy](https://img.shields.io/badge/HAProxy-106DA9?style=for-the-badge&logo=haproxy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Advanced-red?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [📋 Lab Summary](#-lab-summary)
- [🛠️ Key Skills Practiced](#️-key-skills-practiced)
- [🧠 Key Concepts](#-key-concepts)
- [🌍 Real-World Applications](#-real-world-applications)
- [🏁 Conclusion](#-conclusion)

---

## 📋 Lab Summary

In this lab, you built the core building blocks of an **Ansible Automation Platform high availability deployment**:

| # | What You Built | Description |
|---|----------------|-------------|
| 1️⃣ | **Shared PostgreSQL Database** | A database reachable by multiple application nodes |
| 2️⃣ | **HAProxy Load Balancer** | A load balancer performing active health checks |
| 3️⃣ | **Python Monitoring Tool** | A tool that quantifies uptime and response time across a simulated node failure |

By stopping and restarting a node while traffic was flowing, you observed firsthand how a load balancer's health checks detect failure and reroute traffic without interrupting service, and how monitoring data can be used to verify that an HA design meets its availability goals.

> 🎯 **Focus:** Proving high availability with observed behavior and measured data, not assumptions.

---

## 🛠️ Key Skills Practiced

These patterns are exactly what a production HA cluster relies on:

| Pattern | Description |
|---------|-------------|
| 🗄️ **Shared State** | Multiple application nodes using a single shared PostgreSQL database |
| ❤️‍🩹 **Health-Checked Load Balancing** | HAProxy detecting failed nodes and rerouting traffic automatically |
| 📊 **Continuous Monitoring** | Measuring uptime and response time to verify availability goals |

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| **High Availability (HA)** | A design that keeps service running through node failures |
| **Shared PostgreSQL Database** | Common state store reachable by multiple application nodes |
| **HAProxy** | Load balancer distributing traffic across application nodes |
| **Active Health Checks** | Probes that detect failed nodes so traffic can be rerouted |
| **Failover** | Rerouting traffic away from a failed node without interrupting service |
| **Uptime and Response Time** | Metrics used to verify that an HA design meets its availability goals |

---

## 🌍 Real-World Applications

| Scenario | Description |
|----------|-------------|
| 🏢 **Controller and Hub HA Clusters** | Production Automation Controller and Automation Hub clusters rely on shared state, health-checked load balancing, and continuous monitoring |
| 📈 **Scaling** | A practical foundation for scaling real enterprise Ansible Platform deployments |
| 🔧 **Troubleshooting** | A practical foundation for troubleshooting real enterprise Ansible Platform deployments |

---

## 🏁 Conclusion

You now have a practical foundation in the building blocks of an Ansible Automation Platform HA deployment — shared state, health-checked load balancing, and continuous monitoring — and have verified firsthand that traffic keeps flowing through a node failure.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Education-0A66C2?style=for-the-badge)

**Happy Automating! 🔁**

</div>
