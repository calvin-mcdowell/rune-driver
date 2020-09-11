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

    assert os.path.exists(client.root_certificate)


def test_lcu_connectivity():
    """
    Validate successful connectivity to the local LCU server (League of Legends client)
    """

    client = LcuClient()
    assert client.send_request_lcu(uri='/lol-perks/v1/pages').status_code == 200