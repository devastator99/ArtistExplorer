# ArtistExplorer

ArtistExplorer is a simple web application made with Django, HTML, CSS, and JavaScript. It provides a beautiful design with Vanilla JavaScript and leverages the Spotipy API to fetch detailed information about artists.

## Features
- **Artist Details:** Fetches artist information including popularity score, genres, total fan following, and images.
- **CRUD Functionality:** Users can add, edit, update, and delete artist details.
- **Popularity Comparison:** Colorful bars to visually represent and compare artists' popularity scores out of 100.
- **Django ORM:** Utilizes Django ORM for database interactions.
- **Django MVT Architecture:** Follows Django's Model-View-Template (MVT) architecture.

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **API:** Spotipy API
- **Database:** Django ORM

## Local Deployment Guide

Follow these steps to get ArtistExplorer up and running on your local machine.

### Step 1: Clone the Repository
First, clone the repository to your local machine:
```sh
git clone https://github.com/devastator99/ArtistExplorer.git
cd ArtistExplorer
```

### Step 2: Install Django
Ensure you have Python and Django installed. If not,install python and then install Django via pip:
```sh
pip install django
```

### Step 3: Activate Virtual Environment
Activate the given virtual environment:

- On Linux:
```sh
source denv4/bin/activate
```

- On Windows:

```sh
den4/bin/activate.bat
```

### Step 4: Run the Server
- Navigate to the project directory and start the Django development server:

```sh
python manage.py runserver
```


### Additional Information
- **Design:** Beautifully designed using Vanilla JavaScript for a smooth user experience.
- **Functionality:** CRUD operations for managing artist data.
- **API Integration:** Fetches real-time artist data using the Spotipy API.
