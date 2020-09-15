from lcu_client.lcu_client import LcuClient
from random import randint


def test_rune_pages_retrieval():
    """
    Validate the client can retrieve the current rune pages
    """
    client = LcuClient()
    runes = client.get_rune_pages()

    # Fail if no rune pages are returned
    if len(runes) == 0:
        assert False

    # Validates that a random rune page can be returned
    rand_page = runes[randint(0, len(runes))]
    specific_page = client.get_rune_pages(name=rand_page['name'])

    assert rand_page == specific_page

