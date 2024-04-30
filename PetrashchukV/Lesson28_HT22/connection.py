
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PetrashchukV.Lesson28_HT22.create_new_table import CustomObject
from PetrashchukV.Lesson28_HT22.create_new_table import Base

class SqlDatabase:
    def __init__(self):
        self.connection = psycopg2.connect(
            user='postgres',
            password='Qwerty1!',
            host='localhost',
            port='5432',
            database='postgres'
        )
        self.engine = create_engine('postgresql://postgres:Qwerty1!@localhost:5432/postgres')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_object(self, obj):
        self.session.add(obj)
        self.session.commit()

    def get_object_by_id(self, obj_id):
        return self.session.query(CustomObject).filter_by(id=obj_id).first()

    def close_connection(self):
        self.session.close()
        self.connection.close()

engine = create_engine('postgresql://postgres:Qwerty1!@localhost:5432/postgres')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
