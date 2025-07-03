# 🍽️ GastroSal

**GastroSal** is a web application built with Django that allows hospitality workers to anonymously and collaboratively share and view salary information.

The goal is to promote transparency and create an open database about wages, employment conditions, and roles within the gastronomy sector.

---

## 🚀 Features

- 📊 Real-time salary visualization by job position.
- 🔍 Filtering by position, currency, and contract type.
- 📝 Anonymous salary submission form.
- 🔒 Admin panel with authentication (Django Admin).
- 🗃️ PostgreSQL database (or local).

---

## 🛠️ Technologies

- Python 3.13  
- Django 5.2.3  
- Bootstrap (via CDN)  
- PostgreSQL (Railway)  
- HTML5 & CSS3  

---

## 📷 Screenshots

### Main Page – Submit Salary

![Submit your salary]()

### Filterable Data List

![Data list]()

---

## ⚙️ How to Run the Project

1. **Clone the repository:**

```bash
git clone https://github.com/matiassenia/gastrosal.git
cd gastrosal
```

2. **Create a virtual environment and install dependencies:**

```bash
python -m venv env
env\Scripts\activate    # Windows
# source env/bin/activate  # Linux/Mac

pip install -r requirements.txt
```

3. **Set up environment variables:**

Create a `.env` file (or set environment variables directly) with the following content:

```
SECRET_KEY=your_secret_django_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgresql://user:password@localhost:5432/gastrosal
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000
PORT=8000
```

4. **Apply migrations and create a superuser (optional):**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Run the development server:**

```bash
python manage.py runserver
```

---

## ✅ Current Status

- [x] Data submission via form  
- [x] Filterable list  
- [x] Functional admin panel  
- [ ] Custom validations  
- [ ] List pagination  
- [ ] Add charts or visualizations  

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or fork the repository and propose changes via pull request.

---

## 📬 Contact

Developed by [Matías Senia](https://www.linkedin.com/in/matiassenia/)  
📧 matiasseniadev@gmail.com

---

## 🧑‍💻 License

This project is open source under the MIT License.
