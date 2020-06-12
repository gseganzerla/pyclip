from sqlalchemy.orm.exc import NoResultFound

from src.models.clipboard import Clipboard
from src.models.sql import Sql


class ClipboardController(object):
    def __init__(self):
        self.sql = Sql()

    def store(self, clipboard):
        self.sql.handler.add(clipboard)
        self.sql.handler.commit()

    def show(self, id_: int) -> Clipboard:
        clipboard = self.sql.handler.query(Clipboard).filter(Clipboard.id == id_).first()

        if clipboard:
            return clipboard
        
        elif clipboard is None:
            raise NoResultFound
