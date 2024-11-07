# DjangoStore

<p>DjangoStore is an application that gives users opportunities to create orders from listed product.</p>
<p>site has user registration and authorization features. also visitor can switch between languages from main page and also send messages from contact page to our admin.</p>
<p>after successful registration and authorization user can choose one of the products, add it in to the cart and then order from our store.</p>
<p>currently site fully supports two languages. English and Gerogian</p>

### there are next links on our site

1. **localhost/ main page. displays featured products.**
2. **localhost/category/category_slug/ lists products corresponding to category.**
3. **localhost/product/product_slug/ product detailed page.**
4. **localhost/contact/ contact page.**
5. **localhost/order/cart displays cart page.**
6. **localhost/order/checkout/ displays checkout page.**
7. **localhost/user/register/ for handling registration.**
8. **localhost/user/login/ for handling user authorization.**
9. **localhost/user/logout/ for handling user logout process.**

##### after succesful log in you can visit following url to add or modifie translations for translatable fields from the dashboard.

10. **localhost/rosetta/**

## you can either log in using django admin or from the site login page.

<p>Site has superuser (user:admin, pass:admin123).</p>
<p>Site also has testuser (user:testuser, pass:passfortestuser).</p>

##### Notice: newly created users has no ability to do anything from admin dashboard. users that are already registered have visitor statuses. newly registered users should get visitor status by admin to see content at dashboard.

### Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_
- <img src="readme/assets/django.png" width="25" style="position: relative; top: 8px" /> _Django @5.X and up_

#

### Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NikaKhiz/django-store.git
   cd django-store
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

   or

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install django and necessary libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Run scripts**:

- Simply run the `python3 manage.py runserver` command :

```bash
python manage.py runserver
```

or

```bash
python3 manage.py runserver
```

### the code above will start development server and you should be good to go. you can visit site on [localhost](http://127.0.0.1:8000/)!!!

##### in case u want to test custom management command that displays featured products in cli run following command in a root dir

```bash
python manage.py featured_products
```

or

```bash
python3 manage.py featured_products
```
