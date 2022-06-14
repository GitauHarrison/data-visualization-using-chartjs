# Data Visualization Using ChartJS

Powerful stories are told using data. 

![Data stories](/app/static/images/data_stories.gif)


## Overview

This is a sample flask app for a classroom teacher to understand the performance of students in select subjects throught the year. A teacher will add subject meanscores in the form at the end of a term and see how the latest score fares against other meanscores.

## Technologies Used

- Flask framework for the web server
- Python for programming
- ChartJS for the charts
<br>
- SQLite for the database
- SQLAlchemy for the ORM
- Flask-migrate for database migrations
- Flask-wtf for the forms
- Flask-bootstrap for styling and cross-browser responsiveness
- Flask-login to handle user sessions
- Gunicorn and psycopg2 for Heroku deployment

## Deployment

- [Simple chartjs demo on heroku](https://simple-chartjs-demo.herokuapp.com/)

## Live Deployment Usage

You can [log in](https://simple-chartjs-demo.herokuapp.com/login) as a pre-created teacher using the following credentials:
- Email: rahima@test.com
- Password: rahima

Alternatively, you can [register](https://simple-chartjs-demo.herokuapp.com/register) your own user.

## Local Usage

Clone this repo:

```python
$ git clone git@github.com:GitauHarrison/data-visualization-using-chartjs.git
```

Change your current working directory to the root of the repo:

```python
$ cd data-visualization-using-chartjs
```

Create and activate a virtual environment:

```python
$ mkvirtualenv venv # using virtualenvwrapper
```

Install project requirements in the virtual environment:

```python
(venv)$ pip install -r requirements.txt
```

Run the application:

```python
(venv)$ flask run
```

Paste http://localhost:5000/ in your favourite browser to access the project. You should be able to see the application running.


## Reference

If you are interested in understanding how the project was created, please refer to the [this chartjs tutorial](https://github.com/GitauHarrison/notes/blob/master/chartjs.md).