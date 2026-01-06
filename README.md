# Skillio Data & AI Engineering - Week 1

## Overview
This project contains the environment setup for the Data & AI Engineer course projects.

## Setup Instructions
### 1. Initialize the Local Project
* **Create the folder:** `mkdir Week1`
* **Navigate into it:** `cd Week1`
* **Open in VS Code:** `code .` *(Opens the current folder in the editor)*

### 2. Set Up the Virtual Environment (The "Bubble")
* **Create the venv:** `python -m venv venv`
* **Activate it:** `venv\Scripts\activate`

### 3. Create the .gitignore (The "Filter")
* **Create and open the file:** `code .gitignore`
* **Add the rule:** In the editor window, type `venv/` and `*.pdf` on separate lines, then save (**Ctrl + S**).

### 4. Install Libraries & Build Code
* **Install tools:** `pip install requests` (or pandas, etc.)
* **Install from list:** `pip install -r requirements.txt`
* **Write code:** `code main.py` *(Create your script file)*

### 5. Document the "Recipe" (requirements.txt)
* **Freeze dependencies:** `pip freeze > requirements.txt`
* **Purpose:** This allows others to recreate your exact setup.

### 6. Connect to GitHub (Version Control)
* **Initialize Git:** `git init`
* **Stage your files:** `git add .`
  > **Note:** Git will automatically ignore the `venv/` folder because of step 3.
* **Commit:** `git commit -m "Initial commit with project structure"`
* **Link to GitHub:** `git remote add origin <your-repository-url>`
* **Push:** `git push -u origin main`
