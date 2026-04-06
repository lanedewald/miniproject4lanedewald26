# MiniProject3LaneDewald
### INF601 - Advanced Programming in Python
### Lane Dewald
### Mini Project 4


# Mini Project 4

The Personal Book Tracker is a Django-based web application designed to help users manage their reading lists. Users can register for an account, log in, and maintain a private list of books. The app utilizes a relational database to store book details like title, author, and description. It features a responsive UI built with Bootstrap 5, including a custom navigation bar and interactive modals for a modern user experience.

## Getting Started

### Dependencies

```
pip install -r requirements.txt
```

### Executing program

```

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

## Output

This should Register and log in to your own account, add books to a reading list, showing the details of each book with a responsive UI
## Authors

Contributors names and contact info

ex. Lane Dewald

## Acknowledgments

Inspiration, code snippets, etc.

Bootstrap 5 components → https://getbootstrap.com/docs/5.3/components/modal/

Django Documentation for Auth views - https://docs.djangoproject.com/en/stable/topics/auth/default/