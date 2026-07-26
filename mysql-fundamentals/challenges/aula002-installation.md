# Lesson 02 – Installing and Configuring the MySQL Environment

## 📌 Context

When joining a real-world project, one of a developer's first tasks is configuring the local environment to work with the company's database.

Without this, it is impossible to run queries, test features, or develop data-dependent systems.

---

## 🎯 Objective

Prepare the development environment to use MySQL locally, ensuring that any other developer can replicate the process.

---

## 🛠️ Tools Used

* MySQL Server
* MySQL Workbench (optional)
* VS Code
* (Alternative) XAMPP or WAMP

---

## ⚙️ Step-by-Step Installation

### 1. Install MySQL

* Visit the official MySQL website.
* Download the MySQL Installer.
* Choose the standard installation (Developer Default or Server Only).
* Set a password for the root user.

---

### 2. Verify if MySQL is Running

After installation, open your terminal and run:

mysql -u root -p

Enter the password you configured.

If you see something like:

mysql>

It means the database is running correctly.

---

### 3. Create a Test Database

CREATE DATABASE test_db;
USE test_db;

---

### 4. Create a Simple Table

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

---

### 5. Insert Test Data

INSERT INTO users (name) VALUES ('Vinicius');

---

### 6. Query the Data

SELECT * FROM users;

---

## 💻 Using with VS Code

To work more productively:

1. Install the SQLTools extension.
2. Create a connection to MySQL.
3. Run .sql files directly through VS Code.

---

## 🧠 Important Notes

* MySQL must be running to execute queries.
* .sql files are just scripts, not the database itself.
* The database runs locally or on a server.

---

## 📌 Conclusion

With the environment configured, you can now:

* Create databases
* Run SQL queries
* Test applications that use a database

This step is essential in any real-world project involving data.

---

## 👨‍💻 Author

Vinicius Silva