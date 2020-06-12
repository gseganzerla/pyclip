from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

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

    def test_se_find_funciona(self):
        clipboard = Clipboard(clipboard='find me')
        self.session.add(clipboard)
        self.session.commit()

        obtained = self.controller.show(1)

        self.assertEqual(clipboard.id, obtained.id)

    def test_se_find_nao_encontra_o_registro(self):

        self.assertRaises(NoResultFound,
                          self.controller.show, 0)

    def test_se_destroy_funciona(self):
        expected = 0

        clipboard = Clipboard(clipboard='delete me')
        self.session.add(clipboard)
        self.session.commit()


        self.controller.destroy(1)

        obtained =  self.session.query(Clipboard).filter_by(id=1).count()

        self.assertEqual(expected, obtained)

    def test_se_destroy_nao_encontra_o_registro(self):

        self.assertRaises(NoResultFound,
                          self.controller.destroy, 0)



    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()
