# Project X 
Group members: Mohammad Badri - 100003064
               A
               D
This repository contains the materials for **Project X**.  
- Presentation Slides: see [`slides/`](./slides/) folder  
- Notebooks: see [`notebooks/`](./notebooks/) folder
- Data: when you access correct data, place it in [`data/`](./data/) folder
- Results: the folder [`results/`](./result/) contains our figures and tables.
  
---
- Read more about this project on Medium: <Medium_Article_link>
---
## Collocation Network Nootebook
This notebook quantifies Raskolnikov’s social change in Crime and Punishment.
The text is split into early (first 10 chapters) and late (last 10 chapters).
A JSON alias library detects characters accurately, and co-occurrence within a ±40 token window is used to measure interaction strength.

Outputs:

Number of characters connected to Raskolnikov (degree)

Strength of interaction (weighted co-occurrence)

Interactive PyVis networks for early vs late chapters

Used to show a shift from isolation → engagement / recovery.
## 📑 Project Outline


---
## 🚀 Environment Setup

Before starting, please **fork this repository** and create a fresh Python virtual environment.  
All required libraries are listed in `requirements.txt`.

> ⚠️ If you encounter errors during `pip install`, try removing the version pinning for the failing package(s) in `requirements.txt`.  
> On Apple M1/M2 systems you may also need to install additional system packages (the “M1 shizzle”).

---

### macOS / Linux (bash/zsh)

```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (Git Bash)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

You’re now ready to run the session notebooks!

Deactivate the environment when you’re done:
```bash
deactivate
```
