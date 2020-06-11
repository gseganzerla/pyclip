from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Sql(object):
    def __init__(self):
        self.engine = create_engine('sqlite:///clipboard.db', echo=True)
        self.Session = sessionmaker(self.engine)
        self.handler = self.Session()