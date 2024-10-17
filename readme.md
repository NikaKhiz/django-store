# DjangoStore

<p>Application that will give users opportunities to take a look of listed products, see detailed information about specific items, purchase items, see order information and many more.</p>
<p>currently there is only 2 main routes available, products and order routes.</p>

1. **localhost/ admin panel**
2. **localhost/category list all of the categoryes and products counts.**
3. **localhost/category/category_id/products products associated with current category.**
4. **localhost/product/product_slug product detailed page.**
5. **localhost/order displays order creation view.**
6. **localhost/order/id (1,2etc..) displays specific order details view.**

<p>Site has superuser (user:admin, pass:admin123). you can visit localhost/admin and log in to dashboard.</p>
<p>Site has test user aswell (user:testuser, pass:passfortestuser1).</p>
<p>
Test user has readgroup that a readonly group that gives the user access to see already existed products and categories 
</p>

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
