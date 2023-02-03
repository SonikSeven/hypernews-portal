# HyperNews Portal

## Overview
HyperNews Portal is a Django-based web application that serves as a news sharing platform. This application allows users to view news articles, search for articles by keywords, and add new articles.

## Features
- View list of news articles.
- Search news articles by keywords.
- View details of a news article.
- Add a new article to the list.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

Before installing HyperNews Portal, ensure you have Python and Django installed in your environment. Follow the steps below to get the project up and running.

1. **Clone the Repository**

   Open a terminal and run:
   ```
   git clone https://github.com/SonikSeven/hypernews-portal.git
   ```

2. **Navigate to the project directory**
   ```
   cd hypernews-portal
   ```

3. **Install Dependencies**

   It is recommended to use a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # For Unix/macOS
   venv\Scripts\activate  # For Windows
   ```
   Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Django**
   
   Navigate to the project root directory (`hypernews-portal`) where `manage.py` is located, then run migrations to prepare your database.
   ```
   python manage.py migrate
   ```

5. **Start the Server**
   ```
   python manage.py runserver
   ```
   This command starts a local server. By default, the application runs at `http://127.0.0.1:8000/`.

## How to Use
After starting the server, you can use the application through your web browser.

- **Viewing News Articles:** Access the main page at `http://127.0.0.1:8000/`. The homepage displays a list of news articles, sorted by the creation date.
- **Searching for Articles:** Use the search box on the main page to filter articles by keywords found in their titles.
- **Adding New Articles:** Click on the "Create Page" link on the main page to add a new article.

## Project Structure
- **`HyperNews_Portal/urls.py`**: Configures URLs for the admin interface and includes URLs from the `news` app.
- **`news/urls.py`**: Defines URLs for the main news list page, article detail view, and add article form.
- **`news/views.py`**: Contains views for displaying the news list, single article detail, and a form for adding a new article.
- **`news.json`**: Stores the data for the news articles in JSON format.
- **`templates/news`**: Contains HTML templates for the application.

## License
This project is licensed under the [MIT License](LICENSE.txt).
