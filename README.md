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

- ~~[Simple chartjs demo](https://simple-chartjs-demo.herokuapp.com/) - Heroku~~ (heroku app is down)
- [Simple chartjs demo](https://chartjs-demo.onrender.com) - Render

## Live Deployment Usage

You can [log in](https://simple-chartjs-demo.herokuapp.com/login) as a pre-created teacher using the following credentials:
- Email: chico@test.com
- Password: chico

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
(venv)$ pip3 install -r requirements.txt
```

Run the application:

```python
(venv)$ flask run
```

Paste http://localhost:5000/ in your favourite browser to access the project. You should be able to see the application running.

## ChartJS Usage in the Application

All the meanscores from the form are stored in the database. 

```python
form = MeanScore()
if form.validate_on_submit():
    meanscore = Meanscore(
        term=form.term.data,
        math=form.math.data,
        english=form.english.data,
        science=form.science.data,
        ict=form.ict.data,
        history=form.history.data,
        author=current_user)
    db.session.add(meanscore)
    db.session.commit()
```

The database is queried and the results are appended to lists which will be used in the charts.

```python
term_meanscore = teacher.meanscores.all()

terms = []
math = []
english = []
science = []
ict = []
history = []

for term in term_meanscore:
    terms.append(term.term)
    math.append(term.math)
    english.append(term.english)
    science.append(term.science)
    ict.append(term.ict)
    history.append(term.history)
```

In the templates, the indivial elements in the lists are retrieved and used as dataset values in the charts. To draw multiple graphs on one chart, several dictionaries have to be created. Colors are used to add visual flair to the charts.

```js
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [
                {% for term in terms %}
                    'Term {{ term }}',
                {% endfor %}
            ],
            datasets: [{
                label: 'Math',
                data: [
                    {% for math_score in math %}
                        {{ math_score }},
                    {% endfor %}
                ],
                backgroundColor: ['white'],
                borderColor: ['teal'],
                borderWidth: 1
            }, {
                label: 'English',
                data: [
                    {% for english_score in english %}
                        {{ english_score }},
                    {% endfor %}
                ],
                backgroundColor: ['purple'],
                borderColor: ['red'],
            }, {
                label: 'Science',
                data: [
                    {% for science_score in science %}
                        {{ science_score }},
                    {% endfor %}
                ],
                backgroundColor: ['black'],
                borderColor: ['cyan'],
            }, {
                label: 'ICT',
                data: [
                    {% for ict_score in ict %}
                        {{ ict_score }},
                    {% endfor %}
                ],
                backgroundColor: ['orange'],
                borderColor: ['pink'],
            }, {
                label: 'History',
                data: [
                    {% for history_score in history %}
                        {{ history_score }},
                    {% endfor %}
                ],
                backgroundColor: ['green'],
                borderColor: ['yellow'],
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
</script>
```

## Reference

If you are interested in understanding how the project was created, please refer to [this chartjs tutorial](https://github.com/GitauHarrison/notes/blob/master/chartjs.md).