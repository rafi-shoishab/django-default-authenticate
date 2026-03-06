# django-authenticate (default)
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
