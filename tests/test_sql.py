from unittest import TestCase, mock
from src.models.sql import Sql
import json

class TestSql(TestCase):
    def setUp(self):
        self.sql = Sql()

    def test_se_read_config_le_o_arquivo_corretamente(self):
        settings = self.sql._read_config()

        self.assertIsInstance(settings, dict)