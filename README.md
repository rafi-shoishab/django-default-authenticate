# django-authenticate (default)
This project demonstrates a basic Django Authentication System using Django's built-in authentication framework.

## deafult user model
```
| Field        | Type          | Description           |
| ------------ | ------------- | --------------------- |
| username     | CharField     | Required, unique      |
| first_name   | CharField     | Optional              |
| last_name    | CharField     | Optional              |
| email        | EmailField    | Optional              |
| password     | CharField     | Hashed password       |
| is_staff     | BooleanField  | Admin site access     |
| is_active    | BooleanField  | Active user or not    |
| is_superuser | BooleanField  | Full permissions      |
| last_login   | DateTimeField | Last login time       |
| date_joined  | DateTimeField | Account creation time |

```
🏗 Project Structure Overview
```
django-authenticate/
│
├── core/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/              # Authentication app
│   ├── views.py           # Login, Register, Logout logic
│   ├── urls.py            # App URL routing
│   ├── models.py
│   └── migrations/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── include/
│
├── static/                # CSS / JS files
│
├── manage.py
└── requirements.txt
```
## ⚡ 1. Setup Django (Run Project)
### Clone Repository
```
git clone https://github.com/rafi-shoishab/django-authenticate.git
cd django-authenticate
```
### Create Virtual Environment
Mac / Linux
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows
```
python -m venv .venv
.venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
Apply Migrations
```
python manage.py migrate
```
Run Development Server
```
python manage.py runserver
```
Open Browser
```
http://127.0.0.1:8000
```
## 🔐 2. User Registration System

Users can create new accounts through the registration form.

### Registration View

```
📄 accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")
```
## 🔑 3. User Login System

Django provides built-in functions to authenticate users.

### Login View

📄 accounts/views.py

```
📄 accounts/views.py

from django.contrib.auth import authenticate, login

def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html") 
```
## 🚪 4. Logout System

Logout removes the user session from the server.

### Logout View

```
📄 accounts/views.py

from django.contrib.auth import logout

def log_out(request):
    logout(request)
    return redirect("login")
```

## 🔒 5. Protected Routes

Some pages should only be accessible for logged-in users.

### Django provides the login_required decorator.
```
📄 accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html")
```

## 🌐 6. URL Routing

### App URLs

```
📄 accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.log_out, name="logout"),
]
```
### Project URLs
```
📄 core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```
## 🎨 7. Template System

Templates are used to render HTML pages.

```
📄 templates/login.html

<form method="POST">
    {% csrf_token %}

    <input type="text" name="username" placeholder="Username">

    <input type="password" name="password" placeholder="Password">

    <button type="submit">
        Login
    </button>
</form>
```

## 🔁 Django Authentication Flow
```
User Request
     ↓
urls.py
     ↓
views.py
     ↓
authenticate()
     ↓
login()
     ↓
Session Created
     ↓
