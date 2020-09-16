from lcu_client.lcu_client import LcuClient
from random import randint

def test_rune_pages_retrieval():
    """
    Validate the client can retrieve the current rune pages
    """
    client = LcuClient()
    runes = client.get_rune_pages()

    # Fail if no rune pages are returned
    # TODO: Resolve issue where assertion fails when no rune pages exist
    if len(runes) == 0:
        assert False

    # Validates that a random rune page can be returned
    rand_page = runes[randint(0, len(runes)-1)]
    specific_page = client.get_rune_pages(name=rand_page['name'])

    assert rand_page == specific_page

def test_rune_page_modification():
    """
    Validates that the client can delete and add rune pages
    """
    client = LcuClient()
    runes = client.get_rune_pages()

    # If no rune pages are available for retrieval, use a test page
    if len(runes) != 0:
        # Retrieve a random rune page
        rune_page = runes[randint(0, len(runes)-1)]

        # Test for rune page deletion
        assert client.delete_rune_page(id=rune_page['id']).status_code == 204

        # Test for rune page addition
        assert client.post_rune_page(page=rune_page).status_code == 200

    else:
        rune_page = {'autoModifiedSelections': [],
                     'current': True,
                     'id': 170307605,
                     'isActive': False,
                     'isDeletable': True,
                     'isEditable': True,
                     'isValid': True,
                     'lastModified': 1600294650193,
                     'name': 'rune-test',
                     'order': 0,
                     'primaryStyleId': 8000,
                     'selectedPerkIds': [8021, 8009, 9103, 8299, 8226, 8234, 5005, 5002, 5002],
                     'subStyleId': 8200}

        # Test for rune page addition
        assert client.post_rune_page(page=rune_page).status_code == 200

        # Test for rune page deletion
        assert client.delete_rune_page(id=rune_page['id']).status_code == 204

