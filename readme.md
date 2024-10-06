# DjangoStore

<p>Application that will give users opportunities to take a look of listed products, see detailed information about specific items, purchase items, see order information and many more.</p>
<p>currently there is only 2 routes available, products and order routes.</p>

1. **localhost/ we display  products list view.**
2. **localhost/product/id (1,2etc..) displays specific product details view.**
3. **localhost/order displays order creation view.**
4. **localhost/order/id (1,2etc..) displays specific order details view.**

<p>Also site has one superuser (user:admin, pass:admin123). you can visit localhost/admin and log in to dashboard.</p>


### Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

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


### Project Structure

```bash
├─── djangostore
│   ├─── djangostore
│   ├─── order
│   ├─── readme
│   ├─── store
- .gitignore
- manage.py
- readme.md
- requirements.txt
```