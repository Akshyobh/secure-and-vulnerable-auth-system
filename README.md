# Development and Security Assessment of a Web-Based Authentication System

## Overview

This project demonstrates both **secure** and **vulnerable** implementations of a web-based authentication system using **Flask** and **MySQL**.

The purpose of including two versions is to study common web application vulnerabilities and compare them with their secure implementations.

- **Secure Version** – Implements security best practices such as password hashing, input validation, session management, and protection against common attacks.
- **Vulnerable Version** – Intentionally contains security flaws for educational purposes, allowing users to understand how attacks such as SQL Injection and Cross-Site Scripting (XSS) work.

---

> **⚠️ Educational Purpose**
>
> The vulnerable implementation included in this repository is intentionally insecure and has been developed **solely for educational, research, and security testing purposes**. It is provided to demonstrate common web application vulnerabilities such as **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)**, and to compare them with their secure implementations.
>
> **Do not deploy the vulnerable version in a production environment.** It is intentionally designed to contain security weaknesses and should only be used in a controlled learning or testing environment.

---

# Technologies Used

- Python 3
- Flask
- MySQL
- HTML
- CSS
- JavaScript

---

# Prerequisites

Before running the project, install the following:

1. Python 3.10 or later
2. MySQL Community Server
3. MySQL Workbench (Recommended)
4. Git (Optional, for cloning the repository)
5. Visual Studio Code (Recommended)

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Or download the ZIP file from GitHub and extract it.

---

## Step 2: Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

### macOS/Linux

```bash
python3 -m venv .venv
```

---

## Step 3: Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Step 1

Open **MySQL Workbench**.

---

## Step 2

Create a new database named:

```sql
login_record
```

Example:

```sql
CREATE DATABASE login_record;
```

---

## Step 3

Open the provided **login_record.sql** file.

OR

Go to:

```
Server
    ↓
Data Import
```

Select

```
Import from Self-Contained File
```

Choose:

```
login_record.sql
```

Select database:

```
login_record
```

Click:

```
Start Import
```

This will automatically create all required tables.

---

# Configure Database Connection

Open the following files:

- basic.py
- vul.py

Replace the database configuration with your own:

```python
host="localhost"
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
database="login_record"
```

Example:

```python
host="localhost"
user="root"
password="your_mysql_password"
database="login_record"
```

---

# Running the Project

## Secure Version

Run:

```bash
python basic.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Vulnerable Version

Stop the secure server if it is running.

Run:

```bash
python vul.py
```

Open:

```
http://127.0.0.1:5001
```

---

# Why Two Versions?

This project was developed as part of a security assessment to demonstrate the difference between an insecure authentication system and a properly secured implementation.

## Secure Version

Includes:

- Password Hashing
- Input Validation
- Session Management
- Protection against SQL Injection
- Protection against Cross-Site Scripting (XSS)
- Rate Limiting

---

## Vulnerable Version

Intentionally includes vulnerabilities such as:

- SQL Injection
- Cross-Site Scripting (XSS)
- Weak Input Validation

These vulnerabilities are included **only for educational purposes** to demonstrate how attackers exploit insecure applications and how those vulnerabilities can be mitigated.

**Do not deploy the vulnerable version in a production environment.**

---

# Project Structure

```
Login/
│
├── basic.py
├── vul.py
├── requirements.txt
├── login_record.sql
├── README.md
├── templates/
├── static/
└── .gitignore
```

---

# Author

**Akshyobh Kumar Mishra**

B.Tech Computer Science and Engineering

ITER, Siksha 'O' Anusandhan University