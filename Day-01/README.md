- Most of the app are deployed on linux server.
- windows/mac have rich UI
- But, EC2, VM don't come with the GUI.
- So, to perform day-to-day tasks we need to write shell commands.
- .sh -> for shell scripting -> to get information about Linux system and do the automation.
- There can some instaces where we have to write script for window/linux. -> Python
- Complex programs, APIs, data manupulaiton -> Python
- Talk to API of github repo and get the author of the list of issues created.
- Python has rich modules so, the above task can be easily done with python.
- For shell scripting -> curl to interact with API that returns JSON -> use 'jq' to parse the json -> but not robust as python modules.

- So, for the system related activities -> shell scripting
- Advanced concept/tasks -> python


1. python3 --version
2. python3 main.py
3. alias py=python3 -> py main.py



You’re basically describing **when and why we use Shell scripting vs Python in real-world DevOps / backend environments**. Let’s break your points into a clear, connected explanation so the whole picture makes sense.

---

## 🧠 1. Why most apps run on Linux servers

* Production systems (cloud, servers, containers) mostly run on Linux.
* Platforms like AWS EC2, Azure VM, GCP VM **don’t give GUI by default**.
* Reason:

  * Lightweight (no UI overhead)
  * More secure
  * Easier to automate
  * Better performance

👉 So instead of clicking buttons, you interact using:

* Terminal
* Commands
* Scripts

---

## ⚙️ 2. Why Shell Scripting (.sh) is needed

Shell scripting is used for **system-level tasks and automation**.

### Typical use cases:

* Creating users, folders
* Managing processes
* Deployment scripts
* Backup automation
* Monitoring logs

### Example:

```bash
#!/bin/bash
echo "System Info:"
uname -a
df -h
```

👉 This runs directly on Linux without needing extra setup.

---

## ⚡ 3. Why Python is introduced

Shell scripting is powerful, but **limited for complex logic**.

That’s where Python comes in.

### Use Python when:

* Logic becomes complex
* You need data processing
* You interact with APIs
* You need better error handling

---

## 🔗 4. Example: Calling GitHub API

### ❌ Using Shell (less robust)

```bash
curl https://api.github.com/repos/user/repo/issues | jq '.[].user.login'
```

Problems:

* Hard to maintain
* Error handling is weak
* Complex parsing gets messy

---

### ✅ Using Python (clean & scalable)

```python
import requests

url = "https://api.github.com/repos/user/repo/issues"
response = requests.get(url)

for issue in response.json():
    print(issue["user"]["login"])
```

Advantages:

* Clean code
* Better readability
* Exception handling
* Rich libraries (`requests`, `pandas`, etc.)

---

## 🆚 5. Shell vs Python (Clear Difference)

| Feature        | Shell Script           | Python              |
| -------------- | ---------------------- | ------------------- |
| Best for       | System tasks           | Complex logic       |
| Speed          | Faster for simple ops  | Slightly slower     |
| Readability    | Hard for large scripts | Very readable       |
| API handling   | Weak (`curl + jq`)     | Strong (`requests`) |
| Error handling | Limited                | Advanced            |
| Scalability    | Poor                   | Excellent           |

---

## 🧩 6. Rule of Thumb (Very Important)

* 🟢 Use **Shell scripting** → OS-level, automation, DevOps tasks
* 🔵 Use **Python** → APIs, data processing, complex workflows

---

## 🖥️ 7. Python Commands Explained

### Check Python version

```bash
python3 --version
```

👉 Ensures Python is installed and version is correct

---

### Run a Python file

```bash
python3 main.py
```

---

### Create alias (shortcut)

```bash
alias py=python3
```

Now you can run:

```bash
py main.py
```

👉 Saves time and improves workflow

---

## 🔄 8. Real DevOps Scenario

### Deployment pipeline example:

* Shell script:

  * Pull code
  * Build Docker image
  * Restart server

* Python script:

  * Fetch GitHub data
  * Analyze logs
  * Send alerts

👉 Both are used together, not separately.

---

## 🎯 Final Insight

Think like this:

> Shell is for **“doing things in the system”**
> Python is for **“thinking, processing, and building logic”**

---
