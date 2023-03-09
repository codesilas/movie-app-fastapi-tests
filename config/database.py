import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))


# creación de url de DB
database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"


# creación de un engine
engine = create_engine(database_url, echo=True)


# creación de una sesión
Session = sessionmaker(bind=engine)


Base = declarative_base()