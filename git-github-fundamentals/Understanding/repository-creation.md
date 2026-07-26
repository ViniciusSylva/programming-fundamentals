## 📘 Lesson 5 — Creating a Repository (CLI Approach)

In this lesson, the course demonstrates how to create a repository using GitHub Desktop.  
However, in this project, the same process was done using the **Git command line interface (CLI)** to reinforce real-world practices.

---

## 🎯 Objective

Understand how to create and configure a Git repository from scratch and connect it to GitHub.

---

## ⚙️ Steps Performed

### 1. Initialize local repository

git init

This command creates a new Git repository in the current folder.

---

### 2. Add files to staging area

git add .

All files are prepared to be committed.

---

### 3. Create first commit

git commit -m "chore: initial commit"

This records the first version of the project.

---

### 4. Rename default branch

git branch -M main

Ensures the repository uses "main" as the default branch.

---

### 5. Connect to remote repository (GitHub)

git remote add origin https://github.com/your-username/your-repo.git

Links the local repository to GitHub.

---

### 6. Push to GitHub

git push -u origin main

Sends the project to the remote repository.

---

## 🧠 Key Learnings

- How to create a repository using Git CLI  
- Difference between local and remote repositories  
- How to track files and create commits  
- How to connect a project to GitHub  

---

## 💡 Notes

Using CLI instead of GitHub Desktop provides:

- Better understanding of Git internals  
- More control over the workflow  
- A more professional and widely used approach  

---

## 🚀 Conclusion

This lesson established the foundation for working with Git repositories, allowing full control over versioning and integration with GitHub.