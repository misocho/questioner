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

