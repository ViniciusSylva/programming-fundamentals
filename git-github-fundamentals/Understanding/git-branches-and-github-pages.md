## ⚙️ Lessons 12 & 13 — Git Branches & Hosting with GitHub Pages

## 🌿 Lesson 12 — Git Branches Made Easy with Examples

This lesson explained the concept of branches in Git, demonstrating how to create, switch, merge, and manage different lines of development without impacting the main code.

### 🔑 Key Points

- **What are Branches**:
  - Independent development lines that act as branches or parallel copies of a project
  - Allow testing new features, fixing bugs, or experimenting without risking the main branch (`main` or `master`)
- **Management Commands**:
  - List branches: `git branch`
  - Create a new branch: `git branch <branch-name>`
  - Switch branches: `git checkout <branch-name>` or `git switch <branch-name>`
  - Create and switch simultaneously: `git checkout -b <branch-name>` or `git switch -c <branch-name>`
  - Delete a branch: `git branch -d <branch-name>`
- **Merging Changes**:
  - Combine code from a feature branch into the primary branch using `git merge <branch-name>`
  - Resolve merge conflicts when different branches modify the exact same lines of code

### 💡 Concept

- **Code Isolation**:
  - Developing directly on the `main` branch poses stability risks
  - Using branches ensures that `main` only contains stable, fully tested code

---

## 🌐 Lesson 13 — Free Hosting with GitHub Pages

This lesson taught how to host and publish static websites (HTML, CSS, and JavaScript) directly to the web for free using **GitHub Pages**.

### 🔑 Key Points

- **What is GitHub Pages**:
  - Static site hosting service provided directly from a GitHub repository
  - Generates a free public URL formatted as `https://<username>.github.io/<repository>/`
- **How to Set It Up**:
  - Ensure the repository contains an `index.html` file in the root or `/docs` folder
  - Navigate to repository settings (`Settings > Pages`)
  - Select the publishing source by picking the branch (e.g., `main`) and folder (`/root` or `/docs`)
  - Save and wait for the deployment process to complete
- **Additional Features**:
  - Custom domain support
  - Native integration with static site generators like Jekyll

---

## 🛠️ Best Practices

### 1. Branching Workflow

- Always create dedicated branches for new features or bug fixes (`feature/nav-bar`, `fix/header-issue`)
- Merge into `main` only after changes have been tested

### 2. Publishing on GitHub Pages

- Always name your primary HTML file `index.html`
- Use relative file paths for styles, scripts, and media to prevent broken links on the hosted site

---

## 📌 Important Concepts

- Git branches are lightweight pointer references to commits, making creation and switching nearly instantaneous
- GitHub Pages automatically redeploys your live site whenever a new `git push` is executed on the publishing branch

---

## 🚀 Summary

These lessons focused on:

- Mastering Git branches for isolated and safe feature development
- Understanding code merging and conflict resolution
- Publishing live web projects for free using GitHub Pages

Branch → Development → Merge to Main → GitHub Pages → Live Site