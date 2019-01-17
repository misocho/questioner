import psycopg2
from flask import current_app
import migrations
import os

db_url = current_app.config['DATABASE_URL']

def db_init():
    
    con = psycopg2.connect(db_url)
    con.commit()
    return con


def connect():
    con = psycopg2.connect(db_url)
    return con

def create_tables():
    con = psycopg2.connect(db_url)
    cur = con.cursor()
    tables = migrations.tables()

    for query in tables:
        cur.execute(query)
    con.commit()
