<div align="center">

# 🧩 Jinja2 Switch & Router Configuration Generation

### Templates • YAML Data • Python Validation • Troubleshooting

![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Network Automation](https://img.shields.io/badge/Network-Automation-0078D4?style=for-the-badge&logo=cisco&logoColor=white)

</div>

---

## 📑 Table of Contents

- [📋 Lab Summary](#-lab-summary)
- [🎯 Objectives Met](#-objectives-met)
- [🛠️ Key Skills Practiced](#️-key-skills-practiced)
- [📚 Key Concepts](#-key-concepts)
- [🚀 Next Steps](#-next-steps)

---

## 📋 Lab Summary

In this lab, you built a complete **Jinja2-based configuration generation workflow**. You authored reusable switch and router templates, supplied them with structured YAML data, and confirmed through automated Python tooling that the same template can correctly produce distinct, valid configurations for different devices.

---

## 🎯 Objectives Met

All six objectives stated at the start of the lab were met:

| # | Objective | Status |
|---|-----------|--------|
| 1 | Understand Jinja2 fundamentals | ✅ |
| 2 | Create dynamic templates | ✅ |
| 3 | Pass variables dynamically | ✅ |
| 4 | Test templates across multiple device types | ✅ |
| 5 | Apply organizational best practices (separate directories for templates, data, and output) | ✅ |
| 6 | Practice systematic troubleshooting | ✅ |

---

## 🛠️ Key Skills Practiced

**Core Jinja2 mechanics:**

- ✅ Variable substitution
- ✅ `{% for %}` loops over lists of interfaces and VLANs
- ✅ `{% if %}` conditionals for branching logic such as access vs. trunk ports, or OSPF vs. static routing
- ✅ Filters such as `join` and `default`

**Validation and troubleshooting** (essential when templates fail silently or produce incomplete output):

- ✅ Validating template syntax before rendering
- ✅ Extracting and cross-checking variable names against data files
- ✅ Using diff-based comparison and structural statistics to verify generated output meets expectations

---

## 📚 Key Concepts

| Concept | Description |
|---------|-------------|
| **Jinja2 Template** | A reusable text file with placeholders and logic that renders into a device configuration |
| **Variable Substitution** | Replacing placeholders with values supplied from structured YAML data |
| **`{% for %}` Loop** | Iterates over lists such as interfaces and VLANs |
| **`{% if %}` Conditional** | Branches configuration output, e.g. access vs. trunk ports or OSPF vs. static routing |
| **Filters (`join`, `default`)** | Transform values or supply fallbacks inside a template |
| **Syntax Validation** | Checking template correctness before rendering |
| **Diff-Based Verification** | Comparing generated configurations to confirm expected output |
| **Templates/Data/Output Separation** | Organizing templates, data, and generated files in dedicated directories |

---

## 🚀 Next Steps

- 🔗 **Integrate with Ansible** using the `template` module, which uses the same Jinja2 syntax you practiced here but adds inventory-driven variable management and idempotent deployment to real or simulated network devices in a lab environment
- 🧪 **Explore advanced Jinja2 features:**
  - Custom filters
  - Macros for repeated configuration blocks
  - Template inheritance with `{% extends %}` and `{% block %}`
  - Stricter undefined-variable handling (`StrictUndefined`) to catch data/template mismatches earlier in your workflow

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Education-0A66C2?style=for-the-badge)

**Created for Al Nafi Training Labs**

</div>
