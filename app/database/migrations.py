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
        images text NULL,
        title character varying(200) NOT NULL,
        organizer character varying(100) NOT NULL,
        tags text NULL,
        createdOn timestamp default current_timestamp
    );"""

    questions = """CREATE TABLE IF NOT EXISTS questions(
        id serial PRIMARY KEY NOT NULL,
        meetup_id numeric NOT NULL,
        user_id numeric NOT NULL,
        postedBy numeric NOT NULL,
        body text NOT NULL,
        votes integer DEFAULT 0
    );"""

    rsvps = """CREATE TABLE IF NOT EXISTS rsvps(
        id serial NOT NULL,
        meetup_id numeric NOT NULL,
        username character varying(100) NOT NULL,
        response character varying(30) NOT NULL,
        PRIMARY KEY(meetup_id, username)
    );"""

    votes = """CREATE TABLE IF NOT EXISTS votes(
        id serial NOT NULL,
        meetup_id numeric NOT NULL,
        username character varying(100) NOT NULL,
        response character varying(30) NOT NULL,
        PRIMARY KEY(meetup_id, username)
    );"""

    tables = [users, meetups, questions, rsvps]

    return tables
