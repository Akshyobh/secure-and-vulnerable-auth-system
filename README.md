# Development and Security Assessment of a Web-Based Authentication System

## Description
A Flask and MySQL-based authentication system developed to demonstrate secure and vulnerable implementations of user authentication. The project includes user registration, login, application form submission, and security testing.

## Features
- User Registration
- User Login
- Password Hashing
- Session Management
- Application Form
- SQL Injection Demo (Vulnerable Version)
- Cross-Site Scripting (XSS) Demo
- Input Validation
- Secure Authentication
- Rate Limiting

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

## Requirements
- Python 3.x
- MySQL Server

## Installation

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Import `login_record.sql` into MySQL.
4. Open `basic.py` and update:

- Host
- Username
- Password
- Database Name

5. Run:

```bash
python basic.py
```

6. Open:

```
http://127.0.0.1:5000
```

## Project Structure

```
Login/
│── basic.py
│── vul.py
│── templates/
│── static/
│── requirements.txt
│── login_record.sql
└── README.md
```

## Author

Akshyobh Kumar Mishra