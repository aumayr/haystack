import pytest

from haystack.preprocessor.utils import convert_files_to_dicts
from haystack.preprocessor.cleaning import clean_wiki_text


def test_convert_files_to_dicts(xpdf_fixture):
    documents = convert_files_to_dicts(dir_path="samples", clean_func=clean_wiki_text, split_paragraphs=True)
    assert documents and len(documents) > 0


@pytest.mark.tika
def test_tika_convert_files_to_dicts(tika_fixture):
    try:
        from haystack.preprocessor.utils import tika_convert_files_to_dicts
    except Exception as ex:
        raise ex
    documents = tika_convert_files_to_dicts(dir_path="samples", clean_func=clean_wiki_text, split_paragraphs=True)
    assert documents and len(documents) > 0

