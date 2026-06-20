# AureMind

AureMind is an **AI-assisted Personal Manager web app** built as a college software engineering project. It combines note taking, task tracking, and productivity tools into a simple and intuitive interface to help users organize their daily activities and ideas.

##  Overview

AureMind was developed by **Group 10** of the Software Engineering class at Delhi University:

* Prashant Nath
* Demas Fadel Anggara

This project draws inspiration from tools like **Notion**, **Obsidian**, and other productivity applications. It was created to fulfill academic requirements and demonstrate full-stack development skills.

##  Features

* User authentication and profile management
* Create, edit, and delete notes
* Organize tasks and personal schedules
* Simple and responsive UI
* Django-powered backend

##  Tech Stack

| Layer    | Technology     |
| -------- | -------------- |
| Backend  | Python, Django |
| Frontend | HTML, CSS      |
| Database | SQLite         |
| Tools    | Git, GitHub    |

##  Project Structure

```
AureMind/
├── college_project/
├── Django/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

##  Installation

### 1. Clone the repository

```
git clone https://github.com/AureMindOrg/AureMind.git
cd AureMind
```

### 2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Apply migrations

```
python manage.py migrate
```

### 5. Run the development server

```
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

##  Usage

* Register or log in as a user
* Create and manage notes
* Track tasks and organize daily activities

##  Contributing

This project was created primarily for academic purposes, but contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

