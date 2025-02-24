from unittest import TestCase
from Loader import *
from make_dataset import create_tokens, create_documents


class Test(TestCase):

    def test_workflow(self):
        pos_reviews, neg_reviews = create_tokens(10, 10, 10)
        doc_list = create_documents(10, 10, 10)




