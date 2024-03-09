# Music Application

Welcome to the Music Application! This web application allows users to manage and enjoy their favorite music. Users can upload, play, and delete songs, making it a personalized music experience.

## Features

- **User Authentication:** Users can register and log in to the application to access personalized features.
- **Dashboard:** View a list of uploaded songs on the dashboard.
- **Upload Songs:** Users can upload their favorite songs to the application.
- **Play Music:** Listen to uploaded songs directly from the application.
- **Delete Songs:** Remove unwanted songs from the dashboard.

## Technologies Used

- Django: Web framework for building the backend.
- HTML/CSS: Frontend development for user interface.
- SQLite: Database for storing user and song information.

## Getting Started

1. Clone the repository:

   ```bash
    git clone https://github.com/sriharsha66/music_application_LLD.git
    cd music_application_LLD
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver 5001 


## Endpoints

- **Home:** [http://127.0.0.1:5001/](http://127.0.0.1:5001/home)
  - Landing page or welcome screen.
![Music App](/home/sriharsha/django_frac_project/my_music/mussic_app.png)


## Create a virtual environment
python -m venv venv

## Activate the virtual environment (on Windows)
venv\Scripts\activate

## Activate the virtual environment (on macOS or Linux)
source venv/bin/activate
