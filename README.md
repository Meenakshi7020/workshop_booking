# Workshop Booking

This is the **FOSSEE Workshop Booking** project.  
It is a Django-based web application for managing and viewing workshop details, featuring a modern UI with animated gradients and styled login page.

---

## Features

- Login page with animated gradient background and styled login box
- Responsive navbar and footer
- Quote section with animated gradient text
- Workshop listing and statistics pages
- Modern UI enhancements for better user experience

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Meenakshi7020/workshop_booking.git
Navigate to the project folder

cd workshop_booking


Create a virtual environment

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Apply database migrations

python manage.py migrate


Run the development server

python manage.py runserver


Open in your browser

http://127.0.0.1:8000

Project Structure
workshop_booking/
├── workshop_app/        # Django app
│   ├── static/          # CSS, JS, images
│   └── templates/       # HTML templates
├── manage.py
├── db.sqlite3           # Database
├── requirements.txt
└── README.md
Notes

Ensure you have Python 3.8+ installed.

This project uses Django 3.x or above.

All static files are included in workshop_app/static.

Author

Meenakshi Kshirsagar
Developed as part of FOSSEE Internship Task
