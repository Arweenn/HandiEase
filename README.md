# 🌻 HandiEase 🌻

HandiEase is a web application designed to enhance user experience by providing articles related to disabilities through an RSS feed. HandiEase is a single page application (SPA), still under development, allowing users to read articles, sign up, log in, and create a personalized reading list.

## 💻 Features

- **Single Page Application**: Smooth and fast navigation without page reloads.
- **Disability-Related Articles**: Access relevant articles fetched via an RSS feed.
- **Sign Up/Log In Features**: Create an account and log in for a personalized experience.
- **Reading List**: Create and manage your own reading list of articles.

## 🎯 Features to come

- **Accessibility**: Make sure that the website comes with as much options as possible.
- **Calendar**: Reference all events related to handicap, their location and dates.
- **Phonebook**: Reference all structure disability-friendly (public structures or administrative ones) and all qualified professionals.
- **Chatbox**: Create a chatbox so that authentified users can share experiences.

## ⚙️ Technologies Used

- **Backend**: Python Django
- **Frontend**: HTML, CSS, JavaScript

## 💾 Local Usage

### Prerequisites

- Python 3.x
- Django
- `pip`, the Python package manager, must also be installed.

### Installation

To install and run the HandiEase project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/HandiEase.git
    cd HandiEase
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to:
    [http://localhost:8000](http://localhost:8000)

## 🌐 Online Usage

To use HandiEase online, follow these steps:

1. Visit the deployed site: [HandiEase](https://www.handiease.fr/)
2. Create an account or log in if you already have an account.
3. Browse the disability-related articles.
4. Add articles to your reading list to read later.

## 🔖 License

This project is not licensed and is open for personal and non-commercial use. Feel free to explore and use the code as inspiration for your own projects.

## 🪶 Author

**Arwen Dumont**

- **LinkedIn**: [Arwen Dumont](https://www.linkedin.com/in/arwen-dumont-4380932b0/)
- **GitHub**: [Arweenn](https://github.com/Arweenn/)
