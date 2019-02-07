def tables():
    """ defines database table structures"""

    users = """CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY NOT NULL,
        firstname character varying(100) NOT NULL,
        lastname  character varying(100) NOT NULL,
        othername character varying(100) NOT NULL,
        email  character varying(100) UNIQUE,
        phoneNumber character varying(100) UNIQUE,
        username character varying(100) NOT NULL,
        password character varying(250) NOT NULL,
        isAdmin boolean,
        registered timestamp default current_timestamp
    );"""

    meetups = """CREATE TABLE IF NOT EXISTS meetups(
        id serial PRIMARY KEY NOT NULL,
        username character varying(100) NOT NULL,
        happeningOn timestamp NOT NULL,
        location character varying(100) NULL,
        images text,
        title character varying(200) NOT NULL,
        organizer character varying(100) NOT NULL,
        tags varchar [],
        createdOn timestamp default current_timestamp
    );"""

    questions = """CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY NOT NULL,
        meetup_id integer NOT NULL,
        createdOn timestamp default current_timestamp,
        username character varying(100) NOT NULL,
        title text NOT NULL,
        body text NOT NULL,
        votes integer DEFAULT 0
    );"""


    rsvps = """CREATE TABLE IF NOT EXISTS rsvps(
        id serial NOT NULL,
        meetup_id integer NOT NULL,
        username character varying(100) NOT NULL,
        response character varying(30) NOT NULL,
        PRIMARY KEY (meetup_id, username)
    );"""

    votes = """CREATE TABLE IF NOT EXISTS votes(
        id serial NOT NULL,
        question_id integer NOT NULL,
        username character varying(100) NOT NULL,
        PRIMARY KEY (question_id, username) 
    );"""

    comments = """CREATE TABLE IF NOT EXISTS comments(
        id serial NOT NULL,
        question_id integer NOT NULL,
        question_title text NOT NULL,
        question_body text NOT NULL,
        comment text NOT NULL,
        username character varying(100) NOT NULL
    );"""

    tables = [users, meetups, questions, rsvps, votes, comments]

    return tables
