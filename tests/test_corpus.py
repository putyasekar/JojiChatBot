from unittest import TestCase
import os
import io

class CorpusUtilsTestCase(TestCase):
    def test_get_file_path(self):
        path = corpus.get_file_path('chatterbot.corpus.english')
