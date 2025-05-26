# 📝 Django Todo List API

This is a simple **Todo List application** built with **Django** and **Django REST Framework**. It supports both web-based UI and REST API endpoints for managing tasks.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) tasks
- Web interface using Django templates
- RESTful API with:
  - Filtering
  - Searching
  - Pagination
  - Sorting
- API Versioning support (`/api/v1/`, `/api/v2/`)

---

## 📦 Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (default DB)

---

## 🛠️ Installation

1. **Clone the repository**


git clone https://github.com/banothjalandhar/todo-django-api.git
cd todo-django-api
Create virtual environment (optional but recommended)

python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
Install dependencies


pip install -r requirements.txt
Apply migrations


python manage.py migrate
Run the server

python manage.py runserver
🌐 Endpoints
Web UI
/ → Task list

/create/ → Add new task

/update/<id>/ → Edit task

/delete/<id>/ → Delete task

API Endpoints
Method	Endpoint	Description
GET	/api/v1/tasks/	List all tasks
GET	/api/v1/tasks/1/	Retrieve a task
POST	/api/v1/tasks/	Create new task
PUT	/api/v1/tasks/1/	Update task
DELETE	/api/v1/tasks/1/	Delete task

Supports:
✅ Pagination
✅ Search (?search=title)
✅ Ordering (?ordering=title)

📁 Folder Structure

todo_project/
│
├── tasks/                  # App with views, models, serializers, urls
├── todo_project/           # Main Django project settings
├── templates/              # HTML templates
├── db.sqlite3              # Default DB
└── manage.py
📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Developed by [Banoth Jalandhar](https://github.com/banothjalandhar)
