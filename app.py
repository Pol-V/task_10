import logging
from logging.config import dictConfig
import psycopg2
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from functions import fill_groups, make_groups, make_students


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

STUDENTS = make_students()
GROUPS = fill_groups()



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

log = logging.getLogger()

@app.route('/')
def make_group():
    class GroupModel(db.Model):
        __tablename__ = 'groups'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))
    groups = GROUPS
    for id, name in enumerate(groups, 1):
        try:
            g = GroupModel( id=id, name=name)
            db.session.add(g)
            db.session.commit()
            db.session.close()
        except Exception as e:
            return e

@app.route('/1')
def make_students():
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="postgres",
        password="mysecretpassword",
    )

    cur = conn.cursor()
    cur.execute('''CREATE TABLE STUDENT  
         (ID INT PRIMARY KEY NOT NULL,
         GROUP_ID INTEGER FOREIGN KEY NOT NULL,
         FIRST_NAME TEXT NOT NULL,
         LAST_NAME TEXT NOT NULL);''')
    cur.commit()
    for person in students
    cur.execute(
        "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
    )
    cur.close()
    conn.close()





if __name__ == '__main__':
    """This part is responsible for connecting to Postrgres-database.
    # Config must match to parametres from docker-compose.yml"""
    try:
        log.warning('Creating connection to db')
        conn = psycopg2.connect(
            host="db",
            database="mydatabase",
            user="postgres",
            password="mysecretpassword",
        )
        log.info('Connected successfully')

        cur = conn.cursor()


    except Exception as e:
        log.error(e)

    app.run(debug=True)