User Logged In
```

🛠 Django Admin Panel
Apply Migrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser

Login Admin Panel
http://127.0.0.1:8000/admin/
🔧 Git Workflow (Quick Guide)
First Time
git add .

git commit -m "initial commit"

git push -u origin main

Daily Workflow
git pull

git add .

git commit -m "update message"

git push


readme markdown dorkar git er repo link dile sob file read kore banay dite parba>

হ্যাঁ, পারব 🙂
তুমি যদি GitHub repo link দাও, আমি—

পুরো repository structure দেখব

গুরুত্বপূর্ণ files (README না থাকলে code, folders, requirements, etc.) analyze করব

তারপর তোমার project এর জন্য professional README.md বানিয়ে দেব।

README তে সাধারণত আমি এগুলো দিই:

📌 Project Title

📖 Description

✨ Features

🛠️ Tech Stack

📂 Project Structure

⚙️ Installation / Setup

▶️ How to Run

📷 Screenshots (optional)

🤝 Contributing

📜 License

তুমি চাইলে আমি এটাও করতে পারি:

GitHub-ready markdown formatting

Badges (Python, Django, License, etc.)

API / Model explanation

Professional portfolio style README

✅ এখন শুধু তোমার GitHub repo link দাও।
আমি দেখে complete README.md markdown লিখে দেব।


https://github.com/rafi-shoishab/django-authenticate

give me in one file, submit ready, copy paste. & follow this style bellow

# Django Intro 🚀 (Template, Admin Panel & Media)

This project demonstrates the **basic to intermediate workflow of Django**.
It is designed for beginners to understand how Django works internally, including
**default Admin Panel exploration and media (image upload) handling**.

---

## 🎯 Learning Objectives

By working with this project, you will learn:

- Django project setup
- Creating Django apps
- URL routing
- HTTP response handling
- Template rendering
- Django request → response lifecycle
- Django default admin panel exploration
- Model registration using admin decorators
- Media (image upload) configuration

---

## 🏗 Project Structure Overview

django-intro-template-admin-media/
│
├── core/
│   ├── settings.py        # Project settings (MEDIA_ROOT, MEDIA_URL)
│   ├── urls.py            # URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── navigation/            # Django app
│   ├── models.py          # Database models
│   ├── admin.py           # Admin panel customization
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/             # HTML templates
│   └── include/
│
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded files (images)
│
├── manage.py
└── requirements.txt



---

## 📌 Project Overview

This project shows how:

- Django handles HTTP requests
- Views return responses
- URLs connect to views
- Templates render HTML pages
- Admin panel manages database records
- Media files are uploaded and served

---

# ⚡ 1. Setup Django (Run Project)

## Clone Repository

bash

git clone https://github.com/rafi-shoishab/django-intro.git

cd django-intro

### Create Virtual Environment

Mac / Linux

python3 -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv 

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Development Server

python manage.py runserver

### Open browser:

http://127.0.0.1:8000

# 🌐 2. HTTP Response Implementation

## Step 2.1 — Create Django App
python manage.py startapp navigation

## Step 2.2 — Register App

📄 core/settings.py

INSTALLED_APPS = [
    ...
    'navigation',
]

## Step 2.3 — Create View

📄 navigation/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")


## Step 2.4 — App URLs

📄 navigation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]


## Step 2.5 — Project URLs

📄 core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigation.urls')),
]


Test:

http://127.0.0.1:8000/hello/

# 🎨 3. Template Rendering

## Step 3.1 — Create Template

📄 templates/index.html

<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django Template 🎉</h1>
</body>
</html>


## Step 3.2 — Configure Templates

📄 core/settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]


## Step 3.3 — Render Template

📄 navigation/views.py

from django.shortcuts import render

def home(request):
    return render(request, "index.html")


🔁 Django Request → Response Flow
User Request
     ↓
urls.py
     ↓
views.py
     ↓
Template Rendering
     ↓
HTTP Response

# 🛠 4. Django Admin Panel Exploration

## Step 4.1 — Apply Migrations
python manage.py migrate

## Step 4.2 — Create Superuser
python manage.py createsuperuser

Login:

http://127.0.0.1:8000/admin/

## 📦 Step 4.3 — Create Model

📄 navigation/models.py

from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    std_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    image = models.ImageField(upload_to='student_img/', null=True, blank=True)

    def __str__(self):
        return self.name


## 🧩 Step 4.4 — Register Model Using Decorator

📄 navigation/admin.py

from django.contrib import admin
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'age', 'email', 'dob', 'dept')
    search_fields = ('name', 'std_id', 'email')
    list_filter = ('dept',)
    ordering = ('id',)


# 🖼 5. Media (Image Upload) Configuration

## Step 5.1 — Media Settings

📄 core/settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


## Step 5.2 — Serve Media Files

📄 core/urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Uploaded images will be stored in:

media/student_img/

# 🔧 Git Workflow (Quick Guide)

## First Time

git add .

git commit -m "initial commit"

git push -u origin main

## Daily Workflow

git pull

git add .

git commit -m "update message"

git push

### Recommended .gitignore

.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/

# 👨‍💻 Author

Rafiur Rahman Shoishab
GitHub: https://github.com/rafi-shoishab

## 📄 License

This project is created for educational purposes.


আমি তোমার GitHub repo django-authenticate দেখে তোমার দেওয়া স্টাইল ফলো করে একটা complete README.md (copy-paste ready) বানিয়ে দিলাম।
তুমি সরাসরি README.md file এ paste করে submit করতে পারবে।

Django Authentication System 🔐 (Login, Register & Logout)
This project demonstrates a basic Django Authentication System using Django's built-in authentication framework.

It shows how to implement:

User Registration

User Login

User Logout

Authentication based navigation

Protected routes for logged-in users

This project is designed for Django beginners who want to understand how authentication works in Django.

🎯 Learning Objectives
By working with this project, you will learn:

Django authentication system

User registration system

Login & logout implementation

Form handling in Django

Template rendering

Django authentication decorators

Redirecting users after login/logout

Django request → response flow

🏗 Project Structure Overview
django-authenticate/
│
├── core/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/              # Authentication app
│   ├── views.py           # Login, Register, Logout logic
│   ├── urls.py            # App URL routing
│   ├── models.py
│   └── migrations/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── include/
│
├── static/                # CSS / JS files
│
├── manage.py
└── requirements.txt
📌 Project Overview
This project shows how:

Users can register new accounts

Registered users can login

Authenticated users can access protected pages

Users can logout safely

Django handles session based authentication

⚡ 1. Setup Django (Run Project)
Clone Repository
git clone https://github.com/rafi-shoishab/django-authenticate.git

cd django-authenticate
Create Virtual Environment
Mac / Linux
python3 -m venv .venv
source .venv/bin/activate
Windows
python -m venv .venv
.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Apply Migrations
python manage.py migrate
Run Development Server
python manage.py runserver
Open Browser
http://127.0.0.1:8000
🔐 2. User Registration System
Users can create new accounts through the registration form.

Registration View
📄 accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")
🔑 3. User Login System
Django provides built-in functions to authenticate users.

Login View
📄 accounts/views.py

from django.contrib.auth import authenticate, login

def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")
🚪 4. Logout System
Logout removes the user session from the server.

Logout View
📄 accounts/views.py

from django.contrib.auth import logout

def log_out(request):
    logout(request)
    return redirect("login")
🔒 5. Protected Routes
Some pages should only be accessible for logged-in users.

Django provides the login_required decorator.

📄 accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html")
🌐 6. URL Routing
App URLs
📄 accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.log_out, name="logout"),
]
Project URLs
📄 core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
🎨 7. Template System
Templates are used to render HTML pages.

Example:

📄 templates/login.html

<form method="POST">
    {% csrf_token %}

    <input type="text" name="username" placeholder="Username">

    <input type="password" name="password" placeholder="Password">

    <button type="submit">
        Login
    </button>
</form>
🔁 Django Authentication Flow
User Request
     ↓
urls.py
     ↓
views.py
     ↓
authenticate()
     ↓
login()
     ↓
Session Created
     ↓
User Logged In
🛠 Django Admin Panel
Apply Migrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Login Admin Panel
http://127.0.0.1:8000/admin/
🔧 Git Workflow (Quick Guide)
First Time
git add .

git commit -m "initial commit"

git push -u origin main
Daily Workflow
git pull

git add .

git commit -m "update message"

git push
📄 Recommended .gitignore
.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/


readme markdown dorkar git er repo link dile sob file read kore banay dite parba>

হ্যাঁ, পারব 🙂
তুমি যদি GitHub repo link দাও, আমি—

পুরো repository structure দেখব

গুরুত্বপূর্ণ files (README না থাকলে code, folders, requirements, etc.) analyze করব

তারপর তোমার project এর জন্য professional README.md বানিয়ে দেব।

README তে সাধারণত আমি এগুলো দিই:

📌 Project Title

📖 Description

✨ Features

🛠️ Tech Stack

📂 Project Structure

⚙️ Installation / Setup

▶️ How to Run

📷 Screenshots (optional)

🤝 Contributing

📜 License

তুমি চাইলে আমি এটাও করতে পারি:

GitHub-ready markdown formatting

Badges (Python, Django, License, etc.)

API / Model explanation

Professional portfolio style README

✅ এখন শুধু তোমার GitHub repo link দাও।
আমি দেখে complete README.md markdown লিখে দেব।


https://github.com/rafi-shoishab/django-authenticate

give me in one file, submit ready, copy paste. & follow this style bellow

# Django Intro 🚀 (Template, Admin Panel & Media)

This project demonstrates the **basic to intermediate workflow of Django**.
It is designed for beginners to understand how Django works internally, including
**default Admin Panel exploration and media (image upload) handling**.

---

## 🎯 Learning Objectives

By working with this project, you will learn:

- Django project setup
- Creating Django apps
- URL routing
- HTTP response handling
- Template rendering
- Django request → response lifecycle
- Django default admin panel exploration
- Model registration using admin decorators
- Media (image upload) configuration

---

## 🏗 Project Structure Overview

django-intro-template-admin-media/
│
├── core/
│   ├── settings.py        # Project settings (MEDIA_ROOT, MEDIA_URL)
│   ├── urls.py            # URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── navigation/            # Django app
│   ├── models.py          # Database models
│   ├── admin.py           # Admin panel customization
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/             # HTML templates
│   └── include/
│
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded files (images)
│
├── manage.py
└── requirements.txt



---

## 📌 Project Overview

This project shows how:

- Django handles HTTP requests
- Views return responses
- URLs connect to views
- Templates render HTML pages
- Admin panel manages database records
- Media files are uploaded and served

---

# ⚡ 1. Setup Django (Run Project)

## Clone Repository

bash

git clone https://github.com/rafi-shoishab/django-intro.git

cd django-intro

### Create Virtual Environment

Mac / Linux

python3 -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv 

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Development Server

python manage.py runserver

### Open browser:

http://127.0.0.1:8000

# 🌐 2. HTTP Response Implementation

## Step 2.1 — Create Django App
python manage.py startapp navigation

## Step 2.2 — Register App

📄 core/settings.py

INSTALLED_APPS = [
    ...
    'navigation',
]

## Step 2.3 — Create View

📄 navigation/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")


## Step 2.4 — App URLs

📄 navigation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]


## Step 2.5 — Project URLs

📄 core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigation.urls')),
]


Test:

http://127.0.0.1:8000/hello/

# 🎨 3. Template Rendering

## Step 3.1 — Create Template

📄 templates/index.html

<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django Template 🎉</h1>
</body>
</html>


## Step 3.2 — Configure Templates

📄 core/settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]


## Step 3.3 — Render Template

📄 navigation/views.py

from django.shortcuts import render

def home(request):
    return render(request, "index.html")


🔁 Django Request → Response Flow
User Request
     ↓
urls.py
     ↓
views.py
     ↓
Template Rendering
     ↓
HTTP Response

# 🛠 4. Django Admin Panel Exploration

## Step 4.1 — Apply Migrations
python manage.py migrate

## Step 4.2 — Create Superuser
python manage.py createsuperuser

Login:

http://127.0.0.1:8000/admin/

## 📦 Step 4.3 — Create Model

📄 navigation/models.py

from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    std_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    image = models.ImageField(upload_to='student_img/', null=True, blank=True)

    def __str__(self):
        return self.name


## 🧩 Step 4.4 — Register Model Using Decorator

📄 navigation/admin.py

from django.contrib import admin
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'age', 'email', 'dob', 'dept')
    search_fields = ('name', 'std_id', 'email')
    list_filter = ('dept',)
    ordering = ('id',)


# 🖼 5. Media (Image Upload) Configuration

## Step 5.1 — Media Settings

📄 core/settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


## Step 5.2 — Serve Media Files

📄 core/urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Uploaded images will be stored in:

media/student_img/

# 🔧 Git Workflow (Quick Guide)

## First Time

git add .

git commit -m "initial commit"

git push -u origin main

## Daily Workflow

git pull

git add .

git commit -m "update message"

git push

### Recommended .gitignore

.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/

# 👨‍💻 Author

Rafiur Rahman Shoishab
GitHub: https://github.com/rafi-shoishab

## 📄 License

This project is created for educational purposes.


আমি তোমার GitHub repo django-authenticate দেখে তোমার দেওয়া স্টাইল ফলো করে একটা complete README.md (copy-paste ready) বানিয়ে দিলাম।
তুমি সরাসরি README.md file এ paste করে submit করতে পারবে।

Django Authentication System 🔐 (Login, Register & Logout)
This project demonstrates a basic Django Authentication System using Django's built-in authentication framework.

It shows how to implement:

User Registration

User Login

User Logout

Authentication based navigation

Protected routes for logged-in users

This project is designed for Django beginners who want to understand how authentication works in Django.

🎯 Learning Objectives
By working with this project, you will learn:

Django authentication system

User registration system

Login & logout implementation

Form handling in Django

Template rendering

Django authentication decorators

Redirecting users after login/logout

Django request → response flow

🏗 Project Structure Overview
django-authenticate/
│
├── core/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/              # Authentication app
│   ├── views.py           # Login, Register, Logout logic
│   ├── urls.py            # App URL routing
│   ├── models.py
│   └── migrations/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── include/
│
├── static/                # CSS / JS files
│
├── manage.py
└── requirements.txt
📌 Project Overview
This project shows how:

Users can register new accounts

Registered users can login

Authenticated users can access protected pages

Users can logout safely

Django handles session based authentication

⚡ 1. Setup Django (Run Project)
Clone Repository
git clone https://github.com/rafi-shoishab/django-authenticate.git

cd django-authenticate
Create Virtual Environment
Mac / Linux
python3 -m venv .venv
source .venv/bin/activate
Windows
python -m venv .venv
.venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Apply Migrations
python manage.py migrate
Run Development Server
python manage.py runserver
Open Browser
http://127.0.0.1:8000
🔐 2. User Registration System
Users can create new accounts through the registration form.

Registration View
📄 accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")
🔑 3. User Login System
Django provides built-in functions to authenticate users.

Login View
📄 accounts/views.py

from django.contrib.auth import authenticate, login

def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")
🚪 4. Logout System
Logout removes the user session from the server.

Logout View
📄 accounts/views.py

from django.contrib.auth import logout

def log_out(request):
    logout(request)
    return redirect("login")
🔒 5. Protected Routes
Some pages should only be accessible for logged-in users.

Django provides the login_required decorator.

📄 accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html")
🌐 6. URL Routing
### App URLs
```
📄 accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.log_out, name="logout"),
]
```
### Project URLs
```
📄 core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```
## 🎨 7. Template System
Templates are used to render HTML pages.

Example:
```
📄 templates/login.html
<form method="POST">
    {% csrf_token %}

    <input type="text" name="username" placeholder="Username">

    <input type="password" name="password" placeholder="Password">

    <button type="submit">
        Login
    </button>
</form>
```
## 🔁 Django Authentication Flow
```
User Request
     ↓
urls.py
     ↓
views.py
     ↓
authenticate()
     ↓
login()
     ↓
Session Created
     ↓
User Logged In
```

## 🛠 Django Admin Panel
### Apply Migrations
python manage.py migrate
### Create Superuser
python manage.py createsuperuser
### Login Admin Panel
http://127.0.0.1:8000/admin/

## 🔧 Git Workflow (Quick Guide)

### First Time
```
git add .

git commit -m "initial commit"

git push -u origin main
```

### Daily Workflow

```
git pull

git add .

git commit -m "update message"

git push
```
## 📄 Recommended .gitignore
```
.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/
```
## 👨‍💻 Author
Rafiur Rahman Shoishab

GitHub:
https://github.com/rafi-shoishab

## 📜 License
This project is created for educational purposes to learn Django authentication.
