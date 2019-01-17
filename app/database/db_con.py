import psycopg2
from flask import current_app
from app.database import migrations
import os


def connect():
    try:
        con = psycopg2.connect("dbname='questioner_db' host='localhost'user='postgres' password='scorpion234' port=5432")
        return con
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def close():
    con = connect()
    cursor = con.cursor()
    if (con):
        cursor.close()
        con.close()


def create_tables():
    try:
    
                con = psycopg2.connect("dbname='questioner_db' host='localhost'user='postgres' password='scorpion234' port=5432")
                cursor = con.cursor()
                tables = migrations.tables()

                for query in tables:
                    cursor.execute(query)
                con.commit()
                print("Tables created successfully in PostgreSQL ")
    except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)
    finally:
            #closing database connection.
                if(con):
                    cursor.close()
                    con.close()
                    print("PostgreSQL connection is closed")

def main():
    create_tables()

if __name__==('__main__'):
    main()
