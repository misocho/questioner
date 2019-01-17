import psycopg2
import os


db_url = os.getenv('DATABASE_URL')


print(db_url)
# creats db connection
con = psycopg2.connect(db_url)


# cretes the coursor
cur = con.cursor()

# close the connection
con.close()
