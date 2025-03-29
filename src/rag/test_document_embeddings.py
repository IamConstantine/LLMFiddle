import os
import unittest

from document_embeddings import load_documents, split_documents, CHROMA_PATH

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class TestDocumentEmbeddings(unittest.TestCase):

    TEST_DATA_PATH = 'test_data'

    def setUp(self):
        # Create a dummy file for testing
        os.makedirs(self.TEST_DATA_PATH, exist_ok=True)
        with open(os.path.join(self.TEST_DATA_PATH, 'test_file.txt'), 'w') as f:
            f.write("This is a test document.It has two lines.")

    def tearDown(self):
        # Clean up the dummy file and directory
        import shutil
        shutil.rmtree(self.TEST_DATA_PATH)
        if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)

    def test_load_documents(self):

        documents = load_documents(self.TEST_DATA_PATH)
        self.assertEqual(len(documents), 1)
        self.assertTrue("test_file.txt" in documents[0].metadata['source'])

    def test_split_documents(self):
        documents = load_documents(self.TEST_DATA_PATH)
        chunks = split_documents(documents)
        self.assertEqual(len(chunks), 1) #because chunk size is 1000 and test doc is very small
        self.assertTrue("test document" in chunks[0].page_content)
