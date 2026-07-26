# 📊 Database Fundamentals

## 💼 Why Do Companies Use Databases?

Companies use databases to store, manage, and access data efficiently and securely.

### 🔑 Main Reasons:

- **Data Organization**  
  Keeps information structured (customers, orders, products, etc.)

- **Fast Data Access**  
  Retrieve specific data quickly, even from large datasets

- **Better Security**  
  Access control and permissions to protect sensitive data

- **Scalability**  
  Supports growth from small to very large amounts of data

- **Error Prevention**  
  Rules and constraints help maintain data integrity

---

## 📉 Problems with Using Excel as a Database

Although Excel is useful for analysis, it is not suitable for managing large or complex systems.

### 🚫 Main Issues:

- **Does Not Scale Well**  
  Performance drops with large volumes of data

- **Duplicate Data**  
  No strict control, leading to redundancy

- **Lack of Data Integrity**  
  Easy to modify or delete data incorrectly

- **Difficult to Automate**  
  Limited integration with systems and applications

- **Weak Security**  
  Limited control over access and data protection

---

## 🧠 What is SQL?

**SQL (Structured Query Language)** is the language used to communicate with databases.

### 💡 With SQL, you can:

- **Create tables**
```sql
CREATE TABLE users (
  id INT,
  name VARCHAR(100)
);
