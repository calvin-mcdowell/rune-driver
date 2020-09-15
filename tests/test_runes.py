from lcu_client.lcu_client import LcuClient


def test_rune_pages_retrieval():
    """
    Validate the client can retrieve the current rune pages
    """
    client = LcuClient()
    runes = client.get_rune_pages()

    assert len(runes) != 0

