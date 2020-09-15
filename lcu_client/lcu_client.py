"""
https://github.com/calvin-mcdowell/rune-driver

Class to provide helper functions while interacting with the local LCU (League Client Update) server.
"""
import os
import requests


class LcuClient:
    """
    """

    def __init__(self):
        # TODO: Add a function to find the lockfile in custom installation directories
        lock_file = 'D:\Riot Games\League of Legends\lockfile'

        # Retrieve the listening LCU port and generated password from the local lockfile
        try:
            with open(lock_file, 'r') as f:
                lock_data = f.read()
                self.port = lock_data.split(':')[2]
                self.password = lock_data.split(':')[3]
        except Exception as err:
            # TODO: Add logging
            # https://stackoverflow.com/questions/15727420/using-logging-in-multiple-modulesprint('tset')
            return None

        # Download the Riot Games root SSL certificate
        self.download_root_certificate()

    def send_request_lcu(self, uri, rtype='GET', data=None, json=None):
        """
        Handles all HTTPS requests to the local LCU server. This function will attempt to download the latest
            riotgames.pem file and all requests require the use of HTTP Basic Authentication (BA)

        :param uri: string of the destination resource
        :param rtype: string indicating which supported HTTP method to use
        :param data: dict/list of tuples defining the HTTP message body data
        :param json: dict/list of tuples defining the HTTP message body data to be converted to JSON automatically
        :return: requests.Response Object
        """

        url = f'https://127.0.0.1:{self.port}{uri}'

        try:
            # HTTP GET request handling
            if rtype == 'GET':
                response = requests.get(url, verify=self.root_certificate, auth=('riot', self.password))
            # HTTP DELETE request handling
            elif rtype == 'DELETE':
                response = requests.delete(url, verify=self.root_certificate, auth=('riot', self.password))
            # HTTP POST request handling (General HTTP body data)
            elif rtype == 'POST' and data != None:
                response = requests.post(url, verify=self.root_certificate, auth=('riot', self.password), data=data)
            # HTTP POST request handling (JSON data, typically rune pages in this case)
            elif rtype == 'POST' and json != None:
                response = requests.post(url, verify=self.root_certificate, auth=('riot', self.password), json=json)
            # TODO: Add implementation of the PUT method
            #       EX: http://lcu.vivide.re/#operation--lol-perks-v1-pages--id--put

            # Handle any undesirable HTTP response codes, otherwise return the requests.Response object
            response.raise_for_status()
            return response

        except Exception as err:
            # TODO: Add logging
            # TODO: Add pythonic exception handling
            # TODO: Implement handling for empty JSON objects being returned by the LCU server
            pass

    def download_root_certificate(self):
        """
        Downloads the latest root certificate from Riot Games for validation of HTTPS connections to the LCU server

        :return: boolean indicating success/failure of root certificate download
        """

        # Create certificates folder if nonexistent
        try:
            if not os.path.exists('lcu_client/certificates'):
                os.makedirs('lcu_client/certificates')
                print('certificates folder made\n')
                # TODO: Log folder creation
        except OSError as err:
            # TODO: Add logging
            # TODO: Add pythonic exception handling
            return False

        # Download certificate regardless if the file is there as it may have been updated
        try:
            response = requests.get('https://static.developer.riotgames.com/docs/lol/riotgames.pem')
            response.raise_for_status()

            with open(f'lcu_client/certificates/riotgames.pem', 'wb') as cert_file:
                cert_file.write(response.content)

            self.root_certificate = 'lcu_client/certificates/riotgames.pem'
            return True
        except Exception as err:
            # TODO: Add logging
            # TODO: Add pythonic exception handling
            return False

    def get_rune_pages(self):
        """
        Retrieves all current rune pages from the LCU server and returns editable rune pages

        KEYS available per rune page.json()
	        autoModifiedSelections
	        current
	        id
	        isActive
	        isDeletable
	        isEditable
	        isValid
	        lastModified
	        name
	        order
	        primaryStyleId
	        selectedPerkIds
	        subStyleId

        :return:
        """
        r = self.send_request_lcu('/lol-perks/v1/pages').json()
        # TODO: Handle responses that return no content

        runes = [ page for page in r if page['isDeletable'] == True ]
        return runes

