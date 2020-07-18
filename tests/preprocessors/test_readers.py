import pytest

from sentfrag.preprocessors.readers import PDFReader, TXTReader


# @pytest.mark.parametrize("file, expected", [("tests/data/test_document.pdf", ["foo bar"])])
# def test_pdf_reader_read(file, expected):
#     reader = PDFReader(file, "")

#     for (expected_val, actual_val) in zip(iter(expected), reader.read()):
#         assert(expected_val == actual_val)

    

@pytest.mark.parametrize("file, expected", [("tests/data/test_document.txt", ["foo bar."])])
def test_txt_reader_read(file, expected):
    reader = TXTReader(file)

    for (expected_val, actual_val) in zip(iter(expected), reader.read()):
        assert(expected_val == actual_val)
