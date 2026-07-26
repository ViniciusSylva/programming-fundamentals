## ⚙️ Lessons 08 & 09 — Versioning Existing Projects & Issues with Pull Requests

## 📁 Versioning Existing Projects & `.gitignore`

This lesson focused on converting an unversioned project folder into a Git repository and preventing unwanted files from being tracked.

### 🔑 Key Points

- Converting existing projects:
  - Run `git init` inside the project folder
  - Turns a regular folder into a Git repository by creating a hidden `.git` folder
- Using `.gitignore`:
  - Ignores sensitive data, temporary files, logs, or local configurations
  - Must be created in the root folder before committing untracked files
- Local workflow for existing code:
  - `git status` to check untracked/modified files
  - `git add .` to stage changes
  - `git commit -m "initial commit"` to save a snapshot
- Pushing to GitHub:
  - Link remote: `git remote add origin <repository-url>`
  - Rename main branch: `git branch -M main`
  - Upload changes: `git push -u origin main`

### 💡 Concept

- Unversioned folders vs. Git repositories:
  - `git init` activates version control on legacy/existing files
- The role of `.gitignore`:
  - Keeps the remote repository clean and secure by excluding heavy dependencies or credentials

---

## 🎟️ Working with Issues & Pull Requests (PRs)

This lesson covered task tracking, bug reporting, and collaborative code reviews on GitHub.

### 🔑 Key Points

- Issues:
  - Track bugs, tasks, enhancements, and feature requests
  - Support labels (e.g., `bug`, `documentation`), assignees, and milestones
  - Serve as a discussion thread linked directly to the repository
- Pull Requests (PRs):
  - Proposed changes submitted from a branch/fork to the main branch
  - Enable peer code reviews and discussion before merging code
- Linking Issues to PRs:
  - Automatic closure of Issues using keywords in PRs (e.g., `Closes #1`, `Fixes #3`)

---

## 🛠️ Contribution Workflow

### 1. Documenting Tasks

- Create an **Issue** describing the problem or feature

### 2. Developing Solution

- Create a dedicated branch (`git checkout -b feature-branch`)
- Commit and push changes to remote (`git push origin feature-branch`)

### 3. Submitting Changes

- Open a **Pull Request** targeting `main`
- Reference the Issue ID in the description (`Closes #ID`)
- Review changes and perform the **Merge**

---

## 📌 Important Concepts

- Issues keep project management integrated into the codebase
- Pull Requests prevent untested or broken code from entering `main`
- Using closing keywords (`Closes #1`) automates repository management

---

## 🚀 Summary

These lessons focused on:

- Transforming existing projects into Git repositories
- Preventing unnecessary files from being tracked using `.gitignore`
- Organizing team tasks and bug reports using Issues
- Reviewing and integrating code changes using Pull Requests

Init → `.gitignore` → Issue → Branch → Pull Request → Merge