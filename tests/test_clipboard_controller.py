from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.controllers.clipboard_controller import \
    ClipboardController as Controller
from src.models.clipboard import Base, Clipboard


class TestClipboardController(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///clipboard.db', echo=False)
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        self.controller = Controller()

    def test_se_store_funciona(self):
        clipboard = Clipboard(clipboard="any text")
        self.controller.store(clipboard)

        clipboards = self.session.query(Clipboard).all()

    
        for i in range(len(clipboards)):
            with self.subTest(i=i):
                self.assertIn(clipboard.clipboard, clipboards[i].clipboard)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()
