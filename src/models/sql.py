import os
from dotenv import load_dotenv, find_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# class Sql(object):
#     def __init__(self):
#         settings = self._read_config()
        

#         self.engine = create_engine(
#             f"{settings['engine']}://{settings['database']}", echo=True
#         )

#         print(self.engine)
#         self.Session = sessionmaker(self.engine)
#         self.handler = self.Session()

#     def _read_config(self):
#         with open('.json', 'r') as file:
#             return json.load(file)


# if __name__ == "__main__":
#     sql = Sql()



load_dotenv(find_dotenv())