from src.models.sql import Sql
from src.models.clipboard import Clipboard


class ClipboardController(object):
    def __init__(self):
        self.sql = Sql()

    def store(self, clipboard):
        self.sql.handler.add(clipboard)
        self.sql.handler.commit()