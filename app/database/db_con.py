import psycopg2
from flask import current_app
from app.database import migrations
import os
from psycopg2.extras import RealDictCursor


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
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)

    @classmethod
    def destroy_tables(cls):
        """ Drops all tables """

        query = """DROP TABLE IF EXISTS users, meetups, questions, rsvps,\
        comments, votes;"""
        cls.cursor.execute(query)
        cls.con.commit()

    @classmethod
    def save(cls, query):
        """ Saves a user in the database """

        cls.cursor.execute(query)
        cls.con.commit()
        data = cls.cursor.fetchone()
        return data

    @classmethod
    def fetch_one(cls, query):
        """ Returns a specified item """
        cls.cursor.execute(query)
        return cls.cursor.fetchone()