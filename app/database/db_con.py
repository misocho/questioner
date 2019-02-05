import psycopg2
from flask import current_app
from app.database import migrations
import os
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash

class QuestionerDB:
    """ DB connection class """

    @classmethod
    def connect(cls, url):
        try:
            cls.con = psycopg2.connect(url)
            cls.cursor = cls.con.cursor(cursor_factory=RealDictCursor)
        except (Exception, psycopg2.DatabaseError) as error:
            raise error

    @classmethod
    def create_tables(cls):
        try:
            tables = migrations.tables()

            for query in tables:
                cls.cursor.execute(query)
            cls.con.commit()
            print("Tables created successfully in PostgreSQL ")
            cls.create_admin()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)

    @classmethod
    def destroy_tables(cls):
        """ Drops all tables """
        try:
            query = """DROP TABLE IF EXISTS users, meetups, questions, rsvps, votes, comments;"""
            cls.cursor.execute(query)
            cls.con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while dropping PostgreSQL table", error)

    @classmethod
    def save(cls, query, data):
        """ Saves a user in the database """

        cls.cursor.execute(query, data)
        cls.con.commit()
        result = cls.cursor.fetchone()
        if result:
            return result

    @classmethod
    def fetch_one(cls, query):
        """ Returns a specified item """

        cls.cursor.execute(query)
        return cls.cursor.fetchone()

    @classmethod
    def fetch_all(cls, query):
        """ Returns all specified items """

        cls.cursor.execute(query)
        return cls.cursor.fetchall()

    @classmethod
    def delete_one(cls, query):
        """ Deletes a specified item """

        cls.cursor.execute(query)
        cls.cursor.commit()

    @classmethod
    def update_vote(cls, query):
        """ upvotes or downvotes """

        cls.cursor.execute(query)
        data = cls.cursor.fetchone()
        return data

    @classmethod
    def create_admin(cls):
        """ checks if an admin user exists """
        query = "SELECT * FROM users WHERE isAdmin=true"
        admin = cls.fetch_one(query)
        if not admin:
            firstname = "admin"
            lastname = "admin"
            othername = "admin"
            email = "questioneradmin@gmail.com"
            phoneNumber = "254798724968"
            username = "admin"
            password = generate_password_hash("@Admin1254")
            isAdmin = "True"

            query_2 = """ INSERT INTO users (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING firstname, lastname, othername, email, phoneNumber,
                username, isAdmin"""

            data = (firstname, lastname, othername, email, phoneNumber,
                    username, password, isAdmin)

            cls.save(query_2, data)
            
            print("Admin user created")
