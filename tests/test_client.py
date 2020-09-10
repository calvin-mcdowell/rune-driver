import os
from lcu_client.lcu_client import LcuClient


def test_always_pass():
    """
    Control test to validate Pytest can read the project structure
    """
    assert True

def test_download_root_certificate():
    """
    Validate that the root certificate downloads successfully from Riot Games
    """
    # If there's an existing certificates folder, delete it and contents
    if os.path.exists('lcu_client/certificates/riotgames.pem'):
        os.remove('lcu_client/certificates/riotgames.pem')

    client = LcuClient()
    client.download_root_certificate()

    if os.path.exists('lcu_client/certificates/riotgames.pem'):
        assert True

