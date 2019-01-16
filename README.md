# Questioner
Questioner is a web application that crowd-sources questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

[![Build Status](https://travis-ci.org/misocho/questioner.svg?branch=develop)](https://travis-ci.org/misocho/questioner)           [![Coverage Status](https://coveralls.io/repos/github/misocho/questioner/badge.svg)](https://coveralls.io/github/misocho/questioner)  [![Maintainability](https://api.codeclimate.com/v1/badges/7ee445560f8a76810e01/maintainability)](https://codeclimate.com/github/misocho/questioner/maintainability)

# The required API endpoints that enable one:
* Create a meetup record.
* Create a question record.
* Get a specific meetup record.
* Get all meetup records.
* Upvote or downvote a question.
* Rsvp for a meetup

# List of functioning API endpoints:

| Method | Endpoint | Functionality |
|--------|----------|---------------|
| POST | /api/v1/meetups | Creates a meetup record|
| POST | /api/v1/questions | Creates a question record|
| PATCH | /api/v1/meetups/<meetup_id>/rsvp |Rsvp for a meetup |
| PATCH | /api/v1/questions/<question_id>/upvote | Upvote a question |
| POST | api/v1/questions/<question_id>/downvote | Downvote a question |
| GET | api/v1/meetups | Get all upcoming meetups |
| GET | api/v1/meetups/<meeutp_id>/ | Get a specific meetup |
| POST | api/v1/auth/signup | Signup user |
| POST | api/v1/auth/signin | Signin user |

# Installation
 Make sure you have git, python3 and pip installed
* Git clone this repo and navigate to the project directory
```
$ git clone https://github.com/misocho/questioner.git
$ cd questioner
```
* Create a virtual enviroment and activate it
```
$ Virtualenv venv
$ source venv/bin/activet
```
* Install the dependencies in the requirements text file
```
$ pip install requirements.txtx
```
* Run the app
```
$ export FLASK_APP="run.py"
$ export FLASK_ENV=development
$ flask run
```

# Testing the endpoints
* Install postman to test the endpoints
*  Open postman and enter ypur localhost url and add the endpoint you are testing
```
http://127.0.0.1:5000/api/v1/<endpoint>
```
# Running tests
* To check if all test pass
```
$ pytest
```
* To check test coverage
```
$ pytest --cov=app/
```
# Technologies used
* Python 3.6
* flask framework
* unittesting for testing
# Acknowledgements
* Andela workshops
* Team 8
# Author: Brian Misocho

