from sentfrag.infra.builders import DocumentBuilder

import pytest

TEST_FILEPATH = "tests/data/lorem.txt"
TEST_AUTHOR = "Jommy Cross"

@pytest.fixture(scope="module")
def db():
    doc_builder = DocumentBuilder()
    return doc_builder
 

def test_get_reader(db):
    reader = db._get_reader(TEST_FILEPATH)
    assert reader

@pytest.mark.parametrize("file", ["testfile.mp4", "testfile.mp3", "testfile.png"])
def test_invalid_file_type(db, file):
    with pytest.raises(ValueError):
        _ = db._get_reader(file)

def test_build_document(db):
    doc = db.build_document(TEST_FILEPATH, TEST_AUTHOR)
    assert doc and doc.get_author() == TEST_AUTHOR

@pytest.mark.parametrize("file", ["testfile.mp4", "testfile.mp3", "testfile.png"])
def test_build_document_invalid_file_type(db, file):
    with pytest.raises(ValueError):
        _ = db.build_document(file, TEST_AUTHOR)
    
        

