# [Flask Theme Argon](https://github.com/app-generator/flask-theme-argon)

Modern template for **Django Admin Interface** coded on top of **Argon Dashboard**, an open-source `Boostrap 5` design from `Creative-Tim`.


---
**[Flask Theme Argon](https://github.com/app-generator/flask-theme-argon)** - Modern Admin Interface for Flask.




## ✨ Quick Start

> 👉 Rename `env.sample` to `.env`

- Add `SECRET_KEY`

<br />

> 👉 Install dependencies

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Start the App

```bash
$ flask run
```

<br />


## ✨ Codebase structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- argon_app/__init__.py
   |-- argon_app/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- navigation-rtl.html  # RTL top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- sidebar-rtl.html     # RTL sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-rtl.html        # Used by RTL pages
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |    |-- pages/                    # UI kit pages
   |    |    |    |-- dashboard.html       # Index page
   |    |    |    |-- billing.html         # Billing page
   |    |    |    |-- tables.html          # Tables page
   |    |    |    |-- profile.html         # Profile page
   |    |    |    |-- virtual-reality.html # Virtula reality page
   |    |    |    |-- rtl.html             # RTL page
   |    |    |-- accounts/                 # Authentication pages
   |    |    |    |-- sign-in.html         # Sign In page
   |    |    |    |-- sign-up.html         # Sign Up page
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

